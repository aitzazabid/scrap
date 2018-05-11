from bs4 import BeautifulSoup
import requests


def total_record(breadcurm_text):
    for t in breadcurm_text :
        full_text = t.text
        full_text = full_text.split('/')[1]
        count = full_text.split(' ')[0].replace('\n','')
        count = count.replace(',','')
        count = int(count)
        total_page_count = int(count/10)
        return total_page_count


def get_phone_number(phone_number,location,name,record_list=[]):
    for obj, obj2,obj3 in zip(phone_number, location, name):
        dictionary = {'phone_number':obj.text, ' location': obj2.text.replace('\t','').replace('\n',''), 'name': obj3.text }
        record_list.append(dictionary)


def get_british_phone_number(phone_number,location,name,record_list=[]):
    dictionary = {'phone_number':phone_number, ' location': location, 'name': name }
    record_list.append(dictionary)


def get_total_records_counts(values):

    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post('http://www.britishphonebook.com/search.php', values,
                             headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')
    table_content = soup.find_all('table')

    total = table_content[0].find_all('td')
    to = total[0].get_text()

    text = to.split(' are your ')[1]
    text_ = text.split(' results:')[0]
    return int(text_)