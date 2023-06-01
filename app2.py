from flask import Flask, request, jsonify
import os

app = Flask(__name__)
processed_output = None

@app.route('/convert', methods=['POST'])
def convert_digit_to_word():
    digit = request.json.get('digit')
    
    words = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
    }
    
    result = words.get(digit, 'Invalid input. Please enter a digit from 0 to 9.')
    global processed_output
    processed_output = result
    
    return jsonify({'word': result})

@app.route('/get_output', methods=['GET'])
def get_processed_output():
    return processed_output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
