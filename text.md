## Dataverseエンティティ設計

### 1. プロセスケース（Process Cases）エンティティ

**表示名**: プロセスケース  
**内部名**: new_processcase  
**説明**: 各業務プロセスの実行インスタンスを管理

| 表示名 | 内部名 | 説明 | データ型 |
|--------|--------|------|----------|
| ケースID | new_caseid | プロセスケースの一意識別子 | Text (100) |
| プロセス名 | new_processname | 実行されたプロセスの名称 | Text (200) |
| 開始日時 | new_starttime | プロセス開始のタイムスタンプ | Date and Time |
| 終了日時 | new_endtime | プロセス終了のタイムスタンプ | Date and Time |
| 実行時間（分） | new_duration | プロセス全体の実行時間 | Whole Number |
| ステータス | new_status | プロセスの実行状態 | Choice (実行中, 完了, 失敗, キャンセル) |
| 開始者 | new_initiator | プロセスを開始したユーザー | Text (100) |
| 優先度 | new_priority | プロセスの優先度レベル | Choice (高, 中, 低) |
| カテゴリ | new_category | プロセスの分類 | Choice (承認, 申請, データ処理, 報告) |
| 部署 | new_department | 実行部署 | Text (100) |
| コスト | new_cost | プロセス実行コスト | Currency |
| 満足度 | new_satisfaction | プロセス完了後の満足度 | Choice (1, 2, 3, 4, 5) |

### 2. プロセスアクティビティ（Process Activities）エンティティ

**表示名**: プロセスアクティビティ  
**内部名**: new_processactivity  
**説明**: プロセス内の個別アクティビティを記録

| 表示名 | 内部名 | 説明 | データ型 |
|--------|--------|------|----------|
| アクティビティID | new_activityid | アクティビティの一意識別子 | Text (100) |
| ケース参照 | new_caseref | 関連プロセスケースへの参照 | Lookup (new_processcase) |
| アクティビティ名 | new_activityname | 実行されたアクティビティの名称 | Text (200) |
| 開始日時 | new_starttime | アクティビティ開始時刻 | Date and Time |
| 終了日時 | new_endtime | アクティビティ終了時刻 | Date and Time |
| 実行時間（分） | new_duration | アクティビティの実行時間 | Whole Number |
| ステータス | new_status | アクティビティの実行状態 | Choice (実行中, 完了, 失敗, スキップ) |
| 実行者 | new_executor | アクティビティを実行したリソース | Text (100) |
| アクティビティタイプ | new_activitytype | アクティビティの種類 | Choice (手動, 自動, 承認, 確認, データ入力) |
| シーケンス番号 | new_sequencenumber | アクティビティの実行順序 | Whole Number |
| 前アクティビティ | new_previousactivity | 直前のアクティビティID | Text (100) |
| エラーメッセージ | new_errormessage | 失敗時のエラー内容 | Text Area |
| 待機時間（分） | new_waitingtime | 前アクティビティ終了からの待機時間 | Whole Number |

### 3. プロセスリソース（Process Resources）エンティティ

**表示名**: プロセスリソース  
**内部名**: new_processresource  
**説明**: プロセス実行に関わるリソース情報

| 表示名 | 内部名 | 説明 | データ型 |
|--------|--------|------|----------|
| リソースID | new_resourceid | リソースの一意識別子 | Text (100) |
| リソース名 | new_resourcename | リソースの名称 | Text (100) |
| リソースタイプ | new_resourcetype | リソースの種類 | Choice (ユーザー, ボット, システム, 外部API) |
| 部署 | new_department | 所属部署 | Text (100) |
| 時間単価 | new_hourlycost | 1時間あたりのコスト | Currency |
| 稼働状況 | new_availability | リソースの利用可能状況 | Choice (利用可能, 多忙, 利用不可) |
| スキルレベル | new_skilllevel | 専門スキルのレベル | Choice (初級, 中級, 上級, エキスパート) |
| 所在地 | new_location | リソースの所在地 | Text (100) |
| 勤務時間開始 | new_workstart | 勤務開始時刻 | Text (10) |
| 勤務時間終了 | new_workend | 勤務終了時刻 | Text (10) |

### 4. プロセス定義（Process Definitions）エンティティ

**表示名**: プロセス定義  
**内部名**: new_processdefinition  
**説明**: 標準プロセスの定義情報

