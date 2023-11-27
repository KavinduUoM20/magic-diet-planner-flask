from flask import Flask, render_template, request, url_for, redirect
#import pickle
#import numpy as np

app = Flask(__name__)


@app.route('/')
def load_index():
    return render_template('index.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    return render_template('index.html', a="15%", b="34.5", c="45")


if __name__ == '__main__':
    app.run(debug=True)
