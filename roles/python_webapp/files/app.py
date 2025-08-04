from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Hello DevOps Engineer, learning Ansible Tower AWX UI automation done"

if __name__ == "__main__":
    app.run()