| 表示名 | 内部名 | 説明 | データ型 |
|--------|--------|------|----------|
| プロセス定義ID | new_processdefinitionid | プロセス定義の一意識別子 | Text (100) |
| プロセス名 | new_processname | プロセスの標準名称 | Text (200) |
| バージョン | new_version | プロセス定義のバージョン | Text (20) |
| 説明 | new_description | プロセスの詳細説明 | Text Area |
| カテゴリ | new_category | プロセスの分類 | Choice (承認, 申請, データ処理, 報告) |
| オーナー | new_owner | プロセスの責任者 | Text (100) |
| 作成日 | new_createddate | プロセス定義作成日 | Date and Time |
| 最終更新日 | new_lastmodified | 最終更新日時 | Date and Time |
| ステータス | new_status | プロセス定義の状態 | Choice (アクティブ, 非アクティブ, 廃止予定) |
| 標準実行時間 | new_standardduration | 標準的な実行時間（分） | Whole Number |
| 複雑度 | new_complexity | プロセスの複雑度 | Choice (低, 中, 高) |

### 5. プロセス例外（Process Exceptions）エンティティ

**表示名**: プロセス例外  
**内部名**: new_processexception  
**説明**: プロセス実行中の例外・エラー情報

| 表示名 | 内部名 | 説明 | データ型 |
|--------|--------|------|----------|
| 例外ID | new_exceptionid | 例外の一意識別子 | Text (100) |
| ケース参照 | new_caseref | 関連プロセスケースへの参照 | Lookup (new_processcase) |
| アクティビティ参照 | new_activityref | 関連アクティビティへの参照 | Lookup (new_processactivity) |
| 例外タイプ | new_exceptiontype | 例外の種類 | Choice (システムエラー, ビジネスルール違反, タイムアウト, 手動停止) |
| 発生日時 | new_occurredtime | 例外発生の日時 | Date and Time |
| エラーコード | new_errorcode | システムエラーコード | Text (50) |
| エラーメッセージ | new_errormessage | 詳細なエラーメッセージ | Text Area |
| 解決ステータス | new_resolutionstatus | 例外の解決状況 | Choice (未解決, 調査中, 解決済み, 無視) |
| 解決者 | new_resolver | 例外を解決した担当者 | Text (100) |
| 解決日時 | new_resolvedtime | 例外解決日時 | Date and Time |
| 影響度 | new_impact | ビジネスへの影響度 | Choice (低, 中, 高, 重大) |

### 6. パフォーマンス指標（Performance Metrics）エンティティ

**表示名**: パフォーマンス指標  
**内部名**: new_performancemetric  
**説明**: プロセスのKPI・メトリクス情報

| 表示名 | 内部名 | 説明 | データ型 |
|--------|--------|------|----------|
| メトリクスID | new_metricid | メトリクスの一意識別子 | Text (100) |
| ケース参照 | new_caseref | 関連プロセスケースへの参照 | Lookup (new_processcase) |
| 測定日時 | new_measurementtime | 測定実施日時 | Date and Time |
| スループット | new_throughput | 単位時間あたりの処理件数 | Decimal Number |
| サイクルタイム | new_cycletime | 開始から完了までの時間（分） | Whole Number |
| 待機時間 | new_waitingtime | 待機時間の合計（分） | Whole Number |
| 処理時間 | new_processingtime | 実際の処理時間（分） | Whole Number |
| 品質スコア | new_qualityscore | プロセス品質の評価スコア | Decimal Number |
| コスト効率 | new_costefficiency | コスト効率の指標 | Decimal Number |
| 顧客満足度 | new_customersatisfaction | 顧客満足度スコア | Decimal Number |


## データモデル - リレーションシップ設計

### リレーションシップ一覧

#### **1. プロセス定義 → プロセスケース (1:N)**
- **親エンティティ**: new_processdefinition
- **子エンティティ**: new_processcase
- **関係**: 1つのプロセス定義から複数のプロセスケースが実行される
- **外部キー**: new_processcase.new_processdefinitionref
- **カスケード動作**: 制限削除（プロセス定義削除時、関連ケースが存在する場合は削除不可）

#### **2. プロセスケース → プロセスアクティビティ (1:N)**
- **親エンティティ**: new_processcase
- **子エンティティ**: new_processactivity
- **関係**: 1つのプロセスケースは複数のアクティビティで構成される
- **外部キー**: new_processactivity.new_caseref
- **カスケード動作**: カスケード削除（ケース削除時、関連アクティビティも削除）

#### **3. プロセスリソース → プロセスアクティビティ (1:N)**
- **親エンティティ**: new_processresource
- **子エンティティ**: new_processactivity
- **関係**: 1つのリソースが複数のアクティビティを実行する
- **外部キー**: new_processactivity.new_resourceref
- **カスケード動作**: 制限削除（リソース削除時、関連アクティビティが存在する場合は削除不可）

