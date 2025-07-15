import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def init_driver():
    driver = webdriver.Chrome()
    yield
    driver.quit()



