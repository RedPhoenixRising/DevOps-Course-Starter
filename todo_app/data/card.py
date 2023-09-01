class Card:
    def __init__(self, json_input, list):
        self.id = json_input['id']
        self.closed = json_input['closed']
        self.due = json_input['due']
        self.idboard = json_input['idBoard']
        self.name = json_input['name']
        self.shortUrl = json_input['shortUrl']
        self.start = json_input['start']
        self.status = list.name    
        self.list_id = list.id 

    def print(self):
        print("Card")
        print(f"Card ID: {self.id}")
        print(f"Closed Status: {self.closed}")
        print(f"Due Date: {self.due}")
        print(f"Board ID: {self.idboard}")
        print(f"Card Name: {self.name}")
        print(f"Card Short URL: {self.shortUrl}")
        print(f"Card Start Date: {self.start}")
        print(f"Card Status (List Name): {self.status}")
        print("\n\n")


