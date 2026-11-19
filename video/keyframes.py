"""视频关键帧：GOP、时间轴与码率的核心实现。"""


def gop_size(fps, seconds):
    """GOP 帧数：按帧率乘时长，四舍五入到整数帧。"""
    return int(round(fps * seconds))

def keyframe_times(duration, gop):
    """关键帧时间：从 0 开始按 GOP 步进，包含起点 0。"""
    return list(range(0, duration, gop))

def pts_to_ms(pts, timescale):
    """PTS 换算成毫秒，保留浮点精度。"""
    return pts / timescale * 1000.0

def decode_order(pts):
    """按 PTS 升序给出解码顺序（返回原始下标）。"""
    return sorted(range(len(pts)), key=lambda i: pts[i])

def scene_cut(previous, current, threshold):
    """场景切换：两帧逐像素平均绝对差超过阈值即判定。"""
    n = len(previous)
    if n == 0:
        return False
    mean_diff = sum(abs(a - b) for a, b in zip(previous, current)) / n
    return mean_diff > threshold

def bitrate_budget(width, height, fps, bits_per_pixel):
    """码率预算：宽 × 高 × 帧率 × 每像素比特数。"""
    return int(round(width * height * fps * bits_per_pixel))

def timestamp_wrap(timestamp, bits):
    """时间戳按位数回绕（取模 2**bits）。"""
    return timestamp % (1 << bits)

def segment_keyframes(times, start, end):
    """关键帧分段：落在 [start, end] 闭区间内的关键帧。"""
    return [t for t in times if start <= t <= end]

def drift_correct(expected, actual):
    """漂移修正量：expected - actual，直接加到实际值上即可对齐。"""
    return expected - actual

def commit_export(statuses):
    """批量导出：全部成功才提交。"""
    return all(statuses)
