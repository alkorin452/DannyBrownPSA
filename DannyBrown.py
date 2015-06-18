import praw
import smtplib

def getDanny():

    danny = 'Danny Brown'
    #Enter your reddit usernamer
    r = praw.Reddit(user_agent = '')
    submissions = r.get_subreddit('hiphopheads').get_hot(limit = 20)
    list = [str(x) for x in submissions]
    for i in list:
        if danny in i:
            sendEmail()


def sendEmail():

    content = 'DANNY BROWN IS ON THE FRONTPAGE OF HHH'
    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    #Email , Password
    mail.login('','')
    #From email address, Receiver's email, content
    mail.sendmail('','',content)
    mail.close()




getDanny()

