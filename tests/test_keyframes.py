import pytest

from video import keyframes as mod

CASES = [
    ('gop_size', [30, 2], 60, False),
    ('keyframe_times', [100, 30], [0, 30, 60, 90], False),
    ('pts_to_ms', [90000, 90000], 1000.0, True),
    ('decode_order', [[2, 0, 1]], [1, 2, 0], False),
    ('scene_cut', [[0, 0, 0], [1, 1, 1], 0.5], True, False),
    ('scene_cut', [[0, 0, 0], [0, 0, 0], 0.5], False, False),
    ('bitrate_budget', [1920, 1080, 30, 0.1], 6220800, False),
    ('timestamp_wrap', [300, 8], 44, False),
    ('segment_keyframes', [[0, 30, 60, 90], 30, 60], [30, 60], False),
    ('drift_correct', [1000, 1010], -10, False),
    ('commit_export', [[True, True]], True, False),
    ('gop_size', [24, 1], 24, False),
    ('keyframe_times', [1, 30], [0], False),
    ('timestamp_wrap', [256, 8], 0, False),
    ('segment_keyframes', [[0, 10], 5, 5], [], False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_keyframes_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
