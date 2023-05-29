import datetime

import pandas as pd
import requests
import time
import json
import pandas

cookie = {'cookie': '_gcl_au=1.1.851631560.1685251950; _biz_uid=7f99158fa00041f7f233690544ea2119; osano_consentmanager_uuid=38a82475-c728-4579-b1d5-dfbe4b6b1e3a; osano_consentmanager=APWqENxitT0WyMk55DJe41QLCZ-bYCWRsqW0t1Av62FFosetwNeWpSQ1VZ1cgM6xl2wGAo5bL2wnilD24QQapIF9062IdnShxN0cW663fKdUdi-RpU6hrpiqdHe2X0VBljjDUQHDwobb6UAX-QnYrvzbmb-B6thd8mBmVpoycnLBXGFLNzNItpar7EYSPueGyYMU-x57fZsfqy3ipnczhTb3iE-7oR-B4RLXJEm0GfLYNCJyDC6hNTDqURxMrzIuKb5Jt14BAyzCNZXu7PhKkvSPRi_-qh78AcAwjQ==; _mkto_trk=id:351-RWH-315&token:_mch-sensortower-china.com-1685251951565-52984; _fbp=fb.1.1685251952064.1396337652; _ga=GA1.2.644618037.1685251954; _gid=GA1.2.714532061.1685251954; __adroll_fpc=fdfdfe57d4d969cf0b0f2e8d16384f39-1685251955104; osano_consentmanager_uuid=5a6501ee-f873-4ec7-82e1-763241f0bcd7; osano_consentmanager=H9JDFZHe9hMx_lzFBUGE1_FoHJrd-NO26dJrlQEpIIFOfnc5WeiUCq58mnhyta6sHR3VquH7CkvBsBOG-DUI9l63nHMQHhrGsNgjZ1lZdKZ63mN65JU2HSWvGTaoDVqhYNWxrzthocqTa1GO_9kI-sEWFTBz5GJykFm5KvvO8SC7JKqb2qXwF1yJz1WuLSP9dsiyf2fW89HKoYz72c4A4P0QIbmE-Qupd-WHcMXGS_tKuP2-XlvjOTS_eVvnXQF5VjlTow0MdIF7zUPQj1yySAjrZh7qM047DJduDQ==; ln_or=eyIxMzMwMzMwIjoiZCJ9; slireg=https://scout.us2.salesloft.com; slirequested=true; sliguid=0de7011e-3dba-4fbb-999f-3cedc707ea34; __adroll_fpc=fdfdfe57d4d969cf0b0f2e8d16384f39-1685251955104; device_id=2f14ce26-db73-463f-b65a-55ccf97cf31e; __ar_v4=%7CLRZVPNVHWBAMTM3BBVO5B2%3A20230527%3A1%7CIJHL33OI3RDZRJSDZZT2U3%3A20230527%3A2; session=c3f0926692c7c7565f3face90f09bba8; locale=en; _biz_nA=7; _biz_flagsA=%7B%22Version%22%3A1%2C%22XDomain%22%3A%221%22%2C%22ViewThrough%22%3A%221%22%2C%22Mkto%22%3A%221%22%7D; __ar_v4=IJHL33OI3RDZRJSDZZT2U3%3A20230527%3A2%7CLRZVPNVHWBAMTM3BBVO5B2%3A20230527%3A2; _biz_pendingA=%5B%5D; amplitude_id_6edb64137a31fa337b6f553dbccf2d8bsensortower-china.com=eyJkZXZpY2VJZCI6ImMyMDM2YmU1LTdlOTAtNDdkMi1iZmFhLWJjMGUwOWFiOWQ3Y1IiLCJ1c2VySWQiOiJjaGVuLmhhbmxpYW5nLjI3MUBnbWFpbC5jb20iLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE2ODUyNjQ4MjQ1NTQsImxhc3RFdmVudFRpbWUiOjE2ODUyNjU2MzkwOTgsImV2ZW50SWQiOjE2NywiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjE2N30='}
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer <your_access_token>',
    'If-None-Match': 'W/"7ef3c777ec933f3213c20e37869c879e"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Ch-Ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',

}
# 获取当前日期
today = datetime.date.today()
# 将日期转换为字符串格式
today_str = today.strftime('%Y-%m-%d')

category_list = ['6014', '7001', '7002', '7003', '7004', '7005',
                 '7006', '7009','7018', '7019',  '7011', '7012',
                 '7013','7014','7015', '7016', '7017']

# 建立数字和游戏类型之间的对应关系
mapping = {
    '6014': 'game',
    '7001': 'game_action',
    '7002': 'game_adventure',
    '7004': 'game_board',
    '7005': 'game_card',
    '7006': 'game_casino',
    '7009': 'game_family',
    '7003': 'game_casual',
    '7011': 'game_music',
    '7012': 'game_puzzle',
    '7013': 'game_racing',
    '7014': 'game_role_playing',
    '7015': 'game_simulation',
    '7016': 'game_sports',
    '7017': 'game_strategy',
    '7018': 'game_trivia',
    '7019': 'game_word'
}

for category in category_list:
    # channel = 'android'
    channel = 'ios'
    country = 'US'
    df = pd.DataFrame(columns=["rank","name", "app_id", "category", 'country', "channel", "rating", "rating_count"], index=[0])

    # url = 'http://app.sensortower-china.com/api/' + channel + '/category_rankings?onset=1&limit=100&category=' + category + '&country=' + country + '&date=' + today_str

    url = 'http://app.sensortower-china.com/api/' + channel + '/category_rankings?onset=1&limit=100&category=' + category + '&country=' + country + '&date=' + today_str + '&device=iphone'
    print(url)

    time.sleep(10)
    response = requests.get(url, headers=header, cookies=cookie)
    json_data = response.json()
    data = json_data.get("data").get("grossing")
    for app in data:
        if category in mapping:
            category_str = mapping[category]
            new_df = pd.DataFrame({"rank": app["rank"], "name": app["name"], "app_id": app["app_id"], "category": category_str, 'country': country, "channel": channel,  "rating": app["rating"], "rating_count": app["rating_count"]}, index=[0])
            df = pd.concat([df, new_df], ignore_index=True)
    df = df.drop(0)
    if category in mapping:
        category_str = mapping[category]
        df.to_csv(country + "_" + channel + "_" + category_str + "_" + today_str + '.csv')
    print(df)
