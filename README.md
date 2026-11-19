# 视频关键帧：GOP、时间轴与码率

转码后关键帧对不上、拖动条跳帧：GOP 按秒取整错，关键帧时间没有包含 0，PTS 换算丢精度，B 帧解码顺序没按 PTS，场景切换阈值按单像素，码率预算漏了帧率，时间戳回绕没取模，关键帧分段漏端点，漂移修正方向反，批量导出只提交一半。

## 目录结构

```
README.md
conftest.py
.gitignore
video/__init__.py
video/keyframes.py
tests/test_keyframes.py
```

## 当前状态

`video/keyframes.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_keyframes.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. GOP 按帧率与秒数取整
2. 关键帧时间包含起点
3. PTS 按时间基换算
4. B 帧按 PTS 排序
5. 场景切换按平均差
6. 码率预算含帧率
7. 时间戳按位数回绕
8. 关键帧分段含端点
9. 漂移修正方向
10. 批量导出统一提交

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `video/keyframes.py`
后 15 条用例应全部通过。
