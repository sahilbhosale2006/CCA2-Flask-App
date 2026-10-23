from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>CCA 2 - CI/CD Pipeline</h1>
    <h2>Version 2 - Successfully Deployed!</h2>
    <p>Updated using GitHub, Jenkins, Docker and Kubernetes.</p>
    <p>Automated CI/CD Pipeline Demonstration.</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)