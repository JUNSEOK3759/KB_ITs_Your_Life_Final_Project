import os
from flask_cors import CORS
from flask import Flask, jsonify, request
import main

app = Flask(__name__)
app.config['DEBUG'] = True
CORS(app)


@app.route('/react_to_flask', methods=['POST'])
def react_to_flask():
    parsed_request = request.files.get('file')
    fileName = request.form.get('fileName')

    dir_path = '../test/'
    saved_file_path = os.path.join(dir_path, fileName)
    parsed_request.save(saved_file_path)  # saved_file_path 경로에 받은 file 저장

    data = ['123','456','789']
    # target = ['./test/ex15.jpg']
    # data = run(target)
    return data

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)