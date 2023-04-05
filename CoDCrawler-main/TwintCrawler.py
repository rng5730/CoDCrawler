import os
import twint
import shutil

def scrape(keyword, limit):
    # configuration
    config = twint.Config()
    config.Search = keyword
    config.Lang = "en"
    config.Limit = limit
    config.Store_json = True
    config.Output = "twint " + keyword + ".txt"
    # running search
    twint.run.Search(config)

if __name__ == "__main__":
    searchWord = '#shareyourprofits'
    scrape(searchWord, limit=1000)
    file = "twint " + searchWord + ".txt"
    original = r'C:\Users\pc-179\PycharmProjects\CoDCrawler'
    target = r'C:\Users\pc-179\PycharmProjects\CoDCrawler\data'
    shutil.move(os.path.join(original, file), os.path.join(target, file))



