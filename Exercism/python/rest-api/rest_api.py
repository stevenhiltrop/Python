import json


class RestAPI:
    def __init__(self, database=None):
        self.users = database

    def get(self, url, payload=None):
        if url == "/users":
            return json.dumps(self.users)

    def post(self, url, payload=None):
        if url == "/add":
            user = self.users["users"] = {
                "name": json.loads(payload)['user'],
                "owes": {},
                "owed_by": {},
                "balance": 0.0
            }
            return json.dumps(user)
        elif url == "/iou":
            pass

# database = {"users": []}
# api = RestAPI(database)
#
# response = api.get("/users")
# expected = {"users": []}
