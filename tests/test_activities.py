"""Tests for the activities listing endpoint."""


def test_get_activities_returns_expected_shape(client):
    # Arrange
    endpoint = "/activities"
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get(endpoint)
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert "Chess Club" in payload

    for _, details in payload.items():
        assert required_fields.issubset(details.keys())
        assert isinstance(details["participants"], list)
