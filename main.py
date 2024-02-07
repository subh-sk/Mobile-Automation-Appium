import unittest
from typing import Dict,Any
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities:Dict[str,Any] = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_battery(self) -> None:
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
        el.click()
    
    # def find_button(self) -> None:
    #     el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.miui.calculator:id/btn_8_s"]')
    #     print("el = ",el)
    #     # el.click()

if __name__ == '__main__':
    unittest.main()