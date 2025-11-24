from app import get_message

def test_print():
    assert get_message() == "Hello world"
