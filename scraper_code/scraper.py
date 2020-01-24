from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import re 
import urllib

#create a webdriver object and set options for headless browsing
options = Options()
options.headless = True

#running chromedriver on Windows
browser = webdriver.Chrome('./chromedriver.exe',options=options)

#running chromedriver on Linux
#browser = webdriver.Chrome('./chromedriver',options=options)

#uses webdriver object to execute javascript code and get dynamically loaded webcontent
def get_js_soup(url,browser):
    browser.get(url)
    res_html = browser.execute_script('return document.body.innerHTML')
    soup = BeautifulSoup(res_html,'html.parser') #beautiful soup object to be used for parsing html content
    return soup

#tidies extracted text 
def process_bio(bio):
    bio = bio.encode('ascii',errors='ignore').decode('utf-8')       #removes non-ascii characters
    bio = re.sub('\s+',' ',bio)       #repalces repeated whitespace characters with single space
    return bio

''' More tidying
Sometimes the text extracted HTML webpage may contain javascript code and some style elements. 
This function removes script and style tags from HTML so that extracted text does not contain them.
'''
def remove_script(soup):
    for script in soup(["script", "style"]):
        script.decompose()
    return soup

#Checks if bio_url is a valid faculty homepage
def is_valid_homepage(bio_url,dir_url):
    try:
        #sometimes the homepage url points to the faculty profile page
        #which should be treated differently from an actual homepage
        ret_url = urllib.request.urlopen(bio_url).geturl() 
    except:
        return False       #unable to access bio_url
    urls = [re.sub('((https?://)|(www.))','',url) for url in [ret_url,dir_url]] #removes url scheme (https,http) or www 
    return not(urls[0]== urls[1])

#extracts all Faculty Profile page urls from the Directory Listing Page
def scrape_dir_page(dir_url,browser):
    print ('-'*20,'Scraping directory page','-'*20)
    faculty_links = []
    faculty_base_url = 'https://www.engineering.unsw.edu.au/computer-science-engineering/'
    #execute js on webpage to load faculty listings on webpage and get ready to parse the loaded HTML 
    soup = get_js_soup(dir_url,browser)     

    #scraping odd faculty list
    for link_holder in soup.find_all('td',style='background-color:#f1f1f1; vertical-align:top;'):
        rel_link = link_holder.find('a')['ng-href'] #get url
        #url returned is relative, so we need to add base url
        #pop first 3 chars of '../'
        rel_link = rel_link[3:]
        faculty_links.append(faculty_base_url+rel_link) 

    #scraping even faculty list
    for link_holder in soup.find_all('td',style='vertical-align:top;'):
        rel_link = link_holder.find('a')['ng-href'] #get url
        #pop first 3 chars of '../'
        rel_link = rel_link[3:]
        #url returned is relative, so we need to add base url
        faculty_links.append(faculty_base_url+rel_link) 
    print ('-'*20,'Found {} faculty profile urls'.format(len(faculty_links)),'-'*20)
    return faculty_links

dir_url = 'https://www.engineering.unsw.edu.au/computer-science-engineering/academic-profiles/cse-academic-profiles' #url of directory listings of CS faculty
faculty_links = scrape_dir_page(dir_url,browser)

def scrape_faculty_page(fac_url,browser):

    soup = get_js_soup(fac_url,browser)
    
    #In UNSW Faculty page there are no information on external homepage for each faculty
    bio_url = fac_url #treat faculty profile page as homepage
    bio = ''
        
    #we're only interested in some parts of the profile page namely the address
    #and information listed under the Overview, Research, Publication and Awards tab
    bio = soup.find('div',class_='field-items').get_text(separator=' ')+': '
    #for tab in soup.find_all('div',class_='tab-pane'):
    #bio += tab.get_text(separator=' ')+'. '
    bio = process_bio(bio) 
    bio = bio[11:] #pop ' Biography:' string in the beginning
    #print(bio)
    return bio_url,bio

#Scrape all faculty homepages using profile page urls
bio_urls, bios = [],[]
tot_urls = len(faculty_links)
for i,link in enumerate(faculty_links):
    print ('-'*20,'Scraping faculty url {}/{}'.format(i+1,tot_urls),'-'*20)
    bio_url,bio = scrape_faculty_page(link,browser)
    bio_urls.append(bio_url)
    bios.append(bio)

def write_lst(lst,file_):
    with open(file_,'w') as f:
        for l in lst:
            f.write(l)
            f.write('\n')

bio_urls_file = 'bio_urls.txt'
bios_file = 'bios.txt'
write_lst(bio_urls,bio_urls_file)
write_lst(bios,bios_file)
