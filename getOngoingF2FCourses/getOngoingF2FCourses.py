# 수강중인(했던) 대면 강의 목록 크롤러
import sys
import requests

# 실행 방법: python3 getOngoingF2FCourses.py 학번 비번
# 예:       python3 getOngoingF2FCourses.py 19930121 passw0r6

loginURL = 'https://daejin.ac.kr/subLogin/daejin/login.do'  # 로그인 엔드포인트
timeTableURL = 'https://dreams2.daejin.ac.kr/sugang/center/BlsnTotalTimeTableLst.jsp'  # 포털대진 시간표 조회 페이지 URL
JSESSIONID = ''  # 접속자 세션 유지용 쿠키
SSOCookie = ''  # 로그인 성공할 경우 받아온 SSO 로그인 세션 쿠키 보관
dreamsCookie = {}  # 포털대진 전용 세션 쿠키 보관
creds = {'userId': sys.argv[0], 'userPwd': sys.argv[1]}  # 명령행 인자에서 로그인 정보 가져오기
# defaultHeaders = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.28 Safari/537.36'}

s = requests.Session()  # 쿠키 유지를 위해 세션 객체 생성
# s.headers = defaultHeaders
JSESSIONID = s.get(loginURL)  # 로그인 전 JSESSIONID 쿠키 취득
print(JSESSIONID)

# SSOCookie = post(loginURL, data=creds)
# print(SSOCookie.headers)
