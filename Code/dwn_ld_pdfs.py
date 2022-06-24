from requests import Session
import requests
import pdfkit
import lxml.html

# def cas_login(service, username, password):
#     # GET parameters - URL we'd like to log into.
#     params = {'service': service}
#     LOGIN_URL = 'https://login.case.edu/cas/login'

#     # Start session and get login form.
#     session = requests.session()
#     login = session.get(LOGIN_URL, params=params)

#     # Get the hidden elements and put them in our form.
#     login_html = lxml.html.fromstring(login.text)
#     hidden_elements = login_html.xpath('//form//input[@type="hidden"]')
#     form = {x.attrib['name']: x.attrib['value'] for x in hidden_elements}

#     # "Fill out" the form.
#     form['username'] = username
#     form['password'] = password

#     # Finally, login and return the session.
#     session.post(LOGIN_URL, data=form, params=params)
#     return session

url_login = 'http://172.20.102.15/technical_wiki/index.php?title=Special:UserLogin&returnto=Special%3AUserLogout&returntoquery='
# s = Session()
# s.post(url_login, {"password":"Password123", "email":"stephen.ghool@digicelgroup.com", "status":""})
# print(s.url)
# # pdfkit.from_url('http://172.20.102.15/technical_wiki/index.php/123_Plan', 'out.pdf')

# cas_login(url_login,'Sghool','Password123')


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# wiki credentials
username = "Sghool"
password = "Password123"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

# head to wiki login page
driver.get("http://172.20.102.15/technical_wiki/index.php/Special:UserLogin")
# find username field and send the username itself to the input field
driver.find_element(By.ID,"wpName1").send_keys(username)
# find password input field and insert password as well
driver.find_element(By.ID,"wpPassword1").send_keys(password)
# click login button
driver.find_element(By.ID,"wpLoginAttempt").click()

# # head to github login page
# driver.get("https://github.com/login")
# # find username/email field and send the username itself to the input field
# driver.find_element_by_id("login_field").send_keys(username)
# # find password input field and insert password as well
# driver.find_element_by_id("password").send_keys(password)
# # click login button
# driver.find_element_by_name("commit").click()