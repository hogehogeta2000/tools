import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta
import numpy as np

# 日本語対応のFakerを初期化
fake = Faker(['ja_JP'])
random.seed(42)  # 再現性のため

print("=== 金融機関プロセスマイニング サンプルデータ生成 ===\n")

# 1. ProcessDefinition（プロセス定義）- マスタデータ
print("1. ProcessDefinition（プロセス定義）を生成中...")
process_definitions = [
    {
        'processdefinitionid': 'PD-0001',
        'name': '住宅ローン審査プロセス',
        'processkey': 'HL',
        'description': '個人顧客の住宅ローン申込から融資実行までの審査プロセス',
        'processtype': 100000000,  # 審査系
        'targetdurationhours': 168,  # 1週間
        'sladurationhours': 336,     # 2週間
        'owningdepartment': '融資部',
        'isactive': True
    },
    {
        'processdefinitionid': 'PD-0002', 
        'name': '法人口座開設プロセス',
        'processkey': 'CA',
        'description': '法人顧客の新規口座開設プロセス',
        'processtype': 100000000,  # 審査系
        'targetdurationhours': 72,   # 3日
        'sladurationhours': 168,     # 1週間
        'owningdepartment': '営業部',
        'isactive': True
    },
    {
        'processdefinitionid': 'PD-0003',
        'name': '投資信託販売プロセス', 
        'processkey': 'IT',
        'description': '個人顧客への投資信託商品販売プロセス',
        'processtype': 100000001,  # 販売系
        'targetdurationhours': 24,   # 1日
        'sladurationhours': 72,      # 3日
        'owningdepartment': '商品部',
        'isactive': True
    },
    {
        'processdefinitionid': 'PD-0004',
        'name': '外国為替取引プロセス',
        'processkey': 'FX', 
        'description': '法人顧客の外貨取引プロセス',
        'processtype': 100000002,  # 取引系
        'targetdurationhours': 4,    # 4時間
        'sladurationhours': 8,       # 8時間
        'owningdepartment': '外為部',
        'isactive': True
    },
    {
        'processdefinitionid': 'PD-0005',
        'name': '個人融資審査プロセス',
        'processkey': 'PL',
        'description': '個人顧客への各種融資審査プロセス', 
        'processtype': 100000000,  # 審査系
        'targetdurationhours': 120,  # 5日
        'sladurationhours': 240,     # 10日
        'owningdepartment': '融資部',
        'isactive': True
    }
]

df_process_def = pd.DataFrame(process_definitions)
df_process_def.to_csv('process_definition.csv', index=False, encoding='utf-8-sig')
print(f"ProcessDefinition: {len(df_process_def)}件")

