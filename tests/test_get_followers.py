import pytest
import requests


def test_get_followers():
    api_key = "TxD8FO9dF3Uk9LJOAylBogiz81GhrnhX37SPU8gi"
    url = "https://api.nasa.gov/planetary/apod" + "?api_key=" + api_key
    response = requests.get(url)
    assert response.status_code == 200
