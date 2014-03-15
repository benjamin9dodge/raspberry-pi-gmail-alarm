raspberry-pi-gmail-alarm
========================

A Python script written for the Raspberry Pi which checks your Gmail inbox for an alarming subject and sounds an alarm if it finds it.

##How to Use##

1. Make sure your Raspberry Pi has a reliable Internet connection.
2. Change the following constants as needed.
    - `GMAIL_IMAP_URL` = the URL to Gmail's IMAP service
    - `GMAIL_ADDRESS` = the Gmail address
    - `GMAIL_PASSWORD` = the Gmail password
    - `ALARMING_SUBJECT` = If the subject contains this text, sound the alarm.
    - `ALARM_COMMAND` = If the alarm is sounded, this is the Linux command that will get run. The default is to run `mpg321` against `alarm.mp3` in the present working directory.
3. If you are using the default `ALARM_COMMAND`, find an alarming MP3 file, name it `alarm.mp3`, and drop it into the present working directory. Otherwise, do what you need to do get your custom `ALARM_COMMAND` working.
4. Add a cron job which runs this python script as often as you like. The easiest way to do this is to run `crontab -e` and add a line to the crontab file.

##MIT LICENSE##

The MIT License (MIT)

Copyright (c) 2014 Ben Dodge

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
