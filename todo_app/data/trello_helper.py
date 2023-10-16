import os, requests
from todo_app.data.list import List
from flask import session

class TrelloHelper:

    _TRELLO_LISTS_URL_BASE="https://api.trello.com/1/boards/"
    _TRELLO_LISTS_URL_AFTER_BOARD_ID_BEFORE_KEY="/lists"
    _TRELLO_MOVE_CARD_TO_LIST_URL_BASE="https://api.trello.com/1/cards/"
    _ACCEPT_JSON_HEADER={"Accept":"application/json"}
    _LIST_TO_DO = "To Do"
    _LIST_DOING = "Doing"
    _LIST_DONE = "Done"
    _PARAM_KEY = "key"
    _PARAM_TOKEN = "token"
    _PARAM_CARDS = "cards"
    _PARAM_FIELDS = "fields"
    _PARAM_ID_LIST = "idList"
    _PARAM_CARD_FIELDS = "card_fields"
    _PARAM_VALUE_ALL_CARDS = "all"
    _PARAM_VALUE_OPEN_CARDS = "open"
    _PARAM_VALUE_NAME_FIELD = "name"
    _ENV_TRELLO_API_KEY = "TRELLO_API_KEY"
    _ENV_TRELLO_TOKEN = "TRELLO_TOKEN"
    _ENV_TRELLO_BOARD_ID = "TRELLO_BOARD_ID"

    def __init__(self):
        self.api_key = os.getenv(self._ENV_TRELLO_API_KEY)
        self.trello_token = os.getenv(self._ENV_TRELLO_TOKEN)
        self.trello_board_id = os.getenv(self._ENV_TRELLO_BOARD_ID)

    def set_list_ids(self):
        if self.card_lists:
            if self._LIST_TO_DO in self.card_lists:
                self.todo_list_id = self.card_lists[self._LIST_TO_DO].id
            else:
                self.todo_list_id = "TO_DO_LIST_ID"

            if self._LIST_DOING in self.card_lists:
                self.doing_list_id = self.card_lists[self._LIST_DOING].id
            else:
                self.doing_list_id = "DOING_LIST_ID"

            if self._LIST_DONE in self.card_lists:
                self.done_list_id = self.card_lists[self._LIST_DONE].id
            else:
                self.done_list_id = "DONE_LIST_ID"
        
    def refresh_lists(self):
        
        params = {self._PARAM_KEY : self.api_key, \
                  self._PARAM_TOKEN : self.trello_token, \
                  self._PARAM_CARDS: self._PARAM_VALUE_ALL_CARDS}

        url = self._TRELLO_LISTS_URL_BASE + self.trello_board_id\
            + self._TRELLO_LISTS_URL_AFTER_BOARD_ID_BEFORE_KEY

        response = requests.get(url, params=params)
        lists = {}

        json_response = response.json()

        for json_list in json_response:
            new_list = List(json_list)
            lists[new_list.name] = new_list

        self.card_lists = lists  

    def move_card_to_list(self,id,list):
        card = self.get_card_by_id(id)
        url = self._TRELLO_MOVE_CARD_TO_LIST_URL_BASE + id
        data = {self._PARAM_KEY : self.api_key ,
                self._PARAM_TOKEN : self.trello_token,
                self._PARAM_ID_LIST : list}
        response = requests.put(url, data=data, headers=self._ACCEPT_JSON_HEADER)
        self.refresh_lists()

    def move_card_to_complete(self,id):
        self.move_card_to_list(id, self.done_list_id)

    def move_card_to_todo(self,id):
        self.move_card_to_list(id, self.todo_list_id)

    def get_cards(self, list_name):
        if list_name in self.card_lists:
            return self.card_lists[list_name].get_cards()

    def get_card_by_id(self, id):
        for key in self.card_lists:
            list = self.card_lists[key]
            for card in list.get_cards():
                if card.id == id:
                    return card

