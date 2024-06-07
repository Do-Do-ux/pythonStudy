import pymongo

#접속된 객체를 conn으로 받는다
myclient = pymongo.MongoClient("localhost", 27017)

#test 데이터베이스가 없으면 자동으로 생성됩니다.
mydb = myclient["python"]

#컬렉션은 테이블같은 개념. sql에서는 table , mongodb는 컬렉션.
#members 컬렉션 없을 경우 생성됨.
mycol = mydb["emp"]   
# 정보 삽입 (반복해서 수행할 경우 같은 정보가 계속 인서트 됩니다.)


x = mycol.update_one(
    {"e_id":"2"}, {"$set":{"e_name" :"6","gen" : "6","addr" : "6"}}
    )
print(x)



    