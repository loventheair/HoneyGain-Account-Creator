from imap_tools import MailBox, AND
import time
from bs4 import BeautifulSoup

# Settings

imap_username = "mail@shork.email"
imap_password = "@But@!ib$iriy3v200311"
imap_server = "shiriyev.me"

for _ in range(10):
    while True:
        try:
            with MailBox(imap_server).login(imap_username, imap_password, 'INBOX') as mailbox:
                for msg in mailbox.fetch(AND(from_='no-reply@honeygain.com', seen=False)):
                    soup = BeautifulSoup(msg.html, "html.parser")
                    for link in soup.findAll('a'):
                        all_links = link.get('href')
                        if "https://dashboard.honeygain.com/register/confirm" in all_links:
                            print(all_links)

        except Exception as mail_error:
            print(f"Mail Error: {mail_error}")