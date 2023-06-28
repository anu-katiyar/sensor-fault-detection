from sensor.config.mongo_db_conn import MongoDBClient

if __name__ == '__main__':
    mongdb_client = MongoDBClient()
    print("collectionname:", mongdb_client.database.list_collection_names())