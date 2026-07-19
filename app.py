from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/icons/<path:filename>")
def icons(filename):
    return send_from_directory("icons", filename)

@app.route("/image/<path:filename>")
def image(filename):
    return send_from_directory("image", filename)

@app.route("/featured-projects/<path:filename>")
def featured_projects(filename):
    return send_from_directory("featured Project image", filename)

if __name__ == "__main__":
    app.run(debug=True)