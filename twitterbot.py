from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from TempApi.EmalTemp import *
from bs4 import BeautifulSoup as Soup
from element import *
import time
import random
import os

path = "users/humanname.list"


class account(object):

    def __init__(self, proxy=None):
        self.user = TempMail()
        self.proxy = proxy

    def email(self):
        emailTemp = self.user.createEmail()
        return emailTemp

    def verificationCode(self):
        time.sleep(2)
        get_inbox_id = self.user.get_inbox_message_id()
        inbox_id = get_inbox_id or "empty"

        if (inbox_id != "empty"):
            time.sleep(1)
            get_message = self.user.get_inbox_message(inbox_id)
            message = get_message or "empty"

            if (message != "empty"):
                read_message = self.user.read_inbox_message(message)
                # convert twiiter email to file xml
                with open("codetemp.xml", 'w') as file:
                    file.write(read_message)

                 # TODO SCRAPING VERIFICATION CODE FROM TWITER
                # MAYBE YES MAYBE NO
                time.sleep(2)
                with open("codetemp.xml", 'r') as file:
                    data = file.read()
                    scraping = Soup(data, "lxml")
                    list = scraping.table.find_all("tr")[12:]

                    codeVerify = []
                    for codein in list:
                        data = codein.td.text
                        codeVerify.append(data.replace(" ", ""))

                    return codeVerify[0]
    

class username(object):

    def __init__(self, path):
        self.path = path
    
    def user(self):
        with open(self.path, "r") as files:
            data = files.readlines()
            name = []

            for human in data:
                name.append(human)

            awal = "".join(random.choice(name))
            longname = awal.replace("\n", "").lower()
            num = random.randint(300, 1000)
            return f"{longname}_{num}"

#################################################
# property

