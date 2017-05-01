from fixtures import test_data, test_data_json, call_cli
import re


def test_single_key(test_data, test_data_json):
    result = call_cli(test_data_json, {'item': re.compile(r'name')})
    for item in test_data:
        for key in item.keys():
            if key != 'name':
                item.pop(key)
    assert result == test_data


def test_mask_key(test_data, test_data_json):
    result = call_cli(test_data_json, {'item': re.compile(r'name|friends')})
    for item in test_data:
        for key in item.keys():
            if key not in ['name', 'friends']:
                item.pop(key)
    assert result == test_data


def test_nested_key(test_data, test_data_json):
    result = call_cli(test_data_json, {'item.friends.item': re.compile('firstname')})
    for item in test_data:
        for friend in item['friends']:
            friend.pop('lastname')

    assert result == test_data
