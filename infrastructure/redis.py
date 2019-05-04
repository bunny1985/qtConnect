from walrus import Database

db: Database = Database(host='redis', port=6379, db=0, charset="utf-8", decode_responses=True)
