from todo_app.data.trello_helper import TrelloHelper

class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items
    
    @property
    def to_do_items(self):
        return self._items[TrelloHelper._LIST_TO_DO]
    
    @property
    def doing_items(self):
        return self._items[TrelloHelper._LIST_DOING]
    
    @property 
    def done_items(self):
        return self._items[TrelloHelper._LIST_DONE]
    

    