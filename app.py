from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    print("=" * 50)
    print("New Contact Form Submission")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Message: {message}")
    print("=" * 50)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)