#### **4. プロセスケース → プロセス例外 (1:N)**
- **親エンティティ**: new_processcase
- **子エンティティ**: new_processexception
- **関係**: 1つのプロセスケースで複数の例外が発生する可能性
- **外部キー**: new_processexception.new_caseref
- **カスケード動作**: カスケード削除（ケース削除時、関連例外も削除）

#### **5. プロセスアクティビティ → プロセス例外 (1:N)**
- **親エンティティ**: new_processactivity
- **子エンティティ**: new_processexception
- **関係**: 1つのアクティビティで複数の例外が発生する可能性
- **外部キー**: new_processexception.new_activityref
- **カスケード動作**: カスケード削除（アクティビティ削除時、関連例外も削除）

#### **6. プロセスケース → パフォーマンス指標 (1:N)**
- **親エンティティ**: new_processcase
- **子エンティティ**: new_performancemetric
- **関係**: 1つのプロセスケースに対して複数のパフォーマンス指標が測定される
- **外部キー**: new_performancemetric.new_caseref
- **カスケード動作**: カスケード削除（ケース削除時、関連メトリクスも削除）

#### **7. プロセスアクティビティ → プロセスアクティビティ (自己参照)**
- **親エンティティ**: new_processactivity
- **子エンティティ**: new_processactivity
- **関係**: アクティビティ間の順序関係（前後関係）
- **外部キー**: new_processactivity.new_previousactivityref
- **カスケード動作**: NULL設定（親アクティビティ削除時、子の参照をNULLに設定）

### 追加必要列（リレーションシップ用）

以下の列を各エンティティに追加する必要があります：

#### **new_processcase エンティティに追加**
| 表示名 | 内部名 | 説明 | データ型 |
|--------|--------|------|----------|
| プロセス定義参照 | new_processdefinitionref | 関連するプロセス定義への参照 | Lookup (new_processdefinition) |

#### **new_processactivity エンティティに追加**
| 表示名 | 内部名 | 説明 | データ型 |
|--------|--------|------|----------|
| リソース参照 | new_resourceref | アクティビティを実行するリソースへの参照 | Lookup (new_processresource) |
| 前アクティビティ参照 | new_previousactivityref | 直前のアクティビティへの参照 | Lookup (new_processactivity) |

## ER図（マーメイド）### データモデル設計のポイント

#### **1. 主要な設計原則**
- **正規化**: データの重複を避け、整合性を保つ
- **拡張性**: 将来的なRPA連携に対応できる構造
- **パフォーマンス**: 効率的なクエリ実行が可能な設計

#### **2. 重要な考慮事項**

**カスケード削除の設定**
- プロセスケース削除時：関連するアクティビティ、例外、メトリクスも自動削除
- プロセス定義・リソース削除時：関連データが存在する場合は削除を制限

**自己参照関係**
- アクティビティの順序関係は自己参照で実装
- 循環参照を避けるためのバリデーション要検討

**インデックス推奨**
- new_processcase.new_starttime（時系列分析用）
- new_processactivity.new_caseref（ケース単位での集計用）
- new_processactivity.new_sequencenumber（順序分析用）

#### **3. 拡張計画**
将来的なPower Automate for desktop連携時には、以下のエンティティ追加を予定：
- RPA実行ログエンティティ
- アクションログエンティティ
- ボット管理エンティティ

## Power BIダッシュボード用 使用列一覧

プロセスマイニングのPower BIダッシュボードで使用する列を分析観点別に整理いたします。

### 1. 時間分析（Time Analysis）

#### **プロセスケースエンティティ (new_processcase)**
- `new_starttime` - プロセス開始日時（時系列分析、トレンド分析）
- `new_endtime` - プロセス終了日時（完了タイミング分析）
- `new_duration` - プロセス実行時間（サイクルタイム分析、パフォーマンス評価）
- `new_caseid` - ケース識別子（集計キー）
- `new_processname` - プロセス名（プロセス別時間比較）
- `new_status` - ステータス（完了/失敗による時間差分析）

#### **プロセスアクティビティエンティティ (new_processactivity)**
- `new_starttime` - アクティビティ開始日時（詳細時間分析）
- `new_endtime` - アクティビティ終了日時（処理時間計算）
- `new_duration` - アクティビティ実行時間（ボトルネック特定）
- `new_waitingtime` - 待機時間（非付加価値時間の特定）
- `new_sequencenumber` - 実行順序（プロセスフロー分析）
- `new_activityname` - アクティビティ名（活動別時間分析）

### 2. プロセスフロー分析（Process Flow Analysis）

