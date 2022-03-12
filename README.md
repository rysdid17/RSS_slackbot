# 기술블로그 포스팅 알리미 Ver.2

## 기능
매일 다양한 기술블로그들에서 글이 올라왔는지 확인한 뒤, 슬랙으로 포스팅 여부를 알려준다.

## 각 파일의 역할
1. **post_messages.py** : 토큰을 받아 지정한 채널에 지정한 메세지를 보낸다.
2. **get_links.py** : 입력값인 url에서 글들의 포스팅 날짜를 확인한 뒤, 날짜가 오늘인 경우 출력값인 리스트의 원소로 추가한다.
3. **main.py** : get_links에게 날짜를 입력해서 포스팅 정보를 출력받는다. 그 후 포스팅 여부에 따라 슬랙에 메세지를 보낸다.
4. **requirements.txt** : github actions을 사용하여 실행할 수 있도록 적어둔 필수 라이브러리
5. **.gitignore** : env 파일을 숨기기 위함.
6. **url_list.py** : url 목록을 main에서 따로 파일로 빼놓았다. url 추가로 인해 main이 길어지는 것을 대비하기 위함.

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

+) 2022.3.12 수정

   - RSS의 pubDate와 설정한 today의 형식이 맞지 않는 오류를 확인.
   - datetime의 strftime()의 형식에서 '03'과 같이 한 자릿수 숫자 앞에 0이 붙는 것이 이유였음.
   - 형식에 맞추는 함수를 추가함으로써 
