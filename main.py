from scraper import Scraper
import sys

# Check if Command Line Arguments provided
try:
    course_code = sys.argv[1]
    semester = sys.argv[2]
    subject = sys.argv[3]
except IndexError:
    pass

scraper = Scraper()
scraper.check_course()
