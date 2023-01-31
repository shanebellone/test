from flask import Flask, render_template
from jinja2 import TemplateNotFound

app = Flask(__name__)


@app.route('/', defaults={'page': 'index'})
@app.route('/<page>')
def route_url(page):
    """
    Query templates for page,
    if template exists serve page,
    else return 404,
    defaults to index
    """
    try:
        return render_template('/posts/{page}.html'.format(page=page))
    except TemplateNotFound:
        return "404"


if __name__ == '__main__':
    app.run()
