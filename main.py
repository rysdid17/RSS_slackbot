import os
from datetime import date, datetime
from dotenv import load_dotenv
import url_list
import post_message
import get_links
import make_rss_date

load_dotenv(verbose=True)
# 토큰(env 파일로 저장)
token = os.getenv('SLACK_TOKEN')
# 보내고픈 채널명
channel = '#chattest'

url_list = url_list.urlList

link_list = []
today = make_rss_date.make_today()

if __name__ == "__main__":
    # 기술블로그에서 글 정보 가져오기
    for url in url_list:
        get_links.get_link(url, today, link_list)
    # 기술블로그에 새 글이 올라왔다면?
    if link_list:
        post_message.send_message(token, channel, '오늘 새 글이 올라왔습니다.')
        for link in link_list:
            post_message.send_message(token, channel, link)
    # 새로운 글이 없다면?
    else:
        post_message.send_message(token, channel, '오늘 새 글이 없습니다.')