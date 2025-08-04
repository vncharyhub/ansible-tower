from flask import Flask, render_template
import os

# Set the base directory of the script
base_dir = os.path.dirname(os.path.abspath(__file__))

# Point Flask to the templates folder explicitly
app = Flask(__name__, template_folder=os.path.join(base_dir, 'templates'))

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
