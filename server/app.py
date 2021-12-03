import os
from flask import Flask
from flask import render_template


app = Flask(__name__, template_folder='template')


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
