from pyrogram import Client, Filters
import random
app = Client("icc",715451,"d2cba6f7bf5d1a45682da5bb9071a307")




@app.on_message(Filters.command("delete"))
def main(client, message):
 for message.message_id in range(int(message.text.split(' ')[1]), int(message.text.split(' ')[2])):
  try:
   client.delete_messages(message.chat.id,message.message_id)
  except:
   continue

@app.on_message(Filters.command("g"))
def main(client, message):
 if message.from_user.id == 491634139:
    client.send_message(
    chat_id=message.chat.id,
    text=random.choice(["Teri maa ki chut maderchod","mkc","bahan ke loude","Behenchod","Teri maa ko chodu","Aaukat se bahar ja rha hai","Tere jese to me gaand dhone me rakhta hu","Gand mara mkc teri" ,"Randy ki oald","Teri maiya ka bhoada","Maderchod"]),
    reply_to_message_id=message.reply_to_message.message_id
    )
    client.delete_messages(message.chat.id,message.message_id)

@app.on_message(Filters.private)
def forawrd(client, message):
 f = False
 files = open("sure.txt","r")
 x = files.readlines()
 files.close()
 for y in x:
  z = y.split()
  for f in z:
   if f == str(message.chat.id):
     f = True
 if not f:
    message.reply("Wait, Surendra reply you as soon as he come online ✔️. Don't spam his account . thank you 😊")
    file = open("sure.txt","a")
    file.write(" " + str(message.chat.id))
    file.close()
   
app.run()
