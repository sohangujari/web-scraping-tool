# Web Scraper

This is a simple web scraping tool with a Tkinter GUI. It allows scraping data from a website into a CSV file.

## Usage

The `main.py` file contains the web scraper code. It uses:

- `requests` and `BeautifulSoup` to scrape web pages
- `pandas` to store scraped data in a dataframe 
- `Tkinter` to create the GUI

To scrape data:

1. Enter a URL
2. Select tags, classes and column names 
3. Click submit to scrape data into a CSV

The GUI allows choosing to create a new CSV file or append to an existing one.

### Required Libraries

This project requires the following libraries:

- requests
- beautifulsoup4
- pandas
- Tkinter

Install requirements:

```
pip install -r requirements.txt
``` 

### Running the Scraper

```
python main.py
```

This will launch the Tkinter GUI. Fill out the fields and click submit to scrape data.

### Customizing

The scrape logic inside `submit()` can be customized for different websites by:

- Changing the tags, classes and other selectors
- Altering the data flow and transformations
- Adding more sources and joins

## To Do

Potential improvements:

- More flexibility in specifying selectors 
- GUI enhancements like validation
- Multipage scraping
- Export formats besides CSV
