import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/", methods=["GET", "POST"])
def questionnaire():
    if request.method == "POST":
        family_history = request.form.get("family_history")
        exercise = float(request.form.get("exercise", 0))
        smoking = request.form.get("smoking")
        alcohol = float(request.form.get("alcohol", 0))
        chronic = request.form.get("chronic")
        mental_activity = int(request.form.get("mental_activity", 5))
        diet = int(request.form.get("diet", 3))
        sleep = float(request.form.get("sleep", 7))
        income = int(request.form.get("income", 5))
        pollution = int(request.form.get("pollution", 5))
        healthcare = int(request.form.get("healthcare", 2))
        social = float(request.form.get("social", 3))
        stress = int(request.form.get("stress", 5))

        # منطق تخمین طول عمر
        score = 80  # مقدار پایه طول عمر

        # تأثیر ورزش
        score += exercise * 0.5

        # تأثیر رژیم غذایی
        score += (diet - 3) * 1.5

        # تأثیر خواب
        score += (sleep - 7) * 2

        # تأثیر روابط اجتماعی
        score += social * 0.5

        # تأثیر استرس
        score -= stress * 1.2

        # تأثیر سابقه خانوادگی
        if family_history == "بله":
            score += 5

        # تأثیر سیگار و الکل
        if smoking == "بله":
            score -= 10
        score -= alcohol * 0.8  # مصرف بیشتر الکل تأثیر منفی دارد

        # تأثیر بیماری‌های مزمن
        if chronic and chronic.strip():
            score -= 7  # اگر فرد بیماری مزمن دارد، امتیاز کاهش می‌یابد

        # تأثیر فعالیت ذهنی
        score += (mental_activity - 5) * 1.2  # فعالیت ذهنی بیشتر تأثیر مثبت دارد

        # تأثیر آلودگی هوا
        score -= (pollution - 5) * 1.5  # آلودگی بیشتر تأثیر منفی دارد

        # تأثیر دسترسی به خدمات بهداشتی
        score += healthcare * 0.7  # مراجعه بیشتر به پزشک تأثیر مثبت دارد

        # محدود کردن مقدار طول عمر به بازه منطقی
        score = max(40, min(score, 120))

        result_message = f"طول عمر تخمینی: {round(score, 1)} سال"
        return render_template("result.html", result=result_message)

    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
