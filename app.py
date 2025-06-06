import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/", methods=["GET", "POST"])
def questionnaire():
    if request.method == "POST":
        family_history = request.form.get("family_history")
        exercise = float(request.form.get("exercise", 0))
        smoking = request.form.get("smoking")
        diet = int(request.form.get("diet", 3))
        sleep = float(request.form.get("sleep", 7))
        income = int(request.form.get("income", 5))
        social = float(request.form.get("social", 3))
        stress = int(request.form.get("stress", 5))
        
        # Lifespan estimation logic
        score = 80
        score += exercise * 0.5
        score += (diet - 3) * 1.5
        score += (sleep - 7) * 2
        score += social * 0.5
        score -= stress * 1.2
        
        if family_history == "بله":
            score += 5
        if smoking == "بله":
            score -= 10
        
        result_message = f"طول عمر تخمینی: {round(score, 1)} سال"
        return render_template("result.html", result=result_message)
    
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
