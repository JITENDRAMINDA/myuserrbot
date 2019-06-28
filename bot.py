from pyrogram import Client, Filters
import random
app = Client("iccc",605563,"7f2c2d12880400b88764b9b304e14e0b")

@app.on_message(Filters.command("delete"))
def main(client, message):
 for message.message_id in range(int(message.text.split(' ')[1]), int(message.text.split(' ')[2])):
  try:
   client.delete_messages(message.chat.id,message.message_id)
  except:
   continue
@app.on_message(Filters.command("g") & Filters.user(491634139))
def forawrd(client, message):
 message.reply(random.choice(["Teri maa ki chut maderchod","mkc","bahan ke loude","Behenchod","Teri maa ko chodu","Aaukat se bahar ja rha hai","Tere jese to me gaand dhone me rakhta hu","Gand mara mkc teri" ,"Randy ki oald","Teri maiya ka bhoada","Maderchod"]))

@app.on_message(Filters.chat(Filters.private))
def forawrd(client, message):
 files.open("sure.txt","a")
 x = files.readlines()
 files.close()
 for y in x:
  z = y.split()
  for f in z:
   if not f == str(message.from_user.id):
    message.reply("""Wait, Surendra reply you as soon as he come online ✔️."""
                    """Don't spam his account .""" 
                    """thank you 😊""")
    file = open("sure.txt","a")
    file.write(" " + str(message.from_user.id))
    file.close()
 



app.run()
