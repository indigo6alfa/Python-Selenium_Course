from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
from datetime import date
import pytest
import time

class Test_Sauce():

    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok = True)

    
    def teardown_method(self):
        self.driver.quit()

    def wait_for_element_visible(self,locator):
        WebDriverWait(self.driver,6).until(EC.visibility_of_element_located(locator))

    # Valid Login
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_valid_Login(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()      
        self.driver.save_screenshot(f"{self.folderPath}/test-get-login-{username}-{password}.png") 

    
    # Invalid Login
    @pytest.mark.parametrize("username,password",[("3","3"),("celal","kam"),("cemil","qwerty")])
    def test_invalid_login(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput, username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        errorMesage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png") 
        assert errorMesage.text == 'Epic sadface: Username and password do not match any user in this service'

    # Any Login
    @pytest.mark.parametrize("username,password",[("", "")])
    def test_any_Login(self,username,password):
        self.wait_for_element_visible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        
        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-empty-login-{username}-{password}.png")
        assert errorMessage.text == 'Epic sadface: Username is required'      

    # No Password Login
    @pytest.mark.parametrize("username,password",[("karaman","")])
    def test_no_Password(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-empty-password-login-{username}-{password}.png")
        assert errorMessage.text == 'Epic sadface: Password is required'

    # User+Password
    @pytest.mark.parametrize("username,password",[("locked_out_user","secret_sauce")])
    def test_block_out(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-locked-out-login-{username}-{password}.png")
        assert errorMessage.text == 'Epic sadface: Sorry, this user has been locked out.'
        
    # Icon
    @pytest.mark.parametrize("username,password",[("yaz","kış")])
    def test_x_Icon(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        self.driver.save_screenshot(f"{self.folderPath}/test-icon-{username}-{password}.png")

        sBtn = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button")
        sBtn.click()

    # Product
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_product(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()
        
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        self.driver.get("https://www.saucedemo.com/inventory.html")
        self.driver.save_screenshot(f"{self.folderPath}/test-product-list-{username}-{password}.png")
   
   # Product Number
    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
    def test_p_number(self, username, password):
        self.wait_for_element_visible((By.ID, "user-name"))
        userNameInput = self.driver.find_element(By.ID, "user-name")
       
        self.wait_for_element_visible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(userNameInput, username)
        action.send_keys_to_element(passwordInput, password)
        action.perform()
       
        logIn = self.driver.find_element(By.ID, "login-button")
        logIn.click()
       
        pNumber = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        self.driver.save_screenshot(f"{self.folderPath}/test-item-number-{username}-{password}.png")
        assert len(pNumber) == 6

    # Add Product
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_add_Product(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        add_button = self.driver.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-bike-light']")
        add_button.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-add-cart-{username}-{password}.png")

        pbutton = self.driver.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a")
        pbutton.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-add-cart-{username}-{password}.png")


    # Filter
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_product_F(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        fBtn = self.driver.find_element(By.CLASS_NAME,"product_sort_container")
        fBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-product-sort-{username}-{password}.png")


    # Exit
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_Log_Out(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()
        
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        mBtn = self.driver.find_element(By.ID,"react-burger-menu-btn")
        mBtn.click()
        time.sleep(1)

        l_OutBtn = self.driver.find_element(By.ID,"logout_sidebar_link")
        l_OutBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-log-out-{username}-{password}.png")

        test = Test_Sauce()
        test.test_valid_Login()
        test.test_invalid_login()
        test.test_any_Login()
        test.test_no_Password()
        test.test_block_out()
        test.test_x_Icon()
        test.test_product()
        test.test_p_number()
        test.test_add_Product()
        test.test_product_F()
        test.test_Log_Out()