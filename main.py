## threads use karne hain search karne mai
"""Importing Modules requests and BeautifulSoup """
import requests
from bs4 import BeautifulSoup
import re
from threading import Thread

#Python script to take keywords as input and return
#relavent headlines accordingly
class GetHeadlines:
    """Class GetHeadlines """
    #defining constructor w/ one parameter 'link'
    #this will be the link of the website to get headlines
    def __init__(self):
        self.url = ""
        self.word_list = [] # lists that will store the keywords
        self.url_choice = 0 # int value representing the url user's choice (1-4)
        self.url_dict={} # dict that will store all the headlines retrieved from urls


    #getting keywords from user
    def get_words(self):
        """Function that gets keywords from the user"""

        num = input("How many keywords do you want to enter? ")
        for i in range(int(num)):
            print('Enter keyword ', i,': ')
            user_input = input()
            self.word_list.append(user_input)
            
        #calling get_page() function to retrieve data
        self.get_page()

        # print(self.word_list)
        # print(self.url_dict)
        # result_dict = {key: [x for x in self.url_dict[key] for a in self.word_list if a.lower() in x.lower()] for key in self.url_dict}

        for key, value in self.url_dict.items():
                    print("{}:\n{}".format(key, "\n".join(value)))
        # print(result_dict)

    #getting webpage    )

    def get_page(self):
        """Function that scrapes page from web"""
        
        #adding all urls to a list
        urls = ["https://www.reddit.com/r/programming/",
                "https://news.ycombinator.com/",
                "https://www.theguardian.com/us/technology",
                "http://www.nytimes.com/pages/technology/index.html"]
        
        #creating a dictionary 
        self.url_dict = {url: [] for url in urls}
        
        
        for url in urls:
            
            #if url = reddit
            if re.search(r"\breddit\b", url):
                
                # Loop over each keyword and scrape data for it
                for word in self.word_list:
                    # Build the search URL with the keyword as a query parameter
                    # search_url = f"{url}search?q={word}"
                    search_url = url

                    # Send a GET request to the search URL
                    page = requests.get(search_url,timeout=500)

                    soup = BeautifulSoup(page.content, "html.parser")
                    
                    # Finding all headlines (all share an h3 tag)
                    headlines = soup.findAll("h3")
                    # print(headlines)
                    for head_lines in headlines:
                        print(head_lines.text)
                        
                        text = head_lines.get_text().lower()
                        for word in self.word_list:
                            
                            if re.search(word, text):
                                # print('success')
                                self.url_dict[url].append(text)
                        self.url_dict[url].append(head_lines.text) 
                
                
            # #if url = ycombinator
            elif re.search(r"\bycombinator\b",url):
                 # Loop over each keyword and scrape data for it
                for word in self.word_list:
                    # Build the search URL with the keyword as a query parameter
                    # search_url = f"{url}search?q={word}"
                    # print(url)
                    # Send a GET request to the search URL
                    page = requests.get(url)
               
                    soup = BeautifulSoup(page.content, "html.parser")                
                    span = soup.find_all('span', {'class': 'titleline'})

                    # Finding corresponding a tags
                    for sp_an in span:
                        a_tags = sp_an.find_all('a')

                        for a in a_tags:
                                    text = a.get_text().lower()
                                    for word in self.word_list:
                                        
                                        if re.search(word, text):
                                            self.url_dict[url].append(text)
                                            
                            
                    # print(self.url_dict)
                    
            # #if url = guardian
            elif re.search(r"\btheguardian\b",url):
                # Loop over each keyword and scrape data for it
                for word in self.word_list:
                    # Build the search URL with the keyword as a query parameter
                    search_url = url

                    # Send a GET request to the search URL
                    page = requests.get(search_url,timeout=50)
               
                    soup = BeautifulSoup(page.content, "html.parser")         
                    div = soup.find_all("div",{"class":"fc-item__container"})
                    # print(div)
                    for d_tag in div:
                        a = d_tag.find('a')
                        text = a.get_text().lower()
                        # print(text)
                        for word in self.word_list:
                            if re.search(word,text):
                                self.url_dict[url].append(a.text)
                        
                        # print(a.text,"\n")
                    # print(self.headline_list)
                    # print(self.url_dict)

            # # #if url == nytimes
            elif re.search(r"\bnytimes\b",url):
                search_url=url
                page = requests.get(search_url)
                soup = BeautifulSoup(page.content, "html.parser")   

                # Finding all article sections on the page
                article_sections = soup.find_all('div', {'class': 'css-10wtrbd'})

                # Looping through each article section
                for section in article_sections:
                    
                    # Find the headline element for the article
                    headline_element = section.find('a')
                    
                    # Get the text of the headline
                    headline_text = headline_element.get_text().lower()
                    
                    # Check if the headline contains any of the user's keywords
                    for keyword in self.word_list:
                        if keyword in headline_text:
                            # If it does, add the headline to the url_dict
                            self.url_dict[url].append(headline_text)
                # print(self.url_dict[url])

       
                # for key, value in self.url_dict.items():
                #     print("{}:\n{}".format(key, "\n".join(value)))



                        
                        
                
        
        
    


    # def get_url(self):
    #     """Function that gets url from user"""



    #     # print("Select a url from below: ")
    #     # for i in range(len(urls)):
    #     #     print(i+1,"-",urls[i])        
    #     # self.url_choice = input("Your choice: ")
    #     # print("you chose: ",urls[int(self.url_choice)-1])
    #     # # setting class variable url to the one chosen by user
    #     # self.url = urls[int(self.url_choice)-1]
    #     self.get_page()


obj1 = GetHeadlines()

#function to get keywords from user
obj1.get_words()

#calling get_page() function using threads
t1 = Thread(target=obj1.get_page)
t2 = Thread(target=obj1.get_page)
t3 = Thread(target=obj1.get_page)
t4 = Thread(target=obj1.get_page)

t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
#function to scrape data according to keywords
# obj1.get_page()

# print(x)
        