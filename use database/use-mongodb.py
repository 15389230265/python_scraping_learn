# coding:utf-8
import pymongo
import datetime


if __name__ == "__main__":
    client = pymongo.MongoClient()
    db = client.papers
    collection = db.books
    book = {"author": "Mike",
            "text": "My first book!",
            "tages": ["爬虫", "python", "网络"],
            "data": datetime.datetime.utcnow()}
    book_id = collection.insert(book)
    for b in collection.find():
        print(b)
