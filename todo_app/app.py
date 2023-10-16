from flask import Flask, render_template, redirect, request
from todo_app.data.view_model import ViewModel
from todo_app.flask_config import Config
from todo_app.data.session_items import get_items,add_item
from todo_app.data.trello_helper import TrelloHelper

import os

app = Flask(__name__)
app.config.from_object(Config())

helper = TrelloHelper()

@app.route('/')
def index():
    helper.refresh_lists()
    helper.set_list_ids()
    to_do_cards = helper.get_cards(TrelloHelper._LIST_TO_DO)
    doing_cards = helper.get_cards(TrelloHelper._LIST_DOING)
    done_cards = helper.get_cards(TrelloHelper._LIST_DONE)

    cards = {TrelloHelper._LIST_TO_DO: to_do_cards, TrelloHelper._LIST_DOING : doing_cards, TrelloHelper._LIST_DONE : done_cards}

    view_model = ViewModel(cards)

    return render_template('index.html', view_model=view_model)

@app.route('/completeItem/<id>', methods=["POST"])
def complete_item(id):
    helper.move_card_to_complete(id)
    return redirect("/", 302)

@app.route('/reopenItem/<id>', methods=["POST"])
def reopen_item(id):
    helper.move_card_to_todo(id)
    return redirect("/", 302)
