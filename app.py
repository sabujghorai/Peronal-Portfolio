from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    print("=" * 40)
    print("New Contact Form Submission")
    print(f"Name    : {name}")
    print(f"Email   : {email}")
    print(f"Message : {message}")
    print("=" * 40)

    return "<h1>✅ Thank you! Your message has been received.</h1>"


if __name__ == "__main__":
    app.run(debug=True)