#### **プロセスアクティビティエンティティ (new_processactivity)**
- `new_caseref` - ケース参照（フロー追跡）
- `new_activityname` - アクティビティ名（ノード表示）
- `new_sequencenumber` - 実行順序（フロー順序）
- `new_previousactivityref` - 前アクティビティ参照（フロー接続）
- `new_status` - アクティビティステータス（成功/失敗パス）
- `new_activitytype` - アクティビティタイプ（自動/手動分類）

#### **プロセスケースエンティティ (new_processcase)**
- `new_caseid` - ケース識別子（フロー単位）
- `new_processname` - プロセス名（プロセス分類）
- `new_status` - ケースステータス（完了パターン分析）

### 3. リソース分析（Resource Analysis）

#### **プロセスリソースエンティティ (new_processresource)**
- `new_resourcename` - リソース名（個別リソース分析）
- `new_resourcetype` - リソースタイプ（ユーザー/ボット/システム分類）
- `new_department` - 部署（組織別分析）
- `new_hourlycost` - 時間単価（コスト分析）
- `new_availability` - 稼働状況（リソース効率性）
- `new_skilllevel` - スキルレベル（能力別分析）
- `new_workstart` - 勤務開始時刻（稼働時間分析）
- `new_workend` - 勤務終了時刻（稼働時間分析）

#### **プロセスアクティビティエンティティ (new_processactivity)**
- `new_executor` - 実行者（リソース使用量）
- `new_resourceref` - リソース参照（リソース紐付け）
- `new_duration` - 実行時間（リソース稼働時間）

### 4. 品質・例外分析（Quality & Exception Analysis）

#### **プロセス例外エンティティ (new_processexception)**
- `new_exceptiontype` - 例外タイプ（エラー分類）
- `new_occurredtime` - 発生日時（例外発生パターン）
- `new_errorcode` - エラーコード（具体的エラー分析）
- `new_resolutionstatus` - 解決ステータス（対応状況）
- `new_impact` - 影響度（重要度別分析）
- `new_caseref` - ケース参照（例外発生プロセス特定）
- `new_activityref` - アクティビティ参照（例外発生箇所特定）

#### **プロセスケースエンティティ (new_processcase)**
- `new_satisfaction` - 満足度（品質評価）
- `new_status` - ステータス（成功率計算）

### 5. パフォーマンス・KPI分析（Performance Analysis）

#### **パフォーマンス指標エンティティ (new_performancemetric)**
- `new_throughput` - スループット（処理能力）
- `new_cycletime` - サイクルタイム（処理効率）
- `new_waitingtime` - 待機時間（非効率時間）
- `new_processingtime` - 処理時間（実作業時間）
- `new_qualityscore` - 品質スコア（品質評価）
- `new_costefficiency` - コスト効率（費用対効果）
- `new_customersatisfaction` - 顧客満足度（サービス品質）
- `new_measurementtime` - 測定日時（時系列KPI分析）
- `new_caseref` - ケース参照（KPI紐付け）

### 6. コスト分析（Cost Analysis）

#### **プロセスケースエンティティ (new_processcase)**
- `new_cost` - プロセスコスト（総コスト分析）
- `new_department` - 部署（部門別コスト）
- `new_priority` - 優先度（優先度別コスト）

#### **プロセスリソースエンティティ (new_processresource)**
- `new_hourlycost` - 時間単価（リソースコスト）

### 7. 分類・フィルタ用ディメンション

#### **プロセス定義エンティティ (new_processdefinition)**
- `new_processname` - プロセス名（プロセス分類）
- `new_category` - カテゴリ（業務分類）
- `new_complexity` - 複雑度（複雑度別分析）
- `new_standardduration` - 標準実行時間（基準値比較）

#### **プロセスケースエンティティ (new_processcase)**
- `new_category` - カテゴリ（業務分類フィルタ）
- `new_department` - 部署（組織フィルタ）
- `new_priority` - 優先度（優先度フィルタ）
- `new_initiator` - 開始者（ユーザー別フィルタ）

### 8. Power BI計算列・メジャー用基礎データ

#### **日時関連の計算用**
- 全ての `new_starttime`, `new_endtime` フィールド
- `new_duration`, `new_waitingtime` フィールド

#### **集計・カウント用**
- 全ての主キー (`new_caseid`, `new_activityid`, `new_exceptionid` など)
- ステータス関連フィールド（成功率、完了率計算）

#### **関係性構築用**
- 全ての Lookup フィールド (`new_caseref`, `new_resourceref` など)

### 推奨Power BI計算列・メジャー

