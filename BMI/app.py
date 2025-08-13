from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

@app.route("/", methods=["GET", "POST"])
def index():
    bmi = None
    category = None
    error = None

    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height = float(request.form["height"])

            if height <= 0:
                error = "Height must be greater than zero."
            else:
                bmi = calculate_bmi(weight, height)
                category = bmi_category(bmi)
        except ValueError:
            error = "Please enter valid numeric values."

    return render_template("index.html", bmi=bmi, category=category, error=error)

if __name__ == "__main__":
    app.run(debug=True)
