from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
import autoit
import random
import unicodedata
from time import sleep

import imageEditor
import sentencesAI as AI

def upload():

    #image
    imageEditor.edit_image()
    image_path = r"E:\Projects\InstagramBot\ai.uttutu\image.jpg"

    #caption
    captionText = AI.get("fact")
    hashtag = get_hashtags()
    emoji=['(ㆆ _ ㆆ)','⊂(◉‿◉)つ','ʕ·͡ᴥ·ʔ','(˵ ͡° ͜ʖ ͡°˵)','ԅ(≖‿≖ԅ)','( ͡° ᴥ ͡°)','(╥﹏╥)','(｡◕‿‿◕｡)','(⌐■_■)','d[-_-]b','(╯°□°)╯','(ಠ_ಠ)','(☞ﾟ∀ﾟ)☞','\(°^°)/','(;´༎ຶД༎ຶ`)','ᕕ( ᐛ )ᕗ']
    emojiCaption = random.sample(emoji,1)
    caption = captionText+"          "+"       "+hashtag+" #ai"+' '.join(emojiCaption) +"                                                                                                                                                                               All the statements on this past are crafted computer gibberish and are not meant to be taken seriously."
    print(caption)
    
    mobile_emulation = { "deviceName": "Pixel 2" }
    opts = Options()
    opts.add_experimental_option("mobileEmulation", mobile_emulation)
    # opts.add_argument("--headless")
    driver = Chrome(chrome_options=opts)

    username ="xxxxxxxxxxxxxxxxxxx"                 #add username here
    password="xxxxxxxxxxxxxxxxxxxx"                 #add password here
    
    driver.get("https://www.instagram.com/")
    sleep(1)

    login(driver,username,password)  
    sleep(1)
    close_reactivated(driver)
    sleep(1)
    close_notification(driver)
    sleep(1)
    close_add_to_home(driver)
    sleep(1)
    close_notification(driver)

    new_post_btn = driver.find_element_by_xpath("//div[@role='menuitem']").click()
    sleep(1)
    autoit.win_active("Open") 
    sleep(1)
    autoit.control_send("Open","Edit1",image_path) 
    sleep(1)
    autoit.control_send("Open","Edit1","{ENTER}")

    sleep(2)

    next_btn = driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()

    sleep(1)

    caption_field = driver.find_element_by_xpath("//textarea[@aria-label='Write a caption…']")
    caption_field.send_keys(caption)
    
    share_btn = driver.find_element_by_xpath("//button[contains(text(),'Share')]").click()

    sleep(10)
    print("\n\n.....DONE.....")
    

    driver.close()



def login(driver,username,password):
    login_button = driver.find_element_by_xpath("//button[contains(text(),'Log In')]")
    login_button.click()
    sleep(1)
    username_input = driver.find_element_by_xpath("//input[@name='username']")
    username_input.send_keys(username)
    password_input = driver.find_element_by_xpath("//input[@name='password']")
    password_input.send_keys(password)
    password_input.submit()
       
    
    

def close_reactivated(driver):
    try:
        sleep(1)
        not_now_btn = driver.find_element_by_xpath("//a[contains(text(),'Not Now')]")
        not_now_btn.click()
    except:
        pass

def close_notification(driver):
    try: 
        sleep(1)
        close_noti_btn = driver.find_element_by_xpath("//button[contains(text(),'Not Now')]")
        close_noti_btn.click()
        sleep(1)
    except:
        pass

def close_add_to_home(driver):
    sleep(1) 
    close_addHome_btn = driver.find_element_by_xpath("//button[contains(text(),'Cancel')]")
    close_addHome_btn.click()
    sleep(1)
    
def get_hashtags():
    with open("./text-hashtags/words_alpha.txt") as words:
        hashtags = "#"+' #'.join(random.sample((words.read().split()),10))
        return(hashtags)

if __name__ == "__main__":
    try:
        upload()
    except Exception as e:
        print("\n\n.....ERROR.....")
        print(e)
    