import codecs
import json
import pytest


@pytest.mark.parametrize(
    'object_name,expected_code,expected_data',
    (
        ('image_123', 200, 'https://rs-uploader-bucket.s3.amazonaws.com/'),
    )
)
def test_get_up_url(client, object_name, expected_code, expected_data):
    assert client.post('/').status_code == 400
    response = client.post('/', data={'object_name': object_name})
    assert expected_code == response.status_code
    assert expected_data == json.loads(response.data)['url']


@pytest.mark.parametrize(
    'object_name,flag,expected_code,expected',
    (
        ('image_123', 'status', 200, b'{"status":"uploaded"}\n'),
        ('image_124', '', 501, b'{"error":"flag is not supported"}\n'),
        ('image_124', 'status', 501, b'{"error":"The specified key does not exist."}\n'),
    )
)
def test_get_status(client, object_name, flag, expected_code, expected):
    assert client.put('/').status_code == 400
    response = client.put('/', data={'object_name': object_name, 'flag': flag})
    assert expected_code == response.status_code
    assert expected == response.data


@pytest.mark.parametrize(
    'object_name,expected_code,timeout',
    (
        ('image_123', 200, 60),
    )
)
def test_get_down_url(client, object_name, expected_code, timeout):
    assert client.get('/').status_code == 400
    response = client.get('/', data={'object_name': object_name, 'timeout': timeout})
    assert expected_code == response.status_code
