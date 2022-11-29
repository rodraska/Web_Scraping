import os
import selenium.webdriver as webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import F

driver_service = Service(executable_path='/nfs/homes/rreis-de/Documents/geckodriver.exe')
driver_options = Options()
driver_options.add_argument('--headless')
driver_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=driver_service,options=driver_options)

driver.get('https://www.zerozero.pt/equipa.php?id=16')
