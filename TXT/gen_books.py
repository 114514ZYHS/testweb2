#!/usr/bin/env python3
"""重新生成 TXT/books.json（书库清单）。

往 TXT/ 里丢完 .txt 之后跑一下这个脚本，阅读器的下拉框才会出现新书。

用法：
    python3 TXT/gen_books.py          # 在仓库根目录跑

规则：
  - 只收 .txt，按文件名排序（跟以前的顺序保持一致）
  - title 去掉 .txt 后缀，原样展示
  - size 用字节数，阅读器拿它显示文件大小
  - 输出 UTF-8 且 ensure_ascii=False，中文直接写出来，方便直接看
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    files = sorted(f for f in os.listdir(HERE) if f.lower().endswith('.txt'))
    books = []
    for f in files:
        p = os.path.join(HERE, f)
        books.append({
            'file': f,
            'title': f[:-4],
            'size': os.path.getsize(p),
        })

    out = os.path.join(HERE, 'books.json')
    with open(out, 'w', encoding='utf-8') as fh:
        json.dump(books, fh, ensure_ascii=False, indent=2)
        fh.write('\n')

    print(f'已生成 {out}')
    print(f'共 {len(books)} 本：')
    for b in books:
        print(f"  {b['size']:>9,}  {b['file']}")


if __name__ == '__main__':
    main()
