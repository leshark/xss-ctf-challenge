from flask import current_app, request, render_template

from jobs import proceed_link
from validators import encode, url_valid, check_captcha


# our index page with custom logic vulnerable to XSS
def index():
    if request.args.get("text"):
        text = request.args.get("text")
        new_text = encode(text)
        return render_template("index.html", r_short="Your new shorten text: {}".format(new_text) if len(
            new_text) < len(text) else "Ops, cannot shorten your text", value=text)
    else:
        return render_template("index.html")


# example of a 'report to admin' page
def report():
    if request.method == "POST":
        link = request.form.get("link")
        captcha_response = request.form.get("g-recaptcha-response")

        user_passed_captcha = check_captcha(captcha_response)

        if url_valid(link) and user_passed_captcha:
            proceed_link.queue(link)
            return render_template("contact.html", result="Admin will check your problem shortly",
                                   site_key=current_app.config.get("CAPTCHA_SITE_KEY"))

        return render_template("contact.html", result="Input is not a valid url or refer to another site",
                               site_key=current_app.config.get("CAPTCHA_SITE_KEY"))

    return render_template("contact.html", site_key=current_app.config.get("CAPTCHA_SITE_KEY"))
