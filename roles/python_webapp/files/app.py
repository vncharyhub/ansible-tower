from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hey DevOps Engineer, Hello from Flask via Nginx + Gunicorn + Ansible!"

if __name__ == "__main__":
    app.run()
