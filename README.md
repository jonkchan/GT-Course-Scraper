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

3. Update `SEMESTER`, `SUBJECT`, & `COURSE_CODE` variables under `main.py`

```python
# ./main.py
SEMESTER = "Fall 2020"
SUBJECT = "Computer Science"
COURSE_CODE = "6300"
```

## Usage

```bash
python main.py
```

## Example

<img src="https://i.imgur.com/IIu6BMV.gif" width="800" />

## License

[MIT](https://choosealicense.com/licenses/mit/)
