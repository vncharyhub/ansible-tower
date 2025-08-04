from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Hello from Flask via Nginx + Gunicorn + Ansible! New Version V1"

if __name__ == "__main__":
    app.run()
