# Contributing to SINOSHOP-Sandbox

感谢您对本项目的关注。

## 参与层级

### L1：数据集使用者
- 直接下载 `data/` 目录下的预计算数据集
- 无需提交任何内容

### L2：代码阅读者
- Fork 本仓库
- 在本地编译运行
- 可提交 Issue 报告问题

### L3：代码贡献者
- 在 `src/core/contrib/` 下提交新的物理模型
- 格式：Jupyter Notebook / Python / C++
- PR 提交后 CI 自动检查编译通过

### L4：R18 规范贡献者
- 将 `src/core/` 中的模型重构为 R18 规范
- 需通过 `scripts/r18-linter.py` 检查

## 署名规则

- 合并 PR 后，CI 自动将您的 GitHub ID 加入 `CONTRIBUTORS.md`
- 如需显示机构名称，请在 PR 描述中注明
- 我们不会主动添加任何未经请求的署名

## PR 提交规范

1. Fork 本仓库
2. 创建分支：`git checkout -b feature/your-feature-name`
3. 提交代码
4. 提交 PR，标题格式：`[type] short description`

类型说明：
- `[physics]`：物理模型相关
- `[r18]`：R18 规范相关
- `[docs]`：文档相关
- `[fix]`：修复问题

## 注意事项

- 本仓库不承诺 PR 合并时间
- 大型改动请先提交 Issue 讨论
- 所有贡献者需遵守 CODE_OF_CONDUCT.md