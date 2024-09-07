import bot as bot
from chatbot import reply
mybot = bot.telegram_chatbot()
update_id = None


while True:
    updates = mybot.get_updates(offset=update_id)
    updates = updates["result"]
    
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                
                message = item["message"]["text"]
            except:
                message = None
            print(item)
            try:
                from_ = item["message"]["from"]["id"]
                try:
                    groupfrom_ = item['message']["chat"]["id"]
                    try:
                      myreply = reply(message,"3","2")
                
                      if myreply ==None:
                        pass
                      if type(myreply) == list:
                        try:
                            for i in myreply:
                                if i[0:4] == "http":
                                    mybot.send_photo(i, groupfrom_)
                                else:
                                    mybot.send_message(i, groupfrom_)
                        except:
                            for i in myreply:
                                if i[0:4] == "http":
                                    mybot.send_photo(i, from_)
                                else:
                                    mybot.send_message(i, from_)
                      else:
                            print("came to reply")
                            try:
                  
                                mybot.send_message(myreply, groupfrom_)
                            except:
                                mybot.send_message(myreply, from_)
        
                    except Exception as e:
                      print(f"Error: {e}")

                except:
                  print("passed twice")
            except:
                print("passed once")
            