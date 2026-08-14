# app/queries.py

"""
All Cypher queries used by CareerGraph.

The queries are kept separately from Flask routes so that:
1. Database logic is easier to maintain.
2. Queries can be tested independently.
3. Routes remain clean and readable.
"""


# ---------------------------------------------------------
# Get all available skills
# ---------------------------------------------------------

GET_ALL_SKILLS = """
MATCH (s:Skill)

RETURN
    s.id AS id,
    s.name AS name,
    s.category AS category

ORDER BY s.name
"""
# ---------------------------------------------------------
# Get all available job roles
# ---------------------------------------------------------

GET_ALL_JOB_ROLES = """
MATCH (j:JobRole)

RETURN
    j.id AS id,
    j.title AS title,
    j.description AS description,
    j.experience_level AS experience_level

ORDER BY j.title
"""

# ---------------------------------------------------------
# Get skills belonging to a specific user
# ---------------------------------------------------------

GET_USER_SKILLS = """
MATCH (u:User {id: $user_id})
      -[r:HAS_SKILL]->
      (s:Skill)

RETURN
    s.id AS id,
    s.name AS name,
    s.category AS category,
    r.proficiency AS proficiency

ORDER BY s.name
"""

# ---------------------------------------------------------
# Get skills required for a job role
# ---------------------------------------------------------

GET_JOB_REQUIRED_SKILLS = """
MATCH (j:JobRole {id: $job_role_id})
      <-[r:REQUIRED_FOR]-
      (s:Skill)

RETURN
    s.id AS id,
    s.name AS name,
    s.category AS category,
    r.importance AS importance

ORDER BY
    CASE r.importance
        WHEN 'High' THEN 1
        WHEN 'Medium' THEN 2
        ELSE 3
    END,
    s.name
"""

# ---------------------------------------------------------
# Find career roles based on a user's existing skills
#
# Traversal:
#
# User
#   ↓ HAS_SKILL
# Skill
#   ↓ REQUIRED_FOR
# JobRole
# ---------------------------------------------------------

GET_CAREER_MATCHES = """
MATCH (u:User {id: $user_id})
      -[:HAS_SKILL]->
      (s:Skill)
      -[:REQUIRED_FOR]->
      (j:JobRole)

WITH
    j,
    COUNT(DISTINCT s) AS matching_skills

MATCH (j)<-[:REQUIRED_FOR]-(required:Skill)

WITH
    j,
    matching_skills,
    COUNT(DISTINCT required) AS total_required_skills

RETURN
    j.id AS id,
    j.title AS title,
    j.description AS description,
    j.experience_level AS experience_level,
    matching_skills,
    total_required_skills,
    ROUND(
        100.0 * matching_skills / total_required_skills
    ) AS match_percentage

ORDER BY match_percentage DESC
"""

# ---------------------------------------------------------
# Find skills a user is missing for a specific job role
# ---------------------------------------------------------

GET_MISSING_SKILLS = """
MATCH (j:JobRole {id: $job_role_id})
      <-[required_rel:REQUIRED_FOR]-
      (required:Skill)

WHERE NOT EXISTS {
    MATCH (u:User {id: $user_id})
          -[:HAS_SKILL]->
          (required)
}

RETURN
    required.id AS id,
    required.name AS name,
    required.category AS category,
    required_rel.importance AS importance

ORDER BY
    CASE required_rel.importance
        WHEN 'High' THEN 1
        WHEN 'Medium' THEN 2
        ELSE 3
    END,
    required.name
"""

# ---------------------------------------------------------
# Recommend courses for skills missing from a career path
#
# Traversal:
#
# JobRole
#   ↓ REQUIRED_FOR
# Skill
#   ↑ TEACHES
# Course
# ---------------------------------------------------------

GET_RECOMMENDED_COURSES = """
MATCH (j:JobRole {id: $job_role_id})
      <-[:REQUIRED_FOR]-
      (skill:Skill)

WHERE NOT EXISTS {
    MATCH (u:User {id: $user_id})
          -[:HAS_SKILL]->
          (skill)
}

MATCH (course:Course)
      -[:TEACHES]->
      (skill)

RETURN DISTINCT
    course.id AS id,
    course.title AS title,
    course.platform AS platform,
    course.url AS url,
    skill.name AS skill

ORDER BY course.title
"""


# ---------------------------------------------------------
# Find companies associated with a job role
# ---------------------------------------------------------

GET_JOB_COMPANIES = """
MATCH (j:JobRole {id: $job_role_id})
      -[:OFFERED_BY]->
      (c:Company)

RETURN
    c.id AS id,
    c.name AS name,
    c.industry AS industry

ORDER BY c.name
"""

# ---------------------------------------------------------
# Recommend projects that develop missing skills
# ---------------------------------------------------------

GET_RECOMMENDED_PROJECTS = """
MATCH (j:JobRole {id: $job_role_id})
      <-[:REQUIRED_FOR]-
      (skill:Skill)

WHERE NOT EXISTS {
    MATCH (u:User {id: $user_id})
          -[:HAS_SKILL]->
          (skill)
}

MATCH (project:Project)
      -[:DEVELOPS]->
      (skill)

RETURN DISTINCT
    project.id AS id,
    project.title AS title,
    project.difficulty AS difficulty,
    project.description AS description,
    skill.name AS skill

ORDER BY project.difficulty, project.title
"""

# ---------------------------------------------------------
# Check whether a user exists
# ---------------------------------------------------------

CHECK_USER_EXISTS = """
MATCH (u:User {id: $user_id})

RETURN u.id AS id
"""