import urllib.request
import os
import ssl

# SSL証明書エラー回避（開発環境用）
ssl._create_default_https_context = ssl._create_unverified_context

logos = {
    'smbc.gif': 'https://www.smbc-card.com/shared/images/logo_smcc_01.gif',
    'mufg.gif': 'https://www.bk.mufg.jp/css/img/header/logo_01.gif',
    'mizuho.svg': 'https://www.mizuhobank.co.jp/common/images/logo.svg',
    'lake.svg': 'https://lakealsa.com/cmn/img/header_logo.svg'
}

save_dir = r"d:\guarantee-clearguide\assets\images\logos"
os.makedirs(save_dir, exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

for filename, url in logos.items():
    save_path = os.path.join(save_dir, filename)
    print(f"Downloading {url} to {save_path}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = response.read()
            with open(save_path, "wb") as f:
                f.write(data)
        print(f"Success: {filename} ({len(data)} bytes)")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
