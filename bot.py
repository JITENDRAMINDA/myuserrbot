from pyrogram import Client, Filters


app = Client("663574960:AAGWfrBnjGYGSczuGHGLG60RVLMp6ebWteM", 605563,"7f2c2d12880400b88764b9b304e14e0b")

          
@app.on_message(Filters.command("add"))
def main(client, message):
  file = open("sure.txt" , "r")
  lines = file.readlines()
  file.close()
  message.reply(lines + 
   "☣️ ["+ message.reply_to_message.text+ "]" + "(" + message.text.split(' ')[1] + ")"
   )
  


app.run()
