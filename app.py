from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        print(f"Username: {username}, Password: {password}")  # Logs to console
        return f"Logged in as {username}"
    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
