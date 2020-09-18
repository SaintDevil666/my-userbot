import datetime
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from time import sleep
app = Client("my_account")



@app.on_message(filters.command("type", prefixes=".") & filters.me)
def typing(app, message):
	orig_text = message.text.split(".type ", maxsplit=1)[1]
	text = orig_text
	tbp = "" # to be printed
	typing_symbol = "▒"

	while (tbp != orig_text):
		try:
			message.edit(tbp + typing_symbol)
			sleep(0.13)
			tbp = tbp + text[0]
			text = text[1:]

			message.edit(tbp)
			sleep(0.13)

		except FloodWait as e:
			sleep(e.x)

@app.on_message(filters.command("joined", prefixes=".") & filters.me)
def joined(app, message):
	try:
		for m in app.iter_chat_members(message.chat.id):
			if message.reply_to_message:
				if m.user.id == message.reply_to_message.from_user.id:
					timestamp = m.joined_date or app.get_messages(message.chat.id, 1).date,
					print(timestamp)
					value = datetime.datetime.fromtimestamp(timestamp[0]).strftime('%Y-%m-%d %H:%M:%S')
					message.edit("{0} joined this chat on {1}".format(m.user.first_name, value))
					break
	except Exception:
		pass

@app.on_message(filters.command("json", prefixes=".") & filters.me)
def printJson(app, message):
	app.send_message("me", "```" + str(message) + "```")
	message.delete()
	
@app.on_message(filters.command("load", prefixes=".") & filters.me)
def load(app, message):
	try:
		text = message.text.split(".load ", maxsplit=1)[1]
	except:
		text = "Uploading file"
	for i in range(26):
		try:
			message.edit(text + "." * ((i % 3) + 1) + "\n" + "█" * (i // 2) + "▒" * (13 - (i // 2)))
		except Exception:
			print(Exception)
		sleep(0.6)
	message.edit("Just kidding, bye")
	sleep(1)
	message.delete()

app.run()