from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import requests
import logging


def get_png(html):

    logging.info('opening browser')

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get('https://htmledit.squarefree.com/')

    ## site uses frames, so it needs navigating between them ##
    driver.switch_to_frame('editbox')
    input = driver.find_element_by_xpath('/html/body/form/textarea')
    input.send_keys(html)

    driver.switch_to.default_content()
    driver.switch_to_frame('dynamicframe')

    ## wait for rendering ##
    time.sleep(5)
    element = driver.find_element_by_id('twitter-widget-0')
    img = element.screenshot('tweet.png')

    logging.info('closing browser')
    driver.close()

    return img


def get_embedded_tweet(url):
    res = requests.get(url)
    return res





