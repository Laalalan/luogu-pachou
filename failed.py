import os
import random
import tempfile
import time
import bs4
import requests
import re

baseUrl = "https://www.luogu.com.cn/problem/P"
savePath = "D:\\study\\软件工程\\luogupachou\\1\\"  # 需要更改为自己的路径
minn = 1000
maxn = 2070  # 最大题号


def main():
    print("计划爬取到P{}".format(maxn))
    failed_problems = []  # 记录爬取失败的题目编号
    for i in range(minn, maxn + 1):
        print("正在爬取P{}...".format(i), end="")
        try:
            url = baseUrl + str(i)
            final_url = get_final_url(url)
            if final_url == "error":
                print("爬取失败，可能是不存在该题或无权查看")
                failed_problems.append(i)  # 记录失败的题目编号
            else:
                html = getHTML(final_url)
                problemMD = getMD(html)
                title = getTitle(html)
                filename = "P{}-{}.md".format(i, title)
                print("爬取成功！正在保存...", end="")
                saveData(problemMD, filename)
                print("保存成功!")
        except Exception as e:
            print("发生异常：", str(e))
            failed_problems.append(i)  # 记录失败的题目编号

        # 添加延时
        time.sleep(5)  # 暂停3秒

        if i == 50:
            print("已爬取到50题,程序停止")
            break

    print("爬取完毕")
    if failed_problems:
        print("以下题目爬取失败：")
        print(failed_problems)
        # 可以将 failed_problems 保存到文件，以便下次运行程序时重新尝试爬取


def get_final_url(url):
    user_agent = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    ]
    headers = {
        "User-Agent": random.choice(user_agent)
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 302 or response.status_code == 301:  # 处理302和301重定向
        final_url = response.headers.get("Location")
        return final_url
    else:
        print("发生HTTP错误:", response.status_code)
        return "error"


def getHTML(url):
    user_agent = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    ]
    headers = {
        "User-Agent": random.choice(user_agent)
    }
    response = requests.get(url, headers=headers)

    if "Exception" not in response.text:  # 洛谷中没找到该题目或无权查看的提示网页中会有该字样
        return response.text
    else:
        return "error"


def getMD(html):
    bs = bs4.BeautifulSoup(html, "html.parser")
    core = bs.select("article")[0]
    md = str(core)
    md = re.sub("<h1>", "# ", md)
    md = re.sub("<h2>", "## ", md)
    md = re.sub("<h3>", "#### ", md)
    md = re.sub("</?[a-zA-Z]+[^<>]*>", "", md)
    return md


def getTitle(html):
    bs = bs4.BeautifulSoup(html, "html.parser")
    title = bs.title.string.split("-")[0].strip()
    return title


def saveData(data, filename):
    cfilename = savePath + filename
    try:
        # 先写入临时文件
        temp_filename = cfilename + '.temp'
        with open(temp_filename, "w", encoding="utf-8") as file:
            file.write(data)

        # 写入成功后再重命名为目标文件
        os.rename(temp_filename, cfilename)
    except IOError as e:
        print("保存文件时发生错误：", str(e))


if __name__ == '__main__':
    main()
