import time
import selenium
from selenium.webdriver.edge import webdriver
from selenium.webdriver.common.by import By


def open_edge():
    edge = selenium.webdriver.Edge()
    edge.get('https://www.baidu.com/')
    element = edge.find_element(By.XPATH, '//*[@id="kw"]')
    element.send_keys('余凯')
    element.submit()

    # edge.find_element(By.XPATH,'//*[@id="su"]').click()
    print('地址为', edge.current_url)
    print('标题为', edge.title)
    time.sleep(120)


if __name__ == '__main__':
    open_edge()
