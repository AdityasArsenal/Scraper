# Scraper

## how to run :

    step 1 install the requirements.txt
    step 2 cammands : 
            (for windows)
            1 cd y_spider
            2 scrapy crawl bbb

creates 2 files in the same directory
1 product_data.csv (visual purposes)
2 product_data.json (data analysis)

(to run the data analysis 👇🏻)
    step 3 cammands:
            (for windows)
            1 cd ../
            2 python data_analysis.py

creates 2 graphs for understanding of data 
and output most and least priced product and it's brand on the platform.

                                         User-Agent-Settings
-------------------------------------------------------------------------------------------------------------
    (to add user-agent for each query👇🏻)
        step 4 go to setting.py
        step 5 uncomment lines = [25,26,27]

    this will enable the middleware where the ScrapeOpsFakeUserAgentMiddleware class fitches fake user-agents through api call.
    
                                OR

    you can also try your costum user-agents
    (to do that👇🏻)
        step 4 go to bbb.py
        step 5 uncomment lines[9:14]
        step 6 uncomment line 72

    this will get the user-agents from the list and add it to the request.
-------------------------------------------------------------------------------------------------------------
    


