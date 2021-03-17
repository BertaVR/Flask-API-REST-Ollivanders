import pytest
from flask import Flask
from tests.configTest import client 



@pytest.mark.item
def test_item(client):
    rv = client.get('/items/Aged Brie')
    assert b'[["Aged Brie", 3, 4]]' in rv.data