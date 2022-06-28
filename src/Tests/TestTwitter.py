import os
import time

from selenium.webdriver import ActionChains
from src.Pages.loginPO import LoginPO
from src.Pages.homePO import HomePO
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager


# -------------------------------------  TWITTER AUTOMATION PROJECT -------------------------------------- #

# Driver Setup

driver = webdriver.Chrome(ChromeDriverManager().install())
print("Test Started -->")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# Navigating to Twitter Page

print("Navigate to Twitter page-->")
driver.get("https://www.twitter.com/login")
driver.implicitly_wait(10)

# LOG IN SECTION

login = LoginPO(driver)
print("Login the user -->\n")
driver.implicitly_wait(15)
login.enter_username("8094159042")
login.enter_password("automationftw01")
print("Clicking Login button -->\n")
login.login_button_click()
driver.implicitly_wait(5)

print("Validating if user logged in --->\n")

# Verify if user has signed in

page_title = driver.title
page_url = driver.current_url
assert page_url == "https://twitter.com/home"
print("ASSERTION: Account has logged in.\n")


# TWEETING SECTION

# ------------------ Tweet Something with Text -------------------- #

driver.implicitly_wait(5)
print("Clicking on New Tweet button -->\n")
home = HomePO(driver)
home.click_tweet_symbol1()
home.input_tweet("This is a tweet example with just text.")
print("Tweeting text -->\n")
driver.implicitly_wait(5)
home.click_tweet_button()
time.sleep(5)

# Validating Text Tweet

driver.implicitly_wait(5)
home.click_last_tweet()
driver.implicitly_wait(5)
print("Validating if text tweet was sent --->\n")
time.sleep(5)
assert driver.find_element_by_xpath("//span[contains(text(), 'tweet')]").is_displayed()
print("ASSERTION: Tweet has been sent.\n")

# ----------------- Tweet Something with Images -------------------- #

driver.get("https://twitter.com/home")
driver.implicitly_wait(5)

home.click_tweet_symbol1()
home.input_tweet("This is one that includes an image attached.")

# Find media button and upload file

try:
    print("TRYING TO TWEET IMAGE -->\n")
    driver.implicitly_wait(5)

    tweet_media_input = driver.find_element_by_xpath("//input[@type='file']")
    driver.execute_script("arguments[0].style.display = 'block';", tweet_media_input)
    driver.execute_script("arguments[0].setAttribute('class', 'visible')", tweet_media_input)

    home.input_media_path("C:/Users/de/PycharmProjects/TwitterAutomation/src/assets/image.png")
except Exception as e:
    print(e)

driver.implicitly_wait(5)
print("Tweeting with Image -->\n")
home.click_tweet_button()
time.sleep(8)


# Validate Media (Image)

print("Validating Tweet with Image --->\n")
driver.implicitly_wait(2)
action = ActionChains(driver)
action.double_click(home.click_last_tweet())
# home.click_last_tweet()
driver.implicitly_wait(3)
image_tweet_verification = driver.find_element_by_xpath("//div[@aria-label='Image']")
assert image_tweet_verification.is_displayed()
print("ASSERTION: Tweet with image has been sent\n")

# ----------------- Tweet Something with Video -------------------- #

driver.get("https://twitter.com/home")
driver.implicitly_wait(5)
home.click_tweet_symbol1()
driver.implicitly_wait(5)
home.input_tweet("This is one that includes a Video attached.")

# Find media button and upload file
try:
    print("TRYING TO TWEET VIDEO -->\n")
    tweet_media_input2 = driver.find_element_by_xpath("//input[@type='file']")
    driver.execute_script("arguments[0].style.display = 'block';", tweet_media_input2)
    driver.execute_script("arguments[0].setAttribute('class', 'visible')", tweet_media_input2)

    home.input_media_path("C:/Users/de/PycharmProjects/TwitterAutomation/src/assets/video.mp4")
    time.sleep(8)
except Exception as e:
    print(e)

home.click_tweet_button()
print("Tweeting with Video -->\n")
print("Please wait while the video is being uploaded...\n")
time.sleep(20)

# Validate Media (Video)

driver.implicitly_wait(5)
action.double_click(home.click_last_media())
driver.implicitly_wait(5)
print("Validating Tweet with Video --->\n")
video_tweet_verification = driver.find_element_by_xpath("//div[@data-testid='videoPlayer']")
assert video_tweet_verification.is_displayed()
print("ASSERTION: Tweet with video has been sent\n")
time.sleep(5)

# Interact with video

driver.implicitly_wait(3)
wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@data-testid='videoPlayer']")))
print("Pausing video -->")
home.click_play_video()
home.click_pause_video()
print("Muting video -->")
home.click_mute_video()
time.sleep(3)
print("Unmuting video -->")
home.click_play_video()
home.click_pause_video()
home.click_unmute_video()
time.sleep(3)
print("Playing video again -->\n")
home.click_play_video()
time.sleep(3)
print("ASSERTION: Video interaction successfully completed\n")


# ----------------- Tweet Something with Link -------------------- #

driver.get("https://twitter.com/home")
driver.implicitly_wait(5)
home.click_tweet_symbol1()
driver.implicitly_wait(2)

print("TRYING TO TWEET LINK -->\n")
home.input_tweet("This is another one but with a link attached - https://www.youtube.com/watch?v=DtL_giO-EB8")
home.click_tweet_button()
print("Tweeting with link -->\n")
time.sleep(5)

# Validate Media (Link)

driver.implicitly_wait(2)
home.click_last_tweet()
driver.implicitly_wait(3)
print("Validating Tweet with Link --->\n")
link_tweet_verification = driver.find_element_by_xpath("//div[@data-testid='card.wrapper']")
assert link_tweet_verification.is_displayed()
print("ASSERTION: Tweet with link has been sent\n")


# Closing down the project
print("Going back to home page\n")

time.sleep(25)
driver.get("https://twitter.com/home")
time.sleep(5)
print("Ending the test and closing the browser --->\n")
driver.implicitly_wait(3)

driver.close()
print("Twitter Automation test has been successfully completed!")
