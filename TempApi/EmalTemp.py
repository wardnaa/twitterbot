import re
import random
import requests
import time
from bs4 import BeautifulSoup
# @ wardana 02--7-2020
class TempMail(object):

    def __init__(self, proxy=None):
        self.sessions = requests.Session()
        self.proxy = proxy
        self.headers = {
            'Connection': 'keep-alive',
			'Pragma': 'no-cache',
			'Cache-Control': 'no-cache',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
			'DNT': '1',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
			'Accept-Language': 'en-US,en;q=0.5',
        }

        self.sessions.headers.update(self.headers)

    def createEmail(self):
        Sessions = self.sessions.get('https://tempmail.net/en/', proxies=self.proxy)
        get_Email = re.compile('<input id="eposta_adres" type="text" class="adres-input" value="(.+?)" readonly>').findall(Sessions.text)
        Email = ''.join(get_Email) or "empty"

        if (Email != "empty"):
            return Email

    def get_inbox_message_id(self):
        time.sleep(1.5)
        Sessions = self.sessions.get('https://tempmail.net/en/', proxies=self.proxy)
        get_inbox = re.compile('<li class="mail " id="(.+?)">').findall(Sessions.text)
        inbox = ''.join(get_inbox) or "empty"

        if (inbox != "empty"):
            return inbox


    def get_inbox_message(self, inbox_id):
        time.sleep(1.5)
        full_url = 'https://tempmail.net/en/{msg_id}/'.format(msg_id=str(inbox_id))
        Sessions = self.sessions.get(full_url, proxies=self.proxy)
        get_message_id = re.compile('<iframe src="(.+?)" style="width:100%;display:block;min-height:208px;"').findall(Sessions.text)
        message_id = ''.join(get_message_id) or "empty"

        if (message_id != "empty"):
            return message_id


    def read_inbox_message(self, message_id):
        inbox_link = self.sessions.get(message_id, proxies=self.proxy)
        # Sessions = self.sessions.get(inbox_link, proxies=self.proxy)
        message = inbox_link.text or "empty"

        if (message != "empty"):
            return message

    #GATAU PALING JUGA ERROR
    def auto_verify_mail(self, msg_id):
        message_id = self.get_inbox_message(msg_id) or "empty"

        if (message_id != "empty"):
            read_message_id = self.read_inbox_message(msg_id)

            PerasaanMu = True

            try:
                for HatiIni in read_message_id:
                    links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', HatiIni)

                    self.sessions.get(links)

            except:
                PerasaanMu = False

                if (PerasaanMu != False):
                    return "Verify akun berhasil!"

                else:
                    return "Verify akun gagal!"


# Email = TempMail()

# temporary = Email.createEmail()
# print("Your Temporary Email : {email}".format(email=temporary))
# print("Wating for ibox Message : ")
# while True:
#     inbox_id = Email.get_inbox_message_id()
#     boxid = inbox_id or "empty"
#     if (boxid != "empty"):
#         print("inbox meesage id : {id}".format(id=boxid))
#         print("Get Message from ibox_id...")
#         read_inbox = Email.get_inbox_message(boxid)
#         read_id = read_inbox or "empty"
#         if (read_id != "empty"):
#             print("Reading The Message From box_id...")
#             message_box = Email.read_inbox_message(read_id)
#             readable_msg = BeautifulSoup(message_box, "lxml").text
#             file = open("message.txt", "w")
#             file.write(readable_msg)
#             file.close()
            

