import unittest
from scrapper import extract_downloadable_link, download_pdf, read_unfcc_config_file

class TestScrapper(unittest.TestCase):
    
    def test_extract_downloadable_link(self):
        url = "http://cdm.unfccc.int/Projects/Validation/DB/UKLMN824TUIYJ8PEWAPX96273EQ01L/view.html"

        downloadble_links = extract_downloadable_link(url)

        self.assertEqual(len(downloadble_links), 8)

    def test_download_pdf(self):
        url = "http://cdm.unfccc.int/Projects/Validation/DB/UKLMN824TUIYJ8PEWAPX96273EQ01L/view.html"

        status = download_pdf(url)

        self.assertEqual(status, 1)

    def test_read_unfcc_config_file(self):
        ids = read_unfcc_config_file()
        self.assertEqual(len(ids), 28)

if __name__ == '__main__':
    unittest.main()