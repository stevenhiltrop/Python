import json


class RestAPI:
    def __init__(self, database=None):
        self.database = database

    def get(self, url, payload=None):
        if url == "/users":
            if payload:
                payload = json.loads(payload)
                try:
                    found_users = [
                        user for user in self.database['users']
                        for requested_user in payload['users']
                        if user["name"] == requested_user
                    ]
                    return json.dumps({"users": found_users})
                except ConnectionError as exception:
                    raise "{1} {0}".format("Database does not exist", exception)
            else:
                return json.dumps(self.database)

    def post(self, url, payload=None):
        if url == "/add":
            self.database["users"] = {
                "name": json.loads(payload)['user'],
                "owes": {},
                "owed_by": {},
                "balance": 0.0
            }
            return json.dumps(self.database['users'])
        elif url == "/iou":
            pass

# database = {"users": []}
# api = RestAPI(database)
#
# response = api.get("/users")
# expected = {"users": []}
