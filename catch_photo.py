from selenium import webdriver
import time
import urllib
import os
#local_path 為存放位置
def got_photo(local_path,dog):
    url = 'https://pic.sogou.com/pics?query='+str(dog)+'&_asf=pic.sogou.com&w=05009900'
    # 目標元素的xpath
    xpath = '//div[@id="imgid"]/ul/li/a/img'
    # 啟動chrome瀏覽器
    chromeDriver = r'/Users/chromedriver'
    driver = webdriver.Chrome(chromeDriver) 

    # 最大化窗口，因為每一次爬取只能看到視窗内的圖片  
    driver.maximize_window()  

    # 紀錄下載過的圖片網址，避免重複下載  
    img_url_dic = {}  

    # 瀏覽器打開爬取頁面
    driver.get(url)  

    # 模擬滾動視窗瀏覽更多圖片
    pos = 0  
    m = 0 # 圖片編號 
    for i in range(1000):  
        pos += i*500 # 每次下滾500  
        js = "document.documentElement.scrollTop=%d" % pos  
        driver.execute_script(js)  
        time.sleep(1)

        for element in driver.find_elements_by_xpath(xpath):
            try:
                img_url = element.get_attribute('src')

                # 保存圖片到指定路徑
                if img_url != None and not img_url in img_url_dic:
                    img_url_dic[img_url] = ''  
                    m += 1
                    filename = str(m)+'.jpg'
                    print(filename)

                    # 保存圖片
                    urllib.request.urlretrieve(img_url, os.path.join(local_path , filename))
                if m == 1000:
                    break

            except OSError:
                print('發生OSError!')
                print(pos)
                break;

    driver.close()
    print("done")

"""for i in range(2,3):
    # 存圖位置
    local_path = 'photo/c'+str(i)
    # 爬取頁面網址
    dogs = ["黃金獵犬","德國牧羊犬","哈士奇"]
    url = 'https://pic.sogou.com/pics?query='+str(dogs[i])+'&_asf=pic.sogou.com&w=05009900'
    got_photo(local_path,url)"""
