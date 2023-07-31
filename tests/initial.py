from appium import webdriver

desired_caps = {
    "app": "C:.exe",  # Replace with the path to your Windows application
    "platformName": "Windows",
    "deviceName": "WindowsPC",
}

driver = webdriver.Remote(command_executor='http://127.0.0.1:4723', desired_capabilities=desired_caps)

# Example test: Launch the application and perform a simple action (replace with your own test steps)
try:
    # Add your test steps here
    # For example, find and click a button with AutomationID "btnLogin":
    login_button = driver.find_element_by_accessibility_id("btnLogin")
    login_button.click()

    # Add assertions or other test steps as needed
    # For example, assert that a certain text is displayed after clicking the button:
    message_text = driver.find_element_by_accessibility_id("txtMessage").text
    assert "Login successful" in message_text

except Exception as e:
    print("Test failed:", str(e))

finally:
    driver.quit()