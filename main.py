from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from imap_tools import MailBox, AND
import random
import string
import time
from bs4 import BeautifulSoup
import os
import pyautogui
import pyperclip
import sys

# Settings

imap_username = "mail@shork.email"
imap_password = "@But@!ib$iriy3v200311"
imap_server = "shiriyev.me"

website_link = "https://dashboard.honeygain.com/sign-up"
password = "Abutalib200311"
email_domain = "@shork.email"
promo_code = ""

try:
    browser = webdriver.Firefox()
    browser.get(website_link)

    # Generate random email
    letters = string.ascii_lowercase
    random_mail = f"{''.join(random.choice(letters) for i in range(stringLength))}{email_domain}"

    # Accept cookies

    WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div/div/div[2]/div[2]/button[1]"))).click()

    # Get Email element and input email in it
    email_element = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div/form/div[1]/div/input"))).send_keys(f"{random_mail}")

    # Get password element and input password in it
    password_element = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div/form/div[2]/div/input"))).send_keys(f"{password}")

    # Click to promo code text
    promo_element = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div/form/div[3]/div"))).click()

    # Put promo code
    repeat_password_element = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div/form/div[3]/div[2]/div[2]/div/div/div/input"))).send_keys(f"{promo_code}")

    # Click Register Button
    WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div/form/div[4]/button"))).click()

    # Wait for email arrive
    time.sleep(5)
    for _ in range(10):
        while True:
            try:
                with MailBox(imap_server).login(imap_username, imap_password, 'INBOX') as mailbox:
                    for msg in mailbox.fetch(AND(seen=False)):
                        if "Welcome to Honeygain!" in msg.subject:
                            soup = BeautifulSoup(msg.html, "html.parser")
                            for link in soup.findAll('a'):
                                fixed_link = link.get('href')
                                if "https://dashboard.honeygain.com/register/confirm" in fixed_link:

                                    # Login to account and connect metamask wallet
                                    browser.get(fixed_link)
                                    browser.refresh()
                                    WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/header/div/div[1]/div[2]/div/div/div[4]/div/div[2]/div[2]/div/div[1]"))).click()
                                    WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div/header/div/div[1]/div[2]/div/div/div[2]/div/div"))).click()
                                    WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div/div/div/button"))).click()

                                    try:
                                        pyautogui.click(89, 1050)
                                        time.sleep(2)
                                        pyautogui.click(1509, 166)
                                        time.sleep(2)
                                        pyautogui.click(1316, 696)
                                        time.sleep(2)
                                        pyautogui.click(1083, 455)
                                        time.sleep(10)
                                        pyautogui.click(956, 255)
                                        time.sleep(2)
                                        print(pyperclip.paste())

                                        metamask_wallet = f"{pyperclip.paste()}"

                                        WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/form/div[1]/div/input"))).send_keys(metamask_wallet)
                                        WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/form/div[2]/button"))).click()

                                        # Wait for second email arrive
                                        for _ in range(10):
                                            while True:
                                                try:
                                                    with MailBox(imap_server).login(imap_username, imap_password, 'INBOX') as second_mailbox:
                                                        for second_msg in second_mailbox.fetch(AND(seen=False)):
                                                            if "Verification Code" in second_msg.subject and "Honeygain" in second_msg.subject:
                                                                verification_code = BeautifulSoup(second_msg.html, 'html.parser').select_one('h2').string
                                                                print(verification_code.strip())
                                                                
                                                                fixed_verification_code = int(verification_code.strip())
                                                                
                                                                #verification_window = browser.find_element("xpath", '/html')

                                                                #browser.switch_to.frame(verification_window)
                                                                
                                                                WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="code"]'))).send_keys(fixed_verification_code)
                                                                WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/button"))).click()
                                                                WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div/div/div/button"))).click()
                                                                print(f"""
                                                                Account information:
                                                                Email: {random_mail}
                                                                Password: {password}
                                                                MetaMask Wallet: {metamask_wallet}
                                                                """)

                                                                save_file = open("accounts.txt", "a")
                                                                save_file.write(f"Email: {random_mail} | Password: {password} | MetaMask Wallet: {metamask_wallet}\n")
                                                                save_file.close()

                                                                os.execl(sys.executable, sys.executable, *sys.argv)
                                                            else:
                                                                print("Nothing about verification code :sad_face:")
                                                                time.sleep(3)
                                                except Exception as mail_error:
                                                    print(f"Mail Error: {mail_error}")
                                    except Exception as error:
                                        print(f"Error: {error}")
            except Exception as mail_error:
                print(f"Mail Error: {mail_error}")
except Exception as error:
    print(f"General Error: {error}")
    os.execl(sys.executable, sys.executable, *sys.argv)