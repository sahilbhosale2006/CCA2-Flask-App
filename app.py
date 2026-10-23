from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>CCA 2 - CI/CD Pipeline</h1>
    <h2>Hello! Flask Application is Running.</h2>
    <p>This application will be deployed using Jenkins, Docker and Kubernetes.</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)