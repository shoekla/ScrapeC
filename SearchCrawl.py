import time
import urllib2
import re
import bleach
import requests
from bs4 import BeautifulSoup
from urllib2 import urlopen
linkText = open("SearchLinks.txt","w")
socialFile=open("Social-Media-Links.txt","w")
def is_in_arr(lis,s):
	result=False
	for item in lis:
		if item==s:
			result=True
	return result

def filter1(page):
	res=True
	bad=["microsoft","republicservice","blogger.com",".pdf", "facebook","twitter","pinterest","linkedin","fb","jpeg","image:","pdf.","instagram","gram","tweet"]
	for item in pages:
		for bad_link in bad:
			if bad_link in item:
				res= False
	return res

def getGoodLink(url):
	k = url.rfind("/")
	return url[:k+1]

def crawl(url,pages):
	try:
		arr=[]
		source_code=requests.get(url)
		plain_text=source_code.text
		soup=BeautifulSoup(plain_text)
		for link in soup.findAll('a'):

			href=link.get('href')
			href_test=str(href)
			#if href_test[0]!='/' and href_test[0]!='j' and href_test!='none' and href_test[0]!='#':
			if is_in_arr(pages,str(href))==False:
				if "microsoft" not in href_test and "facebook" not in href_test and "twitter" not in href_test and "google" not in href_test:
					if href_test.startswith("http"):
						pages.append(str(href))
					else:
						lin=getGoodLink(url)
						pages.append(lin+str(href))
                
    
	except:
		print "Error at: "+str(url)



def crawlSocialMedia(url):
	userIn=url.strip()
	userIn=userIn.replace(" ","%20")
	link="https://www.facebook.com/search/str/"+str(userIn)+"/keywords_top"
	linka="https://twitter.com/search?q="+str(userIn)+"&src=typd&vertical=default&f=users"
	pages=[]
	crawl(link,pages)
	crawl(linka,pages)
	new=deleteDuplicates(pages)
	for item in new:
		if "lang" not in str(item) and "account" not in str(item) and "login" not in str(item):
			if len(getGoodLink(item))>3:
				socialFile.write(item)
				socialFile.write("\n")
	
def scrapeSearch(url):
	
	try:
		regex='<p>(.+?)</p>'
		
		pattern = re.compile(regex);
		htmlfile=urllib2.urlopen(str(url))
		htmltext=htmlfile.read()
		title=re.findall(pattern,htmltext)
		if len(title)>1:
				
			file2.write("Source Page: "+str(url)+"")
			file2.write("Title: "+getTitle(url))
			file2.write("\n"+str(title))

				
					

	except:
		print "Error Excepted"
def deleteDuplicates(lis):
	newLis=[]
	for item in lis:
		if item not in newLis:
			newLis.append(item)
	return newLis
def getTitle(url):

	regex=['<title>(.+?)</title>']
	pattern = re.compile(regex);
	htmlfile=urllib2.urlopen(url)
	htmltext=htmlfile.read()
	title=re.findall(pattern,htmltext)
	return title

def crawlSearchQuery(userIn):
	
	userIn=userIn.strip()
	userIn=userIn.replace(" ","%20")


	links=[]
	finds=[]
	item="http://www.bing.com/search?q="+userIn+"&go=Submit&qs=n&form=QBLH&pq="+userIn+"&sc=8-4&sp=-1&sk=&cvid=21fdaffc3c72488f96e76d5d8378d29d"

	crawl(item,links)

	for link in links:
		crawl(link, finds)
	new=deleteDuplicates(finds)
	for link in new:
		linkText.write(link)
		linkText.write("\n")


def crawlLink(ina):
	links=[]
	finds=[]
	item=ina

	crawl(item,links)

	for link in links:
		crawl(link, finds)
	new=deleteDuplicates(finds)
	for link in new:
		linkText.write(link)
		linkText.write("\n")
def crawlLinkScoial(url):
	try:
		pages=[]
		arr=[]
		source_code=requests.get(url)
		plain_text=source_code.text
		soup=BeautifulSoup(plain_text)
		for link in soup.findAll('a'):

			href=link.get('href')
			href_test=str(href)
			#if href_test[0]!='/' and href_test[0]!='j' and href_test!='none' and href_test[0]!='#':
			if is_in_arr(pages,str(href))==False:
				if "facebook" in href_test or "twitter" in href_test or "google" in href_test:
				
					lin=getGoodLink(url)
					pages.append(lin+str(href))
		newArr=deleteDuplicates(pages)
		for page in newArr:
			socialFile.write(page)
			socialFile.write("\n")
                
    
	except:
		print "Error at: "+str(url)
def link(url):
	crawlLink(url)
	crawlLinkScoial(url)


crawlLinkScoial("http://lamarwebtsa.org/")


