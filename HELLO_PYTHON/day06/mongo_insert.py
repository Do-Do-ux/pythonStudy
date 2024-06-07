import pymongo

#접속된 객체를 conn으로 받는다
conn = pymongo.MongoClient("localhost", 27017)

#test 데이터베이스가 없으면 자동으로 생성됩니다.
db = conn.python

#컬렉션은 테이블같은 개념. sql에서는 table , mongodb는 컬렉션.
#members 컬렉션 없을 경우 생성됨.
col = db.emp


people = {
    "e_id" : "4",
    "e_name" :"4",
    "gen" : "4",
    "addr" : "4"
    }
# people =[{
#     "e_id" : "4",
#     "e_name" :"4",
#     "gen" : "4",
#     "addr" : "4"
#     }]
    
# 정보 삽입 (반복해서 수행할 경우 같은 정보가 계속 인서트 됩니다.)
col.insert.one(people)
#x = col.insert.many(people)