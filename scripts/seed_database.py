from app.database import driver


def create_constraints():
    """
    Create uniqueness constraints for the main graph entities.

    Constraints prevent duplicate IDs from being created.
    """

    constraints = [
        """
        CREATE CONSTRAINT user_id_unique IF NOT EXISTS
        FOR (u:User)
        REQUIRE u.id IS UNIQUE
        """,

        """
        CREATE CONSTRAINT skill_id_unique IF NOT EXISTS
        FOR (s:Skill)
        REQUIRE s.id IS UNIQUE
        """,

        """
        CREATE CONSTRAINT job_role_id_unique IF NOT EXISTS
        FOR (j:JobRole)
        REQUIRE j.id IS UNIQUE
        """,

        """
        CREATE CONSTRAINT company_id_unique IF NOT EXISTS
        FOR (c:Company)
        REQUIRE c.id IS UNIQUE
        """,

        """
        CREATE CONSTRAINT course_id_unique IF NOT EXISTS
        FOR (c:Course)
        REQUIRE c.id IS UNIQUE
        """,

        """
        CREATE CONSTRAINT project_id_unique IF NOT EXISTS
        FOR (p:Project)
        REQUIRE p.id IS UNIQUE
        """
    ]

    with driver.session() as session:

        for query in constraints:
            session.run(query)

    print("✅ Graph constraints created.")

def seed_skills():
    """
    Insert the skills used by CareerGraph.
    """

    skills = [
        {
            "id": "skill_python",
            "name": "Python",
            "category": "Programming"
        },
        {
            "id": "skill_django",
            "name": "Django",
            "category": "Backend"
        },
        {
            "id": "skill_sql",
            "name": "SQL",
            "category": "Database"
        },
        {
            "id": "skill_rest_api",
            "name": "REST API",
            "category": "Backend"
        },
        {
            "id": "skill_git",
            "name": "Git",
            "category": "Tools"
        },
        {
            "id": "skill_javascript",
            "name": "JavaScript",
            "category": "Frontend"
        },
        {
            "id": "skill_html_css",
            "name": "HTML & CSS",
            "category": "Frontend"
        },
        {
            "id": "skill_react",
            "name": "React",
            "category": "Frontend"
        },
        {
            "id": "skill_docker",
            "name": "Docker",
            "category": "DevOps"
        },
        {
            "id": "skill_redis",
            "name": "Redis",
            "category": "Backend"
        }
    ]

    query = """
    UNWIND $skills AS skill

    MERGE (s:Skill {id: skill.id})

    SET
        s.name = skill.name,
        s.category = skill.category
    """

    with driver.session() as session:
        session.run(query, skills=skills)

    print("✅ Skills seeded.")

def seed_users():
    """
    Create sample users.
    """

    users = [
        {
            "id": "user_001",
            "name": "Alex",
            "email": "alex@example.com"
        },
        {
            "id": "user_002",
            "name": "Priya",
            "email": "priya@example.com"
        }
    ]

    query = """
    UNWIND $users AS user

    MERGE (u:User {id: user.id})

    SET
        u.name = user.name,
        u.email = user.email
    """

    with driver.session() as session:
        session.run(query, users=users)

    print("✅ Users seeded.")

def seed_job_roles():
    """
    Create career/job roles.
    """

    job_roles = [
        {
            "id": "role_python_developer",
            "title": "Python Developer",
            "description": "Develop applications using Python.",
            "experience_level": "Entry Level"
        },
        {
            "id": "role_backend_developer",
            "title": "Backend Developer",
            "description": "Build APIs and server-side applications.",
            "experience_level": "Entry Level"
        },
        {
            "id": "role_full_stack_developer",
            "title": "Full Stack Developer",
            "description": "Build both frontend and backend applications.",
            "experience_level": "Entry Level"
        },
        {
            "id": "role_data_analyst",
            "title": "Data Analyst",
            "description": "Analyze data and generate business insights.",
            "experience_level": "Entry Level"
        }
    ]

    query = """
    UNWIND $roles AS role

    MERGE (j:JobRole {id: role.id})

    SET
        j.title = role.title,
        j.description = role.description,
        j.experience_level = role.experience_level
    """

    with driver.session() as session:
        session.run(query, roles=job_roles)

    print("✅ Job roles seeded.")

