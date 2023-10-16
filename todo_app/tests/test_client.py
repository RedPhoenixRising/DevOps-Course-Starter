from dotenv import load_dotenv, find_dotenv
from todo_app import app
from todo_app.data.trello_helper import TrelloHelper
import os, requests, pytest

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    test_app = app.create_app()

    with test_app.test_client() as client:
        yield client



class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data
    

class DataStubResponse():
    def __init__(self, data_from_call):
        self.data_from_call = data_from_call

    def json(self):
        return self.data_from_call

def get_stub(url, params={}):
    test_board_id = os.environ.get('TRELLO_BOARD_ID')
    
    if url == f'https://api.trello.com/1/boards/{test_board_id}/lists':
        fake_response_data = [{
            'id': 'to_do_list_id',
            'name': 'To Do',
            'cards': [{'id':'to_do_card_id','name': 'To_do Test card','shortUrl': 'http://myurl_to_do'}]
        },{
            'id': 'doing_list_id',
            'name': 'Doing',
            'cards': [{'id':'doing_card_id','name': 'Doing Test card','shortUrl': 'http://myurl_doing'}]
        },{
            'id': 'done_list_id',
            'name': 'Done',
            'cards': [{'id':'done_card_id','name': 'Done Test card','shortUrl': 'http://myurl_done'}]
        }]

        return StubResponse(fake_response_data)

    raise Exception(f'Integration test did not expect URL "{url}"')

def put_stub(url, data, headers):
    test_card_id_for_moving = 'to_do_card_id'
    move_to_list = TrelloHelper._LIST_DONE
    if not url == f'https://api.trello.com/1/cards/{test_card_id_for_moving}':
        raise Exception(f'Integration test did not expect URL "{url}"')

def test_index_page(monkeypatch, client):
    monkeypatch.setattr(requests, 'get', get_stub)
    response = client.get('/')

    decoded_data = response.data.decode()

    assert response.status_code == 200
    assert 'To_do Test card' in decoded_data
    assert 'Doing Test card' in decoded_data
    assert 'Done Test card' in decoded_data

def test_complete_item(monkeypatch, client):
    # CALLING GET HERE AS NEED TO INITIALISE LIST ID VARIABLES IN TRELLO HELPER
    monkeypatch.setattr(requests, 'get', get_stub)
    monkeypatch.setattr(requests, 'put', put_stub)
    get_response = client.get('/')
    post_response = client.post('/completeItem/to_do_card_id')
    # NOTE - I WANTED TO TEST THE CONTENT OF THE DATA IN THE POST HERE BUT COULDNT FIGURE OUT HOW TO DO IT
    assert post_response.status_code == 302

    

