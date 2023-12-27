import pytest
from bot import users_out

def test_users_out():
    file_name = 'users.json'
    expected_result = [[730113571], [], {"lng": "rus"}, {}, {}, {"username": "ZhAlexiy"}]

    result = users_out(file_name)
    assert result == expected_result