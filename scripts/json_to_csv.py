#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
工具脚本：将本仓库的 administrative_divisions.json 转换为 CSV 格式。
Usage: python json_to_csv.py
"""
import json
import csv
from pathlib import Path
import sys

def main():
    base_dir = Path(__file__).parent
    json_path = base_dir.parent / 'data' / 'administrative_divisions.json'
    csv_path = base_dir.parent / 'data' / 'administrative_divisions.csv'

    if not json_path.exists():
        sys.exit(f"错误：未找到文件 {json_path}")

    print(f"正在读取并转换 {json_path.name} ...")
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if not data:
        sys.exit("错误：JSON 文件没有内容。")

    # 动态获取表头（取第一条数据的 keys 作为整体表头，适应未来任意增减列）
    headers = list(data[0].keys())

    # 写入 CSV
    with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

    print(f"✅ 转换成功！共处理 {len(data)} 条记录，已保存为 {csv_path.name}")

if __name__ == '__main__':
    main()