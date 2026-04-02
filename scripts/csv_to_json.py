#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
工具脚本：将可能存在的 administrative_divisions.csv 转换为 JSON 格式。
Usage: python csv_to_json.py [input_csv] [output_json]
"""
import argparse
import csv
import json
import sys
from pathlib import Path


def parse_args():
    base_dir = Path(__file__).parent
    default_csv_path = base_dir.parent / "data" / "administrative_divisions.csv"
    default_json_path = base_dir.parent / "data" / "administrative_divisions.json"

    parser = argparse.ArgumentParser(
        description="将 CSV 行政区划数据转换为 JSON 数组。"
    )
    parser.add_argument(
        "input_csv",
        nargs="?",
        default=default_csv_path,
        type=Path,
        help=f"输入 CSV 文件路径，默认：{default_csv_path}",
    )
    parser.add_argument(
        "output_json",
        nargs="?",
        default=default_json_path,
        type=Path,
        help=f"输出 JSON 文件路径，默认：{default_json_path}",
    )
    return parser.parse_args()


def normalize_row(row):
    cleaned = {}
    for key, value in row.items():
        if key is None:
            continue

        normalized_key = key.strip()
        normalized_value = value.strip() if isinstance(value, str) else value

        if normalized_value in ("", None):
            continue

        cleaned[normalized_key] = normalized_value

    return cleaned


def main():
    args = parse_args()
    csv_path = args.input_csv
    json_path = args.output_json

    if not csv_path.exists():
        sys.exit(f"错误：未找到文件 {csv_path}")

    print(f"正在读取并转换 {csv_path.name} ...")

    with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        data = []
        for raw_row in reader:
            row = normalize_row(raw_row)
            if row:
                data.append(row)

    if not data:
        sys.exit("错误：CSV 文件没有可用内容。")

    json_path.parent.mkdir(parents=True, exist_ok=True)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"✅ 转换成功！共处理 {len(data)} 条记录，已保存为 {json_path.name}")


if __name__ == "__main__":
    main()
