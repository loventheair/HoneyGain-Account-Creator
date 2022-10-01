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
import mysql.connector

# Settings

# Mail Settings
imap_username = "mail@shork.email"
imap_password = "@But@!ib$iriy3v200311"
imap_server = "shiriyev.me"

# Database Information's
db_host = "byte.rasbyte.net"
db_user = "admin_omer"
db_password = "@But@!ib$iriy3v200311"
database = "admin_omer"

# Other codes
website_link = "https://dashboard.honeygain.com/sign-up"
password = "1Az234wsx+!"
random_email_domain = "@shork.email"
promo_code = "REF_HB2E04"
metamask_password = "1Az234wsx+"


# Functions

def the_end():
    # Click to hotspot shield
    pyautogui.click(164, 1057)
    time.sleep(2)

    # Click to disconnect
    pyautogui.click(1539, 984)
    time.sleep(5)

    # Click random place before restart
    pyautogui.click(59, 353)

    # Restart Script
    browser.close()
    os.execv(sys.executable, ['python'] + sys.argv)

try:
    # Click to hotspot shield
    pyautogui.click(164, 1057)
    time.sleep(2)

    # Click to connect
    pyautogui.click(1539, 638)
    time.sleep(2)

    # Click to connect anyway
    pyautogui.click(1671, 781)
    time.sleep(15)

    browser = webdriver.Firefox()
    browser.get(website_link)

    # Generate random email
    letters = string.ascii_lowercase
    random_mail = f"{''.join(random.choice(letters) for _ in range(10))}{random_email_domain}"

    # Accept cookies
    WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div/div/div[2]/div[2]/button[1]"))).click()

    # Get Email element and input email in it
    email_element = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div/form/div[1]/div/input"))).send_keys(random_mail)

    # Get password element and input password in it
    password_element = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div/form/div[2]/div/input"))).send_keys(password)

    # Click to promo code text
    promo_element = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div/form/div[3]/div"))).click()

    # Put promo code
    repeat_password_element = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div/form/div[3]/div[2]/div[2]/div/div/div/input"))).send_keys(promo_code)

    # Click Register Button
    WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div/form/div[4]/button"))).click()

    # Wait for email arrive
    time.sleep(5)

    # Check mailbox for email
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
                                time.sleep(3)
                                browser.refresh()
                                time.sleep(3)
                                WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/header/div/div[1]/div[2]/div/div/div[4]/div/div[2]/div[2]/div/div[1]"))).click()
                                WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div/header/div/div[1]/div[2]/div/div/div[2]/div/div"))).click()
                                WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div/div/div/button"))).click()
                                while True:
                                    try:
                                        time.sleep(2)
                                        # Paste metamask wallet
                                        WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/form/div[1]/div/input"))).send_keys(metamask_wallet)
                                        WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/form/div[2]/button"))).click()

                                        # Wait for second email arrive
                                        while True:
                                            try:
                                                with MailBox(imap_server).login(imap_username, imap_password, 'INBOX') as second_mailbox:
                                                    for second_msg in second_mailbox.fetch(AND(seen=False)):
                                                        if "Verification Code" in second_msg.subject and "Honeygain" in second_msg.subject:
                                                            verification_code = BeautifulSoup(second_msg.html, 'html.parser').select_one('h2').string

                                                            # Fix verification code
                                                            fixed_verification_code = verification_code.strip()
                                                            print(fixed_verification_code)

                                                            # Type verification code
                                                            WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="code"]'))).send_keys(fixed_verification_code)
                                                            WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/button"))).click()
                                                            WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div/div/div/button"))).click()

                                                            # Print account information's
                                                            print(f"""
                                                            Account information:
                                                            Email: {random_mail}
                                                            Password: {password}
                                                            MetaMask Wallet: {metamask_wallet}
                                                            """)

                                                            # Save account to file
                                                            save_file = open("accounts.txt", "a")
                                                            save_file.write(f"Email: {random_mail} | Password: {password} | MetaMask Wallet: {metamask_wallet}\n")
                                                            save_file.close()

                                                            while True:
                                                                try:
                                                                    # Save account to database
                                                                    mydb = mysql.connector.connect(
                                                                        host=f"{db_host}",
                                                                        user=f"{db_user}",
                                                                        password=f"{db_password}",
                                                                        database=f"{database}"
                                                                    )

                                                                    mycursor = mydb.cursor()

                                                                    sql = "INSERT INTO honey_accounts (email, password, metamask, private_key) VALUES (%s, %s, %s, %s)"
                                                                    val = (f"{random_mail}", f"{password}", f"{metamask_wallet}", f"Demo")
                                                                    mycursor.execute(sql, val)
                                                                    mydb.commit()
                                                                    print(mycursor.rowcount, "Account saved to database.")

                                                                    # Get secret code
                                                                    time.sleep(2)

                                                                    # Click Three Dot
                                                                    pyautogui.click(1522, 223)
                                                                    time.sleep(2)

                                                                    # Click Account details
                                                                    pyautogui.click(1505, 364)
                                                                    time.sleep(2)

                                                                    # Click Export private key
                                                                    pyautogui.click(970, 720)
                                                                    time.sleep(2)

                                                                    # Enter Password
                                                                    pyautogui.click(948, 494)
                                                                    pyperclip.copy(metamask_password)
                                                                    pyautogui.hotkey('ctrl', 'v')
                                                                    time.sleep(3)

                                                                    # Click confirm
                                                                    pyautogui.click(1052, 688)
                                                                    time.sleep(3)

                                                                    # Click to "click to copy"
                                                                    pyautogui.click(970, 507)
                                                                    time.sleep(3)

                                                                    # Click Done
                                                                    pyautogui.click(975, 726)
                                                                    time.sleep(1)

                                                                    # Get Private Code
                                                                    metamask_wallet_private = f"{pyperclip.paste()}"

                                                                    mysql_test = 1
                                                                    while True:
                                                                        try:
                                                                            # Update database
                                                                            mydb = mysql.connector.connect(
                                                                                host=f"{db_host}",
                                                                                user=f"{db_user}",
                                                                                password=f"{db_password}",
                                                                                database=f"{database}"
                                                                            )

                                                                            mycursor = mydb.cursor()
                                                                            sql = f"UPDATE honey_accounts SET private_key = '{metamask_wallet_private}' WHERE email = '{random_mail}'"
                                                                            mycursor.execute(sql)
                                                                            mydb.commit()
                                                                            print(mycursor.rowcount, "record(s) affected")

                                                                            # Call ending function
                                                                            the_end()
                                                                        except Exception as database_error:
                                                                            print(f"Last Database Error: {database_error}")
                                                                            mysql_test = mysql_test + 1
                                                                            if mysql_test == 10:

                                                                                # Call ending function
                                                                                the_end()
                                                                except Exception as first_database:
                                                                    print(f"First Database Error: {first_database}")
                                                        else:
                                                            print("Nothing about verification code :sad_face:")
                                                            time.sleep(3)
                                            except Exception as mail_error:
                                                print(f"Second Mail Error: {mail_error}")
                                                # Call ending function
                                                the_end()
                                    except Exception as error:
                                        print(f"Error: {error}")
        except Exception as mail_error:
            print(f"Mail Error: {mail_error}")
            the_end()
except Exception as error:
    print(f"General Error: {error}")
    os.execv(sys.executable, ['python'] + sys.argv)
