from linebot import WebhookHandler
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)
from linebot.exceptions import InvalidSignatureError
from flask import request, abort, jsonify
import os
import json

# Initialize the webhook handler with your Channel Secret
handler = WebhookHandler(os.getenv('ChannelSecret'))

# Define your webhook endpoint function
def linebot(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Get the request body as text
        body = request.get_data(as_text=True)
        signature = request.headers.get('X-Line-Signature')

        try:
            # Handle the webhook event
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return 'OK'
    else:
        # Handle non-POST requests gracefully
        return jsonify({'message': 'Method not allowed'}), 405

# Define message event handler for handling text messages
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    # Get the user ID and text message from the event
    user_id = event.source.user_id
    msg = event.message.text

    # Process the received message
    if msg == '!清空':
        reply_msg = '已清空'
        # Implement logic for clearing data or performing specific actions
    elif msg == '!摘要':
        reply_msg = '尚未實作摘要功能'  # Placeholder for summary feature
    else:
        reply_msg = "哈囉你好嗎"

    # Send a reply message back to the user
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_msg)
    )

    # Return HTTP response OK
    return 'OK'
