# transportation_census_3jiod_pmtiles

## データの加工
### 3jiod_od_pattern_count.py
- 3次ODデータのマージ及びODパターン数の集計を行うプログラムです。
#### 使用データ
- 3次ODデータ（2021年12月某日1日目）及び3次ODデータ（2021年12月某日2日目）
- `https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/+transportation-census/3jiod/3jiod.7z`,966.0MB
#### 出力結果
- 2021年12月某日1日目
- `https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/+transportation-census/3jiod/01_3jiod_od_pattern_count/out/202112_1/202112_1_3jiod_od_pattern_count.csv`,60.6MB
- 2021年12月某日2日目
- `https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/+transportation-census/3jiod/01_3jiod_od_pattern_count/out/202112_2/202112_2_3jiod_od_pattern_count.csv`,61.9MB

### csvfile-add-coordinate.py
- 3次ODデータに国土数値情報の鉄道データの駅座標を付与するプログラムです。
- なお、駅座標データは、国土数値情報の鉄道データのラインデータを重心に変換したデータになります。
#### 使用データ
- 国土数値情報の鉄道データ

#### 出力結果
