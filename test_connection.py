from app.database import driver


def test_database():
    """
    Run a simple Cypher query against CognoDB.
    """

    try:

        # Open a database session
        with driver.session() as session:

            # Execute a simple Cypher query
            result = session.run(
                "RETURN 'Hello from CareerGraph' AS message"
            )

            # Get the first returned record
            record = result.single()

            # Print the result
            print(record["message"])

    except Exception as error:

        print(f"❌ Database query failed: {error}")

    finally:

        # Close the driver when the test is finished
        driver.close()


if __name__ == "__main__":
    test_database()