def seed_companies():
    """
    Create sample companies.
    """

    companies = [
        {
            "id": "company_001",
            "name": "TechNova",
            "industry": "Software"
        },
        {
            "id": "company_002",
            "name": "DataSphere",
            "industry": "Data & Analytics"
        },
        {
            "id": "company_003",
            "name": "CloudWorks",
            "industry": "Cloud Technology"
        }
    ]

    query = """
    UNWIND $companies AS company

    MERGE (c:Company {id: company.id})

    SET
        c.name = company.name,
        c.industry = company.industry
    """

    with driver.session() as session:
        session.run(query, companies=companies)

    print("✅ Companies seeded.")

def seed_courses():
    """
    Create learning resources.
    """

    courses = [
        {
            "id": "course_python",
            "title": "Python Fundamentals",
            "platform": "CareerGraph Academy",
            "url": "https://example.com/python"
        },
        {
            "id": "course_django",
            "title": "Django Web Development",
            "platform": "CareerGraph Academy",
            "url": "https://example.com/django"
        },
        {
            "id": "course_rest",
            "title": "Building REST APIs",
            "platform": "CareerGraph Academy",
            "url": "https://example.com/rest"
        },
        {
            "id": "course_docker",
            "title": "Docker for Developers",
            "platform": "CareerGraph Academy",
            "url": "https://example.com/docker"
        },
        {
            "id": "course_sql",
            "title": "SQL for Developers",
            "platform": "CareerGraph Academy",
            "url": "https://example.com/sql"
        }
    ]

    query = """
    UNWIND $courses AS course

    MERGE (c:Course {id: course.id})

    SET
        c.title = course.title,
        c.platform = course.platform,
        c.url = course.url
    """

    with driver.session() as session:
        session.run(query, courses=courses)

    print("✅ Courses seeded.")

def seed_projects():
    """
    Create practical projects that help develop skills.
    """

    projects = [
        {
            "id": "project_rest_api",
            "title": "E-Commerce REST API",
            "difficulty": "Intermediate",
            "description": "Build a REST API for an online store."
        },
        {
            "id": "project_dashboard",
            "title": "Data Analytics Dashboard",
            "difficulty": "Beginner",
            "description": "Build a dashboard for analyzing business data."
        },
        {
            "id": "project_full_stack",
            "title": "Task Management Platform",
            "difficulty": "Intermediate",
            "description": "Build a complete full-stack task management application."
        }
    ]

    query = """
    UNWIND $projects AS project

    MERGE (p:Project {id: project.id})

    SET
        p.title = project.title,
        p.difficulty = project.difficulty,
        p.description = project.description
    """

    with driver.session() as session:
        session.run(query, projects=projects)

    print("✅ Projects seeded.")

def seed_user_skills():
    """
    Connect users to the skills they already have.
    """

    relationships = [
        {
            "user_id": "user_001",
            "skill_id": "skill_python",
            "proficiency": "Advanced"
        },
        {
            "user_id": "user_001",
            "skill_id": "skill_sql",
            "proficiency": "Intermediate"
        },
        {
            "user_id": "user_001",
            "skill_id": "skill_django",
            "proficiency": "Intermediate"
        },
        {
            "user_id": "user_001",
            "skill_id": "skill_git",
            "proficiency": "Intermediate"
        },

        {
            "user_id": "user_002",
            "skill_id": "skill_python",
            "proficiency": "Intermediate"
        },
        {
            "user_id": "user_002",
            "skill_id": "skill_javascript",
            "proficiency": "Intermediate"
        },
        {
            "user_id": "user_002",
            "skill_id": "skill_html_css",
            "proficiency": "Advanced"
        }
    ]

    query = """
    UNWIND $relationships AS rel

    MATCH (u:User {id: rel.user_id})
    MATCH (s:Skill {id: rel.skill_id})

    MERGE (u)-[r:HAS_SKILL]->(s)

    SET r.proficiency = rel.proficiency
    """

    with driver.session() as session:
        session.run(
            query,
            relationships=relationships
        )

    print("✅ User-skill relationships created.")

