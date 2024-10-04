from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import re

# 获取已打开的浏览器实例（以 Chrome 为例）
options = webdriver.ChromeOptions()
options.debugger_address = "127.0.0.1:9222"  # 根据实际情况调整端口
driver = webdriver.Chrome(options=options)


def open_link_and_check_video(link):
    # 打开链接
    driver.get(link)
    time.sleep(5)
    # 等待视频加载完成
    try:
        complete_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-v-7a22ffd8].text')))
        complete = complete_element.text
        if '100' in complete:
            print("视频之前已经播放完成，准备跳转到下一个链接。")
            return False
        
        video_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "video"))
        )
        while True:
            # 判断视频是否播放完成
            ended = driver.execute_script("return arguments[0].ended;", video_element)
            if ended:
                print("视频播放完成，准备跳转到下一个链接。")
                return False
            is_playing = driver.execute_script("return arguments[0].paused === false;", video_element)
            if not is_playing:
                print("视频停止播放，尝试继续播放。")
                # 根据实际情况模拟点击播放按钮或执行播放操作
                # 假设播放按钮有特定的类名'play-button'
                play_button = driver.find_element(By.CLASS_NAME, 'xt_video_bit_play_btn')
                play_button.click()
            time.sleep(5)
    except Exception as e:
        print(f"发生错误：{e}")
        return False

# 假设链接列表
head_link = "https://buaa.yuketang.cn/pro/lms/Baa8BNvtpbN/23421341/video/"
links = [ '52731971', '52731977', '52731988','52731997','52732008', '52732015', '52732022', '52732032', '52732042',
 '52732048', '52732060', '52732058', '52732069', '52732078', '52732086', '52732094', '52732103', '52732105', '52732118',
   '52732127', '52732129', '52732132', '52732134', '52732136', '52732164', '52732165', '52732178', '52732179', '52732194',
     '52732196', '52732198', '52732200', '52732209', '52732204', '52732207', '52732248', '52732259', '52732267', '52732273',
       '52732280', '52732286']


for link in links:
    # num1 = int(link)
    # num2 = 52732118
    # if num1 >= num2:
    url_link = head_link + link
    result = open_link_and_check_video(url_link)

# driver.quit()
