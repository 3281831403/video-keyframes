"""视频关键帧：GOP、时间轴与码率：待实现的核心模块。"""


def gop_size(fps, seconds):
    """GOP 帧数。"""
    raise NotImplementedError

def keyframe_times(duration, gop):
    """关键帧时间包含起点。"""
    raise NotImplementedError

def pts_to_ms(pts, timescale):
    """PTS 换算成毫秒。"""
    raise NotImplementedError

def decode_order(pts):
    """按 PTS 给出解码顺序。"""
    raise NotImplementedError

def scene_cut(previous, current, threshold):
    """场景切换按平均差判定。"""
    raise NotImplementedError

def bitrate_budget(width, height, fps, bits_per_pixel):
    """码率预算含帧率。"""
    raise NotImplementedError

def timestamp_wrap(timestamp, bits):
    """时间戳按位数回绕。"""
    raise NotImplementedError

def segment_keyframes(times, start, end):
    """关键帧分段含端点。"""
    raise NotImplementedError

def drift_correct(expected, actual):
    """漂移修正方向。"""
    raise NotImplementedError

def commit_export(statuses):
    """批量导出全部成功才提交。"""
    raise NotImplementedError