# 2. ActivityDefinition（アクティビティ定義）- マスタデータ
print("2. ActivityDefinition（アクティビティ定義）を生成中...")
activity_definitions = [
    # 住宅ローン審査プロセス (HL)
    {'activitydefinitionid': 'AD-0001', 'name': '事前相談受付', 'activitykey': 'HL_001', 'processdefinition': 'PD-0001', 'activitysequence': 1, 'activitytype': 100000000, 'responsibledepartment': '営業店', 'standarddurationminutes': 30, 'sladurationminutes': 60, 'ismandatory': True, 'canparallel': False, 'automationlevel': 100000000, 'skillrequired': '融資相談'},
    {'activitydefinitionid': 'AD-0002', 'name': '仮審査申込受付', 'activitykey': 'HL_002', 'processdefinition': 'PD-0001', 'activitysequence': 2, 'activitytype': 100000000, 'responsibledepartment': '営業店', 'standarddurationminutes': 45, 'sladurationminutes': 90, 'ismandatory': True, 'canparallel': False, 'automationlevel': 100000000, 'skillrequired': '申込手続き'},
    {'activitydefinitionid': 'AD-0003', 'name': '信用情報照会', 'activitykey': 'HL_003', 'processdefinition': 'PD-0001', 'activitysequence': 3, 'activitytype': 100000001, 'responsibledepartment': '審査部', 'standarddurationminutes': 15, 'sladurationminutes': 30, 'ismandatory': True, 'canparallel': True, 'automationlevel': 100000001, 'skillrequired': '信用調査'},
    {'activitydefinitionid': 'AD-0004', 'name': '所得確認', 'activitykey': 'HL_004', 'processdefinition': 'PD-0001', 'activitysequence': 4, 'activitytype': 100000001, 'responsibledepartment': '審査部', 'standarddurationminutes': 60, 'sladurationminutes': 120, 'ismandatory': True, 'canparallel': True, 'automationlevel': 100000000, 'skillrequired': '所得審査'},
    {'activitydefinitionid': 'AD-0005', 'name': '物件評価依頼', 'activitykey': 'HL_005', 'processdefinition': 'PD-0001', 'activitysequence': 5, 'activitytype': 100000003, 'responsibledepartment': '融資部', 'standarddurationminutes': 30, 'sladurationminutes': 60, 'ismandatory': True, 'canparallel': True, 'automationlevel': 100000000, 'skillrequired': '担保評価'},
    {'activitydefinitionid': 'AD-0006', 'name': '物件評価完了', 'activitykey': 'HL_006', 'processdefinition': 'PD-0001', 'activitysequence': 6, 'activitytype': 100000003, 'responsibledepartment': '外部業者', 'standarddurationminutes': 4320, 'sladurationminutes': 7200, 'ismandatory': True, 'canparallel': False, 'automationlevel': 100000000, 'skillrequired': '不動産鑑定'},
    {'activitydefinitionid': 'AD-0007', 'name': '仮審査結果通知', 'activitykey': 'HL_007', 'processdefinition': 'PD-0001', 'activitysequence': 7, 'activitytype': 100000005, 'responsibledepartment': '営業店', 'standarddurationminutes': 30, 'sladurationminutes': 60, 'ismandatory': True, 'canparallel': False, 'automationlevel': 100000000, 'skillrequired': '顧客対応'},
    {'activitydefinitionid': 'AD-0008', 'name': '本審査申込受付', 'activitykey': 'HL_008', 'processdefinition': 'PD-0001', 'activitysequence': 8, 'activitytype': 100000000, 'responsibledepartment': '営業店', 'standarddurationminutes': 60, 'sladurationminutes': 120, 'ismandatory': True, 'canparallel': False, 'automationlevel': 100000000, 'skillrequired': '申込手続き'},
    {'activitydefinitionid': 'AD-0009', 'name': '本審査実施', 'activitykey': 'HL_009', 'processdefinition': 'PD-0001', 'activitysequence': 9, 'activitytype': 100000002, 'responsibledepartment': '審査部', 'standarddurationminutes': 2880, 'sladurationminutes': 4320, 'ismandatory': True, 'canparallel': False, 'automationlevel': 100000000, 'skillrequired': '融資審査'},
    {'activitydefinitionid': 'AD-0010', 'name': '契約締結', 'activitykey': 'HL_010', 'processdefinition': 'PD-0001', 'activitysequence': 10, 'activitytype': 100000003, 'responsibledepartment': '営業店', 'standarddurationminutes': 90, 'sladurationminutes': 180, 'ismandatory': True, 'canparallel': False, 'automationlevel': 100000000, 'skillrequired': '契約手続き'},

    # 法人口座開設プロセス (CA)
    {'activitydefinitionid': 'AD-0011', 'name': '開設申込受付', 'activitykey': 'CA_001', 'processdefinition': 'PD-0002', 'activitysequence': 1, 'activitytype': 100000000, 'responsibledepartment': '営業店', 'standarddurationminutes': 45, 'sladurationminutes': 90, 'ismandatory': True, 'canparallel': False, 'automationlevel': 100000000, 'skillrequired': '口座開設'},
    {'activitydefinitionid': 'AD-0012', 'name': '法人登記確認', 'activitykey': 'CA_002', 'processdefinition': 'PD-0002', 'activitysequence': 2, 'activitytype': 100000001, 'responsibledepartment': '事務部', 'standarddurationminutes': 30, 'sladurationminutes': 60, 'ismandatory': True, 'canparallel': True, 'automationlevel': 100000001, 'skillrequired': '登記確認'},
    {'activitydefinitionid': 'AD-0013', 'name': '実質的支配者確認', 'activitykey': 'CA_003', 'processdefinition': 'PD-0002', 'activitysequence': 3, 'activitytype': 100000001, 'responsibledepartment': 'コンプライアンス部', 'standarddurationminutes': 60, 'sladurationminutes': 120, 'ismandatory': True, 'canparallel': True, 'automationlevel': 100000000, 'skillrequired': 'KYC'},
    {'activitydefinitionid': 'AD-0014', 'name': 'マネロン確認', 'activitykey': 'CA_004', 'processdefinition': 'PD-0002', 'activitysequence': 4, 'activitytype': 100000001, 'responsibledepartment': 'コンプライアンス部', 'standarddurationminutes': 90, 'sladurationminutes': 180, 'ismandatory': True, 'canparallel': True, 'automationlevel': 100000001, 'skillrequired': 'AML'},
    {'activitydefinitionid': 'AD-0015', 'name': '反社チェック', 'activitykey': 'CA_005', 'processdefinition': 'PD-0002', 'activitysequence': 5, 'activitytype': 100000001, 'responsibledepartment': 'コンプライアンス部', 'standarddurationminutes': 60, 'sladurationminutes': 120, 'ismandatory': True, 'canparallel': True, 'automationlevel': 100000001, 'skillrequired': '反社チェック'},
    {'activitydefinitionid': 'AD-0016', 'name': '開設可否判定', 'activitykey': 'CA_006', 'processdefinition': 'PD-0002', 'activitysequence': 6, 'activitytype': 100000002, 'responsibledepartment': '審査部', 'standarddurationminutes': 30, 'sladurationminutes': 60, 'ismandatory': True, 'canparallel': False, 'automationlevel': 100000000, 'skillrequired': '総合判断'},
    {'activitydefinitionid': 'AD-0017', 'name': '口座開設処理', 'activitykey': 'CA_007', 'processdefinition': 'PD-0002', 'activitysequence': 7, 'activitytype': 100000003, 'responsibledepartment': '事務部', 'standarddurationminutes': 30, 'sladurationminutes': 60, 'ismandatory': True, 'canparallel': False, 'automationlevel': 100000001, 'skillrequired': 'システム操作'},

    # 投資信託販売プロセス (IT)
    {'activitydefinitionid': 'AD-0018', 'name': '投資相談受付', 'activitykey': 'IT_001', 'processdefinition': 'PD-0003', 'activitysequence': 1, 'activitytype': 100000000, 'responsibledepartment': '営業店', 'standarddurationminutes': 60, 'sladurationminutes': 120, 'ismandatory': True, 'canparallel': False, 'automationlevel': 100000000, 'skillrequired': '投資相談'},
    {'activitydefinitionid': 'AD-0019', 'name': 'リスク許容度診断', 'activitykey': 'IT_002', 'processdefinition': 'PD-0003', 'activitysequence': 2, 'activitytype': 100000001, 'responsibledepartment': '営業店', 'standarddurationminutes': 45, 'sladurationminutes': 90, 'ismandatory': True, 'canparallel': False, 'automationlevel': 100000000, 'skillrequired': 'リスク評価'},
    {'activitydefinitionid': 'AD-0020', 'name': '商品説明', 'activitykey': 'IT_003', 'processdefinition': 'PD-0003', 'activitysequence': 3, 'activitytype': 100000001, 'responsibledepartment': '営業店', 'standarddurationminutes': 60, 'sladurationminutes': 120, 'ismandatory': True, 'canparallel': False, 'automationlevel': 100000000, 'skillrequired': '商品知識'},
    {'activitydefinitionid': 'AD-0021', 'name': '適合性確認', 'activitykey': 'IT_004', 'processdefinition': 'PD-0003', 'activitysequence': 4, 'activitytype': 100000001, 'responsibledepartment': '営業店', 'standarddurationminutes': 30, 'sladurationminutes': 60, 'ismandatory': True, 'canparallel': False, 'automationlevel': 100000000, 'skillrequired': '適合性判断'},
    {'activitydefinitionid': 'AD-0022', 'name': '注文受付', 'activitykey': 'IT_005', 'processdefinition': 'PD-0003', 'activitysequence': 5, 'activitytype': 100000000, 'responsibledepartment': '営業店', 'standarddurationminutes': 30, 'sladurationminutes': 60, 'ismandatory': True, 'canparallel': False, 'automationlevel': 100000000, 'skillrequired': '注文処理'},
    {'activitydefinitionid': 'AD-0023', 'name': '約定処理', 'activitykey': 'IT_006', 'processdefinition': 'PD-0003', 'activitysequence': 6, 'activitytype': 100000003, 'responsibledepartment': '事務部', 'standarddurationminutes': 30, 'sladurationminutes': 60, 'ismandatory': True, 'canparallel': False, 'automationlevel': 100000001, 'skillrequired': 'システム処理'},

    # 外国為替取引プロセス (FX)  
    {'activitydefinitionid': 'AD-0024', 'name': '取引申込受付', 'activitykey': 'FX_001', 'processdefinition': 'PD-0004', 'activitysequence': 1, 'activitytype': 100000000, 'responsibledepartment': '営業店', 'standarddurationminutes': 15, 'sladurationminutes': 30, 'ismandatory': True, 'canparallel': False, 'automationlevel': 100000000, 'skillrequired': '外為知識'},
    {'activitydefinitionid': 'AD-0025', 'name': '信用限度額確認', 'activitykey': 'FX_002', 'processdefinition': 'PD-0004', 'activitysequence': 2, 'activitytype': 100000001, 'responsibledepartment': '外為部', 'standarddurationminutes': 10, 'sladurationminutes': 20, 'ismandatory': True, 'canparallel': False, 'automationlevel': 100000001, 'skillrequired': '与信管理'},
    {'activitydefinitionid': 'AD-0026', 'name': 'レート提示', 'activitykey': 'FX_003', 'processdefinition': 'PD-0004', 'activitysequence': 3, 'activitytype': 100000003, 'responsibledepartment': '外為部', 'standarddurationminutes': 5, 'sladurationminutes': 10, 'ismandatory': True, 'canparallel': False, 'automationlevel': 100000001, 'skillrequired': 'レート算定'},
    {'activitydefinitionid': 'AD-0027', 'name': '取引約定', 'activitykey': 'FX_004', 'processdefinition': 'PD-0004', 'activitysequence': 4, 'activitytype': 100000003, 'responsibledepartment': '外為部', 'standarddurationminutes': 5, 'sladurationminutes': 10, 'ismandatory': True, 'canparallel': False, 'automationlevel': 100000001, 'skillrequired': 'ディーリング'},
    {'activitydefinitionid': 'AD-0028', 'name': '決済処理', 'activitykey': 'FX_005', 'processdefinition': 'PD-0004', 'activitysequence': 5, 'activitytype': 100000003, 'responsibledepartment': '事務部', 'standarddurationminutes': 30, 'sladurationminutes': 60, 'ismandatory': True, 'canparallel': False, 'automationlevel': 100000001, 'skillrequired': '外為事務'},

    # 個人融資審査プロセス (PL)
    {'activitydefinitionid': 'AD-0029', 'name': '融資申込受付', 'activitykey': 'PL_001', 'processdefinition': 'PD-0005', 'activitysequence': 1, 'activitytype': 100000000, 'responsibledepartment': '営業店', 'standarddurationminutes': 45, 'sladurationminutes': 90, 'ismandatory': True, 'canparallel': False, 'automationlevel': 100000000, 'skillrequired': '融資相談'},
    {'activitydefinitionid': 'AD-0030', 'name': '申込書類確認', 'activitykey': 'PL_002', 'processdefinition': 'PD-0005', 'activitysequence': 2, 'activitytype': 100000001, 'responsibledepartment': '営業店', 'standarddurationminutes': 30, 'sladurationminutes': 60, 'ismandatory': True, 'canparallel': False, 'automationlevel': 100000000, 'skillrequired': '書類確認'},
    {'activitydefinitionid': 'AD-0031', 'name': '信用情報照会', 'activitykey': 'PL_003', 'processdefinition': 'PD-0005', 'activitysequence': 3, 'activitytype': 100000001, 'responsibledepartment': '審査部', 'standarddurationminutes': 15, 'sladurationminutes': 30, 'ismandatory': True, 'canparallel': True, 'automationlevel': 100000001, 'skillrequired': '信用調査'},
    {'activitydefinitionid': 'AD-0032', 'name': '所得証明確認', 'activitykey': 'PL_004', 'processdefinition': 'PD-0005', 'activitysequence': 4, 'activitytype': 100000001, 'responsibledepartment': '審査部', 'standarddurationminutes': 30, 'sladurationminutes': 60, 'ismandatory': True, 'canparallel': True, 'automationlevel': 100000000, 'skillrequired': '所得審査'},
    {'activitydefinitionid': 'AD-0033', 'name': '返済能力審査', 'activitykey': 'PL_005', 'processdefinition': 'PD-0005', 'activitysequence': 5, 'activitytype': 100000002, 'responsibledepartment': '審査部', 'standarddurationminutes': 90, 'sladurationminutes': 180, 'ismandatory': True, 'canparallel': False, 'automationlevel': 100000000, 'skillrequired': '財務分析'},
    {'activitydefinitionid': 'AD-0034', 'name': '融資可否決定', 'activitykey': 'PL_006', 'processdefinition': 'PD-0005', 'activitysequence': 6, 'activitytype': 100000002, 'responsibledepartment': '審査部', 'standarddurationminutes': 15, 'sladurationminutes': 30, 'ismandatory': True, 'canparallel': False, 'automationlevel': 100000000, 'skillrequired': '審査判定'},
    {'activitydefinitionid': 'AD-0035', 'name': '契約締結', 'activitykey': 'PL_007', 'processdefinition': 'PD-0005', 'activitysequence': 7, 'activitytype': 100000003, 'responsibledepartment': '営業店', 'standarddurationminutes': 60, 'sladurationminutes': 120, 'ismandatory': True, 'canparallel': False, 'automationlevel': 100000000, 'skillrequired': '契約手続き'},
]

