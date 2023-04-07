from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from constants import globalConstants

class Test_Homework6:

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(globalConstants.URL)

    def test_username_password(self):
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        loginUserNameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        loginUserPasswordInput = self.driver.find_element(By.ID,"password")
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(loginUserNameInput,"")
        actions.send_keys_to_element(loginUserPasswordInput,"")
        actions.perform()
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        print(errorMessage)
        testResult = errorMessage.text == "Epic sadface: Username and Password is required"
        print(f"Test Result : {testResult}")
        errorIcon = self.driver.find_element(By.CLASS_NAME,"error-button")
        errorIcon.click()
        print(errorIcon)

    def test_password(self):
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        loginUserNameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        loginUserPasswordInput = self.driver.find_element(By.ID,"password")
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(loginUserNameInput,"1")
        actions.send_keys_to_element(loginUserPasswordInput,"")
        actions.perform()
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        print(errorMessage)
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"Test Result : {testResult}")

    def test_out(self):
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        loginUserNameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        loginUserPasswordInput = self.driver.find_element(By.ID,"password")
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(loginUserNameInput,"locked_out_user")
        actions.send_keys_to_element(loginUserPasswordInput,"secret_sauce")
        actions.perform()
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        print(errorMessage)
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Test Result : {testResult}")
    
    def test_valid_login(self):
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        loginUserNameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        loginUserPasswordInput = self.driver.find_element(By.ID,"password")
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(loginUserNameInput,"standard_user")
        actions.send_keys_to_element(loginUserPasswordInput,"secret_sauce")
        actions.perform()
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        print(errorMessage)
        testResult = errorMessage.text == "Epic sadface: invalid login."
        print(f"Test Result : {testResult}")

    def test_invalid_login(self):
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        loginUserNameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        loginUserPasswordInput = self.driver.find_element(By.ID,"password")
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(loginUserNameInput,"1")
        actions.send_keys_to_element(loginUserPasswordInput,"1")
        actions.perform()
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        print(errorMessage)
        testResult = errorMessage.text == "Epic sadface: invalid login."
        print(f"Test Result : {testResult}")

    def test_icon(self):
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        loginUserNameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        loginUserPasswordInput = self.driver.find_element(By.ID,"password")
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(loginUserNameInput,"1")
        actions.send_keys_to_element(loginUserPasswordInput,"1")
        actions.perform()
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.CLASS_NAME,"error-button")
        print(errorMessage)
        testResult = errorMessage.text == "Epic sadface: Sorry, icon click."
        print(f"Test Result : {testResult}")

    def test_product_number(self):
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        loginUserNameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        loginUserPasswordInput = self.driver.find_element(By.ID,"password")
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(loginUserNameInput,"standard_user")
        actions.send_keys_to_element(loginUserPasswordInput,"secret_sauce")
        actions.perform()
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located(By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        self.driver.get("https://www.saucedemo.com/inventory.html")
        listOfProduct = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Total Product Number {len(listOfProduct)}")

    def test_filter(self):
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        loginUserNameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        loginUserPasswordInput = self.driver.find_element(By.ID,"password")
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(loginUserNameInput,"standard_user")
        actions.send_keys_to_element(loginUserPasswordInput,"secret_sauce")
        actions.perform()
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located(By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        self.driver.get("https://www.saucedemo.com/inventory.html")
        listOfProduct = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Product Number: {len(listOfProduct)}")

    def test_add(self, username, password):
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        loginUserNameInput = self.driver.find_element((By.ID, "user-name"))
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        loginUserPasswordInput = self.driver.find_element(By.ID, "password")
        action = ActionChains(self.driver)
        action.send_keys_to_element(loginUserNameInput, username)
        action.send_keys_to_element(loginUserPasswordInput, password)
        action.perform()
        logIn = self.driver.find_element(By.ID, "login-button")
        logIn.click()
        self.driver.get("https://www.saucedemo.com/inventory.html")

    def test_page(self):
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        loginUserNameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        loginUserPasswordInput = self.driver.find_element(By.ID,"password")
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(loginUserNameInput,"standard_user")
        actions.send_keys_to_element(loginUserPasswordInput,"secret_sauce")
        actions.perform()
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located(By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        self.driver.get("https://www.saucedemo.com/inventory.html")
        
test = Test_Homework6()
test.test_invalid_login()
test.test_valid_login()
test.test_username_password()
test.test_password()
test.test_icon()
test.test_product_number()
test.test_filter()
test.test_add()
test.test_page()
test.test_out()