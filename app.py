from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from jabebot import ask, append_interaction_to_chat_log
app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-random-string'

@app.route('/davidbot', methods=['POST'])
def david():
    incoming_msg = request.values['Body']
    chat_log = session.get('chat_log')
    answer = ask(incoming_msg, chat_log)
    session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer, chat_log)
    msg = MessagingResponse()
    msg.message(answer)
    return str(msg)

if __name__ == '__main__':
    app.run(debug=True)