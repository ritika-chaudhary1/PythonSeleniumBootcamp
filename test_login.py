# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager


# def test_login():
#     driver = webdriver.Chrome(
#         service=Service(ChromeDriverManager().install())
#     )

#     driver.get("https://the-internet.herokuapp.com/login")

#     username = driver.find_element(By.ID, "username")
#     password = driver.find_element(By.ID, "password")

#     username.send_keys("tomsmith")
#     password.send_keys("SuperSecretPassword!")

#     driver.find_element(
#         By.CSS_SELECTOR,
#         "button[type='submit']"
#     ).click()

#     print("Login test executed")

#     driver.quit()

    #now we learn the assertions in the same page by changing some part.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_login():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.get("https://the-internet.herokuapp.com/login")

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")

    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")


#for assertins
    driver.find_element(
    By.CSS_SELECTOR,
    "button[type='submit']"
     ).click()
#for test pass url
    # assert driver.current_url == "https://the-internet.herokuapp.com/secure"    

#for test fail url
    # assert driver.current_url == "https://example.com"


#for assertion:
 # Assertion 1: Verify URL
    assert driver.current_url == "https://the-internet.herokuapp.com/secure"

    # Assertion 2: Verify page title
    assert driver.title == "The Internet"

    # Assertion 3: Verify heading
    assert driver.find_element(By.CSS_SELECTOR, "h2").text == "Secure Area"

    # Assertion 4: Verify text exists on page
    assert "Secure" in driver.page_source
    # assert "WrongText" in driver.page_source


    print("Login test passed")

    driver.quit()

