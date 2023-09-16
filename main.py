import re
import os
import requests
import urllib.request
import time
import markdown
from bs4 import BeautifulSoup
import json
import random
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 获取一组标题

url = "https://www.luogu.com.cn/problem/P"
savedate = "D:/study/软件工程/luogupachou/2"

# 从给定的 URL 获取问题列表


def getlist(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76",
        "Cookie": "__client_id=383641e8eb3654287f93d5612bfe6e423cbda2fa; _uid=667359; C3VK=f7b0e2",
    }
    try:
        # 使用 with 语句发送 GET 请求并处理响应
        with requests.get(url, headers=headers) as response:
            response.raise_for_status()
            problemlist = re.findall(r'<a\shref="(.*?)">', response.text)
            P = [x[9:14] for x in problemlist if x]
            return P
    except requests.exceptions.RequestException as e:
        print("请求出错：", e)

# 获取洛谷题库题目


def getProblem(url, num):
    headers = {
        "Cookie": "client_id=98cfc2cc86d451827cf762d426dc1b5e5551a763; login_referer=https%3A%2F%2Fwww.luogu.com.cn%2Fproblem%2FP1000; _uid=561385",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()  # 检查请求是否成功
        html = response.text

        # 数据整理
        bs = BeautifulSoup(html, "html.parser")
        core = bs.select("article")[0]
        md = str(core)
        md = re.sub("<h1>", "# ", md)
        md = re.sub("<h2>", "## ", md)
        md = re.sub("<h3>", "#### ", md)
        md = re.sub("</?[a-zA-Z]+[^<>]*>", "", md)

        # 提取标签
        tags = bs.select(".problem-tag")
        tag_list = [tag.get_text(strip=True) for tag in tags]
        tag_string = ", ".join(tag_list)
        md += "\n\n**Tags:** " + tag_string

        # 保存数据
        global fn
        fn = bs.title.string
        fn = fn[:-5]
        if not os.path.exists(savedate):
            os.mkdir(savedate)
        filename = savedate + '/' + "P" + str(num) + "-" + fn + ".md"
        with open(filename, "w", encoding="utf-8") as fp:
            fp.write(md)
    except requests.exceptions.RequestException as e:
        print("请求出错:", e)


# 获取洛谷题目的解答
def getSolution(url, num):
    headers = {
        "Cookie": "__client_id=7298f81227f1bc2d6e646cba05a73571d5f5ac0c; _uid=1091435",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()  # 检查请求是否成功
        html = response.text

        # 整理数据
        soup = BeautifulSoup(html, "html.parser")
        encoded_content_element = soup.find('script')
        encoded_content = encoded_content_element.text
        start = encoded_content.find('"')
        end = encoded_content.find('"', start + 1)
        encoded_content = encoded_content[start + 1:end]
        decoded_content = urllib.parse.unquote(encoded_content)
        decoded_content = decoded_content.encode(
            'utf-8').decode('unicode_escape')
        start = decoded_content.find('"content":"')
        end = decoded_content.find('","type":"题解"')
        decoded_content = decoded_content[start + 11:end]

        # 保存数据
        if not os.path.exists(savedate):
            os.mkdir(savedate)
        filename = savedate + '/' + "P" + str(num) + "-" + fn + "-题解" ".md"
        with open(filename, "w", encoding="utf-8") as fp:
            fp.write(decoded_content)
    except requests.exceptions.RequestException as e:
        print("请求出错:", e)


def getTitle(html):
    soup = BeautifulSoup(html, "html.parser")
    a = soup.findAll("li")
    titles = []
    for aa in a:
        b = aa.find("a")
        titles.append((b.string))
    return titles


# 主程序
url_list = []
for i in range(1000, 1050):
    url = "https://www.luogu.com.cn/problem/P" + str(i)
    url_list.append(url)

for i, url in enumerate(url_list):
    getProblem(url, i+1000)
    getSolution(url, i+1000)
    sleep_time = random.randint(1, 5)  # 生成1秒到5秒之间的随机数
    time.sleep(sleep_time)  # 随机休眠时长
