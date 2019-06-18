from pyrogram import Client, Filters


app = Client("663574960:AAGWfrBnjGYGSczuGHGLG60RVLMp6ebWteM", 605563,"7f2c2d12880400b88764b9b304e14e0b")

          
@app.on_message(Filters.command("delete"))
def main(client, message):
  for message in range(int(message.text.split(' ')[1]), int(message.text.split(' ')[2])):
    try:
        client.delete_messages(message.chat.id,message)
    except:
        continue


app.run()
