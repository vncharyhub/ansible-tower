from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Hello DevOps Engineer, learning Ansible Tower AWX UI automation SUCCESSFULLY COMPLETED"

if __name__ == "__main__":
    app.run()
