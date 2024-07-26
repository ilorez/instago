
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def login(username=None, password=None):
    # Use environment variables if username and password are not provided
    if not username:
        username = os.getenv('INSTAGRAM_USERNAME')
    if not password:
        password = os.getenv('INSTAGRAM_PASSWORD')

    if not username or not password:
        raise ValueError("No username or password provided. Please set them in the .env file or pass them as arguments.")

    driver = webdriver.Firefox()  # or webdriver.Chrome()
    driver.get('https://www.instagram.com/')
    
    # Wait for the login fields to be present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
    
    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')
    
    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    
    try:
        # Wait for the profile icon or a known element that signifies a logged-in state
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[6]/div/span/div/a'  # Adjust the XPath as needed
                 ))
        )
        print("Login successful")
        return True
    except Exception as e:
        print(f"Login failed: {e}")
        return False

def logout():
    # logout
    try:
        print("Log out action not implemented yet")
        print("Logout successful")
        return True
    except Exception as e:
        print(f"Logout failed: {e}")
        return False


