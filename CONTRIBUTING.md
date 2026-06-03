# Contributing to SINOSHOP-Sandbox

感谢您对本项目的关注。SINOSHOP-R21A 遵循“善乐生”工程哲学——工程向善、乐业创造、生生不息。

> 🔗 **SINOSHOP 生态导航**：[SINOSHOP-Sandbox](https://gitee.com/sinoshop/SINOSHOP-Sandbox) · [思维范式接口](https://gitee.com/sinoshop/SINOSHOP-Sandbox/tree/master/api/R21A-MIND) · [产品手册](https://gitee.com/sinoshop/SINOSHOP-Sandbox/tree/master/products)

---

## 项目结构
SINOSHOP-Sandbox/
├── challenges/ # 技术挑战与仿真任务
├── api/ # R21A标准接口规范
│ └── R21A-MIND/ # 思维范式Prompt模板
├── products/ # 核心标准模块产品手册
├── scripts/ # 自动化验证脚本
├── docs/ # 技术文档
├── src/ # 源代码
│ └── core/ # 核心物理模型
│ └── contrib/ # 社区贡献模型
└── data/ # 预计算数据集
text
￼
￼
复制
￼
￼
下载
---

## 参与层级

### L1：数据集使用者
- 直接下载 data/ 目录下的预计算数据集
- 无需提交任何内容

### L2：代码阅读者
- Fork 本仓库
- 在本地编译运行
- 可提交 Issue 报告问题

### L3：代码贡献者
- 在 src/core/contrib/ 下提交新的物理模型
- 格式：Jupyter Notebook / Python / C++
- PR 提交后 CI 自动检查编译通过

### L4：R18 规范贡献者
- 将 src/core/ 中的模型重构为 R18 规范
- 需通过 scripts/r18-linter.py 检查

---

## 快速开始（新贡献者）

1. Fork 本仓库
2. 找到标记为 `难度：入门` 的 Issue，评论认领
3. 30分钟内即可完成首次贡献

---

## Issue 标签体系

| 标签 | 含义 |
|:---|:---|
| `难度：入门` | 1-4小时，适合新人 |
| `难度：中级` | 1-2天，需要一定背景 |
| `难度：挑战` | 长期任务，核心贡献 |
| `状态：待认领` | 无人处理，欢迎接手 |
| `状态：进行中` | 已被认领 |
| `状态：待审核` | 已提交PR，等待审查 |
| `类型：代码` | 编程相关 |
| `类型：文档` | 文档相关 |
| `类型：仿真` | 仿真与验证相关 |

---

## 署名规则
- 合并 PR 后，CI 自动将您的 GitHub ID 加入 CONTRIBUTORS.md
- 如需显示机构名称，请在 PR 描述中注明
- 我们不会主动添加任何未经请求的署名

---

## PR 提交规范
1. Fork 本仓库
2. 创建分支：git checkout -b feature/your-feature-name
3. 提交代码
4. 提交 PR，标题格式：[type] short description

类型说明：
- [physics]：物理模型相关
- [r18]：R18 规范相关
- [docs]：文档相关
- [fix]：修复问题

---

## 注意事项
- 本仓库不承诺 PR 合并时间
- 大型改动请先提交 Issue 讨论
- 所有贡献者需遵守 CODE_OF_CONDUCT.md

---

## 获取帮助
- 在本仓库提 Issue
- 联系邮箱：[填写您的邮箱]

---

## 更新日志
- 初始版本（15天前）：L1-L4参与层级、PR规范
- 2026-06-03：新增Issue标签体系、项目结构导航、快速开始指南

---

*本指南由梁振雄与SINOSHOP AI军团联合编制。*