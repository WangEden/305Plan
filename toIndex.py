import os
import re


fileList = os.listdir("./")
pattern = r"\.md$"
file_path = [file for file in fileList if re.search(pattern, file)][0]
print("find markdown file: ", file_path)

html_path = "output.html"
html_path = "index.html"
print("target html: ", html_path)

template = """
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="apple-mobile-web-app-capable" content="yes"/>
    <meta name="apple-touch-fullscreen" content="yes"/>
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent"/>
    <link rel="manifest" href="./manifest.json"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-2048x2732.png" media="(device-width: 1024px) and (device-height: 1366px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-2732x2048.png" media="(device-width: 1024px) and (device-height: 1366px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1668x2388.png" media="(device-width: 834px) and (device-height: 1194px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-2388x1668.png" media="(device-width: 834px) and (device-height: 1194px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1536x2048.png" media="(device-width: 768px) and (device-height: 1024px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-2048x1536.png" media="(device-width: 768px) and (device-height: 1024px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1668x2224.png" media="(device-width: 834px) and (device-height: 1112px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-2224x1668.png" media="(device-width: 834px) and (device-height: 1112px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1620x2160.png" media="(device-width: 810px) and (device-height: 1080px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-2160x1620.png" media="(device-width: 810px) and (device-height: 1080px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1290x2796.png" media="(device-width: 430px) and (device-height: 932px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-2796x1290.png" media="(device-width: 430px) and (device-height: 932px) and (-webkit-device-pixel-ratio: 3) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1179x2556.png" media="(device-width: 393px) and (device-height: 852px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-2556x1179.png" media="(device-width: 393px) and (device-height: 852px) and (-webkit-device-pixel-ratio: 3) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1248x2778.png" media="(device-width: 428px) and (device-height: 926px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-2778x1248.png" media="(device-width: 428px) and (device-height: 926px) and (-webkit-device-pixel-ratio: 3) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1170x2532.png" media="(device-width: 390px) and (device-height: 844px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-2532x1170.png" media="(device-width: 390px) and (device-height: 844px) and (-webkit-device-pixel-ratio: 3) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1125x2436.png" media="(device-width: 375px) and (device-height: 812px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-2436x1125.png" media="(device-width: 375px) and (device-height: 812px) and (-webkit-device-pixel-ratio: 3) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1242x2688.png" media="(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-2688x1242.png" media="(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 3) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-828x1792.png" media="(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1792x828.png" media="(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1242x2208.png" media="(device-width: 414px) and (device-height: 736px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-2208x1242.png" media="(device-width: 414px) and (device-height: 736px) and (-webkit-device-pixel-ratio: 3) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-750x1334.png" media="(device-width: 375px) and (device-height: 667px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1334x750.png" media="(device-width: 375px) and (device-height: 667px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-640x1136.png" media="(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1136x640.png" media="(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)"/>
    <title>305任务清单</title>
    <link rel="stylesheet" href="./style/style.css">
</head>
<body>
    <div class="container">
        <h2>先进视觉赛</h2>
        <div class="section">
            <h3>技术文档</h3>
            <div class="soupDest"></div>
            <h3>实际任务</h3>
            <div class="soupDest"></div>
            <h3>答辩任务</h3>
            <div class="soupDest"></div>
            <h3>提交内容：</h3>
            <div class="soupDest"></div>
        </div>
    </div>
</body>
</html>
"""


import markdown
from bs4 import BeautifulSoup


# 读取 Markdown
with open(file_path, 'r', encoding="utf-8") as file:
    md_text = file.read()

# 将内容转成简易的 HTML 节点
html = markdown.markdown(md_text)

# 利用 BeautifulSoup 修改
sourceSoup = BeautifulSoup(html, 'html.parser')
targetSoup = BeautifulSoup(template, 'html.parser')

sourceTaskNodeList = sourceSoup.find_all('ul')
targetTaskNodeList = targetSoup.find_all(class_="soupDest")

for index, value in enumerate(sourceTaskNodeList):
    targetTaskNodeList[index].append(value)
    
html = targetSoup.prettify()
# print(html)

with open(html_path, 'w', encoding='utf-8') as file:
    file.write(html)
    print("ok")
