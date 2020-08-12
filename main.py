from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os

from dotenv import load_dotenv
load_dotenv()

# Open Webdriver for Chrome Version 84
options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(
    executable_path='.\drivers\chromedriver.exe', chrome_options=options)

# Navigate to GT Course Registration Website
URL = r'https://login.gatech.edu/cas/login?service=https%3A%2F%2Fsso.sis.gatech.edu%3A443%2Fssomanager%2Fc%2FSSB'
driver.get(URL)

# Load GT OSCAR Credentials from .env file
GTID = os.getenv('GTID')
GTPW = os.getenv('GTPW')

# Log into GT OSCAR with credentials
print("Logging in...")
driver.find_element_by_name("username").send_keys(GTID)
driver.find_element_by_name("password").send_keys(GTPW)
driver.find_element_by_name("submit").click()

# Update Semester, Subject, and Course Code accordingly
SEMESTER = "Fall 2020"
SUBJECT = "Computer Science"
COURSE_CODE = "6300"

try:
    # Navigate to Student Services & Financial Aid - Select Term
    URL = r"https://oscar.gatech.edu/pls/bprod/bwskfreg.P_AltPin"
    driver.get(URL)

    # Select Semester from dropdown
    print("Selecting Semester...")
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
    print("Selecting Subject...")
    subjects = driver.find_elements_by_css_selector("option")
    for subject in subjects:
        if subject.get_attribute("innerText") == SUBJECT:
            subject.click()

    # Click on 'Course Search' button
    course_search_btn = driver.find_element_by_css_selector(
        "input[type='submit'][name='SUB_BTN'][value='Course Search']")
    course_search_btn.click()

    # Click on 'View Section' button for matching COURSE CODE
    print("Selecting Course...")
    course_rows = driver.find_elements_by_tag_name("tr")
    for course_row in course_rows:
        if COURSE_CODE in course_row.get_attribute("innerText"):
            view_section_button = course_row.find_element_by_css_selector(
                "input[name='SUB_BTN'][value='View Sections']")
            view_section_button.click()
            break

    # Print available course section data
    section_rows = driver.find_elements_by_css_selector(
        "table.datadisplaytable tbody tr")
    for section_row in section_rows:
        if COURSE_CODE in section_row.get_attribute("innerText"):
            print(section_row.get_attribute("innerText"))

except Exception as e:
    print(e)

# Close Webdriver
# driver.quit()
