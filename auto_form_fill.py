from selenium import webdriver
from selenium.webdriver.common.by import By
from random_detail import *


def form_fill():
    option = webdriver.ChromeOptions()
    option.add_argument("-incognito")
    option.add_experimental_option("excludeSwitches", ['enable-automation'])
    browser = webdriver.Chrome(options=option)
    browser.get("https://forms.gle/xE5xodU3WvGzbUnA9")

    name = generate_random_name()
    year = select_random_year()
    gender = select_random_gender()
    q1ans = select_q1_answer()

    namex = browser.find_elements(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    yearx = browser.find_elements(By.XPATH, year)
    genderx = browser.find_elements(By.XPATH, gender)
    q1x = browser.find_elements(By.XPATH, q1ans)
    submitbutton = browser.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div")

    namex[0].send_keys(name)
    yearx[0].click()
    genderx[0].click()
    q1x[0].click()
    submitbutton.click()
