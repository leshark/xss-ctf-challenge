import os

from dotenv import load_dotenv
from flask import Flask

from logic import index, report
from validators import escape


def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config["IP_OR_DOMAIN_WITH_PORT"] = "{}:{}".format(os.environ["IP_OR_DOMAIN"], os.environ["PORT"])
    app.config["CAPTCHA_TOKEN"] = os.getenv("CAPTCHA_TOKEN")
    app.config["CAPTCHA_SITE_KEY"] = os.getenv("CAPTCHA_SITE_KEY")

    from jobs import rq
    rq.init_app(app)

    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/report', 'report', report, methods=["GET", "POST"])
    app.add_template_filter(escape, "e")

    return app
