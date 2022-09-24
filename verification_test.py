from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from imap_tools import MailBox, AND
import random
import string
import time
from bs4 import BeautifulSoup

# Settings

imap_username = "mail@shork.email"
imap_password = "@But@!ib$iriy3v200311"
imap_server = "shiriyev.me"

try:
    browser = webdriver.Firefox()
    browser.get("https://dashboard.honeygain.com/login")

    # Get Email element and input email in it
    email_element = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div/form/div[1]/div/input"))).send_keys(f"gkqdtjoxty@shork.email")

    # Get password element and input password in it
    password_element = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div/form/div[2]/div/input"))).send_keys(f"Abutalib200311")

    # Click Register Button
    WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div/form/div[5]/button"))).click()


    WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div/div/div[2]/div[2]/button[1]"))).click()
    WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/header/div/div[1]/div[2]/div/div/div[4]/div/div[2]/div[2]/div/div[1]"))).click()
    WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div/header/div/div[1]/div[2]/div/div/div[2]/div/div"))).click()
    WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div/div[2]/div/div/div/button"))).click()
    metamask_wallet = "0xb24feE2D1f82D431272c8452f2cFC26d2A280c54"

    WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/form/div[1]/div/input"))).send_keys(metamask_wallet)
    WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/form/div[2]/button"))).click()

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
                            WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button"))).click()
                            WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div/div[2]/div/div/div/button"))).click()
                        else:
                            print("Nothing about verification code :sad_face:")
                            time.sleep(3)
            except Exception as mail_error:
                print(f"Mail Error: {mail_error}")
except Exception as error:
    print(f"General Error: {error}")
