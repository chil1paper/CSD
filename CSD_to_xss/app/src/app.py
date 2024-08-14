from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return """<h1>Welcome</h1>
    <script src='/static/main.js'></script>"""

if __name__ == "__main__":
    app.run("0.0.0.0", 5001)
