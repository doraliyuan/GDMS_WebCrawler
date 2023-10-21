# GDMS_WebCrawler
Auto download Taiwan GPS data from CWB (Central Weather Bureau) GDMS (Geophysical Data Management System)

# 程式目的
於氣象署網站下載GPS觀測資料。

網站全名為 中華民國交通部-中央氣象署-臺灣地震與地球物理資料管理系統，其網址為https://gdmsn.cwb.gov.tw/

# 緣起
GPS觀測資料的索取方式為登入後，於資料索取頁面提交所要的資料類型與時間區間，網站經過一段時間後會把提交的資料打包好送至個人空間，於時效內即可點擊下載。

但由於GPS觀測資料網站每天都會更新，希望可以把這些下載動作交給電腦去執行。

# 執行程式之前需要
1. 去網站申請註冊為GDMS的使用者。
2. 於程式第30行的地方輸入GDMS使用者的帳號密碼。
3. 個人環境中安裝所需的python套件。

# 如何使用
`python download_cwb_gdms_data.py [start_year] [start_doy] [end_year] [end_doy]`


指令後面接的變數依序代表索取資料的 時間開始年份、時間開始doy、時間結束年份、時間結束doy

*doy: day of year

搭配Linux shell、crontab即可每天例行下載資料。

# 注意
此方式其實是作者從網站原始碼中找到隱藏的API，非公開的API，請小心使用。
