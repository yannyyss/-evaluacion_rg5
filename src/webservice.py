import csv
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/',methods=['GET'])
def read_csv():
    route = 'data/employees.csv'
    with open(route, 'r') as archivo_csv:
        doc = csv.DictReader(archivo_csv)
        list = []
        for linea in doc:
            list.append(linea)
        return jsonify(list)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")