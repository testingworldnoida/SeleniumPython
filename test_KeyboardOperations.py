from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def test_mycase():
    path="C:\\Users\\TestingWorld\\Downloads\\chromedriver_win32 (3)\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://www.theTestingWorld.com/testings")
    driver.find_element_by_name("fld_username").send_keys("Hello")

    act = ActionChains(driver)
    act.send_keys(Keys.CONTROL).send_keys("a").perform()
