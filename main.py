from flask import Flask
# Imported from the greetings module on requirements.txt
from greetings.greetings_module import greetings

app = Flask(__name__)


# Open a second terminal and run the following command:
# curl -X POST http://localhost:8080/say_hello
@app.route('/say_hello', methods=['POST'])
def say_hello():
    hi = greetings()
    return hi


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
