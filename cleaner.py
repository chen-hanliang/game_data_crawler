import os
import pandas as pd
import datetime

# 设置文件夹路径
country = 'VN'
folder_path = 'C:/Users/admin/Desktop/game_info'
channel = "android"
# 获取当前日期
today = datetime.date.today()
today_str = today.strftime('%Y-%m-%d')

# {简称：国家} dict
country_dict = {'BR': '巴西', 'DE': '德国', 'ES': '西班牙', 'FR': '法国', 'GB': '英国',
                'IT': '意大利', 'PL': '波兰', 'RO': '罗马尼亚', 'US': '美国', 'VN': '越南',
                'PT': '葡萄牙', 'HK': '香港', 'ID': '印度尼西亚', 'TH': '泰国'}

# {cata_en: cata_cn} dict
game_dict = {'game_action': '动作', 'game_adventure': '冒险', 'game_arcade': '街机',
             'game_board': '棋盘', 'game_card': '卡牌', 'game_casino': '博彩',
             'game_casual': '休闲', 'game_educational': '教育', 'game_music': '音乐',
             'game_puzzle': '解谜', 'game_racing': '赛车', 'game_role_playing': '角色扮演',
             'game_simulation': '模拟', 'game_sports': '体育', 'game_strategy': '策略',
             'game_trivia': '冷知识', 'game_word': '单词'}

country_lst = ['ID', 'TH', 'HK', 'PT', 'BR', 'DE', 'ES', 'FR', 'GB', 'IT', 'PL', 'RO', 'US', 'VN']
for country in country_lst:
    folder_path = 'C:/Users/admin/Desktop/game_info'
    channel = "android"
    try:
        # 获取文件夹内所有csv文件的文件名
        file_names = [f for f in os.listdir(folder_path + "/" + country) if f.endswith('.csv')]

        # 创建一个空的DataFrame
        df = pd.DataFrame()
        for file_name in file_names:
            file_path = os.path.join(folder_path + "/" + country, file_name)
            temp_df = pd.read_csv(file_path)
            df = pd.concat([df, temp_df], ignore_index=True)
            column_list = list(df.columns)
            print(column_list)
        df = df.drop(columns=['Unnamed: 0', 'rating', 'rating_count', 'rank'])
        df = df.rename(columns={'channel':"渠道", 'name': '应用名', "app_id": '包名'})
        df["渠道"] = "安卓"
        df["类别"] = "游戏"
        df["子类别"] = df["category"].map(game_dict)
        df["排序"] = df.reset_index().index + 1
        df["国家"] = country_dict[country]
        df = df.loc[:, ["渠道", "类别", "子类别",  "应用名", "包名", "排序", "国家"]]
        df.to_csv(folder_path + "/" + country + "_" + channel + "_game_info_" + today_str + ".csv", index=False)
    except:
        exit(1)
