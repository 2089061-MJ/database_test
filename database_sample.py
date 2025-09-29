# MySQL과 유사한데 파이썬에 기본으로 내장된 표준 라이브러리!
import sqlite3

# 전제 : 이 파이썬 파일과 같은 폴더 내에 *.db 파일이 하나 존재한다.

# 이 파이썬 파일과 데이터베이스 파일을 연결하여 작업 가능하게 만든다.
conn = sqlite3.connect("database_sample.db")
print(conn)

# 연결이 되었다면, 연결된 파일에 SQL 구문을 전달해서 실행할 객체를 생성해야함!
cur = conn.cursor()

# 테이블 생성 명령 실행
#cur.execute("CREATE TABLE customer(name TEXT, age INT)")
# 위에서 만든 테이블에 데이터 두 개 삽입 후, 한 개 삭제해보기!
#cur.execute("INSERT INTO customer(name, age) values('홍길동', '25')")
#cur.execute("INSERT INTO customer(name, age) values('차둘이', '28')")

cur.execute("DELETE FROM customer WHERE name='차둘이'")

# 명령을 다 실행했으니, 확정시키고 연결 해제하자!
conn.commit()   # 작업 확정
conn.close()    # 연결 해제