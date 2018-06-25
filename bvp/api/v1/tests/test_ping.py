from flask import url_for


def test_ping_ok(client):
    pong = client.get(url_for("bvp_api_v1.get_ping"))
    assert pong.status_code == 200
    assert pong.json["message"] == "ok"
