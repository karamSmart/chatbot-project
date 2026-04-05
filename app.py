from flask import Flask, request
import os
import datetime

app = Flask(__name__)

# الصفحة الرئيسية
@app.route("/")
def home():
    return '''
    <h1>🤖 AI Chatbot</h1>
    <form action="/chat" method="post">
        <input name="message" placeholder="Say something..." />
        <button type="submit">Send</button>
    </form>
    <br>
    <a href="/test">🧪 Test Page</a>
    '''

# الشات
@app.route("/chat", methods=["POST"])
def chat():
    msg = request.form["message"].lower()

    if msg == "hello":
        reply = "Hi 👋"
    elif msg == "how are you":
        reply = "I'm doing great 😄"
    elif msg == "time":
        reply = str(datetime.datetime.now())
    elif msg == "date":
        reply = str(datetime.date.today())
    elif msg == "your name":
        reply = "I'm Karam's AI Bot 🤖"
    elif msg == "bye":
        reply = "Goodbye 👋"
    else:
        reply = "I don't understand 🤔"

    return f"""
    <h2>Bot: {reply}</h2>
    <a href="/">⬅️ Back</a>
    """

# صفحة اختبار
@app.route("/test")
def test():
    return '''
    <h2>🧪 Test Page</h2>
    <ul>
        <li><a href="/ping">Ping</a></li>
        <li><a href="/info">Server Info</a></li>
    </ul>
    <a href="/">⬅️ Back</a>
    '''

# اختبار سريع
@app.route("/ping")
def ping():
    return "pong ✅"

# معلومات السيرفر
@app.route("/info")
def info():
    return {
        "status": "running",
        "time": str(datetime.datetime.now())
    }

# تشغيل السيرفر (مهم لـ Render)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)