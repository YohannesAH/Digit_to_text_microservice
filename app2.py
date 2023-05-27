from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_digit_to_word():
    data = request.get_json()
    digit = data.get('digit')

    words = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
    }

    result = words.get(digit, 'Invalid input. Please enter a digit from 0 to 9.')

    return jsonify({'word': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
