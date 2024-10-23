from blue_alliance import getRegionalData
from fmf_scraper import scrape_fmf_news
from gundam import getGundamContent


def GetAllContent():
    return  {
        "blue_alliance": getRegionalData(),
        "fmf_news": scrape_fmf_news(),
        "gundam": getGundamContent()
    }