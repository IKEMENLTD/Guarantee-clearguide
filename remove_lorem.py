#!/usr/bin/env python3
import os
import re

# HTMLファイルを検索して処理
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 「Photo from Lorem Picsum」と「Photo from Lorem Picsum 」を削除
                original = content
                content = content.replace('Photo from Lorem Picsum ', '')
                content = content.replace('Photo from Lorem Picsum', '')
                
                # 変更があった場合のみ書き込み
                if content != original:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f'✓ 修正: {filepath}')
            except Exception as e:
                print(f'✗ エラー {filepath}: {e}')

print('\n完了！')
