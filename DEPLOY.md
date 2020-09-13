## Installation(UNIX):

#### install redis and nodejs
`apt install redis nodejs`

#### install npm packages
`npm i dotenv puppeteer`

install your distro dependencies for puppeteer at stated [here](https://github.com/puppeteer/puppeteer/blob/main/docs/troubleshooting.md)

#### install python libraries
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Installation(WINDOWS):
**currently not supported** because of the limitations of python rq.
However you may change backend worker to the one supporting windows (i.e celery).
Other steps of installation should remain the same. 
(You may need to change IP_OR_DOMAIN to `localhost` later in configuration)

## Configuration:
Create .env file in your project root directory with such content:
```
# default settings for testing on local machine
IP_OR_DOMAIN=127.0.0.1
PORT=5000
CAPTCHA_TOKEN=your_google_captcha_token_here
CAPTCHA_SITE_KEY=your_google_captcha_site_key_here
FLAG=flag{simple_xss_task}
```
Change values if needed <br>
Don't forget to uncomment html commentary in templates/contact.html

## Running

#### Start redis on your server
`redis-server`

> remember to activate virtual environment before running next commands

#### Run in the root directory
`rq worker`

#### Run the app with:
`python wsgi.py` <br>
...or run with gunicorn <br>
`gunicorn 'wsgi:create_app()'` <br>
more info about gunicorn [here](https://docs.gunicorn.org/en/latest/run.html)