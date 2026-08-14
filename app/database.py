import os

from dotenv import load_dotenv
from neo4j import GraphDatabase


# Load variables from .env
load_dotenv()


# Read CognoDB credentials from environment variables
COGNODB_URI = os.getenv("COGNODB_URI")
COGNODB_USERNAME = os.getenv("COGNODB_USERNAME", "cognodb")
COGNODB_PASSWORD = os.getenv("COGNODB_PASSWORD")


# Stop the application early if credentials are missing
if not COGNODB_URI or not COGNODB_PASSWORD:
    raise RuntimeError(
        "COGNODB_URI and COGNODB_PASSWORD must be set in .env"
    )


# Create the Neo4j driver.
# CognoDB communicates using the Bolt protocol.
driver = GraphDatabase.driver(
    COGNODB_URI,
    auth=(COGNODB_USERNAME, COGNODB_PASSWORD),
)


def verify_database_connection():
    """
    Verify that Python can connect to CognoDB.
    """

    try:
        driver.verify_connectivity()

        print("✅ Successfully connected to CognoDB!")

        return True

    except Exception as error:

        print("❌ Could not connect to CognoDB")
        print(f"Error: {error}")

        return False