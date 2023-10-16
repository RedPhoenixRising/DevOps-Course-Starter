class Card:
    def __init__(self, id, name, shortUrl, status, list_id):
        self.id = id
        self.name = name
        self.shortUrl = shortUrl
        self.status = status 
        self.list_id = list_id

    @classmethod
    def from_json_input(cls, json_input, list_name, list_id):
        return cls(json_input['id'], json_input['name'], json_input['shortUrl'], list_name, list_id)
        

    def print(self):
        print("Card")
        print(f"Card ID: {self.id}")
        print(f"Card Name: {self.name}")
        print(f"Card Short URL: {self.shortUrl}")
        print(f"Card Status (List Name): {self.status}")
        print("\n\n")


