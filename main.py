from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3795852668&f_AL=true&geoId=101174742&keywords=junior%20developer&location=Canada&origin=JOB_SEARCH_PAGE_LOCATION_HISTORY&refresh=true")

time.sleep(5)
#this is the updated version
sign_in_button =driver.find_element("link text", "Sign in")
#this is the old version
#sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()


email_field = driver.find_element(By.ID, "username")
email_field.send_keys("adamluqmanhakim96@gmail.com")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("0132821933")
password_field.send_keys(Keys.ENTER)

all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    time.sleep(20)
    listing_text = listing.text  # Extract the text of the listing
    #print("called " + listing_text+"\n")
    listing.click()
    time.sleep(2)
    check_easy_button_exist = driver.find_element(By.CSS_SELECTOR,'div[class="jobs-s-apply jobs-s-apply--fadein inline-flex mr2"]')
    check_easy_button_exist_text = check_easy_button_exist.text
    if check_easy_button_exist_text == "Easy Apply":
        print("Applying")
        easy_button = driver.find_element(By.CLASS_NAME,
                                          "jobs-apply-button--top-card")
        time.sleep(2)
        easy_button.click()
        time.sleep(2)
        #next step


        try:
            next_button=driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Continue to next step"]')
            next_button_text = next_button.text
            print("------"+next_button_text)
            while driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Continue to next step"]').text == "Next":
                print("footer_button_text")
                next_button.click()
                print("next ")
                time.sleep(15)
        except NoSuchElementException:
            print("No application button ")


            #review

        try:
            print("-------------------")

            time.sleep(2)
            review_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Review your application"]')
            driver.execute_script("arguments[0].scrollIntoView();", review_button)
            review_button_text = review_button.text
            print("review_button_text = "+review_button.text)
            if review_button_text == "Review":
                review_button.click()
                time.sleep(2)
                #error
                try:
                    # Attempt to find the element
                    error_review = driver.find_element(By.CSS_SELECTOR, 'li-icon[aria-hidden="true"]')

                    # If the element is found, print a success message
                    print("Element found!")
                    time.sleep(2)
                    dismiss_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss"]')
                    dismiss_button.click()
                    time.sleep(2)
                    save_button = driver.find_element(By.CSS_SELECTOR,'[data-control-name="save_application_btn"]')
                    save_button.click()
                    time.sleep(2)


                except NoSuchElementException:
                    # If the element is not found, print a failure message
                    print("Element not found!")
                    pass

            else:
                print("No review button ")
        except NoSuchElementException:
            print("No Review button ")

        #submit

        time.sleep(2)
        # Scroll to the element
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


        time.sleep(2)
        submit_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Submit application"]')

        #scroll until you find the submit button
        driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        time.sleep(2)
        #click submit button
        submit_button.click()
        time.sleep(2)
        #Dismiss
        dismiss_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss"]')
        dismiss_button.click()



    else :
        print("Already applied")













