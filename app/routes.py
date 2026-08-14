from flask import Blueprint, jsonify

from app.database import driver
from app.queries import (
    GET_ALL_SKILLS,
    GET_ALL_JOB_ROLES,
    GET_USER_SKILLS,
    GET_CAREER_MATCHES,
    GET_MISSING_SKILLS,
    GET_RECOMMENDED_COURSES,
    GET_JOB_COMPANIES,
    GET_RECOMMENDED_PROJECTS,
    CHECK_USER_EXISTS,
)


# All routes in this file will start with /api
api = Blueprint(
    "api",
    __name__,
    url_prefix="/api"
)


def execute_query(query, **parameters):
    """
    Execute a Cypher query using the Neo4j driver.

    Parameters are passed separately instead of being
    concatenated into the Cypher query.
    """

    with driver.session() as session:

        result = session.run(
            query,
            **parameters
        )

        return result.data()



# ---------------------------------------------------------
# Health Check
# ---------------------------------------------------------

@api.get("/health")
def health_check():
    """
    Check whether the Flask API and CognoDB are working.
    """

    try:

        # Simple database query
        execute_query("RETURN 1 AS status")

        return jsonify({
            "success": True,
            "api": "running",
            "database": "connected"
        })

    except Exception as error:

        print(f"Health check failed: {error}")

        return jsonify({
            "success": False,
            "api": "running",
            "database": "unavailable"
        }), 503



# ---------------------------------------------------------
# Skills
# ---------------------------------------------------------

@api.get("/skills")
def get_skills():
    """Return all available skills."""

    try:

        skills = execute_query(
            GET_ALL_SKILLS
        )

        return jsonify({
            "success": True,
            "data": skills
        })

    except Exception as error:

        print(f"Error loading skills: {error}")

        return jsonify({
            "success": False,
            "message": "Unable to load skills."
        }), 500


# ---------------------------------------------------------
# Job Roles
# ---------------------------------------------------------

@api.get("/jobs")
def get_jobs():
    """Return all available job roles."""

    try:

        jobs = execute_query(
            GET_ALL_JOB_ROLES
        )

        return jsonify({
            "success": True,
            "data": jobs
        })

    except Exception as error:

        print(f"Error loading jobs: {error}")

        return jsonify({
            "success": False,
            "message": "Unable to load job roles."
        }), 500


# ---------------------------------------------------------
# User Skills
# ---------------------------------------------------------

@api.get("/users/<user_id>/skills")
def get_user_skills(user_id):
    """Return skills belonging to a specific user."""

    try:

        skills = execute_query(
            GET_USER_SKILLS,
            user_id=user_id
        )

        return jsonify({
            "success": True,
            "data": skills
        })

    except Exception as error:

        print(f"Error loading user skills: {error}")

        return jsonify({
            "success": False,
            "message": "Unable to load user skills."
        }), 500


# ---------------------------------------------------------
# Career Matches
# ---------------------------------------------------------

@api.get("/users/<user_id>/career-matches")
def get_career_matches(user_id):
    """Find careers matching the user's skills."""

    try:
         # First make sure the user exists
        if not user_exists(user_id):

            return jsonify({
                "success": False,
                "message": "User not found."
            }), 404
        
        matches = execute_query(
            GET_CAREER_MATCHES,
            user_id=user_id
        )

        return jsonify({
            "success": True,
            "data": matches
        })

    except Exception as error:

        print(f"Error finding career matches: {error}")

        return jsonify({
            "success": False,
            "message": "Unable to calculate career matches."
        }), 500


# ---------------------------------------------------------
# Missing Skills
# ---------------------------------------------------------

@api.get("/users/<user_id>/missing-skills/<job_role_id>")
def get_missing_skills(user_id, job_role_id):
    """Find skills missing for a specific career."""

    try:

        skills = execute_query(
            GET_MISSING_SKILLS,
            user_id=user_id,
            job_role_id=job_role_id
        )

        return jsonify({
            "success": True,
            "data": skills
        })

    except Exception as error:

        print(f"Error finding missing skills: {error}")

        return jsonify({
            "success": False,
            "message": "Unable to calculate missing skills."
        }), 500


# ---------------------------------------------------------
# Recommended Courses
# ---------------------------------------------------------

@api.get("/users/<user_id>/courses/<job_role_id>")
def get_recommended_courses(user_id, job_role_id):
    """Recommend courses based on missing skills."""

    try:

        courses = execute_query(
            GET_RECOMMENDED_COURSES,
            user_id=user_id,
            job_role_id=job_role_id
        )

        return jsonify({
            "success": True,
            "data": courses
        })

    except Exception as error:

        print(f"Error finding courses: {error}")

        return jsonify({
            "success": False,
            "message": "Unable to load course recommendations."
        }), 500


# ---------------------------------------------------------
# Companies
# ---------------------------------------------------------

@api.get("/jobs/<job_role_id>/companies")
def get_job_companies(job_role_id):
    """Find companies associated with a career."""

    try:

        companies = execute_query(
            GET_JOB_COMPANIES,
            job_role_id=job_role_id
        )

        return jsonify({
            "success": True,
            "data": companies
        })

    except Exception as error:

        print(f"Error loading companies: {error}")

        return jsonify({
            "success": False,
            "message": "Unable to load companies."
        }), 500


# ---------------------------------------------------------
# Recommended Projects
# ---------------------------------------------------------

@api.get("/users/<user_id>/projects/<job_role_id>")
def get_recommended_projects(user_id, job_role_id):
    """Recommend projects based on missing skills."""

    try:

        projects = execute_query(
            GET_RECOMMENDED_PROJECTS,
            user_id=user_id,
            job_role_id=job_role_id
        )

        return jsonify({
            "success": True,
            "data": projects
        })

    except Exception as error:

        print(f"Error finding projects: {error}")

        return jsonify({
            "success": False,
            "message": "Unable to load project recommendations."
        }), 500

def user_exists(user_id):
    """
    Check whether a user exists in CognoDB.
    """

    result = execute_query(
        CHECK_USER_EXISTS,
        user_id=user_id
    )

    return len(result) > 0