def seed_job_skills():
    """
    Connect job roles to their required skills.
    """

    relationships = [

        # Python Developer
        {
            "role_id": "role_python_developer",
            "skill_id": "skill_python",
            "importance": "High"
        },
        {
            "role_id": "role_python_developer",
            "skill_id": "skill_sql",
            "importance": "High"
        },
        {
            "role_id": "role_python_developer",
            "skill_id": "skill_git",
            "importance": "Medium"
        },

        # Backend Developer
        {
            "role_id": "role_backend_developer",
            "skill_id": "skill_python",
            "importance": "High"
        },
        {
            "role_id": "role_backend_developer",
            "skill_id": "skill_django",
            "importance": "High"
        },
        {
            "role_id": "role_backend_developer",
            "skill_id": "skill_rest_api",
            "importance": "High"
        },
        {
            "role_id": "role_backend_developer",
            "skill_id": "skill_sql",
            "importance": "Medium"
        },
        {
            "role_id": "role_backend_developer",
            "skill_id": "skill_git",
            "importance": "Medium"
        },
        {
            "role_id": "role_backend_developer",
            "skill_id": "skill_docker",
            "importance": "Medium"
        },

        # Full Stack Developer
        {
            "role_id": "role_full_stack_developer",
            "skill_id": "skill_python",
            "importance": "High"
        },
        {
            "role_id": "role_full_stack_developer",
            "skill_id": "skill_javascript",
            "importance": "High"
        },
        {
            "role_id": "role_full_stack_developer",
            "skill_id": "skill_html_css",
            "importance": "High"
        },
        {
            "role_id": "role_full_stack_developer",
            "skill_id": "skill_rest_api",
            "importance": "Medium"
        },
        {
            "role_id": "role_full_stack_developer",
            "skill_id": "skill_sql",
            "importance": "Medium"
        },

        # Data Analyst
        {
            "role_id": "role_data_analyst",
            "skill_id": "skill_python",
            "importance": "High"
        },
        {
            "role_id": "role_data_analyst",
            "skill_id": "skill_sql",
            "importance": "High"
        }
    ]

    query = """
    UNWIND $relationships AS rel

    MATCH (j:JobRole {id: rel.role_id})
    MATCH (s:Skill {id: rel.skill_id})

    MERGE (s)-[r:REQUIRED_FOR]->(j)

    SET r.importance = rel.importance
    """

    with driver.session() as session:
        session.run(
            query,
            relationships=relationships
        )

    print("✅ Job-skill relationships created.")

def seed_job_companies():
    """
    Connect job roles with companies.
    """

    relationships = [
        {
            "role_id": "role_python_developer",
            "company_id": "company_001"
        },
        {
            "role_id": "role_backend_developer",
            "company_id": "company_001"
        },
        {
            "role_id": "role_backend_developer",
            "company_id": "company_003"
        },
        {
            "role_id": "role_full_stack_developer",
            "company_id": "company_003"
        },
        {
            "role_id": "role_data_analyst",
            "company_id": "company_002"
        }
    ]

    query = """
    UNWIND $relationships AS rel

    MATCH (j:JobRole {id: rel.role_id})
    MATCH (c:Company {id: rel.company_id})

    MERGE (j)-[:OFFERED_BY]->(c)
    """

    with driver.session() as session:
        session.run(
            query,
            relationships=relationships
        )

    print("✅ Job-company relationships created.")

