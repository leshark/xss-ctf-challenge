import subprocess

from flask_rq2 import RQ

rq = RQ()

info_log = open("info.log", "a")
error_log = open("error.log", "a")


@rq.job(timeout=15)
def proceed_link(link):
    subprocess.run(
        ["node", "xss_bot_pupet.js", link], timeout=15, stderr=error_log, stdout=info_log)
