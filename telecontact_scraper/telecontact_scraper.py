"""
Usage:
    telecontact_scraper.py mine <string> <ou> [--file_path=<destination_file>]

Options:
    <string>    Qui,quoi? (raison sociale ou activité)
    <ou>        Où? (Casablanca)   
    --file_path file to save results to 
"""

from docopt import docopt
import logging
logging.basicConfig(level=logging.INFO,format='%(levelname)s %(message)s')

#import configs
from configs import configs
#import helpers
from helpers.helpers import get_results,save_results


def Main():
    args = docopt(__doc__,version="Telecontact Scraper 0.1")
    if args["mine"]:
        configs.QUERY_PARAMS["string"] = args["<string>"]
        configs.QUERY_PARAMS["ou"] = args["<ou>"]
        results,stats = get_results(configs)
        logging.info(stats)
        if args["--file_path"]:
            if results:
                save_results(results,args["--file_path"])
        else:
            print(results)


if __name__=="__main__":
    Main()