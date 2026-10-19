from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return "Shasha Bot is LIVE! 🔥 - by Consider Mushaka"

@app.route('/webhook', methods=['GET','POST'])
def webhook():
    if request.method == 'GET':
        return request.args.get('hub.challenge', 'OK')
    return "Message received", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