def seed_course_skills():
    """
    Connect courses to the skills they teach.
    """

    relationships = [
        {
            "course_id": "course_python",
            "skill_id": "skill_python"
        },
        {
            "course_id": "course_django",
            "skill_id": "skill_django"
        },
        {
            "course_id": "course_rest",
            "skill_id": "skill_rest_api"
        },
        {
            "course_id": "course_docker",
            "skill_id": "skill_docker"
        },
        {
            "course_id": "course_sql",
            "skill_id": "skill_sql"
        }
    ]

    query = """
    UNWIND $relationships AS rel

    MATCH (c:Course {id: rel.course_id})
    MATCH (s:Skill {id: rel.skill_id})

    MERGE (c)-[:TEACHES]->(s)
    """

    with driver.session() as session:
        session.run(
            query,
            relationships=relationships
        )

    print("✅ Course-skill relationships created.")

def seed_job_courses():
    """
    Connect job roles to recommended courses.
    """

    relationships = [
        {
            "role_id": "role_python_developer",
            "course_id": "course_python"
        },
        {
            "role_id": "role_python_developer",
            "course_id": "course_sql"
        },
        {
            "role_id": "role_backend_developer",
            "course_id": "course_django"
        },
        {
            "role_id": "role_backend_developer",
            "course_id": "course_rest"
        },
        {
            "role_id": "role_backend_developer",
            "course_id": "course_docker"
        }
    ]

    query = """
    UNWIND $relationships AS rel

    MATCH (j:JobRole {id: rel.role_id})
    MATCH (c:Course {id: rel.course_id})

    MERGE (j)-[:RECOMMENDS]->(c)
    """

    with driver.session() as session:
        session.run(
            query,
            relationships=relationships
        )

    print("✅ Job-course relationships created.")

def seed_project_skills():
    """
    Connect practical projects to the skills they develop.
    """

    relationships = [
        {
            "project_id": "project_rest_api",
            "skill_id": "skill_python"
        },
        {
            "project_id": "project_rest_api",
            "skill_id": "skill_rest_api"
        },
        {
            "project_id": "project_rest_api",
            "skill_id": "skill_sql"
        },
        {
            "project_id": "project_dashboard",
            "skill_id": "skill_python"
        },
        {
            "project_id": "project_dashboard",
            "skill_id": "skill_sql"
        },
        {
            "project_id": "project_full_stack",
            "skill_id": "skill_python"
        },
        {
            "project_id": "project_full_stack",
            "skill_id": "skill_javascript"
        },
        {
            "project_id": "project_full_stack",
            "skill_id": "skill_html_css"
        },
        {
            "project_id": "project_full_stack",
            "skill_id": "skill_rest_api"
        }
    ]

    query = """
    UNWIND $relationships AS rel

    MATCH (p:Project {id: rel.project_id})
    MATCH (s:Skill {id: rel.skill_id})

    MERGE (p)-[:DEVELOPS]->(s)
    """

    with driver.session() as session:
        session.run(
            query,
            relationships=relationships
        )

    print("✅ Project-skill relationships created.")

def main():
    """
    Run the complete database seeding process.
    """

    print("🚀 Starting CareerGraph database setup...")

    try:

        create_constraints()

        seed_skills()
        seed_users()
        seed_job_roles()
        seed_companies()
        seed_courses()
        seed_projects()

        seed_user_skills()
        seed_job_skills()
        seed_job_companies()
        seed_course_skills()
        seed_job_courses()
        seed_project_skills()

        print("\n🎉 CareerGraph database seeded successfully!")

    except Exception as error:

        print("\n❌ Database seeding failed.")
        print(f"Error: {error}")

    finally:

        # Close the database driver
        driver.close()


if __name__ == "__main__":
    main()