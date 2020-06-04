from flask import Flask, jsonify

# Create the Flask App
app = Flask(__name__)

# Create the Endpoint
@app.route('/')
def index():
    return 'Nav'

# Run the App
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=50)
