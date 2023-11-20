#!/usr/bin/env python3
# -*- coding: utf-8 -*-

config = {
    'API_KEY' : "212817d980b9a03add91e5814d02"
}

class API(object):
    def __init__(self, apikey):
        self.apikey = apikey

    def renderHTML(self, templateHTML, title, text):
        return (templateHTML.format(title=title, text=text))

if __name__ == '__main__':
    a = API(config['API_KEY'])

    templateHTML = """<!DOCTYPE html>
<html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>{title}</title>
    </head>
    <body>
        <p>{text}</p>
    </body>
</html>"""

    text = "This is text !"
    print(a.renderHTML("<p>{self.__init__.__globals__}</p>", "Vuln web render App", text))

# "<p>{text.__init__}</p>"
# "<p>{self.__init__.__globals__}</p>"
# "<p>{self.__init__.__globals__[config][API_KEY]}</p>"
