from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Python & Selenium Kursu
# 18 Mart 2023 
# Ödev-4

driver = webdriver.Chrome(ChromeDriverManager().install())

class SauceDemo:
    def noUserPass(self):
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        loginBtn = driver.find_element(By.ID , "login-button")
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH , "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        errorResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"Test Sonucu-1: {errorResult}")

    def noPass(self):
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        usernameInput = driver.find_element(By.ID , "user-name")
        passwordInput = driver.find_element(By.ID , "password")
        usernameInput.send_keys("Test")
        passwordInput.send_keys()
        sleep(1)
        loginBtn = driver.find_element(By.ID , "login-button")
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH , "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        errorResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"Test Sonucu-2: {errorResult}")

    def wrongUserPass(self):
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        usernameInput = driver.find_element(By.ID , "user-name")
        passwordInput = driver.find_element(By.ID , "password")
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(1)
        loginBtn = driver.find_element(By.ID , "login-button")
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH , "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        errorResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Test Sonucu-3: {errorResult}")

    def icon(self):
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        usernameInput = driver.find_element(By.ID , "user-name")
        passwordInput = driver.find_element(By.ID , "password")
        usernameInput.send_keys()
        passwordInput.send_keys()
        sleep(1)
        loginBtn = driver.find_element(By.ID , "login-button")
        loginBtn.click()
        sleep(1)
        iconFind = driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3 > button > svg > path")
        iconFind.click()
        
    def login(self):
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        usernameInput = driver.find_element(By.ID , "user-name")
        passwordInput = driver.find_element(By.ID , "password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(1)
        loginBtn = driver.find_element(By.ID , "login-button")
        loginBtn.click()
        sleep(1)
        product = driver.find_elements(By.CLASS_NAME, "inventory_item")
        if len(product) == 6:
            print(f"Test Başarılı! Anlık Ürün Sayısı: {len(product)}")
        else :
            print("Test Başarısız! 6'dan fazla ürün mevcut.")

# Tüm Testler
Test = SauceDemo()
Test.noUserPass()
Test.noPass()
Test.wrongUserPass()
Test.icon()
Test.login()

while True:
    continue

#indigo6alfa

#SON
#SON
#SON