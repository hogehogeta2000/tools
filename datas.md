Power Appsモデル駆動型アプリでFAQ管理システムを構築するためのデータモデル・テーブル設計をご提案します。

## 主要テーブル設計

### 1. **FAQナレッジベーステーブル (cr_faq_knowledge)**

| フィールド名 | データ型 | 説明 |
|------------|---------|------|
| cr_faq_id | 主キー | FAQ ID（自動採番）|
| cr_title | テキスト | FAQ タイトル |
| cr_question | 複数行テキスト | 質問内容 |
| cr_answer | 複数行テキスト | 回答内容 |
| cr_category | 選択肢（カテゴリテーブル参照） | カテゴリ |
| cr_priority | 選択肢 | 優先度（高/中/低）|
| cr_status | 選択肢 | ステータス（下書き/レビュー中/公開/非公開）|
| cr_view_count | 整数 | 閲覧回数 |
| cr_helpful_count | 整数 | 役立った評価数 |
| cr_created_by | ユーザー | 作成者 |
| cr_created_on | 日時 | 作成日時 |
| cr_modified_by | ユーザー | 更新者 |
| cr_modified_on | 日時 | 更新日時 |

### 2. **問い合わせテーブル (cr_inquiry)**

| フィールド名 | データ型 | 説明 |
|------------|---------|------|
| cr_inquiry_id | 主キー | 問い合わせID |
| cr_inquiry_title | テキスト | 問い合わせタイトル |
| cr_inquiry_content | 複数行テキスト | 問い合わせ内容 |
| cr_inquirer_name | テキスト | 問い合わせ者名 |
| cr_inquirer_email | 電子メール | 問い合わせ者メール |
| cr_inquiry_source | 選択肢 | 受付チャネル（Copilot Studio/Forms/電話/メール）|
| cr_inquiry_status | 選択肢 | ステータス（新規/対応中/完了/保留）|
| cr_assigned_to | ユーザー | 担当者 |
| cr_response_content | 複数行テキスト | 対応内容 |
| cr_related_faq | 参照（FAQナレッジベース） | 関連FAQ |
| cr_created_on | 日時 | 受付日時 |
| cr_responded_on | 日時 | 対応完了日時 |

### 3. **カテゴリテーブル (cr_category)**

| フィールド名 | データ型 | 説明 |
|------------|---------|------|
| cr_category_id | 主キー | カテゴリID |
| cr_category_name | テキスト | カテゴリ名 |
| cr_category_description | 複数行テキスト | カテゴリ説明 |
| cr_parent_category | 参照（自己参照） | 親カテゴリ |
| cr_sort_order | 整数 | 表示順序 |

### 4. **タグテーブル (cr_tag)**

| フィールド名 | データ型 | 説明 |
|------------|---------|------|
| cr_tag_id | 主キー | タグID |
| cr_tag_name | テキスト | タグ名 |
| cr_tag_color | テキスト | タグ色（HEXコード）|

### 5. **FAQ-タグ関連テーブル (cr_faq_tag)**

| フィールド名 | データ型 | 説明 |
|------------|---------|------|
| cr_faq_tag_id | 主キー | 関連ID |
| cr_faq | 参照（FAQナレッジベース） | FAQ |
| cr_tag | 参照（タグテーブル） | タグ |

### 6. **トークスクリプトテーブル (cr_talk_script)**

| フィールド名 | データ型 | 説明 |
|------------|---------|------|
| cr_script_id | 主キー | スクリプトID |
| cr_script_title | テキスト | スクリプトタイトル |
| cr_script_content | 複数行テキスト | スクリプト内容 |
| cr_related_faq | 参照（FAQナレッジベース） | 関連FAQ |
| cr_script_type | 選択肢 | スクリプト種別（電話/チャット/メール）|
| cr_ai_generated | 二択 | AI生成フラグ |
| cr_created_by | ユーザー | 作成者 |
| cr_created_on | 日時 | 作成日時 |

### 7. **検索履歴テーブル (cr_search_history)**

| フィールド名 | データ型 | 説明 |
|------------|---------|------|
| cr_search_id | 主キー | 検索ID |
| cr_search_keyword | テキスト | 検索キーワード |
| cr_search_user | ユーザー | 検索者 |
| cr_search_datetime | 日時 | 検索日時 |
| cr_result_count | 整数 | 検索結果件数 |
| cr_selected_faq | 参照（FAQナレッジベース） | 選択されたFAQ |

## リレーションシップ

- **FAQナレッジベース ← カテゴリ**: 1対多（1つのカテゴリに複数のFAQ）
- **FAQナレッジベース ←→ タグ**: 多対多（FAQ-タグ関連テーブル経由）
- **問い合わせ → FAQナレッジベース**: 多対1（複数の問い合わせが同じFAQを参照可能）
- **トークスクリプト → FAQナレッジベース**: 多対1
- **検索履歴 → FAQナレッジベース**: 多対1

## セキュリティロール設計案

1. **FAQ管理者**: 全テーブルの作成・読み取り・更新・削除
2. **オペレーター**: FAQ・問い合わせ・検索履歴の読み取り、問い合わせの更新
3. **コンテンツ作成者**: FAQ・トークスクリプトの作成・更新

この設計により、検索機能とAIトークスクリプト生成機能を効率的に実装できる基盤が整います。次のステップとして、具体的なビューやフォームの設計に進むことができます。
