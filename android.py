from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

desired_caps = {
    "deviceName": "Galaxy S20",
    "platformName": "Android",
    "platformVersion": "10",
    "app": "APP_URL",  # Enter app_url here
    "isRealMobile": True,
    "build": "Python Vanilla Android",
    "name": "Sample Test - Python",
    "autoGrantPermissions": True,
    "network": False,
    "visual": True,
    "video": True
}


def startingTest():
    if os.environ.get("LT_USERNAME") is None:
        # Enter LT username here if environment variables have not been added
        username = "YOUR_LT_USERNAME"
    else:
        username = os.environ.get("LT_USERNAME")
    if os.environ.get("LT_ACCESS_KEY") is None:
        # Enter LT accesskey here if environment variables have not been added
        accesskey = "YOUR_ACCESS_KEY"
    else:
        accesskey = os.environ.get("LT_ACCESS_KEY")

    try:
        driver = webdriver.Remote(desired_capabilities=desired_caps, command_executor="https://" +
                                  username+":"+accesskey+"@mobile-hub.lambdatest.com/wd/hub")
        readMoreButtonElement = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/readMoreButton")))
        readMoreButtonElement.click()
        time.sleep(3)

        backButtonReadMorePageElement = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((MobileBy.ID, "com.lambdatest.proverbial:id/backButtonReadMorePage")))
        backButtonReadMorePageElement.click()
        time.sleep(3)

        LocationElement = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ACCESSIBILITY_ID, "Location")))
        LocationElement.click()
        time.sleep(3)

        driver.back()

        browser = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.XPATH, "//android.widget.FrameLayout[@content-desc=\"Browser\"]/android.widget.FrameLayout/android.widget.ImageView")))
        browser.click()
        time.sleep(3)

        url = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/url")))
        url.send_keys("https://www.lambdatest.com")
        time.sleep(3)

        find = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/find")))
        find.click()
        time.sleep(3)

        Home = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ACCESSIBILITY_ID, "Home")))
        Home.click()
        time.sleep(5)

        Drawer = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ACCESSIBILITY_ID, "drawer open")))
        Drawer.click()
        time.sleep(3)

        notification = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.XPATH, "//android.widget.CheckedTextView[contains(@text,\"Push Notification\")]")))
        notification.click()
        time.sleep(5)

        driver.back()

        closeDrawer = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ACCESSIBILITY_ID, "drawer Closed")))
        closeDrawer.click()
        time.sleep(3)

        
        driver.quit()
    except:
        driver.quit()


startingTest()
