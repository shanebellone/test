from flask import Flask, render_template, send_from_directory
from jinja2 import TemplateNotFound

from utilities.sitemap import generate_sitemap

app = Flask(__name__)


@app.route('/', defaults={'page': 'index'})
@app.route('/<page>/')
def route_url(page):
    match page:
        case "sitemap.txt":
            generate_sitemap()
            return send_from_directory('static', "sitemap.txt")
    try:
        return render_template('/posts/{page}.html'.format(page=page))
    except TemplateNotFound:
        return "404"


if __name__ == '__main__':

    app.run()
