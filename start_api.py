from flask import Flask, jsonify

import devil_names

app = Flask(__name__)

@app.route('/')
def get_random_devil_name():
    return jsonify(devil_names.get_random_devil_name())

@app.route('/devil/<index>')
def get_devil_name(index):
    try: 
        index = int(index)
        return jsonify(devil_names.get_devil_name(index))
    except ValueError:
        return jsonify(index+' is not a possible index for devil names.')

if __name__ == '__main__':
    app.run()