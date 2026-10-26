from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("pwd")

    return render_template("success.html", username=username)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003, debug=True)
    



