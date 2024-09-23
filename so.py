import requests
from bs4 import BeautifulSoup

# 定义目标URL
url = 'https://t.me/s/cf_push'

# 发起请求并获取页面内容
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 找到所有的文本文件链接
txt_links = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href and href.endswith('.txt'):
        txt_links.append(href)

# 合并所有TXT文件内容
all_content = ''
for txt_link in txt_links:
    try:
        txt_response = requests.get(txt_link)
        all_content += txt_response.text + '\n'  # 添加换行符以分隔内容
    except Exception as e:
        print(f"无法下载 {txt_link}: {e}")

# 将合并后的内容写入ip.txt文件
with open('ip.txt', 'w', encoding='utf-8') as f:
    f.write(all_content)

print("所有TXT文件已成功合并到 ip.txt")
