import pytest


@pytest.mark.parametrize(
    "timeout,expected",
    (
        (60, b"test down URL"),
    )
)
def test_get_down_url(client, timeout, expected):
    assert client.get("/").status_code == 400
    response = client.get("/", data={"timeout": timeout})
    assert expected in response.data


@pytest.mark.parametrize(
    "data_type,expected",
    (
        ("other", b"not supported"),
        ("image", b"test up URL"),
    )
)
def test_get_up_url(client, data_type, expected):
    assert client.post("/").status_code == 400
    response = client.post("/", data={"data_type": data_type})
    assert expected in response.data


@pytest.mark.parametrize(
    "asset_uuid,expected",
    (
        (0, b"done"),
    )
)
def test_get_status(client, asset_uuid, expected):
    assert client.put("/").status_code == 400
    response = client.put("/", data={"asset_uuid": asset_uuid})
    assert expected in response.data
