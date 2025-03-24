from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    # Run the app on port 5000 and listen on all IP addresses (0.0.0.0)
    app.run(debug=True, host='0.0.0.0', port=5000)
