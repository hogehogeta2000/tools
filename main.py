import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta
import uuid

# 日本語対応のFakerを初期化
fake = Faker(['ja_JP'])

# プロセス定義
PROCESSES = {
    'housing_loan': {
        'name': '住宅ローン審査',
        'steps': [
            '事前相談受付', '仮審査申込受付', '必要書類確認', '信用情報照会',
            '物件評価依頼', '物件評価完了', '本審査開始', '所得確認',
            '担保評価', '保証会社審査', '金利条件提示', '契約条件合意',
            '契約書作成', '契約締結', 'ローン実行'
        ]
    },
    'corporate_account': {
        'name': '法人口座開設',
        'steps': [
            '開設申込受付', '必要書類確認', '法人登記確認', '実質的支配者確認',
            '事業内容審査', 'マネロン・テロ資金供与対策確認', '信用情報照会',
            '口座開設可否判定', '印鑑登録', 'キャッシュカード発行',
            'インターネットバンキング設定', '開設完了通知'
        ]
    },
    'investment_sales': {
        'name': '投資信託販売',
        'steps': [
            '投資相談受付', '顧客属性確認', 'リスク許容度診断', '商品説明',
            '目論見書交付', '適合性確認', '意向確認', '注文受付',
            '本人確認', '資金確認', '約定処理', '受益証券発行',
            '取引報告書作成', '顧客通知'
        ]
    },
    'fx_trading': {
        'name': '外国為替取引',
        'steps': [
            '取引申込受付', '取引条件確認', '信用限度額確認', 'レート提示',
            '顧客承認', '取引約定', 'ポジション管理', 'リスク管理確認',
            '決済指示', '決済処理', '外貨受払', '取引明細作成',
            '顧客報告'
        ]
    },
    'personal_loan': {
        'name': '個人融資審査',
        'steps': [
            '融資申込受付', '申込書類確認', '本人確認', '所得証明確認',
            '信用情報照会', '勤務先確認', '返済能力審査', '担保・保証人確認',
            '融資条件検討', '審査委員会', '融資可否決定', '契約条件提示',
            '契約書作成', '契約締結', '融資実行'
        ]
    }
}

# データ生成関数
def generate_process_data(num_cases=500):
    """プロセスマイニング用のデータを生成"""
    
    all_data = []
    case_id_counter = 1
    
    for process_key, process_info in PROCESSES.items():
        process_name = process_info['name']
        steps = process_info['steps']
        
        # 各プロセスごとに案件を生成
        cases_for_this_process = num_cases // len(PROCESSES)
        
        for case_num in range(cases_for_this_process):
            case_id = f"CASE_{case_id_counter:06d}"
            case_id_counter += 1
            
            # 開始日時をランダムに設定（過去6ヶ月以内）
            start_date = fake.date_time_between(start_date='-6M', end_date='now')
            current_datetime = start_date
            
            # 顧客情報
            customer_id = f"CUST_{fake.random_int(min=100000, max=999999)}"
            customer_name = fake.name()
            
            # プロセスの進行パターンを決定
            completion_rate = random.random()
            
            if completion_rate < 0.7:  # 70%は正常完了
                steps_to_process = steps
                status = '完了'
            elif completion_rate < 0.85:  # 15%は途中で中断
                steps_to_process = steps[:random.randint(3, len(steps)-2)]
                status = '中断'
            else:  # 15%は進行中
                steps_to_process = steps[:random.randint(2, len(steps)-1)]
                status = '進行中'
            
            # 各ステップの処理時間とパフォーマンス設定
            for i, step in enumerate(steps_to_process):
                
                # ステップごとの処理時間（分）- ボトルネックを意図的に作成
                if '審査' in step or '確認' in step:
                    # 審査・確認系は時間がかかる傾向
                    base_duration = random.randint(60, 480)  # 1-8時間
                    if random.random() < 0.2:  # 20%の確率で大幅遅延
                        base_duration *= random.randint(2, 5)
                elif '書類' in step or '登録' in step:
                    base_duration = random.randint(15, 120)  # 15分-2時間
                else:
                    base_duration = random.randint(5, 60)    # 5分-1時間
                
                # 処理者（担当部署・担当者）
                departments = ['営業部', '審査部', '事務部', 'システム部', '法務部']
                processor = f"{random.choice(departments)}_{fake.last_name()}"
                
                # エラー・やり直しの発生
                has_error = random.random() < 0.1  # 10%の確率でエラー
                if has_error:
                    base_duration *= random.randint(2, 3)
                    error_reason = random.choice([
                        '書類不備', '情報不足', 'システムエラー', 
                        '承認待ち', '顧客連絡待ち'
                    ])
                else:
                    error_reason = None
                
                # 開始・終了時刻の計算
                step_start = current_datetime
                step_end = step_start + timedelta(minutes=base_duration)
                
                # 営業時間外は翌営業日に持ち越し
                if step_end.hour >= 18 or step_end.weekday() >= 5:
                    days_to_add = 1
                    if step_end.weekday() >= 5:  # 土日
                        days_to_add = 7 - step_end.weekday() + 1
                    step_end = step_end.replace(hour=9, minute=0) + timedelta(days=days_to_add)
                
                current_datetime = step_end
                
                # データレコード作成
                record = {
                    'case_id': case_id,
                    'process_name': process_name,
                    'process_type': process_key,
                    'step_sequence': i + 1,
                    'step_name': step,
                    'customer_id': customer_id,
                    'customer_name': customer_name,
                    'start_datetime': step_start,
                    'end_datetime': step_end,
                    'duration_minutes': base_duration,
                    'processor': processor,
                    'status': '完了' if i < len(steps_to_process) - 1 or status == '完了' else status,
                    'has_error': has_error,
                    'error_reason': error_reason,
                    'case_status': status
                }
                
                all_data.append(record)
    
    return pd.DataFrame(all_data)

