自動化レベル（automationlevel）のグローバル選択肢を列挙いたします。

## **🤖 automationlevel（自動化レベル）選択肢**

| 値 | ラベル | 説明 | 特徴 | 分析観点 |
|---|-------|------|------|----------|
| **100000000** | 手作業 | 人手による完全手作業 | ・判断・経験に依存<br>・担当者スキルで差が出る<br>・時間のバラつき大 | **スキル課題**の発見対象 |
| **100000001** | システム支援 | システムを使った人手作業 | ・システム習熟度で差<br>・システム応答速度に依存<br>・入力ミスの可能性 | **システム習熟度課題**の発見対象 |
| **100000002** | 半自動化 | システム自動処理＋人手確認 | ・システム処理＋人の判断<br>・自動処理の信頼性に依存<br>・例外処理は人手 | **システム精度課題**の発見対象 |
| **100000003** | 完全自動化 | システムによる完全自動処理 | ・人の介入なし<br>・システム障害で全停止<br>・処理時間は一定 | **システム安定性課題**の発見対象 |

## **📊 各プロセスでの自動化レベル分布**

### **現在のCSVでの使用状況**
- **手作業（100000000）**: 受付業務、承認手続き、通知業務、書類確認等
- **システム支援（100000001）**: システム照会、システム操作、データ確認等

### **分析で期待される課題発見パターン**

#### **🤲 手作業アクティビティ（100000000）**
```sql
-- 手作業での担当者別パフォーマンス差
SELECT resource, activitykey, AVG(processingminutes), STDEV(processingminutes)
FROM activityinstance ai
JOIN activitydefinition ad ON ai.activitydefinition = ad.activitydefinitionid  
WHERE ad.automationlevel = 100000000
GROUP BY resource, activitykey
HAVING STDEV(processingminutes) > AVG(processingminutes) * 0.3
```
**発見される課題**: スキルギャップ、経験差、作業標準化不足

#### **💻 システム支援アクティビティ（100000001）**
```sql
-- システム支援での処理時間の安定性
SELECT activitykey, AVG(processingminutes), 
       COUNT(CASE WHEN processingminutes > standarddurationminutes * 1.5 THEN 1 END) as outlier_count
FROM activityinstance ai
JOIN activitydefinition ad ON ai.activitydefinition = ad.activitydefinitionid
WHERE ad.automationlevel = 100000001
GROUP BY activitykey, standarddurationminutes
```
**発見される課題**: システム性能、操作習熟度、システム障害影響

#### **⚡ 半自動化アクティビティ（100000002）**
```sql
-- 半自動化での例外処理発生率
SELECT activitykey, 
       COUNT(*) as total_executions,
       COUNT(CASE WHEN executionstatus = 100000001 THEN 1 END) as error_executions
FROM activityinstance ai
JOIN activitydefinition ad ON ai.activitydefinition = ad.activitydefinitionid
WHERE ad.automationlevel = 100000002
GROUP BY activitykey
```
**発見される課題**: 自動処理精度、例外ケース対応、人手介入率

#### **🔄 完全自動化アクティビティ（100000003）**
```sql
-- 完全自動化での障害影響
SELECT DATE(timestamp) as process_date,
       COUNT(CASE WHEN executionstatus != 100000000 THEN 1 END) as failure_count,
       AVG(processingminutes) as avg_processing_time
FROM activityinstance ai
JOIN activitydefinition ad ON ai.activitydefinition = ad.activitydefinitionid
WHERE ad.automationlevel = 100000003
GROUP BY DATE(timestamp)
```
**発見される課題**: システム安定性、障害復旧時間、自動化の信頼性

## **🎯 改善戦略の優先順位付け**

### **1. 手作業 → システム支援**
- 標準化可能な作業
- 高頻度・定型的な作業
- スキル差が大きい作業

### **2. システム支援 → 半自動化**  
- システム操作が複雑な作業
- 入力ミスが多い作業
- 処理パターンが決まっている作業

### **3. 半自動化 → 完全自動化**
- 例外処理が少ない作業
- 判断基準が明確な作業
- 高精度が要求される作業

## **📈 Power BI での可視化例**

```dax
-- 自動化レベル別の効率性指標
自動化効率スコア = 
SWITCH(
    [automationlevel],
    100000000, DIVIDE([標準時間], [実績平均時間], 1),  -- 手作業：標準化度
    100000001, DIVIDE([エラー発生数], [総実行数], 0),    -- システム支援：エラー率  
    100000002, DIVIDE([自動処理数], [総処理数], 1),     -- 半自動化：自動化率
    100000003, DIVIDE([正常実行数], [総実行数], 1)      -- 完全自動化：安定性
)
```

この自動化レベル分類により、各アクティビティの改善方向性と投資対効果を明確に分析できます。
