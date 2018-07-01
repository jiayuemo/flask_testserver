from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<string:page_index>')
def render_static(page_index):
    return render_template("%s.html" % page_index)


@app.route('/')
def render_base_page():
    return render_template("basic.html")


if __name__ == '__main__':
    app.run()