df_activity_def = pd.DataFrame(activity_definitions)
df_activity_def.to_csv('activity_definition.csv', index=False, encoding='utf-8-sig')
print(f"ActivityDefinition: {len(df_activity_def)}件")

# 3. Customer（顧客）- ディメンションデータ
print("3. Customer（顧客）を生成中...")
customers = []
branches = ['新宿支店', '渋谷支店', '池袋支店', '品川支店', '銀座支店', '丸の内支店', '新橋支店', '上野支店']

for i in range(20):
    customer_type = random.choice([100000000, 100000001])  # 個人・法人
    customers.append({
        'customerid': f"CUST-{i+1:06d}",
        'name': fake.company() if customer_type == 100000001 else fake.name(),
        'customerkey': f"CUST_{i+100001}",
        'customertype': customer_type,
        'registrationdate': fake.date_between(start_date='-5y', end_date='today'),
        'primarybranch': random.choice(branches),
        'contactemail': fake.email(),
        'contactphone': fake.phone_number(),
        'isactive': True
    })

df_customer = pd.DataFrame(customers)
df_customer.to_csv('customer.csv', index=False, encoding='utf-8-sig')
print(f"Customer: {len(df_customer)}件")

# 4. Resource（リソース）- ディメンションデータ
print("4. Resource（リソース）を生成中...")
departments = ['営業店', '審査部', '事務部', '外為部', '融資部', 'コンプライアンス部', '商品部']
roles = ['主任', '係長', '課長代理', '課長', '部長代理', '担当者']
resource_types = [100000000, 100000001, 100000002]  # 人、システム、外部

