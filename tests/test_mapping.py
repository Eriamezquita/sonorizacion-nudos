from src.sonification.mapping import crossing_sign_to_pitch, crossings_to_events


def test_crossing_sign_to_pitch_positive():
    assert crossing_sign_to_pitch(1, base_pitch=60, interval=7) == 67


def test_crossing_sign_to_pitch_negative():
    assert crossing_sign_to_pitch(-1, base_pitch=60, interval=7) == 53


def test_crossings_to_events_length():
    assert len(crossings_to_events([1, -1, 1])) == 3
