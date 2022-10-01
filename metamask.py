from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import urllib.request
from os.path import exists
import pyperclip

repeat = 50

EXTENSION_PATH = os.getcwd() + '\metamaskExtension.crx'
EXTENSION_ID = 'nkbihfbeogaeaoehlefnkodbefgpgknn'
file = exists("metamaskExtension.crx")

# MetaMask
recoveryPhrase = "globe amateur deposit web pass memory auto shed oppose unique front improve"
password = "Abutalib200311"


if not file:
    # Install extension if not installed
    url = 'https://xord-testing.s3.amazonaws.com/selenium/10.0.2_0.crx'
    urllib.request.urlretrieve(url, os.getcwd() + '/metamaskExtension.crx')
else:
    # Open chrome
    chrome_options = Options()
    chrome_options.add_extension(EXTENSION_PATH)
    driver = webdriver.Chrome(options=chrome_options)


    # Switch window to metamask
    driver.switch_to.window(driver.window_handles[0])

    # Import Wallet
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Get Started"]'))).click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Import wallet"]'))).click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="No Thanks"]'))).click()

    # Enter Recovery Phrase and Password
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[3]/div/div/form/div[4]/div[1]/div/input'))).send_keys(recoveryPhrase)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[3]/div/div/form/div[5]/div/input'))).send_keys(password)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[3]/div/div/form/div[6]/div/input'))).send_keys(password)

    # Accept Terms and Import Wallet
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.first-time-flow__terms'))).click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Import"]'))).click()

    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="All Done"]'))).click()

    # Close Popup Message
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popover-content"]/div/div/section/header/div/button'))).click()

    # Go to Networks Tab
    driver.get('chrome-extension://{}/home.html#settings/networks'.format(EXTENSION_ID))

    # Click Add Network
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div[1]/div/button'))).click()

    # Import Smart Chain Network
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/input'))).send_keys("Smart Chain")
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/input'))).send_keys("https://bsc-dataseed.binance.org/")
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div[2]/div[2]/div[4]/div[2]/div/input'))).send_keys("56")
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div[2]/div[2]/div[5]/div[2]/div/input'))).send_keys("BNB")
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div[2]/div[2]/div[6]/div[2]/div/input'))).send_keys("https://bscscan.com")
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div[2]/div[2]/div[7]/button[2]'))).click()


    for x in range(repeat):
        try:
            # Go to New Account Tab
            driver.get('chrome-extension://{}/home.html#new-account'.format(EXTENSION_ID))

            # Click to Create New Account
            WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div[2]/div/button[2]'))).click()
            # Click 3 dot and click account information
            WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div[1]/button'))).click()
            WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/button[1]'))).click()

            # Go to Private Key
            WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/span/div[1]/div/div/div/button[3]'))).click()
            WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/span/div[1]/div/div/div/div[5]/input'))).send_keys(password)

            # Go To Private Key Menu
            WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/span/div[1]/div/div/div/div[7]/button[2]'))).click()

            # Get Private Key
            private_key = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/span/div[1]/div/div/div/div[5]/div/textarea'))).text

            # Close menu and print result
            WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/span/div[1]/div/div/div/div[7]/button'))).click()

            time.sleep(2)
            # Get wallet address
            WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[4]/div/div/div/div[1]/div/div/div/button"))).click()
            wallet = pyperclip.paste()
            # Print Results
            print(f"{wallet} | {private_key}")

        except Exception as error:
            print(f"Waiting for element... | {error}")
