import praw
import smtplib
import time

print("Enter your Reddit username: ")
global user_name
user_name = raw_input()

print("Enter your Reddit  password: ")
global user_password
user_password = raw_input()

print("Enter your email address: ")
global email
email = raw_input()

print("Enter your email password: ")
global email_password
email_password = raw_input()

def getDanny():
    danny = 'Danny Brown'
    #Enter your reddit usernamer
    reddit = praw.Reddit(client_id='iK-oWv7s_BCUNA',
            client_secret='DG7SqGEZlzd4W_y3UjNS588ey5Y',
            password=user_password,
            user_agent='testscript',
            username=user_name)
    for submission in reddit.subreddit('hiphopheads').hot(limit = 20):
        print(submission.title)
        if danny in submission.title:
            sendEmail()


def sendEmail():

    content = 'Danny Brown is on the front page of /r/HipHopHeads !'
    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    #Email , Password
    mail.login(email, email_password) 
    #From email address, Receiver's email, content
    mail.sendmail(email, email,content)
    mail.close()

while(True):
    getDanny()
    time.sleep(3600)
   

