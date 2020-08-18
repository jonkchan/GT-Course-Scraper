from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from prettytable import PrettyTable
from dotenv import load_dotenv
import os


class Scraper:

    def __init__(self):
        load_dotenv()
        self.GTID = os.getenv('GTID')
        self.GTPW = os.getenv('GTPW')
        if not self.GTID or not self.GTPW:
            raise Exception('Error: GTID / GTPW not provided in .env file')

    def check_course(self, course_code: str = "6300", semester: str = "Fall 2020", subject: str = "Computer Science") -> None:
        # Disable Browser Window
        options = Options()
        options.add_argument('headless')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        path = '.\drivers\chromedriver.exe'

        # Open Webdriver for Chrome Version 84
        driver = webdriver.Chrome(executable_path=path, chrome_options=options)

        try:
            print("> Program starting...")

            # Navigate to GT Course Registration Website
            URL = r'https://login.gatech.edu/cas/login?service=https%3A%2F%2Fsso.sis.gatech.edu%3A443%2Fssomanager%2Fc%2FSSB'
            driver.get(url=URL)

            # Log into GT OSCAR with credentials
            print("> Logging in...")
            driver.find_element_by_name('username').send_keys(self.GTID)
            driver.find_element_by_name('password').send_keys(self.GTPW)
            driver.find_element_by_name('submit').click()

            # Navigate to 'Student Services & Financial Aid - Select Term' page
            URL = r'https://oscar.gatech.edu/pls/bprod/bwskfreg.P_AltPin'
            driver.get(url=URL)

            # Select Semester from dropdown
            print(f"> Selecting {semester} Semester...")
            semester_dropdown = Select(driver.find_element_by_name('term_in'))
            semester_dropdown.select_by_visible_text(semester)

            # Click on 'Submit' button
            submit_btn_css = "input[type='submit'][value='Submit']"
            submit_btn = driver.find_element_by_css_selector(submit_btn_css)
            submit_btn.click()

            # Click on 'Class Search' button
            class_search_css = "input[type='submit'][value='Class Search']"
            class_search_btn = driver.find_element_by_css_selector(
                class_search_css)
            class_search_btn.click()

            # Select Subject from dropdown
            print(f"> Selecting {subject} Subject...")
            subject_found = False
            subjects_css = "select[name='sel_subj'] option"
            subjects = driver.find_elements_by_css_selector(subjects_css)
            for _subject in subjects:
                if _subject.text == subject:
                    subject_found = True
                    _subject.click()

            # Raise Error if subject is not available or invalid
            if not subject_found:
                raise Exception(f"{subject} subject not found")

            # Click on 'Course Search' button
            course_search_css = "input[type='submit'][name='SUB_BTN'][value='Course Search']"
            course_search_btn = driver.find_element_by_css_selector(
                course_search_css)
            course_search_btn.click()

            # Click on 'View Section' button for matching COURSE CODE
            print(f"> Searching Courses for {course_code}...")
            course_found = False
            course_rows = driver.find_elements_by_tag_name('tr')
            for course_row in course_rows:
                if course_code in course_row.get_attribute('innerText'):
                    course_found = True
                    view_section_css = "input[name='SUB_BTN'][value='View Sections']"
                    view_section_button = course_row.find_element_by_css_selector(
                        view_section_css)
                    view_section_button.click()
                    break

            # Raise Error if course is not available or invalid
            if not course_found:
                raise Exception(f"{course_code} course not found")

            # Print available course section data
            print(f"> Searching Sections for {course_code}...")
            sections = []
            section_table_css = 'table.datadisplaytable tbody tr'
            section_rows = driver.find_elements_by_css_selector(
                section_table_css)
            for section_row in section_rows:
                section_row_text = section_row.get_attribute('innerText')
                if course_code in section_row_text:
                    # Delimit section_row inner text by \t and split into array
                    section_data = section_row_text.split("\t")[1:]
                    sections.append(section_data)

            if sections:
                course_section_data = PrettyTable()

                # Course Section Table Header
                course_section_data.field_names = ['CRN', 'Subj', 'Crse', 'Sec', 'Cmp', 'Bas', 'Cred', 'Title', 'Days',
                                                   'Time', 'Cap', 'Act', 'Rem', 'WL Cap', 'WL Act', 'WL Rem', 'Instructor', 'Location', 'Attribute']
                for section in sections:
                    course_section_data.add_row(section)

                print(course_section_data)
            else:
                print('No sections found')

        except Exception as e:
            print(e)

        # Close Webdriver
        driver.quit()
