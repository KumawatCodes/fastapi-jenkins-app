from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message' : "hello from flask in docker and this check of webhook",
        'status': 'Live'
    })

@app.route("/health")
def health():
    return jsonify({"status" : 'health'})

@app.route('/workcheck')
def check():
    return jsonify({'working':'absolutely'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)