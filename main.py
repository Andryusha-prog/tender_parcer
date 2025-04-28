import requests
from bs4 import BeautifulSoup

from setting import BASE_URL, RECORDS_PER_PAGE, COUNT_PAGES
from tasks import get_xml_list, get_data_xml


if __name__ == "__main__":

    for i in range(1, COUNT_PAGES + 1):
        url = f'{BASE_URL}/epz/order/extendedsearch/results.html?fz44=on&recordsPerPage=_{RECORDS_PER_PAGE}&pageNumber={i}'
        # #
        response = requests.get(url, headers={'User-Agent': 'Custom'})
        # #
        soup = BeautifulSoup(response.content, 'html.parser')
    #
        xml_list = get_xml_list(soup)
    #
        print(xml_list)

        data_res = get_data_xml(xml_list)

        for key, value in data_res.items():
            print(f'{key} - {value}')
