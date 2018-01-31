# UNFCC Scrapper
United Nations Framework Convention on Climate Change (UNFCC) content scrapper and extractor

### Installation
---------
Make sure you have python 3.x running on your machine. All the dependencies can be installed using pip
```
pip install PyPDF2
pip install pandas
pip install bs4
```

### Usage
----------
There are two main scripts and both need to be run from the root directory:
```
scrapper.py --> download the pdd files given:
            - list of unfcc_id specified in unfcc_ids_config.ini
            - url or list of url
            - the unfcc_id

e.g:
    - python scrapper.py --config=True
    - python scrapper.py --url="http://cdm.unfccc.int/Projects/Validation/DB/UKLMN824TUIYJ8PEWAPX96273EQ01L/view.html"
    - python scrapper.py --id="UKLMN824TUIYJ8PEWAPX96273EQ01L"

```

```
pdd_reader.py --> read the content from the pdf file that exist in `downloads/` and check if the pdf contains keywords specified in keywords_config.ini

e.g:
    - python pdd_reader.py
```

once you run the `pdd_reader.py`, a xlsx file will be created and saved on the root directory. This file will contains three fields:
```
    - content: the content from section A.4.3
    - EXIST: whether or not the specified keywords exist in a particular pdd file
    - ID: the ID of the unfcc file
```
## Running the tests
---------
you can run the test per script/class by:
```
python -m unittest test.test_scrapper
```

```
python -m unittest test.pdd_reader
```
