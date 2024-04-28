# THIS CODE WORKS WITH VARIABLES FROM .ENV FILE. IF YOU WANT TO USE IT ADD THEM TO YOUR LOCAL .ENV FILE !!!

import time

from selenium import webdriver
from decouple import config
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get("https://www.messenger.com/")

random_messages = [
    'stavaii',
    'spri da spishhh',
    'HriZZi',
    'utre si na uchilishte :))',
    'priqtno sudiistvane v zalata',
    'Hrisiiii'
]

try:
    allow_cookies_button = driver.find_element(By.XPATH, config('ALLOW_COOKIES_BUTTON'))
    allow_cookies_button.click()

    input_email = driver.find_element(By.ID, config('INPUT_EMAIL_ID'))
    input_email.clear()
    input_email.send_keys(config("EMAIL"))

    input_password = driver.find_element(By.ID, config('INPUT_PASSWORD_ID'))
    input_password.clear()
    input_password.send_keys(config("MESSENGER_PASSWORD"))

    login_button = driver.find_element(By.NAME, config('LOGIN_BUTTON_NAME'))
    login_button.click()

    time.sleep(15)

    one_time_code_button = driver.find_element(By.XPATH, config('ONE_TIME_CODE_BUTTON'))
    one_time_code_button.click()

    time.sleep(10)
    dont_sync_button = driver.find_element(By.XPATH, config('DONT_SYNC_BUTTON'))
    dont_sync_button.click()

    find_person = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, config('FIND_PERSON_XPATH')))
    )
    find_person.click()

    time.sleep(5)
    input_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, config('INPUT_FIELD_XPATH')))
    )

    time.sleep(5)

    for idx in range(2):
        input_field.clear()
        input_field.send_keys(random_messages[idx])
        input_field.send_keys(Keys.RETURN)

    time.sleep(5)

finally:
    driver.quit()
