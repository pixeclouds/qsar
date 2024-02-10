from flask import Flask, request, jsonify, render_template
from predict import predict_activity

app = Flask(__name__)

# Define a sample route
@app.route('/', methods=['GET'])
def hello():

    if request.is_json:
        data = request.json
        print(data)
    else:
        data = { "smiles": "N#CC1=C(N)OC(C2=CC=CC=C2)=C(C(C)=O)C1C3=CC=C(Cl)C=C3", "model":"c-qsar"}
    # return jsonify({'message': 'Hello, World!'})
    prediction = predict_activity(data)
    print(prediction)

    return render_template('index.html', prediction=prediction)

# Define a route that accepts POST requests with JSON data
@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()  # Get JSON data from the request
    return jsonify(data)  # Echo back the JSON data

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
