# SINOSHOP-Sandbox

## 深海悬浮隧道数字孪生 | SINOSHOP 3.6.2 标准物理仿真平台

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> 基于 Project Chrono + HydroChrono 的开源深海悬浮隧道物理仿真平台

---

## 快速体验

### Docker 运行

```bash
docker run -p 8080:8080 sinoshop/sandbox:latest
浏览器访问 http://localhost:8080

直接使用预计算数据
python
from sinoshop import DatasetLoader
data = DatasetLoader.load("current_response.hdf5")
print(data.timesteps)
核心内容
内容	说明	访问层级
预计算数据集	洋流响应、疲劳矩阵	L1（直接下载）
PIONEER-01 模型	500米验证断面完整参数	L2（GitHub）
四重冗余控制算法	恒定甲板高度控制律	L2（GitHub）
R18 规范库	无锁数据结构、硬实时调度器	L3（需贡献记录）
参与方式
本仓库采用分级公开策略，参与者自主选择参与深度，通过公开的代码和文档相互学习。不承诺响应时间表。

Powered by Project Chrono


---
