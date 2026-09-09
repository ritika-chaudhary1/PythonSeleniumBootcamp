
# # #for using the fixure
# # import pytest
# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from webdriver_manager.chrome import ChromeDriverManager


# # @pytest.fixture
# # def driver():
# #     driver = webdriver.Chrome(
# #         service=Service(ChromeDriverManager().install())
# #     )

# #     yield driver

# #     driver.quit()


# #using the fixture scope

# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager


# @pytest.fixture(scope="function")
# def driver():
#     driver = webdriver.Chrome(
#         service=Service(ChromeDriverManager().install())
#     )

#     yield driver

#     driver.quit()

#fixture using the module scope

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#for scope class= once per test class
@pytest.fixture(scope="class")


# @pytest.fixture(scope="module")

def driver():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    yield driver

    driver.quit()