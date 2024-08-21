from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup 
import re
import time
import random

def scrape() -> int:
    num_filled_tally_marks = 0

    # create webdriver object 
    options = webdriver.FirefoxOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")

    driver = webdriver.Firefox(options=options) 

    # Navigate to the Planet Fitness gym page
    driver.get("https://www.planetfitness.com/gyms/escondido-ca") 
    time.sleep(random.uniform(3, 5))

    # Click on the element to reject cookies if needed
    driver.find_element(By.ID, "onetrust-reject-all-handler").click()

    try:
        # Wait for the crowd meter to be loaded by waiting for a parent container or element that holds it
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'StripedProgressBar__Container')]"))
        )
        
        # Get the page source
        htmlSource = driver.page_source

        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(htmlSource, 'html.parser')

        # Find all the elements with data-testid="completed-item"
        # NOTE: Planet Fitness website looks different when opened with selenium
        filled_tally_marks = soup.find_all('path', {'data-testid': 'completed-item'})

        # Count the number of filled tally marks
        num_filled_tally_marks = len(filled_tally_marks)

        print(f'Number of filled tally marks: {num_filled_tally_marks}')
        
        if (num_filled_tally_marks > 0):
            driver.close()
            return num_filled_tally_marks
        
    except (TimeoutException, NoSuchElementException) as e:
        print(f"An error occurred: {e}")
        
    try: 
        
        # Get the page source
        htmlSource = driver.page_source

        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(htmlSource, 'html.parser')

        if(num_filled_tally_marks == 0): 
            # Find the element with the aria-label that contains "percent full"
            crowd_meter_label = soup.find(attrs={"aria-label": re.compile(r'\d+ percent full')})

    # Extract the number from the aria-label
        if crowd_meter_label:
            percent_full = re.search(r'\d+', crowd_meter_label['aria-label']).group()
            print(f"The gym is {percent_full}% full.")
            driver.close()
            return int(percent_full)
        else:
            print("Could not find the crowd meter information.")
            driver.close()
            return -1
    except (TimeoutException, NoSuchElementException) as e:
            print(f"An error occurred {e}")
    
    # Close the driver
    driver.close()