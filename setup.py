import os
import sys
import time
import time
import platform
import subprocess
import wget

class machine(object):

    def __init__(self):
        self.author = "@Wardanaaa"
        os.system('clear')
        self._banner()
        self._ask_for_root()
        time.sleep(1)
        self._system_update()
        time.sleep(0.5)
        os.system('clear')
        self._banner()
        self._requirments()
        os.system('python3 twitterbot.py')
    
    def _banner(self):
        print("""                                                   
 _____       _ _   _           _____     _   
|_   _|_ _ _|_| |_| |_ ___ ___| __  |___| |_ 
  | | | | | | |  _|  _| -_|  _| __ -| . |  _|
  |_| |_____|_|_| |_| |___|_| |_____|___|_|  

                            Author    : Wardnaa.a
                            Github    : https://github.com/wardnaa
                            Instagran : https://www.instagram.com/wardnaa.a   
        """)
    def _ask_for_root(self):
        euid = os.getuid()
        if euid != 0:
            print ("Script not started as root. Runing sudo..")
            args = ['sudo', sys.executable] + sys.argv + [os.environ]
            os.execlpe('sudo', *args)
    
    def _system_update(self):
        print("")
        os.system('apt-get update -y && sudo apt-get upgrade -y')
    
    def _requirments(self):
         chrome = subprocess.check_output('command -v google-chrome', shell=True) or "empty"
         if (chrome != 'empty'):
             time.sleep(0.6)
             print("[ ✔ ] Google-Chrome.....................[ Found ]")
         
         else:
             print("[ X ] Google-Chrome -> Not Found!")
             print("[ I ] Installing Google-Chrome -> Process! ")
             wget.download("https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
             os.system('dpkg -i google-chrome-stable_current_amd64.deb -y && apt-get -f install -y ')
             os.system('rm -rf google-chrome-stable_current_amd64.deb')
             print("\n[ Y ] Installing Google-Chrome -> Done!")
         
         chromedriver = subprocess.check_output('command -v chromedriver', shell=True) or "empty"
         if (chromedriver != "empty"):
             time.sleep(0.6)
             print("[ ✔ ] ChromeDriver......................[ Found ]")
        
         else:
            print("[ X ] GoogleDriver -> Not Found!")
            print("[ I ] Installing Google-Chrome -> Process! ")
            os.system('cp chromedriver /bin')
            time.sleep(0.6)
            print("\n[ Y ] Installing Google-Chrome -> Done!")
        

if __name__ == "__main__":
    machine()