```DAX
// 時間関連メジャー
平均サイクルタイム = AVERAGE(new_processcase[new_duration])
平均待機時間 = AVERAGE(new_processactivity[new_waitingtime])

// 効率性メジャー
プロセス完了率 = 
DIVIDE(
    COUNTROWS(FILTER(new_processcase, new_processcase[new_status] = "完了")),
    COUNTROWS(new_processcase)
)

// コスト関連メジャー
総プロセスコスト = SUM(new_processcase[new_cost])
平均コスト効率 = AVERAGE(new_performancemetric[new_costefficiency])

// 品質関連メジャー
例外発生率 = 
DIVIDE(
    COUNTROWS(new_processexception),
    COUNTROWS(new_processcase)
)
```

## Power BIプロセスマイニングダッシュボード デザイン提案

### 1. ダッシュボード全体構成

#### **レイアウト構造**
- **ヘッダー部**: KPI指標サマリー（4-6個のカード）
- **左サイド**: フィルタパネル（スライサー集約）
- **メインエリア**: 3×2グリッドレイアウトでビジュアル配置
- **フッター部**: 詳細分析用テーブル

### 2. 使用ビジュアル詳細

#### **2.1 プロセスフロー分析セクション**

**サンキー図（Process Flow）**
- **目的**: プロセスの流れと各ステップの量的関係を可視化
- **データ**: アクティビティ名（From/To）、ケース数、成功/失敗パス
- **配置**: メインエリア左上（大きめ）
- **特徴**: ボトルネック、分岐点、例外パスを色分け表示

**プロセス実行パターン（Matrix）**
- **目的**: アクティビティ間の遷移パターンを数値で表示
- **データ**: 前アクティビティ × 次アクティビティのクロス集計
- **配置**: メインエリア右上
- **特徴**: ヒートマップ形式で頻度を色の濃淡で表現

#### **2.2 時間分析セクション**

**サイクルタイム推移（Line Chart）**
- **目的**: プロセス実行時間の時系列トレンド
- **データ**: 日付別平均実行時間、目標値線
- **配置**: メインエリア左中
- **特徴**: 異常値検知、季節性パターンの可視化

**アクティビティ別実行時間（Stacked Bar Chart）**
- **目的**: 各アクティビティの時間消費割合
- **データ**: アクティビティ名、平均実行時間、待機時間
- **配置**: メインエリア右中
- **特徴**: 処理時間と待機時間を色分けして積み上げ表示

#### **2.3 リソース・パフォーマンス分析**

**リソース利用率（Donut Chart）**
- **目的**: リソースタイプ別の作業配分
- **データ**: リソースタイプ、実行時間合計
- **配置**: メインエリア左下
- **特徴**: 中央に総稼働時間を表示

**部署別効率性（Scatter Chart）**
- **目的**: コスト効率と品質の相関関係
- **データ**: 部署別平均コスト（X軸）、品質スコア（Y軸）、バブルサイズ（処理件数）
- **配置**: メインエリア右下
- **特徴**: 理想的なポジション（高品質・低コスト）を可視化

#### **2.4 KPI指標カード**

**プロセス完了率カード**
- **データ**: 完了ケース数 / 総ケース数
- **表示**: パーセンテージ + 前月比較

**平均サイクルタイムカード**
- **データ**: 全プロセスの平均実行時間
- **表示**: 時間 + トレンド矢印

**例外発生率カード**
- **データ**: 例外件数 / 総アクティビティ数
- **表示**: パーセンテージ + 警告レベル色分け

**コスト効率カード**
- **データ**: 平均コスト効率指標
- **表示**: スコア + 目標値との比較

#### **2.5 フィルタ・スライサー**

**日付範囲スライサー**
- **タイプ**: Between型スライサー
- **対象**: プロセス開始日

**プロセス名スライサー**
- **タイプ**: チェックボックス型
- **対象**: プロセス定義名

**部署スライサー**
- **タイプ**: ドロップダウン型
- **対象**: 実行部署

**ステータススライサー**
- **タイプ**: ボタン型
- **対象**: プロセス実行ステータス

### 3. ダッシュボードレイアウトイメージ### 4. 各ビジュアルの詳細設定

#### **4.1 色彩設計**
- **プライマリカラー**: #0078d4（Microsoft Blue）
- **セカンダリカラー**: #40e0d0（成功・正常）, #ff6b6b（警告・例外）
- **アクセントカラー**: #ffd93d（注意）, #9370db（その他）

#### **4.2 推奨Power BIビジュアル**

**サンキー図**
- **カスタムビジュアル**: "Sankey Diagram by MAQ Software"
- **設定**: ノード幅30px、リンク透明度70%
- **色分け**: 成功パス（青系）、例外パス（赤系）

**時系列グラフ**
- **標準ビジュアル**: Line Chart
- **設定**: データマーカー有効、トレンドライン追加
- **軸**: X軸（日付）、Y軸（平均実行時間）

