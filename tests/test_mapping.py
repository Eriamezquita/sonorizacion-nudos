from src.sonification.mapping import map_range, sequence_to_events


def test_map_range_midpoint_for_degenerate_interval():
    assert map_range(5, 1, 1, 10, 20) == 15


def test_sequence_to_events_length():
    events = sequence_to_events([1, -1, 0])
    assert len(events) == 3


def test_zero_sequence_event_is_silent():
    events = sequence_to_events([0])
    assert events[0].amplitude == 0.0
