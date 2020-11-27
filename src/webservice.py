import csv
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/',methods=['GET'])
def read_csv():
    doc = csv.reader('data/employees.csv')
    return jsonify(doc)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")