from pyrogram import Client, Filters


app = Client("663574960:AAGWfrBnjGYGSczuGHGLG60RVLMp6ebWteM", 605563,"7f2c2d12880400b88764b9b304e14e0b")

          
@app.on_message(Filters.command("add"))
def main(client, message):
  message.reply("▶️ ["+ message_to_reply.text+ "]" + "(" + message.text.split(' ')[1] + ")")
  


app.run()
