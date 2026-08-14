import os

from dotenv import load_dotenv
from neo4j import GraphDatabase


# Load the .env file
load_dotenv()


# Read credentials
URI = os.getenv("COGNODB_URI")
USERNAME = os.getenv("COGNODB_USERNAME")
PASSWORD = os.getenv("COGNODB_PASSWORD")


print("URI:", URI)
print("USERNAME:", USERNAME)
print("PASSWORD loaded:", bool(PASSWORD))


try:

    # Create CognoDB driver
    driver = GraphDatabase.driver(
        URI,
        auth=(USERNAME, PASSWORD),
    )

    # Test connection
    driver.verify_connectivity()

    print()
    print("==============================")
    print("✅ COGNODB CONNECTION SUCCESS")
    print("==============================")


    # Test an actual Cypher query
    with driver.session() as session:

        result = session.run(
            "RETURN 1 AS test"
        )

        record = result.single()

        print("Query result:", record["test"])


    driver.close()


except Exception as error:

    print()
    print("==============================")
    print("❌ COGNODB CONNECTION FAILED")
    print("==============================")

    print(error)