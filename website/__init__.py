import os

from flask import Flask, render_template, send_from_directory

from website.cv.cv import bp as cv_bp

# TODO: use environment variables to manage keys (dotenv)
# TODO: use proper sqlalchemy to allow for more backends


def create_app(test_config=None):
    app = Flask(
        __name__, instance_relative_config=True, static_folder="assets"
    )
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "website.sqlite"),
    )

    @app.route("/")
    @app.route("/index")
    def index():
        return render_template("index.html")

    app.register_blueprint(cv_bp, url_prefix="/cv")

    return app
