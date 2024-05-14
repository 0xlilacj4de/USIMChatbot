from flask import Flask, request, jsonify, render_template
from flask_bootstrap import Bootstrap
import os
import json
from query_engine import setup_query_engine, query_response

app = Flask(__name__)
Bootstrap(app)

# Setup the query engine once when the app starts
query_engine = setup_query_engine()

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_query = request.form['query']
    response = query_response(query_engine, user_query)
    return jsonify(response=str(response))

if __name__ == '__main__':
    # Ensure data directories exist
    os.makedirs('./contents', exist_ok=True)
    os.makedirs('./stores', exist_ok=True)
    app.run(debug=True)
