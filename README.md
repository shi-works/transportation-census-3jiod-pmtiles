# transportation-census-3jiod-pmtiles
- 本データは、政府統計窓口（e-stat）にて公開されている、[第13回大都市交通センサスの3次ODデータ（2021年12月某日1日目及び2021年12月某日2日目）](https://www.e-stat.go.jp/stat-search/files?page=1&toukei=00600020&tstat=000001103355)の入出場駅間トリップ数を集計するとともに、集計データを[tippecanoe](https://github.com/felt/tippecanoe)で[PMTiles形式](https://github.com/protomaps/PMTiles)に変換したデータになります。
- オープンソースソフトウェアで構築

## デモサイト（MapLibre GL JS）
- 3次ODデータ（2021年12月某日2日目）
- https://web-map-maplibre.s3.ap-northeast-1.amazonaws.com/transportation-census-map/index.html
- サンプル画像
![image](https://user-images.githubusercontent.com/71203808/232016307-b0e54eb0-0108-4e31-9ee9-4ef519ba187f.png)

## データの加工
### 3jiod_od_pattern_count.py
- 3次ODデータのマージ及びODパターン数の集計を行うプログラムです。
#### 使用データ
- 3次ODデータ（2021年12月某日1日目）及び3次ODデータ（2021年12月某日2日目）
- `https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/3jiod/3jiod.7z`,966.0MB
#### 出力結果
- 2021年12月某日1日目
- `https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/3jiod/01_3jiod_od_pattern_count/out/202112_1/202112_1_3jiod_od_pattern_count.csv`,60.6MB
- 2021年12月某日2日目
- `https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/3jiod/01_3jiod_od_pattern_count/out/202112_2/202112_2_3jiod_od_pattern_count.csv`,61.9MB

### csvfile-add-coordinate.py
- 3次ODデータに国土数値情報の鉄道データの駅座標を付与するプログラムです。
- なお、駅座標データは、国土数値情報の鉄道データのラインデータを重心に変換したデータになります。
#### 使用データ
- 国土数値情報の鉄道データ
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
- 駅座標を付与した、3次ODデータについて、入場駅座標及び出場駅座標をもとに、WKT形式（LINESTRING）のデータに変換するプログラムです。
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

### GeoJSON
- WKT形式（LINESTRING）の3次ODデータをGeoJSON形式に変換したデータです。
- 2021年12月某日1日目
- `https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/3jiod/02_3jiod_od_pattern_count_add_coordinate/out/202112_1_3jiod.geojson`,380.3MB
- 2021年12月某日2日目
- `https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/3jiod/02_3jiod_od_pattern_count_add_coordinate/out/202112_2_3jiod.geojson`,388.0MB

### PMTiles
- FlatGeoBuf形式の3次ODデータを[tippecanoe](https://github.com/felt/tippecanoe)で[PMTiles形式](https://github.com/protomaps/PMTiles)に変換したデータです。
- 2021年12月某日1日目
- `https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/3jiod/02_3jiod_od_pattern_count_add_coordinate/out/202112_1_3jiod.pmtiles`,660.7MB
- 2021年12月某日2日目
- `https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/3jiod/02_3jiod_od_pattern_count_add_coordinate/out/202112_2_3jiod.pmtiles`,675.0MB
