from bs4 import BeautifulSoup
from urllib import request
import sqlite3

# 주식 가격 읽어와서 데이터베이스에 저장해보기!
# https://finance.naver.com/item/sise.naver?code={}

stock_codes = ["005930", "000660", "373220", "207940", "012450"]
stock_names = ["삼성전자", "SK하이닉스", "LG에너지솔루션", "삼성바이오로직스", "한화에어로스페이스"]

# 이 주소에서 데이터를 가져올거야~
for i in range(5):
    stock_code = stock_codes[i]
    stock_name = stock_names[i]
    url = f"https://finance.naver.com/item/sise.naver?code={stock_code}"
    # 알려준 주소에서 코드 좀 다 읽어와봐!
    response = request.urlopen(url)
    html = response.read()

    # 가져온 코드의 구조를 분석해서 보유하자!
    soup = BeautifulSoup(html, "html.parser")

    # 분석 결과 내에 내가 원하는 정보가 있다면 가져오자!
    info = soup.select_one("#_nowVal")
    price = info.text

    ''' DB 연습 미션!
    0. database_sample.db와 파이썬 파일을 연결하기
    1. 주식 이름과 가격을 저장할 수 있는 stock 테이블 생성하기
    2. 주식 이름과 가격을 실제로 삽입하기
    3. 삽입한 내용을 확정하고 연결 해제하기
    4. 잘 되었는지 확인하기(데이터베이스 파일 열어보면 됨)
    5. 선택사항 : 어느정도 할 줄 알면 다른 종목도 여러개 넣어보기!
    '''

    conn = sqlite3.connect("database_sample.db")
    print(conn)

    cur = conn.cursor()

    #cur.execute("CREATE TABLE stock_price(code TEXT, name VARCHAR(30), price INT)")
    cur.execute("INSERT INTO stock_price(code, name, price) VALUES(?, ?, ?)", (stock_code, stock_name, price))
    #cur.execute("DELETE FROM stock_price")
    #cur.execute("DROP TABLE stock_price")
    print(f"주식 코드 : {stock_code} \n주식 이름 : {stock_name} \n주식 가격 : {price}")

    conn.commit()
    conn.close()
