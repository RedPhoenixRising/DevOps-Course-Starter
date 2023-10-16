import pytest
from todo_app.data.trello_helper import TrelloHelper
from todo_app.data.card import Card
from todo_app.data.view_model import ViewModel

_to_do_card_name = "My to do task"
_doing_card_name = "My doing task"
_done_card_name = "My done task"
_dummy_url = "http://my.dummy.url.com/"
_to_do_card_id = "1"
_doing_card_id = "2"
_done_card_id = "3"


@pytest.fixture
def get_test_card_list():
    to_do_card = Card(_to_do_card_id, _to_do_card_name, _dummy_url, TrelloHelper._LIST_TO_DO, _to_do_card_id)
    doing_card = Card(_doing_card_id, _doing_card_name, _dummy_url, TrelloHelper._LIST_DOING, _doing_card_id)
    done_card = Card(_done_card_id, _done_card_name, _dummy_url, TrelloHelper._LIST_DONE, _done_card_id)
    item_dict = {TrelloHelper._LIST_TO_DO : to_do_card, TrelloHelper._LIST_DOING : doing_card, TrelloHelper._LIST_DONE: done_card}
    return item_dict


def test_view_model_done_property(get_test_card_list):
    # ARRANGE
    item_dict = get_test_card_list
    view_model = ViewModel(item_dict)

    # ACT
    result = view_model.done_items

    # ASSERT
    assert result.status == TrelloHelper._LIST_DONE
    assert result.id == _done_card_id
    assert result.name == _done_card_name

def test_view_model_to_do_property(get_test_card_list):
    # ARRANGE
    item_dict = get_test_card_list
    view_model = ViewModel(item_dict)

    # ACT
    result = view_model.to_do_items

    # ASSERT
    assert result.status == TrelloHelper._LIST_TO_DO
    assert result.id == _to_do_card_id
    assert result.name == _to_do_card_name

def test_view_model_doing_property(get_test_card_list):
    # ARRANGE
    item_dict = get_test_card_list
    view_model = ViewModel(item_dict)

    # ACT
    result = view_model.doing_items

    # ASSERT    
    assert result.status == TrelloHelper._LIST_DOING
    assert result.id == _doing_card_id
    assert result.name == _doing_card_name
