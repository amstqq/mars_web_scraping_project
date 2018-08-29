def scrape():

    from splinter import Browser
    from bs4 import BeautifulSoup

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    ## NASA Mars News
    # Target url
    url1 = 'https://mars.nasa.gov/news/'
    # Visit url
    browser.visit(url1)
    # Get html of target website
    html1 = browser.html
    soup1 = BeautifulSoup(html1, 'html.parser')

    # Scrape news title and text
    news_title = soup1.find('div', class_="content_title").text
    news_p = soup1.find('div', class_="article_teaser_body").text

    ## JPL Mars Space Images - Featured Image
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)
    html2 = browser.html
    soup2 = BeautifulSoup(html2, "html.parser")

    # Scrape image url
    featured_image_url = 'https://www.jpl.nasa.gov' + soup2.find('a', class_="fancybox").get("data-fancybox-href")


    ## Mars Weather
    url3 = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url3)
    html3 = browser.html
    soup3 = BeautifulSoup(html3, "html.parser")

    mars_weather = soup3.find('p', class_='tweet-text').text


    ## Mars Facts

    import pandas as pd
    url4 = 'https://space-facts.com/mars/'
    tables = pd.read_html(url4)
    # Convert pandas dataframe to html text
    mars_facts = tables[0].to_html(header=False, index=False)


    ## Mars Hemispheres

    url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url5)
    html5 = browser.html
    soup5 = BeautifulSoup(html5, "html.parser")

    # Create a list of name and image url of each hemisphere
    hemis_list = []
    # Obtain all html elements related to available hemispheres titles
    hem_titles = soup5.find_all('h3')

    for i in range(4):
        # Obtain individual name of hemisphere
        hem_title = hem_titles[i].text

        # Click on part of website that directs to url of full image of hemisphere
        browser.click_link_by_partial_text(hem_title)
        img_html = browser.html
        img_soup = BeautifulSoup(img_html, "html.parser")
        # Obtain full hemisphere url
        img_url = "https://astrogeology.usgs.gov" + img_soup.find("img", class_="wide-image").get("src")

        # Append title and url into dictionary
        hemis_list.append({"title":hem_title,"img_url":img_url})

        # Return to last page
        browser.click_link_by_partial_text("Back")

    return {
    "news_title":news_title,
    "news_p":news_p,
    "featured_image_url":featured_image_url,
    "mars_weather":mars_weather,
    "mars_facts":mars_facts,
    "hemis_list":hemis_list
    }
