# GT Course Scraper

GT Course Scraper retrieves the latest course registration data from the GT OSCAR Registration platform.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Installation

1. Use the [pip](https://pip.pypa.io/en/stable/) package manager to install [requirements](./requirements.txt)

```bash
pip install -r requirements.txt
```

2. Create `.env` file and update GT OSCAR Credentials

```bash
touch .env
echo "GTID=<GT ID>" >> .env
echo "GTPW=<GT Password>" >> .env
```

3. Update `SEMESTER`, `SUBJECT`, and `COURSE_CODE` arguments under `scraper.py`

```python
# ./scraper.py
semester = "Fall 2020"
subject = "Computer Science"
course_code = "6300"
```

## Usage

```bash
python main.py <course_code>
```

## Example

<img src="https://i.imgur.com/IIu6BMV.gif" />

## License

[MIT](https://choosealicense.com/licenses/mit/)
