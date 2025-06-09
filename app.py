import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/", methods=["GET", "POST"])
def questionnaire():
    if request.method == "POST":
        # Retrieve basic questions
        family_history = request.form.get("family_history")
        exercise = float(request.form.get("exercise", 0))
        smoking = request.form.get("smoking")
        alcohol = float(request.form.get("alcohol", 0))
        pollution = int(request.form.get("pollution", 5))
        healthcare = int(request.form.get("healthcare", 2))
        social = float(request.form.get("social", 3))
        stress = int(request.form.get("stress", 5))
        
        # Retrieve additional luxury questions
        nutrition = int(request.form.get("nutrition", 5))
        sleep_quality = float(request.form.get("sleep_quality", 5))
        lifestyle = int(request.form.get("lifestyle", 5))
        mental_balance = int(request.form.get("mental_balance", 5))
        entertainment = int(request.form.get("entertainment", 5))
        work_env = int(request.form.get("work_env", 5))
        tech_experience = int(request.form.get("tech_experience", 5))
        self_belief = int(request.form.get("self_belief", 5))
        
        # Calculate the longevity score with a base score of 80 years
        score = 80
        
        # Effects on longevity
        score += exercise * 0.5                            # Regular exercise improves longevity
        score += (nutrition - 5) * 1.5                       # Better nutrition than average adds points
        score += (sleep_quality - 5) * 1.8                   # Quality sleep relative to average (5) boosts score
        score += (lifestyle - 5) * 1.2                       # Overall lifestyle satisfaction factor
        score += (mental_balance - 5) * 1.2                  # Better mental equilibrium has a positive effect
        score += social * 0.5                              # More social interactions yield benefits
        score -= stress * 1.2                              # Higher stress detracts from longevity
        
        # Genetic and habit factors
        if family_history == "بله":
            score += 5                                   # Favorable genetic background adds points
        if smoking == "بله":
            score -= 10                                  # Smoking has a significant negative impact
        score -= alcohol * 0.8                           # Alcohol consumption reduces longevity
        
        # Environmental and healthcare factors
        score -= (pollution - 5) * 1.5                     # Living in heavily polluted areas deducts points
        score += healthcare * 0.7                        # Better access to healthcare is positive
        
        # Additional lifestyle and psychological factors
        score += (entertainment - 5) * 1.0                 # Enjoyment in leisure activities adds a bonus
        score += (work_env - 5) * 1.0                      # Positive work or study environment is beneficial
        score += (tech_experience - 5) * 0.5               # Comfort with modern technology adds marginally
        score += (self_belief - 5) * 1.0                   # Confidence in personal success boosts longevity
        
        # Limit final score to a realistic range: between 40 and 120 years
        score = max(40, min(score, 120))
        result = round(score, 1)
        
        return render_template("result.html", result=result)
    
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
