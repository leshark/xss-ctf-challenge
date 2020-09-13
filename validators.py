from itertools import groupby
from urllib.parse import urlparse

import requests
from flask import current_app


# our vulnerable html escaping function
def escape(html):
    return str(html).replace("document", "").replace(".", "")


def encode(input_string):
    return "".join(str(len(list(g))) + k for k, g in groupby(input_string))


# check if submitted url is http(s) and refers to our domain/ip
def url_valid(link):
    try:
        result = urlparse(link)
        return all(
            [result.scheme in ["http", "https"], result.netloc == current_app.config.get("IP_OR_DOMAIN_WITH_PORT")])
    except ValueError:
        return False


def check_captcha(captcha_res):
    return requests.post(
        "https://www.google.com/recaptcha/api/siteverify",
        data={"secret": current_app.config.get("CAPTCHA_TOKEN"), "response": captcha_res}
    ).json().get("success")
