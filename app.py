from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        birth_date = request.form.get("birth_date")
        gender = request.form.get("gender")
        address = request.form.get("address")
        country = request.form.get("country")
        city = request.form.get("city")
        region = request.form.get("region")
        postal_code = request.form.get("postal_code")

        # Process the data (Save to database, etc.)
        print(f"Received: {full_name}, {email}, {phone}, {birth_date}, {gender}, {address}, {country}, {city}, {region}, {postal_code}")

        return "Registration Successful!"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
