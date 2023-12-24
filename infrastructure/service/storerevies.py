from google_play_scraper import Sort, reviews, reviews_all
from json import loads

class storereviews:
  ''' This class give to application 100 reviews to each request'''
  def __init__(self) -> None:
    pass 
  
  def getReviews(self, appId):
    
    self.result, self.continuation_token = reviews(
        appId,
        lang='en', # defaults to 'en'
        country='br', # defaults to 'us'
        sort=Sort.NEWEST, # defaults to Sort.NEWEST
        count=100, # defaults to 100
    )

    return self.result

  def getAllReviews(self, appId):
    
    self.result = reviews_all(
    appId,
    sleep_milliseconds=0, # defaults to 0
    lang='br', # defaults to 'en'
    country='br', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    filter_score_with=None # defaults to None(means all score)
    )

    return self.result