resources = []
for i, dept in enumerate(departments):
    # 各部署に3-5名の担当者を配置
    for j in range(random.randint(3, 5)):
        resources.append({
            'resourceid': f"RES-{len(resources)+1:04d}",
            'name': f"{fake.last_name()}{fake.first_name()}",
            'resourcekey': f"EMP_{len(resources)+1:03d}",
            'resourcetype': 100000000,  # 人
            'department': dept,
            'role': random.choice(roles),
            'experiencelevel': random.choice([100000000, 100000001, 100000002, 100000003]),
            'costperhour': random.randint(3000, 8000),
            'capacityperday': random.randint(5, 15),
            'isavailable': True
        })

# システムリソース
systems = ['融資システム', '口座管理システム', '外為システム', '投信システム', 'コンプライアンスシステム']
for sys in systems:
    resources.append({
        'resourceid': f"RES-{len(resources)+1:04d}",
        'name': sys,
        'resourcekey': f"SYS_{len(resources)+1:03d}",
        'resourcetype': 100000001,  # システム
        'department': 'システム部',
        'role': 'システム',
        'experiencelevel': None,
        'costperhour': 1000,
        'capacityperday': 100,
        'isavailable': True
    })

# 外部業者
external_vendors = ['不動産鑑定会社A', '信用情報機関', '外部監査法人']
for vendor in external_vendors:
    resources.append({
        'resourceid': f"RES-{len(resources)+1:04d}",
        'name': vendor,
        'resourcekey': f"EXT_{len(resources)+1:03d}",
        'resourcetype': 100000002,  # 外部
        'department': '外部',
        'role': '外部業者',
        'experiencelevel': 100000002,  # 上級
        'costperhour': 10000,
        'capacityperday': 5,
        'isavailable': True
    })

