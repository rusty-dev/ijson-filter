from fixtures import test_data, test_data_json, call_cli


def test_array_head(test_data, test_data_json):
    result = call_cli(test_data_json, {'': 2})
    assert result == test_data[:2]


def test_array_tail(test_data, test_data_json):
    result = call_cli(test_data_json, {'': -2})
    assert result == test_data[-2:]


def test_nested_head(test_data, test_data_json):
    result = call_cli(test_data_json, {'item.friends': 3})
    for item in test_data:
        item['friends'] = item['friends'][:3]

    assert result == test_data
