import requests
import json
class telegram_chatbot():
    def __init__(self):
        self.token = "1890935642:AAG2xBVHNYog-nwSkq5BVFwdDIP30_fKyHk"
        self.base = f"https://api.telegram.org/bot{self.token}"
    
    def get_updates(self, offset=None):
        url = self.base + "/getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset + 1)
        
        r = requests.get(url)
        return json.loads(r.content)
    def send_photo(self, photo, chat_id):
        url = self.base + "/sendPhoto?chat_id={}&photo={}".format(chat_id, photo)
        print(url)
        if photo is not None:
            requests.get(url)
    def send_message(self, msg, chat_id):
      
        url = self.base + "/sendMessage?chat_id={}&text={}".format(chat_id, msg)
        print(url)
        if msg is not None:
            requests.get(url)
        