**マトリックス**
- **標準ビジュアル**: Matrix
- **設定**: 条件付き書式でヒートマップ化
- **色**: 低頻度（薄青）→ 高頻度（濃青）

**積み上げ棒グラフ**
- **標準ビジュアル**: Stacked Bar Chart
- **設定**: データラベル表示、凡例下部配置
- **積み上げ**: 処理時間（青）+ 待機時間（オレンジ）

#### **4.3 インタラクティブ機能**

**クロスフィルタリング**
- 全ビジュアル間でフィルタ連動
- ドリルダウン機能（月→週→日）

**ツールチップ**
- カスタムツールチップで詳細情報表示
- 関連KPIの表示

**ブックマーク**
- 定型分析パターンの保存
- 異常値検知ビュー

### 5. ダッシュボード階層構造

#### **Level 1: エグゼクティブビュー**
- 高レベルKPI中心
- トレンドと例外の概要

#### **Level 2: オペレーショナルビュー** 
- 詳細なプロセス分析
- リソース効率性分析

#### **Level 3: 詳細分析ビュー**
- 個別ケースの深堀り
- 根本原因分析


## Power Apps モデル駆動型アプリ設計

### 1. アプリケーション概要

**アプリケーション名**: プロセスマイニング管理システム  
**対象ユーザー**: プロセス管理者、オペレーター、アナリスト、システム管理者

### 2. サイトマップ設計

#### **2.1 メインナビゲーション構造**

```
📊 プロセスマイニング管理
├── 🏠 ダッシュボード
│   ├── プロセス概要ダッシュボード
│   └── パフォーマンス分析ダッシュボード
│
├── 🔧 プロセス管理
│   ├── プロセス定義
│   ├── プロセスケース
│   └── プロセスアクティビティ
│
├── 👥 リソース管理
│   ├── プロセスリソース
│   └── リソース稼働状況
│
├── ⚠️ 例外・品質管理
│   ├── プロセス例外
│   └── 例外分析レポート
│
├── 📈 パフォーマンス分析
│   ├── パフォーマンス指標
│   └── KPI監視
│
└── ⚙️ システム設定
    ├── ユーザー管理
    └── システム設定
```

### 3. 編集可能テーブルとビュー・フォーム設計

#### **3.1 プロセス定義 (new_processdefinition)**

**編集権限**: プロセス管理者、システム管理者

**ビュー設計**
- **アクティブプロセス定義ビュー（既定）**
  - 表示列: プロセス名, カテゴリ, バージョン, ステータス, オーナー, 最終更新日
  - フィルタ: ステータス = "アクティブ"
  - 並び順: 最終更新日 降順

- **全プロセス定義ビュー**
  - 表示列: プロセス名, カテゴリ, バージョン, ステータス, オーナー, 作成日, 最終更新日
  - 並び順: プロセス名 昇順

- **カテゴリ別プロセス定義ビュー**
  - 表示列: プロセス名, バージョン, 複雑度, 標準実行時間, オーナー
  - グループ化: カテゴリ別

**フォーム設計**
- **メインフォーム（作成・編集）**
  - セクション1: 基本情報（プロセス名, カテゴリ, バージョン, ステータス）
  - セクション2: 詳細情報（説明, 複雑度, 標準実行時間）
  - セクション3: 管理情報（オーナー, 作成日, 最終更新日）
  - タブ: 関連プロセスケース一覧

#### **3.2 プロセスケース (new_processcase)**

**編集権限**: プロセス管理者, オペレーター

**ビュー設計**
- **実行中プロセスビュー（既定）**
  - 表示列: ケースID, プロセス名, 開始日時, 実行時間, ステータス, 開始者, 優先度
  - フィルタ: ステータス = "実行中"
  - 並び順: 開始日時 降順

- **完了プロセスビュー**
  - 表示列: ケースID, プロセス名, 開始日時, 終了日時, 実行時間, 満足度, 部署
  - フィルタ: ステータス = "完了"
  - 並び順: 終了日時 降順

- **例外発生ケースビュー**
  - 表示列: ケースID, プロセス名, 開始日時, ステータス, 開始者, 部署
  - フィルタ: ステータス = "失敗"
  - 並び順: 開始日時 降順

- **部署別プロセスビュー**
  - 表示列: ケースID, プロセス名, ステータス, 開始者, 実行時間, コスト
  - グループ化: 部署別

**フォーム設計**
- **メインフォーム（作成・編集）**
  - セクション1: 基本情報（ケースID, プロセス名, ステータス, 優先度）
  - セクション2: 実行情報（開始日時, 終了日時, 実行時間, 開始者, 部署）
  - セクション3: 評価情報（コスト, 満足度）
  - タブ1: 関連アクティビティ一覧
  - タブ2: 関連例外一覧
  - タブ3: パフォーマンス指標

