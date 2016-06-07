import requests
import re
from bs4 import BeautifulSoup

#mail stuff
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

#BeautifulSoup example found at: http://stackoverflow.com/questions/29422727/exporting-my-web-scrape-results-from-python  

def send_mail(send_from, send_to, subject, text, files=None,
              server="127.0.0.1"):
    #assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
            msg.attach(part)

    #"C:\Program Files\Python\python" -m smtpd -n -c DebuggingServer localhost:1025
    smtp = smtplib.SMTP("mplarray.dsglobal.org","25")
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

urls= "https://play.google.com/store/search?q=voya&c=apps&hl=en"
r = requests.get(urls)
soup=BeautifulSoup(r.text, 'html.parser')
aTags = soup('a')
paragraphs = []
for a in aTags:
    paragraphs.append(str(a))
voyas = []
index = 0
found = 0
for line in paragraphs:
    if ("Voya " in line) & ('class="subtitle"' not in line):
        words = line.split()
        for word in words:
            if "title=" in word:
                found = 1
                temp = word.split('"')
                #grabbing stuff after " mark
                voyas.append(temp[1])
            elif found == 1:
                voyas[index]+=" "
                #this is the case that will be the end of the title
                if '"' in word:
                    temp = word.split('"')
                    #adding stuff before " mark
                    voyas[index]+=temp[0]
                    index+=1
                    found = 0
                #this is a middle word of the title
                else:
                    voyas[index]+=word
#removing duplicates but maintaining order
voyas = sorted(set(voyas))
for i in voyas:
    print(i)
send_mail("melissa.walters@voya.com","melissa.walters@voya.com","test","test")


