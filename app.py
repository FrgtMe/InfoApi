from flask import *
from pyrogram import *
from pyrogram.types import *
from threading import *
app = Flask(__name__)
client = Client("sjskak", api_id=24588661, api_hash="332058c74190c9a3739f43676f3a21e0", bot_token="6416928189:AAFE6PKs2EUS9zgRuHTXw7qtUK7f7dUiATE")
client.start();
@app.route('/info')
def info():
  username = request.args.get("uname")
  if not username:
    return "Misses some parameters!"
  user = client.get_users(username)
  user = str(user)
  return user

def run_flask():
  app.run(host='0.0.0.0', port=80)
Thread(target=run_flask).start();
idle()