# メインデータ生成
print("プロセスマイニング デモデータを生成中...")
df = generate_process_data(1000)  # 1000件のケースを生成

# データの基本統計
print(f"\n=== データ概要 ===")
print(f"総レコード数: {len(df):,}")
print(f"ケース数: {df['case_id'].nunique():,}")
print(f"プロセス種類: {df['process_name'].nunique()}")

print(f"\n=== プロセス別統計 ===")
process_stats = df.groupby('process_name').agg({
    'case_id': 'nunique',
    'duration_minutes': 'mean',
    'has_error': 'mean'
}).round(2)
process_stats.columns = ['ケース数', '平均処理時間(分)', 'エラー率']
print(process_stats)

print(f"\n=== ボトルネック分析（平均処理時間上位10ステップ） ===")
bottleneck_analysis = df.groupby(['process_name', 'step_name'])['duration_minutes'].mean().sort_values(ascending=False).head(10)
for (process, step), duration in bottleneck_analysis.items():
    print(f"{process} - {step}: {duration:.1f}分")

# CSVファイル出力
output_file = 'process_mining_demo_data.csv'
df.to_csv(output_file, index=False, encoding='utf-8-sig')
print(f"\n=== ファイル出力 ===")
print(f"データファイルを出力しました: {output_file}")

# Power Platform用のサンプルクエリも生成
print(f"\n=== Power BI用 DAX サンプル ===")
print("""
-- 平均処理時間（プロセス別）
平均処理時間 = AVERAGE('ProcessData'[duration_minutes])

-- ボトルネックステップ特定
ボトルネック率 = 
DIVIDE(
    CALCULATE(COUNT('ProcessData'[case_id]), 'ProcessData'[duration_minutes] > 240),
    COUNT('ProcessData'[case_id])
)

-- プロセス完了率
完了率 = 
DIVIDE(
    CALCULATE(COUNT('ProcessData'[case_id]), 'ProcessData'[case_status] = "完了"),
    COUNT('ProcessData'[case_id])
)
""")

print(f"\n=== Dataverse エンティティ構造提案 ===")
print("""
主要エンティティ:
1. ProcessCase (プロセスケース)
   - case_id, customer_id, process_type, status, start_date, end_date

2. ProcessStep (プロセスステップ)
   - step_id, case_id, step_name, sequence, start_time, end_time, processor

3. ProcessError (プロセスエラー)
   - error_id, step_id, error_type, error_reason, resolution_time

4. ProcessDefinition (プロセス定義)
   - process_id, process_name, step_definitions
""")

print("デモデータ生成が完了しました！")
