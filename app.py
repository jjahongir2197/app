vfrom flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def quiz():
    score = ""

    if request.method == "POST":
        answer = request.form["q1"]

        if answer == "python":
            score = "Correct ✅"
        else:
            score = "Wrong ❌"

    return render_template("quiz.html", score=score)

if __name__ == "__main__":
    app.run(debug=True)