df_resource = pd.DataFrame(resources)
df_resource.to_csv('resource.csv', index=False, encoding='utf-8-sig')
print(f"Resource: {len(df_resource)}件")

# 5. ProcessCase（プロセスケース）- 少数のファクトデータ
print("5. ProcessCase（プロセスケース）を生成中...")
process_cases = []

for i in range(15):  # 15ケース
    process_def = random.choice(process_definitions)
    customer = random.choice(customers)
    
    start_date = fake.date_time_between(start_date='-3M', end_date='now')
    
    # プロセスの状態を決定
    status_rand = random.random()
    if status_rand < 0.6:  # 60%完了
        case_status = 100000001  # 完了
        complete_date = start_date + timedelta(hours=random.randint(24, int(process_def['sladurationhours'])))
        total_duration = int((complete_date - start_date).total_seconds() / 60)
    elif status_rand < 0.8:  # 20%進行中
        case_status = 100000000  # 進行中
        complete_date = None
        total_duration = None
    else:  # 20%中断
        case_status = 100000002  # 中断
        complete_date = start_date + timedelta(hours=random.randint(12, 48))
        total_duration = int((complete_date - start_date).total_seconds() / 60)
    
    process_cases.append({
        'processcaseid': f"CASE-{i+1:06d}",
        'name': f"{process_def['name']} - {customer['name']}",
        'casekey': f"CASE_{i+1:06d}",
        'processdefinition': process_def['processdefinitionid'],
        'customer': customer['customerid'],
        'casestatus': case_status,
        'priority': random.choice([100000000, 100000001, 100000002]),
        'caseamount': random.randint(100000, 50000000) if process_def['processkey'] in ['HL', 'PL'] else None,
        'startedat': start_date,
        'completedat': complete_date,
        'totalprocessingminutes': random.randint(120, 480) if total_duration else None,
        'totalwaitingminutes': random.randint(60, 240) if total_duration else None,
        'totaldurationminutes': total_duration,
        'initiatingbranch': customer['primarybranch'],
        'currentactivity': None,  # 後で設定
        'slabreach': total_duration > (process_def['sladurationhours'] * 60) if total_duration else False,
        'escalated': random.choice([True, False]) if case_status != 100000001 else False,
        'reworkcount': random.randint(0, 2)
    })

