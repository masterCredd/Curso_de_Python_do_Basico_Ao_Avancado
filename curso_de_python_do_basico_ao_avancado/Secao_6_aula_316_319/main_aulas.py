
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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


    chrome_options = webdriver.ChromeOptions()
    chrome_service = Service(ChromeDriverManager().install())

    browser = webdriver.Chrome(
                    service=chrome_service,
                    options=chrome_options
                    )
    return browser


if __name__ == '__main__':
    #Example
    # options = '--hedless', 'disable-gpu', '--no-sandbox'
    options = ('--hedless', 'disable-gpu', '--no-sandbox')
    browser = make_chrome_browser(*options)
    
    # como antes
    browser.get('http://www.google.com.br')
    
    sleep(10)