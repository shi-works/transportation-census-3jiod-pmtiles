# -*- coding: utf-8 -*-
import csv
import pandas as pd

# 出力WKTファイルオープン
output_csvfile = "./out/202112_2_3jiod_od_pattern_count_add_coordinate.wkt"
with open(output_csvfile, 'a', encoding='utf-8') as f:
    # ヘッダー行出力
    fieldnames = ['geom', '入場事業者名', '入場路線名', '入場駅名',
                  '出場事業者名', '出場路線名', '出場駅名', '件数']
    csvfile_writer = csv.DictWriter(
        f, fieldnames=fieldnames, lineterminator='\n')
    csvfile_writer.writeheader()

    # CSVファイルをリストに格納
    data = pd.read_csv(
        "./out/202112_2_3jiod_od_pattern_count_add_coordinate.csv").values.tolist()

    for i in range(len(data)):
        e_lnglat = str(data[i][4]) + " " + str(data[i][3])
        d_lnglat = str(data[i][9]) + " " + str(data[i][8])
        geom = "LINESTRING(" + e_lnglat + "," + d_lnglat + ")"
        # 出力CSVファイルに書き込む
        csvfile_writer.writerow({
            'geom': geom,
            '入場事業者名': data[i][0],
            '入場路線名': data[i][1],
            '入場駅名': data[i][2],
            '出場事業者名': data[i][5],
            '出場路線名': data[i][6],
            '出場駅名': data[i][7],
            '件数': data[i][10]
        })

print(u'処理終了')
