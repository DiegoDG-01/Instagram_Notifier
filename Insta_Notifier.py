import notify2
import requests
import time 
import os

class Instagram_Updater(object):

    def __init__(self, username):
        self.username = username
        self.CurrenFollowers = ""
        self.LastFollowers = ""

        notify2.init("Instagram Notifier")
        
        self.noti = notify2.Notification("Instagram\n", icon='~/Instagram_Notifier/logo_insta.png')
        self.noti.set_urgency(notify2.URGENCY_NORMAL)
        self.noti.set_timeout(1000)

    def followers(self):
        url = "https://instagram.com/"+self.username

        try:
            query = requests.get(url).text
        except ConnectionError:
            return 0
        
        start = '"edge_followed_by":{"count":'
        finish = '},"followed_by_viewer'

        self.CurrenFollowers = self.LastFollowers
        self.LastFollowers = str(query[query.find(start)+len(start):query.rfind(finish)])

    def main(self, Notificacion_Rate):
        while True:
            self.followers()
            message = f"Current Follows: {self.CurrenFollowers}\t Last Follows: {self.LastFollowers}"
            
            self.noti.update("Instagram\n",message)
            self.noti.show()

            time.sleep(Notificacion_Rate)


if(__name__ == "__main__"):

    username = input(r"Whatś is your username >> ")

    try:
        Notify_Rate = int(input("How to requiere your notify in minutes >> ")) * 60
    except TypeError:
        print("Invalid Data, Notification rate default >> 5 minutes")
        Notify_Rate = 5 * 60

    
    account = Instagram_Updater(username)
    account.main(Notify_Rate)