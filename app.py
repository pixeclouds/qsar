from flask import Flask, request, jsonify, render_template
from predict import predict_activity
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# this is a comment

@app.route('/predict', methods=['POST'])
def hello():

    if request.is_json:
        data = request.json
        print(data)
    else:
        data = { "smiles": "Cl#CC1=C(N)OC(/C(C)=C/C)=C(CC)C1/C=C/C", "model":"c-qsar"}
    prediction = predict_activity(data)
    print(prediction)

    return jsonify({"activity":prediction})


@app.route('/', methods=['GET'])
def echo():

    return jsonify({"message":"Server is up and running"}) 

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
