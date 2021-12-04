import os
from instaloader import Instaloader
class Config:
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    USER = os.environ.get("INSTAGRAM_USERNAME", "")
    OWNER = os.environ.get("OWNER_ID", "")
    INSTA_SESSIONFILE_ID = os.environ.get("INSTA_SESSIONFILE_ID", None)
    S = "0"
    STATUS = set(int(x) for x in (S).split())
    L=Instaloader()
    HELP="""
<b>You Need Help? Click <a href='https://t.me/adhavabiriyanikittiyaalo/5'>Here</a></b>

"""
    HOME_TEXT = """
<b>Hello, [{}](tg://user?id={})

This is a bot of [{}](www.instagram.com/{}) to manage his Instagram account. 
I can only work for my master [{}](tg://user?id={}). You don't need to waste your time by being here! You get nothing.
So, ThankYou.</b>
"""
    HOME_TEXT_OWNER = """
<b>Do whatever! I'm Yours..[{}](tg://user?id={})</b>
"""

