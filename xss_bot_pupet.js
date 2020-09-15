const puppeteer = require('puppeteer');
require('dotenv').config();

const IP_OR_DOMAIN = process.env.IP_OR_DOMAIN;
const FLAG = process.env.FLAG;

const myArgs = process.argv.slice(2);

const url = myArgs[0];

(async () => {
    const browser = await puppeteer.launch({
        args: [
            '--disable-web-security',
            '--ignore-certificate-errors',
            '--no-sandbox',
            '--disable-setuid-sandbox'
        ],
        headless: true,
        ignoreHTTPSErrors: true,
    });
    const page = await browser.newPage();
    await page.setCookie({
        "name": "flag",
        "value": FLAG,
        "domain": IP_OR_DOMAIN,
        "path": "/",
        "httpOnly": false,
        "secure": false,
    });
    await page.goto(url, { waitUntil: 'networkidle0', timeout: 10000});
    console.log("[INFO] rendered page: " + url);
    await page.close();
    await browser.close();
})();