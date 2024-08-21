from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup 
import time
import random

# Chrome brower options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--user-agent=your-user-agent-string")

driver = webdriver.Chrome(options=options)

driver.get("https://www.planetfitness.com/gyms/escondido-ca") 

time.sleep(random.uniform(3,6))

# Click on the element 
driver.find_element(By.ID, "onetrust-reject-all-handler").click()

htmlSource = driver.page_source

soup = BeautifulSoup(htmlSource, 'html.parser')

#print(soup.prettify())

#driver.close()