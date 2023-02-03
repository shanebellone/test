import os

from flask import Flask, render_template, send_from_directory
from jinja2 import TemplateNotFound

app = Flask(__name__)


@app.route('/', defaults={'page': 'index'})
@app.route('/<page>/')
def route_url(page, api=None):
    match page:
        case "sitemap.txt":
            return send_from_directory('static', "sitemap.txt")
    try:
        return render_template('/posts/{page}.html'.format(page=page))
    except TemplateNotFound:
        return "404"


if __name__ == '__main__':
    domain = "https://shanebellone.com/"
    path = "../templates/posts/"
    urls = [(domain + file[:-5]) for file in os.listdir(path)]
    with open(r'static/sitemap.txt', 'w') as sitemap:
        for url in urls:
            sitemap.write("%s\n" % url)

    app.run()
