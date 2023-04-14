# transportation-census-3jiod-pmtiles
- 本データは、政府統計窓口（e-stat）にて公開されている、[第13回大都市交通センサスの3次ODデータ（2021年12月某日1日目及び2021年12月某日2日目）](https://www.e-stat.go.jp/stat-search/files?page=1&toukei=00600020&tstat=000001103355)の入出場駅間トリップ数（以下、3次OD集計データ）を集計するとともに、3次OD集計データを[tippecanoe](https://github.com/felt/tippecanoe)で[PMTiles形式](https://github.com/protomaps/PMTiles)に変換したデータになります。
- オープンソースソフトウェアで構築

## デモサイト（MapLibre GL JS）
- 3次ODデータ集計（2021年12月某日2日目）
- https://web-map-maplibre.s3.ap-northeast-1.amazonaws.com/transportation-census-map/index.html
- サンプル画像
![image](https://user-images.githubusercontent.com/71203808/232016307-b0e54eb0-0108-4e31-9ee9-4ef519ba187f.png)

## データの加工
### 3jiod_od_pattern_count.py
- 3次ODデータのマージ及び入出場駅間トリップ数の集計を行うプログラムです。
#### 使用データ
- 3次ODデータ（2021年12月某日1日目）及び3次ODデータ（2021年12月某日2日目）
- `https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/3jiod/3jiod.7z`,966.0MB
#### 出力結果
- 2021年12月某日1日目
- `https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/3jiod/01_3jiod_od_pattern_count/out/202112_1/202112_1_3jiod_od_pattern_count.csv`,60.6MB
- 2021年12月某日2日目
- `https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/3jiod/01_3jiod_od_pattern_count/out/202112_2/202112_2_3jiod_od_pattern_count.csv`,61.9MB

### csvfile-add-coordinate.py
- 3次OD集計データに国土数値情報の鉄道データの駅座標を付与するプログラムです。
- なお、駅座標データは、国土数値情報の鉄道データのラインデータを重心に変換したデータになります。
#### 使用データ
- 国土数値情報の鉄道データ（重心）
- `https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/3jiod/02_3jiod_od_pattern_count_add_coordinate/data/N02-21_Station_Centroid.csv`,738.0KB
- ODパターン数の集計結果
- 2021年12月某日1日目
- `https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/3jiod/01_3jiod_od_pattern_count/out/202112_1/202112_1_3jiod_od_pattern_count.csv`,60.6MB
- 2021年12月某日2日目
- `https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/3jiod/01_3jiod_od_pattern_count/out/202112_2/202112_2_3jiod_od_pattern_count.csv`,61.9MB
#### 出力結果
- 2021年12月某日1日目
- `https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/3jiod/02_3jiod_od_pattern_count_add_coordinate/out/202112_1_3jiod_od_pattern_count_add_coordinate.csv`,134.0MB
- 2021年12月某日2日目
- `https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/3jiod/02_3jiod_od_pattern_count_add_coordinate/out/202112_2_3jiod_od_pattern_count_add_coordinate.csv`,136.7MB

### LineStringWKTCre.py
- 駅座標を付与した、3次OD集計データについて、入場駅座標及び出場駅座標をもとに、WKT形式（LINESTRING）のデータに変換するプログラムです。
#### 使用データ
- 2021年12月某日1日目
- `https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/3jiod/02_3jiod_od_pattern_count_add_coordinate/out/202112_1_3jiod_od_pattern_count_add_coordinate.csv`,134.0MB
- 2021年12月某日2日目
- `https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/3jiod/02_3jiod_od_pattern_count_add_coordinate/out/202112_2_3jiod_od_pattern_count_add_coordinate.csv`,136.7MB
#### 出力結果
- 2021年12月某日1日目
- `https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/3jiod/02_3jiod_od_pattern_count_add_coordinate/out/202112_1_3jiod_od_pattern_count_add_coordinate.wkt`,126.7MB
- 2021年12月某日2日目
- `https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/3jiod/02_3jiod_od_pattern_count_add_coordinate/out/202112_2_3jiod_od_pattern_count_add_coordinate.wkt`,129.3MB

### GeoJSON形式
- WKT形式（LINESTRING）の3次OD集計データをGeoJSON形式に変換したデータです。
- 2021年12月某日1日目
- `https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/3jiod/02_3jiod_od_pattern_count_add_coordinate/out/202112_1_3jiod.geojson`,380.3MB
- 2021年12月某日2日目
- `https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/3jiod/02_3jiod_od_pattern_count_add_coordinate/out/202112_2_3jiod.geojson`,388.0MB

### PMTiles形式（ベクトルタイル）
- GeoJSON形式の3次OD集計データを[tippecanoe](https://github.com/felt/tippecanoe)で[PMTiles形式](https://github.com/protomaps/PMTiles)に変換したデータです。
- 2021年12月某日1日目
- `https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/3jiod/02_3jiod_od_pattern_count_add_coordinate/out/202112_1_3jiod.pmtiles`,660.7MB
- 2021年12月某日2日目
- `https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/3jiod/02_3jiod_od_pattern_count_add_coordinate/out/202112_2_3jiod.pmtiles`,675.0MB

## ライセンス
本データセット（使用データ及び出力結果）は[CC-BY-4.0](https://github.com/shi-works/traffic-accident-pmtiles/blob/main/LICENSE)で提供されます。使用の際には本レポジトリへのリンクを提示してください。

また、本データセットは、第13回大都市交通センサスの3次ODデータを加工して作成したものです。本データセットの使用・加工にあたっては、[国土交通省のリンク・著作権・免責事項](https://www.mlit.go.jp/link.html)を必ずご確認ください。

## 免責事項
利用者が当該データを用いて行う一切の行為について何ら責任を負うものではありません。
