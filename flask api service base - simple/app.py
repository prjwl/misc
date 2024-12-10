from flask import Flask, jsonfy

app = Flask(__name__)


@app.route('/about', methods=['GET'])
def get_info():
    return jsonfy(
        {
            'status': True,
            'data': {},
            'message': "It's a sample template to build quick and simple apis."
        }
    ), 200


if __name__ == "__main__":
    app.run(port=4242)
