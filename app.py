from flask import Flask, render_template, request, redirect, url_for

# Create a Flask app
app = Flask(__name__)

# Initialize the counter
counter = 3181917

# Homepage
@app.route("/", methods=["GET", "POST"])
def home():
    global counter
    if request.method == "POST":
        # Increment the counter when the form is submitted
        counter += 1
        # Process form data (optional)
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        country = request.form.get("country")
        email = request.form.get("email")
        print(f"New joiner: {first_name} {last_name} from {country} ({email})")
        return redirect(url_for("home"))
    return render_template("index.html", counter=counter)

# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Resources Page
@app.route("/resources")
def resources():
    return render_template("resources.html")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)