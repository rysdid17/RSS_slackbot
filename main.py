import os
from dotenv import load_dotenv
import url_list
import post_message
import make_rss_date
import asyncio
import feedparser
import requests

load_dotenv(verbose=True)
# 토큰(env 파일로 저장)
token = os.getenv('SLACK_TOKEN')
# 보내고픈 채널명
channel = '#chattest'

url_list = url_list.urlList

link_list = []
today = make_rss_date.make_today()

# 오늘 업로드된 글일 경우, 링크 모음에 추가
async def get_link(url, today, list_link):
    rss_url = await loop.run_in_executor(None, requests.get, url)
    rss = rss_url.text
    parsed_rss = await loop.run_in_executor(None, feedparser.parse, rss)
    entry_rss = parsed_rss['entries']

    for entry in entry_rss:
        pubDate = str(entry['updated_parsed'][0]) + str(entry['updated_parsed'][1]) + str(entry['updated_parsed'][2])
        if today == pubDate:
            list_link.append(entry['link'])

# 메인 함수
async def main():
    # 기술블로그에서 글 정보 가져오기
    await asyncio.gather(*[asyncio.create_task(get_link(url, today, link_list)) for url in url_list])
    # 기술블로그에 새 글이 올라왔다면?
    if link_list:
        post_message.send_message(token, channel, '오늘 새 글이 올라왔습니다.')
        for link in link_list:
            post_message.send_message(token, channel, link)
    # 새로운 글이 없다면?
    else:
        post_message.send_message(token, channel, '오늘 새 글이 없습니다.')

# 비동기 처리를 위한 asyncio
loop = asyncio.get_event_loop()          # 이벤트 루프를 얻음
loop.run_until_complete(main())          # main이 끝날 때까지 기다림
loop.close()                             # 이벤트 루프를 닫음