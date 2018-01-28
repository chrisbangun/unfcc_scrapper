import unittest
from pdd_reader import _get_pdd_files, _read_keywords_from_config, _write_to_xls, main

class TestPddReadery(unittest.TestCase):
    
    def test_read_keywords_from_config(self):
        keywords = _read_keywords_from_config()
        self.assertEqual(len(keywords), 3)

    def test_write_to_xls(self):
        pdd_files = ['pdd_file_name_test']
        keywords_in_pdd = ['no*transfer*technology']
        contents = ['this is a content. this is a content-content']

        result = _write_to_xls(pdd_files, keywords_in_pdd, contents)
        self.assertEqual(result, 1) 

if __name__ == '__main__':
    unittest.main()