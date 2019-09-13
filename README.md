# Telecontact-Scraper
a command line tool to scrape [telecontact.ma](https://www.telecontact.ma/) data

## How to use it:
* __install requirements__
```bash
pip install -r requirements.txt
```

* __install package__
```bash
pip install -e .
```

* __command to run the scraping__
```python
"""
Usage:
    telecontact-scraper mine <string> <ou> [--file_path=<destination_file>]

Options:
    <string>    Qui,quoi? (raison sociale ou activité)
    <ou>        Où? (Casablanca)   
    --file_path file to save results to (json format)
"""
```

## Run as docker image

* __build image__
```bash
docker build -t telecontact-scraper .
```

* __run image with arguments__
(Example)
```bash
docker run -it --rm telecontact-scraper tech rabat
```
