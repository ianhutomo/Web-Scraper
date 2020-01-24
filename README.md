# Webpage Scraper

This code is part of the assignment on Text Information Systems course at the University of Illinois at Urbana-Champaign

We will start by building a dataset consisting of the homepages of faculty memebers from different universities' Engineering and Science departments.
To achieve this, you first need to identify the faculty directory listing page where all the faculty members of your chosen department are listed and get the urls for the homepages of all faculty members.
You then need to scrape all the text information, such as the faculty bio, from the faculty homepage.

Specifically, you need to perform the following tasks:

1. Select an Engineering and/or Science department faculty listing page of a university 

2. Scrape the faculty listing page and all the faculty homepages using Python. Finally, you should generate two output .txt files called **bios.txt** and **bio_urls.txt**. 'bio_urls.txt' should contain the urls of all the faculty homepages and have one url per line. 'bios.txt' should contain the text scraped from all the urls in 'bio_urls.txt', and again have one document per line. The two files must have the same order, that is, the first line in 'bios.txt' should correspond to the text extracted from the url in the first line of 'bio_urls.txt'. 

3. Place all your code in one folder and name it **scraper_code**. Add the folder alongwith the two output .txt files here. 

A sample script for scraping UIUC CS department faculty homepages has been provided to you under the sample folder in the form a jupyter notebook. You can download it and run it on your machine using the [jupyter notebook command](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html). We also provide the two output files generated from the script under the same folder. This should help you get started with developing scrapers for other universities' faculty homepages as well. 

Additionally, you might find the following resources useful:

Python Libraries:
- [Beautiful Soup] (https://www.crummy.com/software/BeautifulSoup/bs4/doc/): Useful for parsing HTML extracted from websites.
- [Requests](http://docs.python-requests.org/en/master/): Useful for downloading content from urls
- [Selenium](https://seleniumhq.github.io/selenium/docs/api/py/): Useful when Requests is unable to download content rendered by Javascript
    
Some Tutorials:
- https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
- http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Scraping_a_Webpage_Rendered_by_Javascript_Using_Python.php. 
   
Finally, the browser developer tools are highly useful to inspect and identify the HTML elements where the required information resides in the webpage. 
