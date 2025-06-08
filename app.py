from flask import Flask, render_template, request
import google.generativeai as genai
import os

app = Flask(__name__, template_folder="app/templates")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise EnvironmentError("GEMINI_API_KEY not found in environment variables.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
        "gender": request.form['gender'],
        "height_cm": request.form['height_cm'],
        "weight_kg": request.form['weight_kg'],
        "goal": request.form['goal'],
        "activity_level": request.form['activity_level'],
        "health_issues": request.form.get('health_issues', ''),
        "training_days": request.form['training_days'],
        "equipment": request.form.get('equipment', '')
    }

    profile = (
        f"{data['first_name']} {data['last_name']} is a {data['age']}-year-old {data['gender']} "
        f"who is {data['height_cm']} cm tall and weighs {data['weight_kg']} kg. "
        f"Their main fitness goal is to {data['goal']}. "
        f"They are {data['activity_level']} and plan to train {data['training_days']} times per week. "
        f"Health concerns: {data['health_issues'] or 'none'}. "
        f"Available equipment: {data['equipment'] or 'none'}."
    )

    prompt = f"""
    Based on the following profile, create a customized 1-week fitness training plan with explanations:

    {profile}
    """

    response = model.generate_content(prompt)
    training_plan = response.text

    return render_template(
        'result.html',
        first_name=data['first_name'],
        profile_paragraph=profile,
        training_plan=training_plan
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
