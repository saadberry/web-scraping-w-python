"""Importing Modules requests and BeautifulSoup """
import requests
from bs4 import BeautifulSoup

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
        self.headline_list=[] # list that will store all the headlines retrieved from urls


    #getting keywords from user
    def get_words(self):
        """Function that gets keywords from the user"""

        num = input("How many keywords do you want to enter? ")
        for i in range(int(num)):
            print('Enter keyword ', i,': ')
            user_input = input()
            self.word_list.append(user_input)
        # print(self.word_list)
        lst = [x for x in self.headline_list for a in self.word_list if a.lower() in x.lower()]

        print(lst)

    #getting webpage    )

    def get_page(self):
        """Function that scrapes page from web"""
        # Convert url_choice to an integer
        self.url_choice = int(self.url_choice)
 

        # Making a GET request to link
        # response = requests.get(self.url)
        page = requests.get(self.url, timeout=10)
        soup = BeautifulSoup(page.content, "html.parser")
        # print(soup.prettify())
        # print(soup)
        # If choice  == 1
        if self.url_choice == 1:
            print('hehe')
            # Finding all headlines (all share an h3 tag)
            headlines = soup.findAll("h3")
            for head_lines in headlines:
                self.headline_list.append(head_lines.text)
                # print(h.text)

        # If choice == 2 ( link: https://news.ycombinator.com/ )
        if self.url_choice == 2:
            # Finding span classes
            span = soup.find_all('span', {'class': 'titleline'})

            # Finding corresponding a tags
            for sp_an in span:
                a_tags = sp_an.find_all('a')

                for a in a_tags:
                    self.headline_list.append(a.text)
                    print(a.text,"\n")
                    
                    
        #if choice == 3 (link: https://www.theguardian.com/us/technology)
        if self.url_choice == 3:
            self.headline_list=[]
            # print('hello')
            div = soup.find_all("div",{"class":"fc-item__container"})
            # print(div)
            for d_tag in div:
                a = d_tag.find('a')
                self.headline_list.append(a.text)
                print(a.text,"\n")
            # print(self.headline_list)
        
        
    
        # #if choice == 4 ( link: https://www.theguardian.com/us/technology )
        if self.url_choice == 4:
    
            li_tag = soup.find_all('li')
            print(li_tag)
            for li_x in li_tag:
                article = li_x.find_all('div',{'class':'css-10wtrbd'})
            print(article)
            for a in article:
                headline = a.find("a")
                self.headline_list.append(a.text)
                print(headline.text)

    def get_url(self):
        """Function that gets url from user"""

        #adding all urls to a list
        urls = ["https://www.reddit.com/r/programming/",
                "https://news.ycombinator.com/",
                "https://www.theguardian.com/us/technology",
                "http://www.nytimes.com/pages/technology/index.html"]

        print("Select a url from below: ")
        for i in range(len(urls)):
            print(i+1,"-",urls[i])        
        self.url_choice = input("Your choice: ")
        print("you chose: ",urls[int(self.url_choice)-1])
        # setting class variable url to the one chosen by user
        self.url = urls[int(self.url_choice)-1]
        self.get_page()


obj1 = GetHeadlines()

# obj1.get_page()
obj1.get_url()
obj1.get_words()
# print(x)
        