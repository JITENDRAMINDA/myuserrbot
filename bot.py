from pyrogram import Client, Filters


app = Client('666639160:AAEtopjBMU5r_i_UROx8PTWSSOtIrU6V7W8',605563,"7f2c2d12880400b88764b9b304e14e0b")



u = '-1001130956369'
s = '-1001274887387'


@@app.on_message(Filters.chat(int(s)) & Filters.text & ~ Filters.edited)

def forawrd(client, message):

    mes = client.send_message(int(u), "**" + message.text + "**")
    file = open("sure.txt" , "r")
    lines = file.readlines()
    file.close()
    for line in lines:
         files = open("sure.txt" , "w")
         files.write( line + " " + str(message.message_id) +  " " + str(mes.message_id))
         files.close()       




@app.on_message(Filters.chat(int(s)) & Filters.sticker)

def forawrd(client, message):

   client.send_sticker(int(u),message.sticker.file_id)
            
@app.on_message(Filters.chat(int(s)) & Filters.text & Filters.edited)

def forawrd(client, message):

  file = open("sure.txt" , "r")
  lines = file.readlines()
  file.close()
  for line in lines:
    x = line.split()
    id = str(message.message_id)
    if id in x:
      client.edit_message_text(int(u),int(x[x.index(id)+1]), "**" + message.text + "**" )



app.run()