class twiterbot(object):

    def __init__(self, username, author):
        self.options = Options()
        self.options.add_argument("--headless")
        self.options.add_argument("window-size=1920x1080")
        self.twitbot = webdriver.Chrome(options=self.options)
        self.username = username
        self.password = "d2FyZGFuYQo={user}".format(user=username)
        self.element = element()
        self.emailtemp = account()
        self.author = author
        self.twitbot.get("https://mobile.twitter.com/i/flow/signup")
    
    def infouser(self):

        time.sleep(2)
        # TODO input name to table name
        name = self.username
        time.sleep(1)
        print("\n[ $ ] Usernamebot -> {name}".format(name=name))
        time.sleep(1)
        table_name = self.twitbot.find_element_by_xpath(self.element._table_name())
        table_name.send_keys(name)
        time.sleep(1)

        # TODO change from phone to email
        change_email = self.twitbot.find_element_by_xpath(self.element._change_to_email())
        change_email.click()
        time.sleep(0.5)

        # TODO input email to table email
        email = self.emailtemp.email() or "empty"
        
        if (email != "empty"):
            table_email = self.twitbot.find_element_by_xpath(self.element._table_email())
            table_email.send_keys(email)

            # TODO input value to date of birth form
            # MONTH
            month_val = random.randint(1, 12)
            table_month = self.twitbot.find_element_by_xpath(self.element._tgl_month())
            select_month = Select(table_month)
            time.sleep(0.5)
            select_month.select_by_value(str(month_val))

            #DAY
            day_val = random.randint(1, 28)
            table_day = self.twitbot.find_element_by_xpath(self.element._tgl_day())
            select_day = Select(table_day)
            time.sleep(0.5)
            select_day.select_by_value(str(day_val))

            #YEAR
            year_val = random.randint(1980, 1999)
            table_year = self.twitbot.find_element_by_xpath(self.element._tgl_year())
            select_year = Select(table_year)
            time.sleep(0.5)
            select_year.select_by_value(str(year_val))
            time.sleep(1)
            print(f"[ $ ] Bot birthday -> {month_val}-{day_val}-{year_val}")
            time.sleep(1)
            print("[ $ ] Temporary Email -> {email}".format(email=email))
            self.signup()
    
    def signup(self):

        # TODO signup function
        #next button
        time.sleep(1)
        next_button1 = self.twitbot.find_element_by_xpath(self.element._next_button())
        next_button1.click()
        time.sleep(1)
        next_button2 = self.twitbot.find_element_by_xpath(self.element._next_button())
        next_button2.click()

        # signup button
        # TODO click signup button
        signup_button = self.twitbot.find_element_by_xpath(self.element._sign_up_button())
        signup_button.click()
        time.sleep(1)

        # TODO input verification code to verifcode table
        while True:
            verification_code = self.emailtemp.verificationCode() or "empty"
            if verification_code != "empty":
                print("[ $ ] Verification Code -> {code}".format(code=verification_code))
                break
            
        if (verification_code != "empty"):
            global mau
            verification_table = self.twitbot.find_element_by_xpath(self.element._table_verif_code())
            verification_table.send_keys(verification_code)
            time.sleep(1)
            next_button3 = self.twitbot.find_element_by_xpath(self.element._next_button())
            next_button3.click()

            # TODO input password to password table
            try:
                time.sleep(2)
                password = self.password
                password_table = self.twitbot.find_element_by_xpath(self.element._table_password())
                password_table.send_keys(password)
                time.sleep(1)
                print("[ - ] Bot Account Password -> {paswd}".format(paswd=password))
            
            except Exception as e:
                time.sleep(1)
                print('\n[ X ] Bot Detected Please Use Proxy...')
                time.sleep(1)
                print("[ - ] Bot Shutingdown...")
                mau = "gamau"
            
            kondisi = mau or "empty"

            if (kondisi == "empty"):
                # TODO click Next until die!
                time.sleep(1)
                next_button4 = self.twitbot.find_element_by_xpath(self.element._next_button())
                next_button4.click()
                time.sleep(1)
                skip_button1 = self.twitbot.find_element_by_xpath(self.element._skip_button())
                skip_button1.click()
                time.sleep(1)
                skip_button2 = self.twitbot.find_element_by_xpath(self.element._skip_button())
                skip_button2.click()
                time.sleep(1)
                skip_button3 = self.twitbot.find_element_by_xpath(self.element._skip_button())
                next_button3.click()
                time.sleep(1)
                skip_button4 = self.twitbot.find_element_by_xpath(self.element._skip_button())
                skip_button4.click()
                time.sleep(1)
                skip_button5 = self.twitbot.find_element_by_xpath(self.element._skip_button())
                skip_button5.click()
                time.sleep(1)
                skip_finall6 = self.twitbot.find_element_by_xpath(self.element._skip_for_now())
                skip_finall6.click()

                # TODO Search account to follow @AWardanaaa
                time.sleep(1)
                search_bar = self.twitbot.find_element_by_xpath(self.element._search_bar())
                search_bar.send_keys(self.author)
                time.sleep(1)

                # TODO Click the account
                time.sleep(1)
                account_button = self.twitbot.find_element_by_xpath(self.element._my_profile())
                account_button.click()
                time.sleep(1)

                # TODO Click the follow button 
                time.sleep(1)
                follow_button = self.twitbot.find_element_by_xpath(self.element._follow_button())
                follow_button.click()

                # TODO Save USername and password in file bot.txt
                time.sleep(1)
                self.saveAccount()

                # TODO logout from bot account
                time.sleep(1)
                profile_button = self.twitbot.find_element_by_xpath(self.element._logout_profile())
                profile_button.click()
                time.sleep(1)

                logout_button = self.twitbot.find_element_by_xpath(self.element._logout_account())
                logout_button.click()
                time.sleep(1)

                config_logout_button = self.twitbot.find_element_by_xpath(self.element._logout_finall())
                time.sleep(1)
            
            else:
                self.twitbot.quit()

            
            
    
    def saveAccount(self):
        time.sleep(1)
        usernamebot = self.twitbot.find_element_by_xpath(self.element._username_bot()).text
        passwordbot = self.password

        with open('bot.txt', 'a+') as botfile:
            datas = f"\nusername = {usernamebot}, password = {passwordbot}"
            botfile.write(datas)
            time.sleep(1)
        

class heart(object):

    def __init__(self):
        self.banner()
        time.sleep(1)
        self.username = username(path=path)
        self.botstart = twiterbot(username=self.username.user(), author=self.author())
        self.machine_start()

    def banner(self):
        os.system('clear')
        print("""
 _____       _ _   _           _____     _   
|_   _|_ _ _|_| |_| |_ ___ ___| __  |___| |_ 
  | | | | | | |  _|  _| -_|  _| __ -| . |  _|
  |_| |_____|_|_| |_| |___|_| |_____|___|_|  

                            Author    : Wardnaa.a
                            Github    : https://github.com/wardnaa
                            Instagran : https://www.instagram.com/wardnaa.a

[ + ] Starting Twitterbot account Generator ...
        """)
    def author(self):
        account_to_follow = input("[ ? ] Input Your Twitter account using '@' -> ")
        return account_to_follow
        # with open("author.txt", 'r') as author:
        #     data = author.readlines() 

        #     account_author = []
        #     for name in data:
        #         account_author.append(name.replace("\n", ""))
            
        #     return account_author[0]
    
    def machine_start(self):
            self.botstart.infouser()


if __name__ == "__main__":
    heart()











