# 기술블로그 포스팅 알리미 Ver.2

## 기능
매일 다양한 기술블로그들에서 글이 올라왔는지 확인한 뒤, 슬랙으로 포스팅 여부를 알려준다.

## 각 파일의 역할
1. **post_messages.py** : 토큰을 받아 지정한 채널에 지정한 메세지를 보낸다.
2. **get_links.py** : 입력값인 url에서 글들의 포스팅 날짜를 확인한 뒤, 날짜가 오늘인 경우 출력값인 리스트의 원소로 추가한다.
3. **main.py** : get_links에게 날짜를 입력해서 포스팅 정보를 출력받는다. 그 후 포스팅 여부에 따라 슬랙에 메세지를 보낸다.
4. **requirements.txt** : github actions을 사용하여 실행할 수 있도록 적어둔 필수 라이브러리
5. **.gitignore** : env 파일을 숨기기 위함.

## [Ver.1](https://github.com/rysdid17/techblog_slack) 과 다른 점
* [Ver.1](https://github.com/rysdid17/techblog_slack)에서 포스팅 날짜를 확인하기 위해서 모든 사이트의 html을 직접 확인하던 문제점을 **RSS** 라는 정해진 규격을 이용하여 해결

## 사용언어
* Python

## 사용 라이브러리
* feedparser
* requests
* dotenv

## 기간
* 2021.11 ~ 2021.12
