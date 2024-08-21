from selenium import webdriver 
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup 
import re
import time
import random


# create webdriver object 
options = webdriver.FirefoxOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
# Chrome_options. add_experiment_option ('excludeSwitches', ['enable-automation'])

driver = webdriver.Firefox(options=options) 

# get google.co.in 
driver.get("https://www.planetfitness.com/gyms/escondido-ca") 
time.sleep(random.uniform(3,8))

# Click on the element 
driver.find_element(By.ID, "onetrust-reject-all-handler").click()

htmlSource = driver.page_source

soup = BeautifulSoup(htmlSource, 'html.parser')
try:
    # Find the element with the aria-label that contains "percent full"
    crowd_meter_label = soup.find(attrs={"aria-label": re.compile(r'\d+ percent full')})

    # Extract the number from the aria-label
    if crowd_meter_label:
        crowd_percent_full = re.search(r'\d+', crowd_meter_label['aria-label']).group()
        print(f"The gym is {crowd_percent_full}% full.")
    else:
        print("Could not find the crowd meter information.")
except:
    print("Failed")
    
    
# Close the driver
#driver.close()