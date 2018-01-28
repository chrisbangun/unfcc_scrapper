import PyPDF2
import pandas as pd

from ConfigParser import SafeConfigParser

from os import listdir
from os.path import isfile, join

def _get_pdd_files():
    """"""
    return [f for f in listdir('downloads/') if isfile(join("downloads/", f))]

def _read_keywords_from_config():
    """reads config file and returns the keywords"""
    keywords = []
    config = SafeConfigParser()
    config.read('keywords_config.ini')
    for (key, val) in config.items('main'):
        keywords.append(val)

    return keywords

    
def is_specified_keywords_exist(keywords, pdfFileObj):
    """
    parameter:
    keywords: list
              contains all keywords that need to be checked
    pdfFileObj: pdfObject
    """
    try:
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    except:
        raise ValueError('could not find the %s file' % (file_dir))

    num_pages = pdfReader.numPages
    count = 0
    text = ""

    #The while loop will read each page
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count +=1
        content = pageObj.extractText()
        if "A.4.3" in content:
            text += content # only take section A.4.3
            return text, True
    
    return "", False

def _write_to_xls(pdd_file_names, keywords_in_pdd, contents):
    """"""
    df = pd.DataFrame({'ID': pdd_file_names, 'Exist': keywords_in_pdd,
                       'Content': contents})
    try:
        df.to_excel('unfcc_results.xlsx', sheet_name='sheet1', index=False)
        return 1
    except:
        raise ValueError('cannot save the file to xls')
        return 0
    
def main():
    all_pdd_file_names = _get_pdd_files()
    
    total_pdd_files = len(all_pdd_file_names)

    if not total_pdd_files:
        raise ValueError('No PDD Files exist in downloads/')

    
    keywords =  _read_keywords_from_config()
    keywords_in_pdd = []
    contents = []

    for file_name in all_pdd_file_names:
        file_dir = 'downloads/'+file_name
        try:
            pdfFileObj = open(file_dir,'rb')
        except:
            raise ValueError('could not find the %s file' % (file_dir))

        _content, flag = is_specified_keywords_exist(keywords, pdfFileObj)
        if flag:
            keywords_in_pdd.append('YES')
        else:
            keywords_in_pdd.append('NO')

        contents.append(_content)
        
        

    _write_to_xls(all_pdd_file_names, keywords_in_pdd, contents)


if __name__ == '__main__':
    main()