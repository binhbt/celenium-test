from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle
import traceback

driver = webdriver.Firefox()
executor_url = driver.command_executor._url
session_id = driver.session_id
driver.get("https://www.facebook.com")

elem = driver.find_element_by_name("email")
elem.clear()
elem.send_keys("binhbt@vega.com.vn")
elem1 = driver.find_element_by_name("pass")
elem1.clear()
elem1.send_keys("PrettyBoy88")
elem1.send_keys(Keys.RETURN)

print(session_id)
print(executor_url)

def create_driver_session(session_id, executor_url):
    from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

    # Save the original function, so we can revert our patch
    org_command_execute = RemoteWebDriver.execute

    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return org_command_execute(self, command, params)

    # Patch the function before creating the driver object
    RemoteWebDriver.execute = new_command_execute

    new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    new_driver.session_id = session_id

    # Replace the patched function with original function
    RemoteWebDriver.execute = org_command_execute

    return new_driver

driver2 = create_driver_session(session_id, executor_url)
# driver2.get('https://www.facebook.com/groups/1621345418078039/')
print(driver2.current_url)