import praw
import smtplib

def getDanny():

    danny = 'Danny Brown'
    r = praw.Reddit(user_agent = 'alkorin')
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
    mail.login('alkorin452@gmail.com','Mom Abba Tahlia Yael')
    mail.sendmail('alkorin452@gmail.com','alkorin452@gmail.com',content)
    mail.close()




getDanny()

