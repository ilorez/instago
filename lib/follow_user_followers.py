# lib/follow_user_followers.py

import time
from lib.connection import get_driver
from selenium.webdriver.common.by import By as By

def follow_user_followers(username, max_followers, driver):
    driver.get(f'https://www.instagram.com/{username}/')

    # Wait for the page to load
    time.sleep(5)

    followers_link = driver.find_element(By.XPATH,"//a[contains(@href, '/followers/')]")
    followers_link.click()
    
    # Wait for the followers modal to load
    time.sleep(5)
   
    # Get the followers
    followers_popup_xpath = "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[2]"
    
    followers_popup = driver.find_element(By.XPATH, followers_popup_xpath)

    # Get the last height of the followers popup
    last_height = driver.execute_script("return arguments[0].scrollHeight", followers_popup)

    follow_count = 0
    # Follow the followers
    while True:
        follow_buttons = driver.find_elements(By.XPATH, "//button/div/div[text()='Follow']")
        if not follow_buttons:
            print("No follow buttons found.")
            break
        for button in follow_buttons:
            try:
                button.click()
                print("Followed a user.")
                time.sleep(2)  # Pause between actions to mimic human behavior
                follow_count += 1
            except Exception as e:
                print(f"Error clicking follow button: {e}")
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup)
        time.sleep(5)
        new_height = driver.execute_script("return arguments[0].scrollHeight", followers_popup)
        if new_height == last_height:
            print("Reached the end of the followers list.")
            break
        last_height = new_height

        # break if the max_follow
        if follow_count >= max_followers:
            break

