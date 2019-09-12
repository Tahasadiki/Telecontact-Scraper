from bs4 import BeautifulSoup
import requests
import csv 
import urllib.parse
import json
import logging
logging.basicConfig(level=logging.INFO,format='%(levelname)s %(message)s')

def build_request(base_url,params,page):
    request = base_url
    request+= urllib.parse.urlencode(params)
    request+= f"&page={page}"
    return request

def get_company_details(company):
    company_details={
        "name":None,
        "description":None,
        "prestations":None,
        "address":None,
        "phone_number":None,
        "email":None,
        "website":None
    }
    #company name
    name = company.find("h2",{"itemprop":"name"}).findChild("span",{"id":"resultats_h3_span"})
    if name and name.text.strip():
        company_details["name"] = name.text.strip()     

    #company address
    address = company.find("div",{"class":"results-adress"})
    if address and address.text.strip():
        company_details["address"] = address.text.strip()                                                                                 

    #company description
    description = company.find("div",{"class":"description"})
    if description and description.text.strip():
        company_details["description"] = description.text.strip()  

    #company prestations
    prestations = company.find_all("a",{"class":"rubrique-client"})
    if prestations:
        company_details["prestations"] = ' '.join(map(lambda a:a.text.strip(),prestations)) 

    #company phone_number
    phone_number = company.find("div",{"class":"tel"})
    if phone_number and phone_number.text.strip():
        company_details["phone_number"] = phone_number.text.strip()
    
    #company website
    website = company.find("a",{"itemprop":"url"})
    if website:
        company_details["website"] = website.get("href")

    

    return company_details

def get_page_results(url,headers):
    page_results = []

    try:
        rsp = requests.get(url,headers=headers)
        if rsp.status_code!=200:
            raise(Exception("REQUEST FAILED WITH STATUS CODE {rsp.status_code}"))
        
        soup = BeautifulSoup(rsp.content,features="lxml")

        companies = soup.find_all("article",{"itemprop":"itemListElement"})
        for company in companies:
            company_details = get_company_details(company)
            page_results.append(company_details)
    except Exception as e:
        logging.error(e)

    return page_results

def get_results(configs):
    results = []
    stats = {
        "num_results":0
    }

    

    page=1
    while True:
        request = build_request(configs.URL,configs.QUERY_PARAMS,page)
        logging.info(f"[+] request:{request}")
        page_results = get_page_results(request,configs.REQUEST_HEADERS)
        if page_results:
            results.extend(page_results)
        else:
            logging.info("[+] Done!")
            break
        page+=1

    stats["num_results"] = len(results)

    return results,stats


def save_results(dict_data,json_file):
    try:
        with open(json_file, 'w') as jsonfile:
            json.dump(dict_data,jsonfile)
        return True
    except Exception as e:
        logging.error(f"[ERROR WRITING FILE] {e}")
        return False