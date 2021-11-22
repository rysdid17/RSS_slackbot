import post_message
import os
from datetime import datetime
from dotenv import load_dotenv
import get_links

load_dotenv(verbose=True)
token = os.getenv('SLACK_TOKEN')

url_list = ['https://techblog.woowahan.com/feed/',
            'https://tech.kakao.com/feed/']

link_list = []
today = datetime.now().strftime('%Y%m%d')
channel = '#chattest'

if __name__ == "__main__":
    for url in url_list:
        get_links.get_link(url, today, link_list)
    if link_list:
        post_message.send_message(token, channel, '오늘 새 글이 올라왔습니다.')
        for link in link_list:
            post_message.send_message(token, channel, link)
    else:
        post_message.send_message(token, channel, '오늘 새 글이 없습니다.')