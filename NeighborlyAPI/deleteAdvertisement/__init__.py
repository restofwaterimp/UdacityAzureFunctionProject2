import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            #url = "localhost"  # TODO: Update with appropriate MongoDB connection information
            url = "mongodb://azurefunctioncosmosdb3:EMXuHj7AWuZ6EcPDEuJWO1NUNdaYACwwx2mpsKTTwGx634NvGguXSh6j6SrCRNgs2s4SF3usUlAaSfnv6olkdg==@azurefunctioncosmosdb3.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@azurefunctioncosmosdb3@"
            client = pymongo.MongoClient(url)
            database = client['azure']
            collection = database['advertisements']
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
