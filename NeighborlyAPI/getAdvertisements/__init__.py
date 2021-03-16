import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        #url = "localhost"  # TODO: Update with appropriate MongoDB connection information
        url = "mongodb://azurefunctioncosmosdb3:EMXuHj7AWuZ6EcPDEuJWO1NUNdaYACwwx2mpsKTTwGx634NvGguXSh6j6SrCRNgs2s4SF3usUlAaSfnv6olkdg==@azurefunctioncosmosdb3.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@azurefunctioncosmosdb3@"
        client = pymongo.MongoClient(url)
        database = client['azure']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

