#!/usr/bin/env python3
"""
SINOSHOP-R21A CHALLENGE-010 自动验证脚本
驭风者 · 全向气旋三维拓扑气动抬升算法 — TRL5 门禁检查

用法:
    python validate_challenge_010.py <result.json>

输入 JSON 格式:
{
    "max_wind_speed": 68.5,
    "wind_direction_coverage": [0, 360],
    "rotation_period_range": [1.0, 6.0],
    "passive_only": true,
    "wind_attenuation": 0.82,
    "central_quiet_zone_stable": true,
    "pid_residual_jitter_um": 250.0,
    "max_tilt_angle": 1.8,
    "hash_integrity": true
}
"""

import sys
import json


def validate(result_json_path: str) -> bool:
    """
    验证仿真结果是否通过 TRL5 门禁。
    返回 True 表示全部通过，False 表示存在未达标项。
    """

    with open(result_json_path, "r", encoding="utf-8") as f:
        r = json.load(f)

    checks = []

    # ---- 核心指标 ----
    checks.append((
        r.get("max_wind_speed", 0) >= 65.0,
        f"❌ 风速不达标: {r.get('max_wind_speed')} m/s（要求 ≥ 65 m/s）"
    ))

    checks.append((
        r.get("wind_direction_coverage", [0, 0]) == [0, 360],
        f"❌ 风向覆盖不完整: {r.get('wind_direction_coverage')}（要求 [0, 360]）"
    ))

    checks.append((
        1.0 <= min(r.get("rotation_period_range", [0, 0])) <= 6.0
        and 1.0 <= max(r.get("rotation_period_range", [0, 0])) <= 6.0,
        f"❌ 旋转周期越界: {r.get('rotation_period_range')}（要求 1h-6h）"
    ))

    checks.append((
        r.get("passive_only", False) is True,
        "❌ 启用了外部电能泵组（要求仅几何被动消能）"
    ))

    checks.append((
        r.get("wind_attenuation", 0) >= 0.75,
        f"❌ 风速衰减不足: {r.get('wind_attenuation')*100}%（要求 ≥ 75%）"
    ))

    checks.append((
        r.get("central_quiet_zone_stable", False) is True,
        "❌ 中心静风区未形成绝对三维稳定"
    ))

    # ---- 高频余差 ----
    checks.append((
        r.get("pid_residual_jitter_um", float("inf")) < 300.0,
        f"❌ PID残余微震超标: {r.get('pid_residual_jitter_um')} μm（要求 < 300 μm）"
    ))

    # ---- 黑天鹅工况 ----
    checks.append((
        r.get("max_tilt_angle", float("inf")) <= 3.0,
        f"❌ 最大倾斜角超标: {r.get('max_tilt_angle')}°（要求 ≤ 3°）"
    ))

    checks.append((
        r.get("hash_integrity", False) is True,
        "❌ 主权哈希存证链数据完整性不足（要求 100%）"
    ))

    # ---- 判定 ----
    all_passed = True
    for passed, msg in checks:
        if not passed:
            print(msg)
            all_passed = False

    if all_passed:
        print("✅ 所有 TRL5 门禁通过")
        print("   主权哈希存证就绪 · STI 身份标识待签发")

    return all_passed


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python validate_challenge_010.py <result.json>")
        sys.exit(2)

    sys.exit(0 if validate(sys.argv[1]) else 1)