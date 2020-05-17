from flask import Flask, jsonify

import devil_names

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify(devil_names.get_devil_name())

if __name__ == '__main__':
    app.run()