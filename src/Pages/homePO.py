# -------------------------------------  PAGE OBJECTS -------------------------------------- #
# Here you can find the Page Objects to be used in the Home section of the twitter page.
#
class HomePO():

    def __init__(self, driver):
        self.driver = driver

        self.tweet_xpath = "//a[@data-testid='SideNav_NewTweet_Button']"
        self.tweet_input_xpath = "//div[@role='textbox']"
        self.tweet_button_xpath = "//div[@data-testid='tweetButton']"
        self.tweet_media_xpath = "//input[@type='file']"
        self.last_tweet_xpath = "//div[@data-testid='tweet']"
        self.last_media_xpath = "//article[@tabindex='0']//span[contains(text(), 'Video')]"
        self.play_button_xpath = "//div[@data-testid='videoPlayer']"
        self.unmute_button_xpath = "//div[@aria-label='Unmute']"
        self.mute_button_xpath = "//div[@aria-label='Mute']"
        self.pause_button_xpath = "//div[@data-testid='videoPlayer']"
        # self.media_filepath = "C:/Users/de/PycharmProjects/TwitterAutomation/src/assets/image.png"

    # Inputs a tweet
    def input_tweet(self, tweet):
        self.driver.find_element_by_xpath(self.tweet_input_xpath).send_keys(tweet)

    # Clicks on tweet creation button
    def click_tweet_symbol1(self):
        self.driver.find_element_by_xpath(self.tweet_xpath).click()

    # Clicks on the send tweet button
    def click_tweet_button(self):
        self.driver.find_element_by_xpath(self.tweet_button_xpath).click()

    # Contains path for media input
    def media_input(self):
        self.driver.find_element_by_xpath(self.tweet_media_xpath)

    # Clicks the media input
    def click_media_input(self):
        self.driver.find_element_by_xpath(self.tweet_media_xpath).click()

    # Input the media information
    def input_media_path(self, media_filepath):
        self.driver.find_element_by_xpath(self.tweet_media_xpath).send_keys(media_filepath)

    # Clicks on the last tweet in the timeline
    def click_last_tweet(self):
        self.driver.find_element_by_xpath(self.last_tweet_xpath).click()

    # Clicks on the last media in the timeline
    def click_last_media(self):
        self.driver.find_element_by_xpath(self.last_media_xpath).click()

    # Clicks in the play button
    def click_play_video(self):
        self.driver.find_element_by_xpath(self.play_button_xpath).click()

    # Unmute the video
    def click_unmute_video(self):
        self.driver.find_element_by_xpath(self.unmute_button_xpath).click()

    # Mute the video
    def click_mute_video(self):
        self.driver.find_element_by_xpath(self.mute_button_xpath).click()

    # Pause the video
    def click_pause_video(self):
        self.driver.find_element_by_xpath(self.pause_button_xpath).click()
