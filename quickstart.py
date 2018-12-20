""" Quickstart script for InstaPy usage """
# imports
import os
from instapy import InstaPy
from instapy.util import smart_run



# login credentials
insta_username = ''
insta_password = ''

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=os.environ.get('INSTA_UN'),
                  password=os.environ.get('INSTA_PW'),
                  headless_browser=False)


with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                      delimit_by_numbers=True,
                                       max_followers=4590,
                                        min_followers=45,
                                        min_following=77)
    
    session.set_dont_like(["pizza", "#store"])
    

    # activity
    session.like_by_tags(["coinbase"], amount=10)

    session.follow_commenters(['cointelegraph', 'thetrendytechie', 'terrabitcoin'], amount=100, daysold=365, max_pic = 100, sleep_delay=600, interact=False)





