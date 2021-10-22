from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class LikeBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        bot = self.driver
        bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(5)
        usernameLogin = bot.find_element_by_name('username')
        passwordLogin = bot.find_element_by_name('password')
        usernameLogin.clear()
        passwordLogin.clear()
        usernameLogin.send_keys(self.username)
        passwordLogin.send_keys(self.password)
        passwordLogin.send_keys(Keys.RETURN)
        time.sleep(8)
        try:
            notnow = bot.find_element_by_css_selector(
                'body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
            notnow.click()
        except:
            return

    def likeHome(self):
        bot = self.driver
        for i in range(3):
            posts=[]
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(10)
            print('ok')
            for a in range(1,5):
                posty = bot.find_element_by_xpath('/html/body/span/section/main/section/div[1]/div[1]/div/article['+str(a)+']/div[2]/section[1]/span[1]/button/span')
                posts.append(posty)

            print(posts)
            for post in posts:
                try:
                    print('click?')
                    post.click()
                    print('click.')
                    time.sleep(random.randint(30,37))
                except:
                    time.sleep(60)

    def likeExplore(self):
        bot = self.driver
        for loop in range(2):
            bot.get('https://www.instagram.com/explore/')
            time.sleep(5)
            posts = []
            links = []
            for row in range(1,9):
                for column in range(1,4):
                    post = bot.find_element_by_xpath('/html/body/span/section/main/div/article/div[1]/div/div['+str(row)+']/div['+str(column)+']/a')
                    posts.append(post)
            for post in posts:
                link = post.get_attribute('href')
                links.append(link)
            for link in links:
                bot.get(link)
                time.sleep(10)
                bot.find_element_by_xpath('/html/body/span/section/main/div/div/article/div[2]/section[1]/span[1]/button/span').click()
                time.sleep(3)


a = LikeBot('Motivated_inspirational_phrase', 'dylledu8')
a.login()
a.likeExplore()