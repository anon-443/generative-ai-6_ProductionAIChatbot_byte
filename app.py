import json, os, re
from pathlib import Path
from flask import Flask, jsonify, request

app=Flask(__name__)
BLOCKED=[r"steal.*password", r"exfiltrat", r"make.*malware", r"bypass.*authentication"]

def safe(text): return not any(re.search(p,text.lower()) for p in BLOCKED)

class DemoProvider:
    def reply(self, message, context=""):
        return f"Demo response: I received your request. Context available: {bool(context)}. Replace DemoProvider with a documented model adapter before production."

provider=DemoProvider()
@app.get('/')
def home(): return jsonify({'service':'production-ai-chatbot','status':'ok'})
@app.post('/chat')
def chat():
    body=request.get_json(force=True); msg=str(body.get('message','')).strip(); context=str(body.get('context',''))
    if not msg: return jsonify({'error':'message is required'}),400
    if not safe(msg): return jsonify({'error':'request blocked by safety policy'}),400
    answer=provider.reply(msg,context)
    return jsonify({'answer':answer,'model':os.getenv('CHAT_MODEL','demo'),'safety':'passed'})
if __name__=='__main__': app.run(host='0.0.0.0',port=8000,debug=False)
