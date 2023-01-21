#import libraries
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen 

#import the URL
url='https://wuzzuf.net/search/jobs/?q=illustrator&a=navbl'

client=urlopen(url)

html=client.read()
# print(html)

client.close()
soup=bs(html,"html.parser")
# print(soup)

containers=soup.find_all("div",{"class":"css-1gatmva e1v1l3u10"}) # contain every div in the page
# print(len(conteners))     #numbers of divs = number of jobs

bs.prettify(containers[0])  #print the first div
# print(conteners[0].div.h2.text) #it is a way but not recommended

jtitle=containers[0].findAll("h2",{"class":"css-m604qf"})
# print(jtitle[0].text)
cname=containers[0].findAll("a",{"class":"css-17s97q8"})
# print(cname[0].text)
jtype=containers[0].findAll("div",{"class":"css-1lh32fc"})
# print(jtype[0].text)

f=open("F:\Git Hup\Projects Machine learning\Web Scrapping\WebScrapping2.csv","w")
header="job_title, company_name, job_type\n" # first row in the cv file
f.write(header)

for container in containers :
    jtitle=container.findAll("h2",{"class":"css-m604qf"})
    job_title=jtitle[0].text.strip()
    
    cname=container.findAll("a",{"class":"css-17s97q8"})
    company_name=cname[0].text.strip()
    
    jtype=container.findAll("div",{"class":"css-1lh32fc"})
    job_type=jtype[0].text.strip()

    f.write(job_title + ", " + company_name + ", " + job_type + "\n")
f.close()
