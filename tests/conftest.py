import pytest

from confetti import Config

@pytest.fixture
def nested_config():
    returned = Config({
        'value': 0,
        'a': {
            'value': 1,
            'b': {
                'value': 2,
            }},
        'a2': {
            'value': 3,
        }})
    return returned
