# 프젝 참여자들 주목!

## Guide Line
1. 크롤링 전체적인 틀은 완성됬는데 변경해야할 사항들이 많음
2. 크롤링 사용은 코드 2개로 구분되어있음
- 1. settting(), run()
- 2. setting -> 세팅(csv파일생성 및 스텟종류 세팅) run -> 데이터 수집(경기 Performance Stats수집)
3. Dash Library를 통해 DashBoard 구성할 예정 (Flask질문한 이유도 여기에 있음)
4. 가장 중요한 회귀분석을 해야하는데 Elastic Net을 통해 정규화는 진행할 예정 
5. But... 저번 Linear Regression(선형 회귀)이 아닌 Poly Regression(다차항 회귀)를 잘 못 말함(x축은 나이이고 y축은 회의를 통해 결정)
6. 수식은 완성되면 업데이트
7. test파일은 어디까지나 html, css, js연습용(본인이 프론트로 꾸미고 싶다하면 진행) 선택이지만 개인적으로 해줬으면 좋겠음
8. 실기 끝나고는 굴릴예정 할당량 못 채우면 못 나감(그 때까지 고생 좀 하자!)


## 수정사항
<h3>scrapping.py 전면 수정</h3>
    <p>scrapping.py 설명</p>
    <p>Crawling → Scrapped로 클래스명 변경 Scrapped를 호출해야 사용가능</p>
    <p>attack, pitcher, defense 세 가지의 함수가 존재</p>
    <p>함수들은 각각 해당되는 옛날 전성기 선수들의 스텟을 가져옴</p>
<h3>머신러닝 재 선택</h3>
    <p>다항회귀를 선택 그 전과 동일하게 Elastic Net을 사용할 예정임</p>
    <p>But 데이터 분석하다보면 RNN도 해볼 만 할지도?</p>
<h3>마지막 하고 싶은말</h3>
    <p>프로젝트의 가장 큰 목표는 재미인거지 간절하게 뭐 하고싶으면 이현서한테 찾아오도록 일은 만들어서 줄 수 있음</p>

## 설치방법
<p>pip install pipenv → 가상환경 구축</p>
<p>pipenv install → 필수요소들 설치</p>
<p>pipenv shell → 실행</p>


