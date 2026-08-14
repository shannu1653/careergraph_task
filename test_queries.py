from app.database import driver
from app.queries import (
    GET_ALL_SKILLS,
    GET_USER_SKILLS,
    GET_CAREER_MATCHES,
    GET_MISSING_SKILLS,
    GET_RECOMMENDED_COURSES,
)


def run_query(query, **parameters):
    """
    Execute a Cypher query and return all records as dictionaries.
    """

    with driver.session() as session:

        result = session.run(
            query,
            **parameters
        )

        return result.data()


def main():
    """
    Test the important CareerGraph queries.
    """

    print("\n===== ALL SKILLS =====")

    skills = run_query(GET_ALL_SKILLS)

    for skill in skills:
        print(skill)


    print("\n===== USER SKILLS =====")

    user_skills = run_query(
        GET_USER_SKILLS,
        user_id="user_001"
    )

    for skill in user_skills:
        print(skill)


    print("\n===== CAREER MATCHES =====")

    matches = run_query(
        GET_CAREER_MATCHES,
        user_id="user_001"
    )

    for match in matches:
        print(match)


    print("\n===== MISSING SKILLS =====")

    missing = run_query(
        GET_MISSING_SKILLS,
        user_id="user_001",
        job_role_id="role_backend_developer"
    )

    for skill in missing:
        print(skill)


    print("\n===== RECOMMENDED COURSES =====")

    courses = run_query(
        GET_RECOMMENDED_COURSES,
        user_id="user_001",
        job_role_id="role_backend_developer"
    )

    for course in courses:
        print(course)


    # Close the database driver
    driver.close()


if __name__ == "__main__":
    main()