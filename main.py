import pyautogui
from time import sleep
import random

tweetButton = pyautogui.locateOnScreen('TweetButton.jpg', confidence = 0.7)
tweets = ['What a nice day!', 'Hello World!', 'Drink Water!', 'I am the best bot in the whole world!']




def Tweet():
    random_tweet = random.choice(tweets)
    print('running...')
    pyautogui.moveTo(tweetButton)
    sleep(1)
    pyautogui.click()
    sleep(1)
    pyautogui.write('(Tweet made by bot' + str(i) + ')' + str(random_tweet))
    sleep(1)
    pyautogui.keyDown('ctrlleft')
    pyautogui.press('enter')
    pyautogui.keyUp('ctrlleft')

for i in range(40):
    Tweet()
    sleep(3)

