from pandas import json

import urllib
import urllib2

from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
    """
    extract an e-mail from web page and save i to e_mail
    """
    email = False  # have we already met an e-mail tag
    complete = False  # have we already extracted an e-mail
    e_mail = ""  # an e-mail

    def handle_starttag(self, tag, attrs):
        if not self.complete and self.email and tag == "input":  # if we have no e-mail yet and
            # we had already have e-mail tag and now we have input tag

            self.e_mail = attrs[1][1]  # save e-mail
            self.email = False
            self.complete = True  # mark that we have already have an e-mail

    def handle_data(self, data):
        if data == "E-Mail":
            self.email = True  # mark that we have an e-mail tag


urllib2.install_opener(urllib2.build_opener(urllib2.HTTPCookieProcessor))  # make cookies


def auth(login, pas):
    """
    make auth on login.kpi.ua
    :param login: login
    :param pas: password
    :return: True if success
    """

    params = urllib.urlencode({
        'Login': login,
        'Password': pas
    })
    f = urllib2.urlopen(
        "http://login.kpi.ua/auth/signin.json",
        params)
    if json.loads(f.read())["res"] == "logged":  # is auth success
        return True
    return False


def main(login, pas):
    # make auth
    auth_res = auth(login, pas)
    if auth_res:  # is auth is success
        # parse e-mail
        parser = MyHTMLParser()
        parser.feed(urllib2.urlopen("http://login.kpi.ua").read())
        return parser.e_mail
    else:
        return "can't auth"







