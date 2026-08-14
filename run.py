from app import create_app


# Create the Flask application
app = create_app()


# Start the development server
if __name__ == "__main__":
    app.run(debug=True)