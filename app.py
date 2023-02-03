from flask import Flask, render_template, send_from_directory
from jinja2 import TemplateNotFound

from utilities.access_control import request_authorization
from utilities.sitemap import generate_sitemap

app = Flask(__name__)


@app.route('/', defaults={'page': 'index'})
@app.route('/<page>/')
def route_url(page):
    if request_authorization() is False:
        return "403 - Forbidden"
    match page:
        case "robots.txt":
            return send_from_directory('static', "robots.txt")
        case "sitemap.txt":
            generate_sitemap()
            return send_from_directory('static', "sitemap.txt")
        case other:
            try:
                return render_template('/posts/{page}.html'.format(page=page))
            except TemplateNotFound:
                return "404 - Not Found"


if __name__ == '__main__':
    app.run()
