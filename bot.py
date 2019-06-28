from pyrogram import Client, Filters

app = Client("mcc",715451,"d2cba6f7bf5d1a45682da5bb9071a307")

@app.on_message(Filters.command("delete"))
def main(client, message):
 for message.message_id in range(int(message.text.split(' ')[1]), int(message.text.split(' ')[2])):
  try:
   client.delete_messages(message.chat.id,message.message_id)
  except:
   continue

@app.on_message(Filters.chat(Filters.private)
def forawrd(client, message):
 files.open("sure.txt","a")
 x = files.readlines()
 files.close()
 for y in x:
  z = y.split()
  for f in z:
   if not f == str(message.from_user.id):
   message.reply("""Wait, Surendra reply you as soon as he come online ✔️."""
                    Don't spam his account . 
                    thank you 😊""")
   file = open("sure.txt","a")
   file.write(" " + str(message.from_user.id))
   file.close()
 



app.run()
