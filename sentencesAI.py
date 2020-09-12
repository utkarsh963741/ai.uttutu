import os

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from fake_useragent import UserAgent

from time import sleep

def get(topic):
    chrome_options = Options()
    # ua = UserAgent()
    # userAgent = ua.random
    # print(userAgent)
    # chrome_options.add_argument(f'user-agent={userAgent}')
    chrome_options.add_argument("--headless")
    driver = Chrome(chrome_options=chrome_options)
    driver.get("https://transformer.huggingface.co/doc/gpt2-large")

    if(topic == "advice"):
        return get_advice(driver)
    if(topic == "fact"):
        return get_fact(driver)
    if(topic == "random"):
        line = input("input statement you want to auto complete (the things you write won't be there in result) : ")
        return get_random(driver,line)
    
    driver.quit()


def get_advice(driver): 
    container = driver.find_element_by_class_name('ql-editor')
    container.clear()
    para = driver.find_elements(By.XPATH, '//p')[0]
    para.click()
    para.send_keys("List of the best advice I ever heard: 1. ")
    para.send_keys(Keys.TAB)
    sleep(2)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ql-mention-list")))
    para.send_keys(Keys.ENTER)

    while(True):
        advice = driver.find_elements(By.XPATH, '//strong')[0].text
        print("iterating.......")
        if advice[-1]==".":
            break
        else:
            para.send_keys(Keys.TAB)
            sleep(2)
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ql-mention-list")))
            para.send_keys(Keys.ENTER)

    print("\nDone\n")
    print(advice)
    return advice

def get_fact(driver):
    container = driver.find_element_by_class_name('ql-editor')
    container.clear()
    para = driver.find_elements(By.XPATH, '//p')[0]
    para.click()
    para.send_keys("Heres a fact : ")               #change this
    para.send_keys(Keys.TAB)
    sleep(2)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ql-mention-list")))
    para.send_keys(Keys.ENTER)

    while(True):
        fact = driver.find_elements(By.XPATH, '//strong')[0].text   #change this
        print("iterating.......")
        if fact[-1]==".":       #change this
            break
        else:
            para.send_keys(Keys.TAB)
            sleep(2)
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ql-mention-list")))
            para.send_keys(Keys.ENTER)

    print("\nDone\n")
    print(fact)
    return fact

def get_random(driver,line):
    container = driver.find_element_by_class_name('ql-editor')
    container.clear()
    para = driver.find_elements(By.XPATH, '//p')[0]
    para.click()
    para.send_keys(line)               #change this
    para.send_keys(Keys.TAB)
    sleep(2)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ql-mention-list")))
    para.send_keys(Keys.ENTER)

    while(True):
        result = driver.find_elements(By.XPATH, '//strong')[0].text   #change this
        print("iterating.......")
        if result[-1]==".":       #change this
            break
        else:
            para.send_keys(Keys.TAB)
            sleep(2)
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ql-mention-list")))
            para.send_keys(Keys.ENTER)

    print("\nDone\n")
    print(result)
    return result

if __name__ == "__main__":
    get(input("type category (advice / fact / random) : "))
