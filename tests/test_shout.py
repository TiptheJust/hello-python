from app import shout

def test_shout_caps_and_trim():
    assert shout("  hi there  ") == "HI THERE"
