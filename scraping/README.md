# Bart-children-pipeline

## Folder Structure

```
📦 ProjectName
├── cleaning_links.py          # leave only last part of URL for final_link
├── scraping_data.py       # Collect data from Wikipedia and Vikidia
├── vikidia_links.py       # Crawler to retrieve all links
├── vikidia_links_scraped.txt       # All links retrieved
├── vikidia_links_scraped_cleaned.txt # more clean links than vikidia_links_scraped.txt
├── 📂 utils       # Library code to support other python files
└── README.md       # Project documentation
```

## Command

1. Install selenium on console:
   ```python3 -m pip install selenium``` or python or py, instead of python3

2. Run python code:
   ```python "path_file"``` or python or py, instead of python3


## Usage

Before, you run the code, you have to:
- install selenium
- install chromedriver from the link
- place chromedriver in the folder 
- set variable 'PATH_' at the beginning of the code
- create folder normal and cleaned in 'data/Source' or unzip files


Pipeline for scraping:
- run vikidia_links.py
- run scraping_data.py
- run cleaning_links.py


## Links
- [chromedriver](https://googlechromelabs.github.io/chrome-for-testing/)
- [Project Documentation](https://yourdocumentationlink.com)