from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os

from dotenv import load_dotenv
load_dotenv()

# Open Webdriver for Chrome Version 84
driver = webdriver.Chrome('.\drivers\chromedriver.exe')
# driver = webdriver.Ie('.\drivers\IEDriverServer.exe')

# Navigate to GT Course Registration Website
URL = r'https://login.gatech.edu/cas/login?service=https%3A%2F%2Fsso.sis.gatech.edu%3A443%2Fssomanager%2Fc%2FSSB'
driver.get(URL)

# Load GT OSCAR Credentials from .env file
GTID = os.getenv('GTID')
GTPW = os.getenv('GTPW')

# Log into GT OSCAR with credentials
driver.find_element_by_name("username").send_keys(GTID)
driver.find_element_by_name("password").send_keys(GTPW)
driver.find_element_by_name("submit").click()

# Update Semester, Subject, and Course CRN accordingly
SEMESTER = "Fall 2020"
SUBJECT = "Computer Science"
CRN = "86063"

try:
    # Navigate to Student Services & Financial Aid - Select Term
    URL = r"https://oscar.gatech.edu/pls/bprod/bwskfreg.P_AltPin"
    driver.get(URL)

    # Select Semester from dropdown
    semester_dropdown = Select(driver.find_element_by_name("term_in"))
    semester_dropdown.select_by_visible_text(SEMESTER)

    # Click on 'Submit' button
    submit_btn = driver.find_element_by_css_selector(
        "input[type='submit'][value='Submit']")
    submit_btn.click()

    # Click on 'Class Search' button
    class_search_btn = driver.find_element_by_css_selector(
        "input[type='submit'][value='Class Search']")
    class_search_btn.click()

    # Select Subject from dropdown
    subjects = driver.find_elements_by_css_selector("option")
    for subject in subjects:
        subject_text = subject.get_attribute("innerText")
        if subject_text == SUBJECT:
            subject.click()

    # Click on 'Course Search' button
    course_search_btn = driver.find_element_by_css_selector(
        "input[type='submit'][name='SUB_BTN'][value='Course Search']")
    course_search_btn.click()

    course_row = driver.find_elements_by_css_selector("td[class='dddefault']")
    for row in course_row:
        inner_value = row.get_attribute("value")
        if inner_value == CRN:
            print("matched")

except Exception as e:
    print(e)

# Close Webdriver
# driver.quit()
