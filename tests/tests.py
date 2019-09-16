from telecontact_scraper.helpers.helpers import get_results,save_results
from telecontact_scraper.configs import configs
import unittest

class TestTelecontactScraper(unittest.TestCase):

    def setUp(self):
        self.results, self.stats= get_results(configs)

    def assess_results(self):
        results = self.results
        self.assertTrue(results)
        
if __name__ == '__main__':
    unittest.main()
