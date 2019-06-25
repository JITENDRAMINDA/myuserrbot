from pyrogram import Client, Filters

app = Client("mcc",715451,"d2cba6f7bf5d1a45682da5bb9071a307")

@app.on_message(Filters.command("delete"))
def main(client, message):
 for message.message_id in range(int(message.text.split(' ')[1]), int(message.text.split(' ')[2])):
  try:
   client.delete_messages(message.chat.id,message.message_id)
  except:
   continue

app.run()
