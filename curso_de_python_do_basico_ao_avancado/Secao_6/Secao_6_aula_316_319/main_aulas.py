from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager



# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/

# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html




"""
outra forma
    ROOT_FOLDER = Path(__file__).parent
    CHROMEDRIVER_EXEC= ROOT_FOLDER /'drivers'/'chromedriver.exe'
    chrome_service = Service(executable_path=str(CHROMEDRIVER_EXEC))
"""



# chrome_options.add_argument('--headless')
def make_chrome_browser(*options: str) -> webdriver.Chrome:
    """
    The make_chrome_browser function is a wrapper for the webdriver.Chrome 
        function, which returns an instance of the Chrome browser.
    The make_chrome_browser function takes in any number of options as strings 
    and passes them to the webdriver.ChromeOptions() class, which then passes 
    them to ChromeDriverManager().install(), which installs chromedriver with 
    those options.
    
    :param *options: str: Pass in any number of arguments to the function
    :return: A chrome webdriver object
    :doc-author: Trelent
    """
    chrome_options = webdriver.ChromeOptions()
    chrome_service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(
                    service=chrome_service,
                    options=chrome_options
                    )
    return browser


if __name__ == '__main__':
    #Example
    TIME_PASS = 10
    # options = '--hedless', 'disable-gpu', '--no-sandbox'
    options = ('disable-gpu', '--no-sandbox')
    browser = make_chrome_browser(*options)
    # como antes
    browser.get('http://www.google.com.br')
    # esperar aparece
    search_input = WebDriverWait(
            browser, TIME_PASS
        ).until(EC.presence_of_element_located(
                                    (By.NAME, 'q')
                                )
                )
    # escrever
    search_input.send_keys('achou')
    # tecla
    search_input.send_keys(Keys.ENTER)
    # parte results
    results = browser.find_element(By.ID, 'search')
    links = results.find_elements(By.TAG_NAME, 'a')
    links[0].click()
    # time
    sleep(TIME_PASS)