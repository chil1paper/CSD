from flask import Flask

app = Flask(__name__)

@app.route("/register", methods=["GET", "POST"])
def index():
    return """<h1>The current page is /register</h1>"""

@app.route("/login", methods=["GET", "POST"])
def login():
    return """<h1>The current page is /login</h1>"""

@app.route("/404", methods=["GET", "POST"])
def page_404():
    return """<h1>The current page is /404</h1>"""

if __name__ == "__main__":
    app.run("0.0.0.0", 5001)
