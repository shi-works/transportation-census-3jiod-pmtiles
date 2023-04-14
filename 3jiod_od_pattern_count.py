import os
import sys
import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path


def get_all_files(input_directory, file_extension):
    # 再帰的に指定フォルダ内の全ファイルを取得する
    return list(Path(input_directory).rglob(f'*{file_extension}'))


def process_files(input_directory, output_directory, file_extension, include_header):
    # 開始時刻を記録
    start_time = datetime.now()

    # 対象フォルダ内のすべてのファイルを取得
    all_files = get_all_files(input_directory, file_extension)
    all_files.sort()

    # 各ファイルのパスをログファイルに書き出す
    with open(os.path.join(output_directory, 'log.csv'), mode='w', newline='', encoding='shift-jis') as log_file:
        log_writer = csv.writer(log_file)
        log_writer.writerow(['読み込みファイル'])

        for file_path in all_files:
            log_writer.writerow([str(file_path)])

    # 重複データを格納する辞書を初期化
    duplicates = defaultdict(int)

    # 各ファイルを処理
    for file_path in all_files:
        with open(file_path, mode='r', newline='', encoding='shift-jis') as file:
            reader = csv.reader(file)

            # ヘッダー行を読み飛ばす場合
            if include_header:
                next(reader, None)

            # 各行を処理
            for row in reader:
                tr_count = len(row) // 17

                # 各駅データを処理するために、tr_count回ループ
                for i in range(tr_count):
                    station = '_'.join(
                        row[3 + 17 * i: 6 + 17 * i] + row[10 + 17 * i: 13 + 17 * i])
                    # print(station)
                    duplicates[station] += 1

        print("入力済みファイル: " + str(file_path))

    # 重複データを出力ファイルに書き出す
    with open(os.path.join(output_directory, '3jiod_od_pattern_count.csv'), mode='w', newline='', encoding='shift-jis') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(['入場事業者名', '入場路線名', '入場駅名',
                        '出場事業者名', '出場路線名', '出場駅名', '件数'])

        for key, value in duplicates.items():
            if value > 1 and key != '_____':
                writer.writerow(key.split('_') + [value - 1])

    # 終了時刻を記録し、所要時間を計算
    end_time = datetime.now()
    elapsed_time = (end_time - start_time).total_seconds()

    # 結果を表示
    print(
        f"正常に終了しました\n\n開始時刻： {start_time}\n終了時刻： {end_time}\n所要時間： {elapsed_time / 60:.2f}分")


if __name__ == '__main__':
    input_directory = './202112_2'  # 入力ディレクトリを指定
    output_directory = './out/202112_2'  # 出力ディレクトリを指定
    file_extension = '.csv'  # 読み込むファイルの拡張子を指定
    include_header = True  # ヘッダー行を読み飛ばす場合はTrue、そうでない場合はFalse

    # process_files関数を呼び出して処理を実行
    process_files(input_directory, output_directory,
                  file_extension, include_header)
