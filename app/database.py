import os

from dotenv import load_dotenv
from neo4j import GraphDatabase


# Load environment variables.
# Locally, values come from .env.
# On Render, values come from Render Environment Variables.
load_dotenv()


# Read CognoDB connection details.
COGNODB_URI = os.getenv("COGNODB_URI")
COGNODB_USERNAME = os.getenv("COGNODB_USERNAME", "cognodb")
COGNODB_PASSWORD = os.getenv("COGNODB_PASSWORD")


# Make sure required credentials exist.
if not COGNODB_URI or not COGNODB_PASSWORD:
    raise RuntimeError(
        "COGNODB_URI and COGNODB_PASSWORD must be set."
    )


# Create the Neo4j-compatible driver.
#
# CognoDB Cloud provides a secure Bolt URI:
# bolt+s://...
#
# The Neo4j Python driver communicates with CognoDB
# using the Bolt protocol.
driver = GraphDatabase.driver(
    COGNODB_URI,
    auth=(
        COGNODB_USERNAME,
        COGNODB_PASSWORD,
    ),
)


def verify_database_connection():
    """
    Check whether the application can connect to CognoDB.
    """

    try:
        driver.verify_connectivity()

        print("Successfully connected to CognoDB.")

        return True

    except Exception as error:

        print("Could not connect to CognoDB.")
        print(f"Error: {error}")

        return False