#### **3.3 プロセスアクティビティ (new_processactivity)**

**編集権限**: オペレーター, プロセス管理者

**ビュー設計**
- **実行中アクティビティビュー（既定）**
  - 表示列: アクティビティID, アクティビティ名, ケース参照, 開始日時, 実行者, ステータス
  - フィルタ: ステータス = "実行中"
  - 並び順: 開始日時 降順

- **ケース別アクティビティビュー**
  - 表示列: シーケンス番号, アクティビティ名, 開始日時, 終了日時, 実行時間, ステータス
  - 並び順: シーケンス番号 昇順

- **実行者別アクティビティビュー**
  - 表示列: アクティビティ名, ケース参照, 開始日時, 実行時間, ステータス
  - グループ化: 実行者別

- **エラー発生アクティビティビュー**
  - 表示列: アクティビティID, アクティビティ名, ケース参照, エラーメッセージ, 実行者
  - フィルタ: ステータス = "失敗"

**フォーム設計**
- **メインフォーム（作成・編集）**
  - セクション1: 基本情報（アクティビティID, アクティビティ名, アクティビティタイプ）
  - セクション2: 実行情報（開始日時, 終了日時, 実行時間, 待機時間）
  - セクション3: 関連情報（ケース参照, リソース参照, 実行者, シーケンス番号）
  - セクション4: エラー情報（ステータス, エラーメッセージ）
  - タブ: 関連例外一覧

#### **3.4 プロセスリソース (new_processresource)**

**編集権限**: プロセス管理者, システム管理者

**ビュー設計**
- **利用可能リソースビュー（既定）**
  - 表示列: リソース名, リソースタイプ, 部署, スキルレベル, 稼働状況, 時間単価
  - フィルタ: 稼働状況 = "利用可能"
  - 並び順: リソース名 昇順

- **リソースタイプ別ビュー**
  - 表示列: リソース名, 部署, スキルレベル, 時間単価, 勤務時間
  - グループ化: リソースタイプ別

- **部署別リソースビュー**
  - 表示列: リソース名, リソースタイプ, スキルレベル, 稼働状況, 時間単価
  - グループ化: 部署別

**フォーム設計**
- **メインフォーム（作成・編集）**
  - セクション1: 基本情報（リソース名, リソースタイプ, 部署）
  - セクション2: 能力情報（スキルレベル, 稼働状況）
  - セクション3: コスト情報（時間単価）
  - セクション4: 勤務情報（勤務時間開始, 勤務時間終了, 所在地）
  - タブ: 実行したアクティビティ一覧

#### **3.5 プロセス例外 (new_processexception)**

**編集権限**: アナリスト, プロセス管理者

**ビュー設計**
- **未解決例外ビュー（既定）**
  - 表示列: 例外ID, 例外タイプ, 発生日時, ケース参照, 影響度, 解決ステータス
  - フィルタ: 解決ステータス = "未解決" OR "調査中"
  - 並び順: 発生日時 降順

- **解決済み例外ビュー**
  - 表示列: 例外ID, 例外タイプ, 発生日時, 解決日時, 解決者, 影響度
  - フィルタ: 解決ステータス = "解決済み"
  - 並び順: 解決日時 降順

- **例外タイプ別ビュー**
  - 表示列: 例外ID, 発生日時, ケース参照, 影響度, 解決ステータス
  - グループ化: 例外タイプ別

**フォーム設計**
- **メインフォーム（作成・編集）**
  - セクション1: 基本情報（例外ID, 例外タイプ, 発生日時, 影響度）
  - セクション2: 関連情報（ケース参照, アクティビティ参照）
  - セクション3: エラー詳細（エラーコード, エラーメッセージ）
  - セクション4: 解決情報（解決ステータス, 解決者, 解決日時）

#### **3.6 パフォーマンス指標 (new_performancemetric)**

**編集権限**: アナリスト（参照のみ）, システム管理者（編集可）

**ビュー設計**
- **最新指標ビュー（既定）**
  - 表示列: ケース参照, 測定日時, スループット, サイクルタイム, 品質スコア
  - 並び順: 測定日時 降順

- **KPI監視ビュー**
  - 表示列: ケース参照, サイクルタイム, 品質スコア, コスト効率, 顧客満足度
  - 条件付き書式: 閾値に基づく色分け

**フォーム設計**
- **参照専用フォーム**
  - セクション1: 基本情報（ケース参照, 測定日時）
  - セクション2: 時間指標（スループット, サイクルタイム, 待機時間, 処理時間）
  - セクション3: 品質指標（品質スコア, コスト効率, 顧客満足度）

