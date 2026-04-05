from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <h1>🤖 AI Chatbot</h1>
    <form action="/chat" method="post">
        <input name="message" placeholder="Say something..." />
        <button type="submit">Send</button>
    </form>
    '''

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.form["message"].lower()

    if msg == "hello":
        reply = "Hi 👋"
    elif msg == "how are you":
        reply = "I'm good 😄"
    elif msg == "bye":
        reply = "Goodbye 👋"
    else:
        reply = "I don't understand 🤔"

    return f"<h2>{reply}</h2><br><a href='/'>Back</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)