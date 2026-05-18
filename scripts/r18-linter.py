#!/usr/bin/env python3
"""R18编码规范检查工具"""

import re
import sys
from pathlib import Path

R18_RULES = {
    "NO_LOCK": {
        "pattern": r"std::mutex|std::lock_guard|pthread_mutex",
        "message": "禁止使用互斥锁，请使用无锁数据结构（std::atomic）"
    },
    "NO_MALLOC": {
        "pattern": r"\bnew\b|\bmalloc\b|\bcalloc\b",
        "message": "禁止动态内存分配，请使用静态分配或池分配器"
    },
    "NO_EXCEPTION": {
        "pattern": r"\bthrow\b|\bcatch\b",
        "message": "禁止异常，请使用返回码（std::error_code）"
    },
    "DETERMINISTIC_LOOP": {
        "pattern": r"while\s*\(\s*true\s*\)|for\s*\(\s*;;\s*\)",
        "message": "无限循环必须包含硬实时退出条件"
    }
}

def lint_file(filepath: Path) -> tuple[bool, list[str]]:
    errors = []
    try:
        content = filepath.read_text(encoding='utf-8', errors='ignore')
    except Exception as e:
        errors.append(f"读取文件失败: {e}")
        return False, errors
    
    for rule_name, rule in R18_RULES.items():
        if re.search(rule["pattern"], content, re.MULTILINE):
            errors.append(f"{rule['message']} [{rule_name}]")
    
    return len(errors) == 0, errors

def main():
    if len(sys.argv) < 2:
        print("用法: python r18-linter.py <目录>")
        sys.exit(1)
    
    target_dir = Path(sys.argv[1])
    if not target_dir.exists():
        print(f"错误: 路径不存在 - {target_dir}")
        sys.exit(1)
    
    all_passed = True
    for filepath in target_dir.rglob("*"):
        if filepath.suffix in [".cpp", ".h", ".hpp", ".c", ".cc"]:
            passed, errors = lint_file(filepath)
            if not passed:
                all_passed = False
                print(f"\n{filepath}:")
                for err in errors:
                    print(f"  - {err}")
    
    if all_passed:
        print("R18 规范检查通过")
        sys.exit(0)
    else:
        print("\nR18 规范检查失败")
        sys.exit(1)

if __name__ == "__main__":
    main()