"""Tests for root and static routes."""


def test_root_redirects_to_static_index(client):
    # Arrange
    endpoint = "/"

    # Act
    response = client.get(endpoint, follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_static_index_is_served(client):
    # Arrange
    endpoint = "/static/index.html"

    # Act
    response = client.get(endpoint)

    # Assert
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