df_process_case = pd.DataFrame(process_cases)
df_process_case.to_csv('process_case.csv', index=False, encoding='utf-8-sig')
print(f"ProcessCase: {len(df_process_case)}件")

# 6. ActivityInstance（アクティビティインスタンス）- 50件程度のファクトデータ
print("6. ActivityInstance（アクティビティインスタンス）を生成中...")
activity_instances = []
instance_counter = 1

for case in process_cases:
    # このケースで実行するアクティビティを決定
    case_activities = [ad for ad in activity_definitions if ad['processdefinition'] == case['processdefinition']]
    
    # ケースの状態に応じて実行するアクティビティ数を決定
    if case['casestatus'] == 100000001:  # 完了
        activities_to_execute = case_activities
    elif case['casestatus'] == 100000000:  # 進行中
        activities_to_execute = case_activities[:random.randint(2, len(case_activities)-1)]
    else:  # 中断
        activities_to_execute = case_activities[:random.randint(1, max(1, len(case_activities)//2))]
    
    current_time = case['startedat']
    
    for seq, activity_def in enumerate(activities_to_execute):
        # リソースの選択（担当部署に基づく）
        available_resources = [r for r in resources if r['department'] == activity_def['responsibledepartment']]
        if available_resources:
            resource = random.choice(available_resources)
        else:
            resource = random.choice(resources)
        
        # 待機時間（前のアクティビティからの間隔）
        if seq > 0:
            waiting_minutes = random.randint(5, 120)
            current_time += timedelta(minutes=waiting_minutes)
        else:
            waiting_minutes = 0
        
        # 処理時間（標準時間の80%-200%）
        processing_minutes = int(activity_def['standarddurationminutes'] * random.uniform(0.8, 2.0))
        
        # SLA違反の判定
        sla_breached = processing_minutes > activity_def['sladurationminutes']
        
        # リワークの可能性（10%の確率）
        is_rework = random.random() < 0.1
        iteration_number = 2 if is_rework else 1
        
        start_time = current_time
        end_time = start_time + timedelta(minutes=processing_minutes)
        
        # 営業時間外の調整
        if end_time.hour >= 18 or end_time.weekday() >= 5:
            if end_time.weekday() >= 5:  # 土日
                days_to_add = 7 - end_time.weekday() + 1
            else:
                days_to_add = 1
            end_time = end_time.replace(hour=9, minute=0) + timedelta(days=days_to_add)
        
        current_time = end_time
        
        activity_instances.append({
            'activityinstanceid': f"AI-{instance_counter:07d}",
            'name': f"{case['casekey']} - {activity_def['name']} ({iteration_number})",
            'processcase': case['processcaseid'],
            'activitydefinition': activity_def['activitydefinitionid'],
            'resource': resource['resourceid'],
            'executionsequence': seq + 1,
            'iterationnumber': iteration_number,
            'startedat': start_time,
            'completedat': end_time if case['casestatus'] != 100000000 or seq < len(activities_to_execute)-1 else None,
            'processingminutes': processing_minutes,
            'waitingminutes': waiting_minutes,
            'queueminutes': random.randint(0, 30),
            'executionstatus': 100000000,  # 正常完了
            'reworkreason': random.choice([100000000, 100000001, 100000002]) if is_rework else None,
            'processingcost': (processing_minutes / 60) * resource['costperhour'] if resource['costperhour'] else 0,
            'qualityscore': random.uniform(7.0, 10.0),
            'location': case['initiatingbranch'],
            'systemused': random.choice(['融資システム', '口座管理システム', '外為システム', '投信システム']) if random.random() < 0.7 else None,
            'comments': fake.text(max_nb_chars=50) if random.random() < 0.3 else None,
            'isrework': is_rework,
            'slabreached': sla_breached
        })
        
        instance_counter += 1
        
        # 50件制限
        if len(activity_instances) >= 50:
            break
    
    if len(activity_instances) >= 50:
        break

df_activity_instance = pd.DataFrame(activity_instances)
df_activity_instance.to_csv('activity_instance.csv', index=False, encoding='utf-8-sig')
print(f"ActivityInstance: {len(df_activity_instance)}件")

# 7. ActivityTransition（アクティビティ遷移）
print("7. ActivityTransition（アクティビティ遷移）を生成中...")
transitions = []
transition_counter = 1

# ケースごとに遷移を生成
for case_id in df_activity_instance['processcase'].unique():
    case_activities = df_activity_instance[df_activity_instance['processcase'] == case_id].sort_values('executionsequence')
    
    for i in range(len(case_activities) - 1):
        from_activity = case_activities.iloc[i]
        to_activity = case_activities.iloc[i + 1]
        
        # ハンドオフ時間（同じ部署なら短く、異なる部署なら長く）
        from_resource = df_resource[df_resource['resourceid'] == from_activity['resource']].iloc[0]
        to_resource = df_resource[df_resource['resourceid'] == to_activity['resource']].iloc[0]
        
        if from_resource['department'] == to_resource['department']:
            handoff_duration = random.randint(5, 15)
        else:
            handoff_duration = random.randint(15, 60)
        
        # 待機時間
        waiting_duration = to_activity['waitingminutes']
        
        # ボトルネック判定（待機時間が60分以上）
        is_bottleneck = waiting_duration >= 60
        
        transitions.append({
            'activitytransitionid': f"AT-{transition_counter:07d}",
            'name': f"{from_activity['name']} → {to_activity['name']}",
            'processcase': case_id,
            'fromactivity': from_activity['activityinstanceid'],
            'toactivity': to_activity['activityinstanceid'],
            'transitiontype': 100000000,  # 順次
            'transitiontime': to_activity['startedat'],
            'handoffduration': handoff_duration,
            'waitingduration': waiting_duration,
            'fromresource': from_activity['resource'],
            'toresource': to_activity['resource'],
            'transitionreason': '通常の順次実行',
            'isbottleneck': is_bottleneck
        })
        
        transition_counter += 1

df_activity_transition = pd.DataFrame(transitions)
df_activity_transition.to_csv('activity_transition.csv', index=False, encoding='utf-8-sig')
print(f"ActivityTransition: {len(df_activity_transition)}件")

# 8. ProcessError（プロセスエラー）
print("8. ProcessError（プロセスエラー）を生成中...")
errors = []
error_counter = 1

# アクティビティインスタンスの20%にエラーを発生させる
error_activities = df_activity_instance.sample(n=min(10, len(df_activity_instance)//5))

for _, activity in error_activities.iterrows():
    error_type = random.choice(['書類不備', 'システムエラー', '情報不足', '承認遅延'])
    error_category = random.choice([100000000, 100000001, 100000002, 100000003])
    
    detected_time = activity['startedat'] + timedelta(minutes=random.randint(5, 30))
    resolution_time = detected_time + timedelta(minutes=random.randint(15, 180))
    
    errors.append({
        'processerrorid': f"ERR-{error_counter:07d}",
        'name': f"{error_type} - {activity['name']}",
        'activityinstance': activity['activityinstanceid'],
        'errortype': error_type,
        'errorcategory': error_category,
        'errordescription': fake.text(max_nb_chars=100),
        'detectedat': detected_time,
        'resolvedat': resolution_time,
        'resolutionminutes': int((resolution_time - detected_time).total_seconds() / 60),
        'resolutionaction': fake.text(max_nb_chars=80),
        'additionalcost': random.randint(1000, 10000),
        'causesrework': random.choice([True, False])
    })
    
    error_counter += 1

df_process_error = pd.DataFrame(errors)
df_process_error.to_csv('process_error.csv', index=False, encoding='utf-8-sig')
print(f"ProcessError: {len(df_process_error)}件")

# サマリー出力
print("\n" + "="*60)
print("データ生成完了サマリー")
print("="*60)
print(f"ProcessDefinition:     {len(df_process_def):3d}件 (process_definition.csv)")
print(f"ActivityDefinition:    {len(df_activity_def):3d}件 (activity_definition.csv)")
print(f"Customer:              {len(df_customer):3d}件 (customer.csv)")
print(f"Resource:              {len(df_resource):3d}件 (resource.csv)")
print(f"ProcessCase:           {len(df_process_case):3d}件 (process_case.csv)")
print(f"ActivityInstance:      {len(df_activity_instance):3d}件 (activity_instance.csv)")
print(f"ActivityTransition:    {len(df_activity_transition):3d}件 (activity_transition.csv)")
print(f"ProcessError:          {len(df_process_error):3d}件 (process_error.csv)")
print("="*60)

# データ分析サンプル
print("\n" + "="*60)
print("ボトルネック分析サンプル")
print("="*60)

# 平均処理時間分析
activity_performance = df_activity_instance.groupby('activitydefinition').agg({
    'processingminutes': ['mean', 'max', 'count'],
    'slabreached': 'sum'
}).round(1)
activity_performance.columns = ['平均処理時間', '最大処理時間', '実行回数', 'SLA違反回数']

# アクティビティ名を追加
activity_map = df_activity_def.set_index('activitydefinitionid')['name'].to_dict()
activity_performance['アクティビティ名'] = activity_performance.index.map(activity_map)
activity_performance = activity_performance[['アクティビティ名', '平均処理時間', '最大処理時間', '実行回数', 'SLA違反回数']]

print("【アクティビティ別パフォーマンス TOP10】")
top_bottlenecks = activity_performance.sort_values('平均処理時間', ascending=False).head(10)
print(top_bottlenecks.to_string())

print("\n【ハンドオフボトルネック TOP5】")
handoff_analysis = df_activity_transition.groupby(['fromresource', 'toresource']).agg({
    'waitingduration': 'mean',
    'isbottleneck': 'sum'
}).round(1)
handoff_analysis.columns = ['平均待機時間', 'ボトルネック発生回数']
handoff_bottlenecks = handoff_analysis.sort_values('平均待機時間', ascending=False).head(5)
print(handoff_bottlenecks.to_string())

print("\n【プロセス別完了率】")
process_completion = df_process_case.groupby('processdefinition')['casestatus'].value_counts(normalize=True).unstack(fill_value=0)
process_map = df_process_def.set_index('processdefinitionid')['name'].to_dict()
process_completion.index = process_completion.index.map(process_map)
print((process_completion * 100).round(1).to_string())

print("\n全CSVファイルが正常に生成されました！")
print("Power BIやDataverseでのインポートにご利用ください。")
