from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class RequestSenderBot:
    def __init__(self,x=1):
        if x!=1:
            self.browser = None
            self.l=True
            self.username = ''
            self.password = ''
        else:
            self.l=False
            self.browser = webdriver.Chrome()
            self.browser.get("http://www.facebook.com")
            self.username=''
            self.password=''

    def login(self, account, passw):

        if self.l:
            self.browser = webdriver.Chrome()
            self.browser.get("http://www.facebook.com")
            self.l=False
        #try:
        print(account)
        print(passw)

        username = self.browser.find_element_by_id("email")
        password = self.browser.find_element_by_id("pass")
        submit = self.browser.find_element_by_name("login")
        username.send_keys(account)
        password.send_keys(passw)
        submit.click()
#        except:
 #           return 1
        self.username = account
        self.password = passw
        try:
            username = self.browser.find_element_by_id("email")
            print(username)
        except:
            print("logged in")
            return 0
        else:
            return 2
        return 0

    def add_friend(self, friend_id):
        if len(friend_id) != 15 or not (friend_id.isdecimal()):
            return 'id must be 15 numbers'

        website = "https://m.facebook.com/profile.php?id=" + str(friend_id)
        # open profile of friend
        try:
            print('getting profile.....')
            self.browser.get(website)
        except:
            return 'هذا الرقم غير صحيح'+friend_id
        else:
            print("adding fr....")
            try:
                x = self.browser.find_element_by_id("cover-name-root")
                c = x.text

            except:
                c = 'element not found'
                # try:
                print(c)
                # except:
                # c='unknown'
            try:
                print("seekind add button.....")
                self.browser.find_element_by_xpath('//a[contains(@href,"add")]').click()
            except:

                return 'already added friend  '+c



            return "تمت الاضافة بنجاح"+c

    def close(self):
        self.browser.close()
y=RequestSenderBot()
x=y.login('pythonista@outlook.com','asmaa2031991')
print(x)