import pytest
from services.elementary_service import app


TEST_CASES = [
    {'value1': 1, 'operator': '+', 'value2': 1},
    {'value1': 5, 'operator': '-', 'value2': -3},
    {'value1': -10, 'operator': '*', 'value2': -1},
    {'value1': 100, 'operator': '/', 'value2': 25},
    {'value1': 3, 'operator': '%', 'value2': 2},
    {'value1': 5, 'operator': '//', 'value2': 3},
    {'value1': 2, 'operator': '**', 'value2': 10},
]


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_elementary_service(client):
    for test_case in TEST_CASES:
        result = client.post('/elementary', data=test_case).get_json()['result']
        expected = eval(f'{test_case["value1"]} {test_case["operator"]} {test_case["value2"]}')
        assert result == expected
