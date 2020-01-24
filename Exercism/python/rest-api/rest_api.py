class RestAPI:
    def __init__(self, database=None):
        self.users = database

    def get(self, url, payload=None):
        if url == "/users":
            return self.users

    def post(self, url, payload=None):
        if url == "/add":
            pass
        elif url == "/iou":
            pass

# database = {"users": []}
# api = RestAPI(database)
#
# response = api.get("/users")
# expected = {"users": []}
