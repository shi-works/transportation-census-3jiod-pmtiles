# -*- coding: utf-8 -*-
# コード表を元に読みやすいデータに変換する
import pandas as pd
import csv

# 出力CSVファイルオープン
output_csvfile = "./out/202112_1_3jiod_od_pattern_count_add_coordinate.csv"
with open(output_csvfile, 'a', encoding='utf-8') as f:
    # ヘッダー行出力
    fieldnames = ['入場事業者名', '入場路線名', '入場駅名', '入場駅_緯度', '入場駅_経度',
                  '出場事業者名', '出場路線名', '出場駅名', '出場駅_緯度', '出場駅_経度', '件数']
    csvfile_writer = csv.DictWriter(
        f, fieldnames=fieldnames, lineterminator='\n')
    csvfile_writer.writeheader()

    # 入力CSVファイルをデータフレームに格納
    data = pd.read_csv(
        "./data/202112_1_3jiod_od_pattern_count.csv", dtype=object, encoding="shift-jis").values.tolist()

    # 駅座標データを辞書に読み込み
    csv_file_coordinate = "./data/N02-21_Station_Centroid.csv"
    with open(csv_file_coordinate, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        # 辞書にデータを追加
        '''
        # キー：事業者名＋路線名＋駅名、値：緯度経度
        dict_coordinate = {row[5] + "_" + row[4] + "_" +
                           row[6]: row[0] + "_" + row[1] for row in reader}
        '''
        # キー：事業者名＋駅名、値：緯度経度
        dict_coordinate = {row[5] + "_" + row[6]: row[0] + "_" + row[1] for row in reader}

    # print('--- N02-21_Station_Centroid.csv ---')
    # print(dict_coordinate)

    # 読み替え用の辞書を作成

    # 事業者名
    dict_jigyosya_replace = {
        "東京都交通局": "東京都",
        "名古屋市交通局": "名古屋市",
        "京都市交通局": "京都市",
        "神戸市交通局": "神戸市",
        "横浜市交通局": "横浜市"
    }

    # 事業者名+駅名
    dict_jigyosya_station_replace = {
        "南海電気鉄道_難波": "南海電気鉄道_難波",
        "近畿日本鉄道_大阪難波": "近畿日本鉄道_大阪難波",
        "大阪市高速電気軌道_なんば": "大阪市高速電気軌道_難波",
        "西日本旅客鉄道_ＪＲ難波": "西日本旅客鉄道_JR難波",
        "東京地下鉄_霞ケ関": "東京地下鉄_霞ヶ関",
        "東武鉄道_霞ケ関": "東武鉄道_霞ヶ関",
        "大阪市高速電気軌道_あびこ": "大阪市高速電気軌道_我孫子",
        "泉北高速鉄道_泉ケ丘": "泉北高速鉄道_泉ヶ丘",
        "東京地下鉄_南阿佐ケ谷": "東京地下鉄_南阿佐ヶ谷",
        "横浜市_三ッ沢上町": "横浜市_三ツ沢上町",
        "横浜市_三ッ沢下町": "横浜市_三ツ沢下町",
        "東日本旅客鉄道_佐貫": "東日本旅客鉄道_佐貫町",
        "東京地下鉄_西ケ原": "東京地下鉄_西ヶ原",
        "京浜急行電鉄_花月園前": "京浜急行電鉄_花月総持寺",
        "南海電気鉄道_和歌山大学前（ふじと台）": "南海電気鉄道_和歌山大学前",
        "伊豆箱根鉄道_富士フィルム前": "伊豆箱根鉄道_富士フイルム前",
        "叡山電鉄_宝ケ池": "叡山電鉄_宝ヶ池",
        "東海旅客鉄道_各務ヶ原": "東海旅客鉄道_各務ケ原",
        # 神戸高速線
        "神戸高速鉄道_花隈": "阪急電鉄_花隈",
        "神戸高速鉄道_元町": "阪神電気鉄道_元町",
        "神戸高速鉄道_高速神戸": "阪急電鉄_高速神戸",
        "神戸高速鉄道_高速長田": "阪神電気鉄道_高速長田",
        "神戸高速鉄道_新開地": "阪急電鉄_新開地",
        "神戸高速鉄道_神戸三宮": "阪急電鉄_神戸三宮",
        "神戸高速鉄道_西元町": "阪神電気鉄道_西元町",
        "神戸高速鉄道_西代": "阪神電気鉄道_西代",
        "神戸高速鉄道_大開": "阪神電気鉄道_大開",
        "神戸高速鉄道_湊川": "神戸電鉄_湊川",
        # 西日本旅客鉄道
        "西日本旅客鉄道_ＪＲ総持寺": "西日本旅客鉄道_JR総持寺",
        "西日本旅客鉄道_ＪＲ河内永和": "西日本旅客鉄道_JR河内永和",
        "西日本旅客鉄道_ＪＲ淡路": "西日本旅客鉄道_JR淡路",
        "西日本旅客鉄道_ＪＲ野江": "西日本旅客鉄道_JR野江",
        "西日本旅客鉄道_ＪＲ俊徳道": "西日本旅客鉄道_JR俊徳道",
        "西日本旅客鉄道_ＪＲ長瀬": "西日本旅客鉄道_JR長瀬",
        "西日本旅客鉄道_ＪＲ藤森": "西日本旅客鉄道_JR藤森",
        "西日本旅客鉄道_ＪＲ小倉": "西日本旅客鉄道_JR小倉",
        "西日本旅客鉄道_ＪＲ三山木": "西日本旅客鉄道_JR三山木",
        "西日本旅客鉄道_ＪＲ五位堂": "西日本旅客鉄道_JR五位堂",
        # 京浜急行電鉄
        "京浜急行電鉄_ＹＲＰ野比": "京浜急行電鉄_YRP野比",
        # 神戸新交通
        "神戸新交通_アイランドセンター（ファッションマート前）": "神戸新交通_アイランドセンター",
        "神戸新交通_医療センター（市民病院前）": "神戸新交通_医療センター",
        "神戸新交通_市民広場（コンベンションセンター）": "神戸新交通_市民広場",
        "神戸新交通_みなとじま（キャンパス前）": "神戸新交通_みなとじま",
        "神戸新交通_南公園（IKEA前）": "神戸新交通_南公園",
        "神戸新交通_中埠頭（ジーベックホール前）": "神戸新交通_中埠頭",
        "神戸新交通_南魚崎（酒蔵の道）": "神戸新交通_南魚崎",
        # 名古屋鉄道
        "名古屋鉄道_須ケ口": "名古屋鉄道_須ヶ口",
        "名古屋鉄道_三好ケ丘": "名古屋鉄道_三好ヶ丘",
        "名古屋鉄道_巽ケ丘": "名古屋鉄道_巽ヶ丘",
        "名古屋鉄道_尼ケ坂": "名古屋鉄道_尼ヶ坂",
        "名古屋鉄道_苧ケ瀬": "名古屋鉄道_苧ヶ瀬",
    }

    # 駅名
    dict_station_replace = {
        "羽田空港第１・第２ターミナル": "羽田空港第1・第2ターミナル",
        "羽田空港第１ターミナル": "羽田空港第1ターミナル",
        "羽田空港第２ターミナル": "羽田空港第2ターミナル",
        "羽田空港第３ターミナル": "羽田空港第3ターミナル",
        "四ッ谷": "四ツ谷",
        "市ケ谷": "市ヶ谷",
        "なかもず": "中百舌鳥",
        "空港第２ビル": "空港第2ビル"
    }

    print(len(data))
    for i in range(len(data)):
        # 入場駅の座標を取得
        # e_station = data[i][0] + "_" + data[i][1] + "_" + data[i][2]
        e_station = data[i][0] + "_" + data[i][2]
        e_lat = ''
        e_lng = ''

        #　事業者名読み替え
        if data[i][0] in dict_jigyosya_replace:
            e_station = dict_jigyosya_replace[data[i][0]] + "_" + data[i][2]

        # 事業者名+駅名読み替え
        if e_station in dict_jigyosya_station_replace:
            e_station = dict_jigyosya_station_replace[e_station]

        # 駅名読み替え
        if data[i][2] in dict_station_replace:
            e_station = data[i][0] + "_" + dict_station_replace[data[i][2]]

        # 入場駅の座標を取得
        if e_station in dict_coordinate:
            res_e_coordinate = dict_coordinate[e_station]
            res_e_latlng = res_e_coordinate.split('_')
            e_lat = res_e_latlng[0]
            e_lng = res_e_latlng[1]

        # 出場駅の座標を取得
        # d_station = data[i][3] + "_" + data[i][4] + "_" + data[i][5]
        d_station = data[i][3] + "_" + data[i][5]
        d_lat = ''
        d_lng = ''

        #　事業者名読み替え
        if data[i][3] in dict_jigyosya_replace:
            d_station = dict_jigyosya_replace[data[i][3]] + "_" + data[i][5]

        # 事業者名+駅名読み替え
        if d_station in dict_jigyosya_station_replace:
            d_station = dict_jigyosya_station_replace[d_station]

        # 駅名読み替え
        if data[i][5] in dict_station_replace:
            d_station = data[i][3] + "_" + dict_station_replace[data[i][5]]

        # 出場駅の座標を取得
        if d_station in dict_coordinate:
            res_d_coordinate = dict_coordinate[d_station]
            res_d_latlng = res_d_coordinate.split('_')
            d_lat = res_d_latlng[0]
            d_lng = res_d_latlng[1]

        # 出力CSVファイルに書き込む
        csvfile_writer.writerow({
            '入場事業者名': data[i][0],
            '入場路線名': data[i][1],
            '入場駅名': data[i][2],
            '入場駅_緯度': e_lat,
            '入場駅_経度': e_lng,
            '出場事業者名': data[i][3],
            '出場路線名': data[i][4],
            '出場駅名': data[i][5],
            '出場駅_緯度': d_lat,
            '出場駅_経度': d_lng,
            '件数': data[i][6]
        })

    print(u'処理終了')
