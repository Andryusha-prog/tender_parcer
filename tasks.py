import requests
import xmltodict

from setting import BASE_URL

def get_xml_list(soup_data):
    link_xml_list = []
    links = soup_data.find_all(class_='w-space-nowrap ml-auto registry-entry__header-top__icon')
    for link in links:
        link_html = link.find_all('a')[1].get('href')
        link_xml = link_html.replace('view.html', 'viewXml.html')
        link_xml_list.append(BASE_URL + link_xml)
    return link_xml_list

def get_data_xml(link_xml_list):
    data_add_list = {}
    for link_xml in link_xml_list:
        data = requests.get(link_xml, headers={'User-Agent': 'Custom'})
        dict_el = xmltodict.parse(data.content)
        first_key = list(dict_el.keys())[0]
        data_add_eid = dict_el[first_key]['commonInfo']['publishDTInEIS']
        # data_add_eid = dict_el[dict_el.keys()[0]]['commonInfo']['publishDTInEIS']
        data_add_list[link_xml] = data_add_eid

    return data_add_list