### 4. ビジネスプロセスフロー設計

#### **4.1 プロセス管理フロー**

**フロー名**: プロセス定義から実行まで

**ステージ設計**:

1. **プロセス定義作成**
   - エンティティ: new_processdefinition
   - 必須フィールド: プロセス名, カテゴリ, オーナー
   - ビジネスルール: バージョン自動設定

2. **プロセスケース開始**
   - エンティティ: new_processcase
   - 必須フィールド: ケースID, プロセス定義参照, 開始者
   - ビジネスルール: 開始日時自動設定

3. **アクティビティ実行**
   - エンティティ: new_processactivity
   - 必須フィールド: アクティビティ名, リソース参照
   - ビジネスルール: シーケンス番号自動採番

4. **プロセス完了**
   - エンティティ: new_processcase
   - 必須フィールド: 終了日時, 満足度
   - ビジネスルール: 実行時間自動計算

#### **4.2 例外対応フロー**

**フロー名**: 例外検知から解決まで

**ステージ設計**:

1. **例外検知**
   - エンティティ: new_processexception
   - 必須フィールド: 例外タイプ, ケース参照, 影響度

2. **影響度評価**
   - エンティティ: new_processexception
   - 必須フィールド: 影響度確定, エラー詳細分析

3. **対応措置実行**
   - エンティティ: new_processexception
   - 必須フィールド: 解決者割当, 対応内容

4. **解決確認**
   - エンティティ: new_processexception
   - 必須フィールド: 解決日時, 解決ステータス更新

### 5. セキュリティロール設計

#### **プロセス管理者ロール**
- プロセス定義: 作成, 読み取り, 更新, 削除
- プロセスケース: 作成, 読み取り, 更新
- アクティビティ: 読み取り, 更新
- リソース: 作成, 読み取り, 更新, 削除

#### **オペレーターロール**
- プロセスケース: 作成, 読み取り, 更新（自分が開始したもののみ）
- アクティビティ: 作成, 読み取り, 更新（自分が実行するもののみ）
- リソース: 読み取りのみ

#### **アナリストロール**
- 全エンティティ: 読み取りのみ
- 例外: 読み取り, 更新（解決情報のみ）
- パフォーマンス指標: 読み取りのみ

```
erDiagram
    new_processdefinition {
        string new_processdefinitionid PK
        string new_processname
        string new_version
        text new_description
        choice new_category
        string new_owner
        datetime new_createddate
        datetime new_lastmodified
        choice new_status
        int new_standardduration
        choice new_complexity
    }

    new_processcase {
        string new_caseid PK
        string new_processname
        datetime new_starttime
        datetime new_endtime
        int new_duration
        choice new_status
        string new_initiator
        choice new_priority
        choice new_category
        string new_department
        currency new_cost
        choice new_satisfaction
        lookup new_processdefinitionref FK
    }

    new_processresource {
        string new_resourceid PK
        string new_resourcename
        choice new_resourcetype
        string new_department
        currency new_hourlycost
        choice new_availability
        choice new_skilllevel
        string new_location
        string new_workstart
        string new_workend
    }

    new_processactivity {
        string new_activityid PK
        lookup new_caseref FK
        string new_activityname
        datetime new_starttime
        datetime new_endtime
        int new_duration
        choice new_status
        string new_executor
        choice new_activitytype
        int new_sequencenumber
        string new_previousactivity
        textarea new_errormessage
        int new_waitingtime
        lookup new_resourceref FK
        lookup new_previousactivityref FK
    }

    new_processexception {
        string new_exceptionid PK
        lookup new_caseref FK
        lookup new_activityref FK
        choice new_exceptiontype
        datetime new_occurredtime
        string new_errorcode
        textarea new_errormessage
        choice new_resolutionstatus
        string new_resolver
        datetime new_resolvedtime
        choice new_impact
    }

    new_performancemetric {
        string new_metricid PK
        lookup new_caseref FK
        datetime new_measurementtime
        decimal new_throughput
        int new_cycletime
        int new_waitingtime
        int new_processingtime
        decimal new_qualityscore
        decimal new_costefficiency
        decimal new_customersatisfaction
    }

    %% リレーションシップ定義
    new_processdefinition ||--o{ new_processcase : "defines"
    new_processcase ||--o{ new_processactivity : "contains"
    new_processresource ||--o{ new_processactivity : "executes"
    new_processcase ||--o{ new_processexception : "may_have"
    new_processactivity ||--o{ new_processexception : "may_generate"
    new_processcase ||--o{ new_performancemetric : "measured_by"
    new_processactivity ||--o| new_processactivity : "follows"
```
