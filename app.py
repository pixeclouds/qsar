from flask import Flask, request, jsonify, render_template
from predict import predict_activity

app = Flask(__name__)

# Define a sample route
@app.route('/pred', methods=['GET'])
def hello():

    if request.is_json:
        data = request.json
        print(data)
    else:
        data = { "smiles": "N#CC1=C(N)OC(/C(C)=C/C)=C(CC)C1/C=C/C", "model":"c-qsar"}
    # return jsonify({'message': 'Hello, World!'})
    prediction = predict_activity(data)
    print(prediction)

    return jsonify({"pred":prediction})

# Define a route that accepts POST requests with JSON data
@app.route('/', methods=['GET'])
def echo():
     # Get JSON data from the request
    return "HELLO WORLD"  # Echo back the JSON data

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
