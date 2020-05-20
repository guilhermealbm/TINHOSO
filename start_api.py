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

@app.route('/all')
def get_all_devil_names():
    return jsonify({'devil_names':devil_names.get_all_devil_names()})

@app.route('/new', methods = ['POST'])
def new_devil_name():
    return jsonify("Sorry you cannot add more demons, since you're not Guimarães Rosa. But POST method works just fine!")

if __name__ == '__main__':
    app.run()