from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

def test_firstcase():
    path="C:\\Users\\TestingWorld\\Downloads\\chromedriver_win32 (3)\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://www.theTestingWorld.com/testings")

    # Maximize browser

    driver.maximize_window()

    #  Enter Data to the textbox
    driver.find_element_by_name("fld_username").send_keys("helloworld")
    driver.find_element_by_xpath("//input[@name='fld_email']").send_keys("testingworldindia@gmail.com")
    driver.find_element_by_name("fld_password").send_keys("abcd123")
    driver.find_element_by_name("fld_cpassword").send_keys("abcd123")
    driver.find_element_by_name("fld_username").clear()
    driver.find_element_by_name("fld_username").send_keys("abcd123")




























# Working on Radio button
#driver.find_element_by_xpath("//input[@value='office']").click()

#  Work on Dropdown
#obj = Select(driver.find_element_by_name("sex"))
#obj.select_by_visible_text("Male")
#obj.select_by_value("2")
#obj.select_by_index(2)

# Working on Checkbox
#driver.find_element_by_name("terms").click()

# Work on Button
#driver.find_element_by_xpath("//input[@type='submit']").click()

# Work on Links
#driver.find_element_by_link_text("Read Detail").click()

#driver.close()


