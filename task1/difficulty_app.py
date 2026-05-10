import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

#Step-1:Difficulty Adjustment Logic
def get_next_difficulty(scores):

    # Minimum question count
    if len(scores) < 3:
        return "medium"

    avg_score = np.mean(scores)

    # Consistent low scores
    if all(score < 40 for score in scores):
        return "easy"

    # Consistent high scores
    if all(score > 70 for score in scores):
        return "hard"

    # Main logic
    if avg_score > 75:
        return "hard"

    elif avg_score < 35:
        return "easy"

    else:
        return "medium"

#Srep-2:Home Page
@app.route("/", methods=["GET", "POST"])
def home():

    result = ""
    entered_scores = ""

    if request.method == "POST":

        entered_scores = request.form["scores"]

        # Convert input string into list
        scores = list(map(int, entered_scores.split(",")))

        # Predict difficulty
        result = get_next_difficulty(scores)

    return render_template(
        "index.html",
        result=result,
        scores=entered_scores
    )

#Step-3:Simulation Testing
def simulation_test():

    test_cases = [
        [25, 30, 35],
        [50, 65, 60],
        [85, 80, 95],
        [72, 73, 74],
        [15, 10, 20]
    ]

    print("\n===== Simulation Test Results =====\n")

    for case in test_cases:

        result = get_next_difficulty(case)

        print(f"Scores: {case}")
        print(f"Next Difficulty: {result}")
        print("---------------------------------")

#Step-4: Main Function
if __name__ == "__main__":

    # Run simulation tests
    simulation_test()

    # Start Flask App
    app.run(debug=False)