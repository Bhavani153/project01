import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import sys

# Add the parent directory to the path if amazon_login_page.py is in the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from orange_login_page import OrangeLoginPage

@pytest.fixture
def browser():
    chromedriver_path = r"E:\Automation testing\chromedriver.exe"
    if not os.path.exists(chromedriver_path):
        raise FileNotFoundError(f"ChromeDriver not found at path: {chromedriver_path}")

    os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(60)
    driver.maximize_window()
    yield driver

####Test case ID:TC_login_01
def test_orange_login(browser):
    orange_login_page = OrangeLoginPage(browser)
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Perform login actions
    orange_login_page.enter_username("Admin")
    orange_login_page.enter_password("admin123")
    orange_login_page.click_login_submit()

###Test case ID:TC_login_02
def test_orange_login(browser):
    orange_login_page = OrangeLoginPage(browser)
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    orange_login_page.enter_username("Admin")
    orange_login_page.enter_password("invalid password")
    #try & exception handling
    try:
        orange_login_page.click_login_submit()
    except:
        print("Invalid Credential")

###Test case ID:TC_PIM_01
def test_orange_login(browser):
    orange_login_page = OrangeLoginPage(browser)
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    orange_login_page.enter_username("Admin")
    orange_login_page.enter_password("admin123")
    orange_login_page.click_login_submit()
    orange_login_page.click_pim()
    orange_login_page.click_add()
    orange_login_page.enter_firstname("Bhavani")
    orange_login_page.enter_middlename("Kannan")
    orange_login_page.enter_lastname("K")
    orange_login_page.enter_employeeid("236")
    orange_login_page.click_save()
###Test case ID:TC_PIM_02
    orange_login_page.click_pim()
    orange_login_page.click_edit()
    orange_login_page.enter_otherid("XX23656")
    orange_login_page.enter_drivelicense("236gb45")
    orange_login_page.click_gender()
    orange_login_page.click_save2()
###Test case ID:TC_PIM_03
    orange_login_page.click_pim()
    orange_login_page.click_delete()
    orange_login_page.click_popup_link()

