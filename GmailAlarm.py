#!/usr/bin/env python

#-------------------------------------------------------------------------------
# GmailAlarm.py
#-------------------------------------------------------------------------------
# Description:
# A Python script written for the Raspberry Pi which checks your Gmail inbox for
# an alarming subject and sounds an alarm if it finds it.
# How to use:
# (1) Make sure your Raspberry Pi has a reliable Internet connection.
# (2) Change the following constants as needed.
#     - GMAIL_IMAP_URL = the URL to Gmail's IMAP service
#     - GMAIL_ADDRESS = the Gmail address
#     - GMAIL_PASSWORD = the Gmail password
#     - ALARMING_SUBJECT = If the subject contains this text, sound the alarm.
#     - ALARM_COMMAND = If the alarm is sounded, this is the Linux command
#                       that will get run.
#                       The default is to run mpg321 against alarm.mp3
#                       in the present working directory.
# (3) If you are using the default ALARM_COMMAND, find an alarming MP3 file,
#     name it alarm.mp3, and drop it into the present working directory.
#     Otherwise, do what you need to do get your custom ALARM_COMMAND working.
# (4) Add a cron job which runs this python script as often as you like.
#     The easiest way to do this is to run "crontab -e" and
#     add a line to the crontab file.
#-------------------------------------------------------------------------------

import imaplib, os, sys

# Keep track of the present working directory.
PWD = os.path.dirname(os.path.realpath(sys.argv[0]))

# Change these constants as needed.
GMAIL_IMAP_URL = 'imap.gmail.com'
GMAIL_ADDRESS = 'username@gmail.com'
GMAIL_PASSWORD = 'password'
ALARMING_SUBJECT = 'subject'
ALARM_COMMAND = '/usr/bin/mpg321 ' + PWD + '/alarm.mp3 &'

def checkGmail():
    # Create the Gmail IMAP4 SSL connection.
    gmail = createGmail(GMAIL_IMAP_URL, GMAIL_ADDRESS, GMAIL_PASSWORD)
    # If any of the inbox email subjects are alarming, sound the alarm.
    if inboxEmailSubjectsAreAlarming(gmail):
        alarm()
    else:
        print 'don\'t panic'
    # Destroy the gmail IMAP4 SSL connection.
    destroyGmail(gmail)

def createGmail(gmailImapUrl, gmailAddress, gmailPassword):
    # Create the Gmail IMAP4 SSL connection.
    print 'logging into gmail'
    gmail = imaplib.IMAP4_SSL(gmailImapUrl)
    gmail.login(gmailAddress, gmailPassword)
    return gmail

def inboxEmailSubjectsAreAlarming(gmail):
    # Search the inbox email subjects for the alarming subject.
    print 'searching inbox email subjects for "' + ALARMING_SUBJECT +'"'
    gmail.select('inbox')
    result, data = gmail.uid('search', None, '(SUBJECT "' + ALARMING_SUBJECT +'")')
    # Anything alarming?
    if result != 'OK':
        print 'search failed'
        print 'result: ' + result
        return False
    else:
        uidsString = data[0];
        hasUids = len(uidsString) > 0
        if hasUids:
            print 'found ' + str(len(uidsString.split(' '))) + ' email UID(s): ' + str(uidsString)
            return True
        else:
            print 'found 0 email UIDs'
            return False

def alarm():
    # Sound the alarm!
    print 'ALARM!!!'
    print ALARM_COMMAND
    os.system(ALARM_COMMAND)

def destroyGmail(gmail):
    # Destroy the Gmail IMAP4 SSL connection.
    print 'logging out of gmail'
    gmail.close()
    gmail.logout()

# Check Gmail.
checkGmail()
