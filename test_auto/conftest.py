import pytest
import selenium.webdriver


@pytest.fixture()
def get_driver():
    driver = selenium.webdriver.Edge()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()
