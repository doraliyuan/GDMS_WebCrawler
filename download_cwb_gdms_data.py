'''
Auto download Taiwan GPS data from CWB (Central Weather Bureau) GDMS (Geophysical Data Management System)
Usage: python download_cwb_gdms_data.py [start_year] [start_doy] [end_year] [end_doy] 
Author      : Wang, Li-Yuan
Since       : 2022/11/25
Update notes:
'''

# 需要的套件
import requests
import json
import wget
import time, datetime, sys

# 吃外部變數
try:
    start_year = int(sys.argv[1]) 
    start_doy  = int(sys.argv[2]) 
    end_year   = int(sys.argv[3]) 
    end_doy    = int(sys.argv[4]) 
except IndexError:
    print('Usage: python download_cwb_gdms_data.py [start_year] [start_doy] [end_year] [end_doy]')
    sys.exit()
    
# doy 轉 day
start_time = datetime.date(start_year, 1, 1) + datetime.timedelta(days=start_doy-1)
end_time   = datetime.date(  end_year, 1, 1) + datetime.timedelta(days=  end_doy-1)

# 登入資訊
login_data = {'username':'', 'password':''}

# 欲下載的資料
search_data = {'output':'o', 'network':'GNSS', 'station':'all', 'stDatetime':start_time, 'edDatetime':end_time, 'label':''}

# 偽裝成瀏覽器
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35'}

# 不同視窗索取同一cookies(保持登入狀態)
rs = requests.Session()

# 會員登入頁面
res = rs.post('https://gdmsn.cwb.gov.tw/php/loginProcess.php', data=login_data, headers=headers)

# 資料搜尋頁面
res2 = rs.post('https://gdmsn.cwb.gov.tw/php/sendEqdownload.php', data=search_data, headers=headers)

# 等待伺服器處理
print('Please waiting 120 seconds...  '+time.ctime())
time.sleep(120)
print('Start to download!  '+time.ctime())

# 會員歷史申請資料清單頁面
res3 = rs.get('https://gdmsn.cwb.gov.tw/php/dbconnect/getMemberDownList.php')

# 抓取這次申請資料的url
json_data = json.loads(res3.text)
goal = json_data[0]
href = goal["show_status"]
url = href.split('.')

# 就可以下載囉^^
download = wget.download('https://gdmsn.cwb.gov.tw'+url[1]+'.tgz')

print('Data have been download!')