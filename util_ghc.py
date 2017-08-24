import requests
from bs4 import BeautifulSoup

class get_details:
    def __init__(self,person_url):
        self.person_url = person_url
        self.sourceCode = requests.get('https://github.com/'+person_url)
        self.plain = self.sourceCode.text
        self.soup = BeautifulSoup(self.plain,"html.parser")
        self.soup.encode("utf-8")
    def get_desc(self):
        desc_person_raw = self.soup.find('div', {'class': 'p-note user-profile-bio'})
        desc_person = desc_person_raw.string
        return desc_person
    def get_featured_repo_names(self):
        repo_list = []
        for repo in self.soup.findAll('span',{'class': 'repo js-repo'}):
            repo_list.append(repo.string)
        return repo_list
    def get_location(self):
        person_location_raw = self.soup.find('span', {'class': 'p-label'})
        person_location = person_location_raw.string
        return person_location
    def get_counters_list(self):
        person_count_list = []
        for person_count_list_raw in self.soup.findAll('span', {'class': 'Counter'}):
            person_count_list.append(person_count_list_raw.string)
        return person_count_list
 
    def get_report(self):
        star_url = '/'+self.person_url+'?tab=stars'
        stars_raw = self.soup.find('a',{'href': star_url})
        report = "The person has "+stars_raw.string+" stars"
        return report
