from flask import Flask, render_template


def create_app():
    """
    Application factory.

    Creates and configures the Flask application.
    """

    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static"
    )

    
    # -----------------------------------------------------
    # Register API routes
    # -----------------------------------------------------

    from app.routes import api

    app.register_blueprint(api)


    # -----------------------------------------------------
    # Frontend home page
    # -----------------------------------------------------

    @app.route("/")
    def home():
        """
        Render the CareerGraph frontend.
        """

        return render_template("index.html")


    return app