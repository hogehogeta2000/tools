erDiagram
    %% 中核エンティティ
    cr_faq {
        guid cr_faqid PK "FAQ ID"
        string cr_title "FAQタイトル"
        text cr_summary "概要・要約"
        text cr_content "FAQ本文"
        guid cr_category FK "カテゴリID"
        choice cr_status "状態"
        choice cr_priority "優先度"
        string cr_tags "タグ"
        int cr_viewcount "閲覧数"
        decimal cr_rating "評価スコア"
        string cr_sharepointurl "SharePointURL"
        datetime cr_publishdate "公開日時"
        datetime cr_expiredate "有効期限"
        boolean cr_isactive "有効フラグ"
        guid createdby FK "作成者"
        datetime createdon "作成日時"
        guid modifiedby FK "更新者"
        datetime modifiedon "更新日時"
    }

    cr_category {
        guid cr_categoryid PK "カテゴリID"
        string cr_name "カテゴリ名"
        text cr_description "説明"
        guid cr_parentcategory FK "親カテゴリID"
        string cr_icon "アイコンURL"
        int cr_displayorder "表示順序"
        boolean cr_isactive "有効フラグ"
        guid createdby FK "作成者"
        datetime createdon "作成日時"
        guid modifiedby FK "更新者"
        datetime modifiedon "更新日時"
    }

    %% ユーザー・権限管理
    systemuser {
        guid systemuserid PK "ユーザーID"
        string fullname "氏名"
        string internalemailaddress "メールアドレス"
        string businessunitid "部署ID"
        boolean isdisabled "無効フラグ"
        datetime createdon "作成日時"
        datetime modifiedon "更新日時"
    }

    cr_userrole {
        guid cr_userroleid PK "ユーザーロールID"
        guid cr_userid FK "ユーザーID"
        choice cr_roletype "ロール種別"
        guid cr_categoryid FK "管理カテゴリID"
        boolean cr_canapprove "承認権限"
        boolean cr_isactive "有効フラグ"
        datetime createdon "作成日時"
    }

    %% FAQ関連テーブル
    cr_faqtag {
        guid cr_faqtagid PK "FAQタグID"
        guid cr_faqid FK "FAQ ID"
        string cr_tagname "タグ名"
        datetime createdon "作成日時"
    }

    cr_faqrating {
        guid cr_faqratingid PK "FAQ評価ID"
        guid cr_faqid FK "FAQ ID"
        guid cr_userid FK "評価者ID"
        int cr_rating "評価スコア"
        text cr_comment "コメント"
        datetime createdon "評価日時"
    }

    cr_faqview {
        guid cr_faqviewid PK "FAQ閲覧ID"
        guid cr_faqid FK "FAQ ID"
        guid cr_userid FK "閲覧者ID"
        string cr_ipaddress "IPアドレス"
        string cr_useragent "ユーザーエージェント"
        datetime cr_viewdate "閲覧日時"
    }

    %% 承認ワークフロー
    cr_faqapproval {
        guid cr_faqapprovalid PK "FAQ承認ID"
        guid cr_faqid FK "FAQ ID"
        guid cr_requesterid FK "申請者ID"
        guid cr_approverid FK "承認者ID"
        choice cr_status "承認状態"
        text cr_comment "承認コメント"
        datetime cr_requestdate "申請日時"
        datetime cr_approvaldate "承認日時"
    }

    %% 検索・ログ
    cr_searchlog {
        guid cr_searchlogid PK "検索ログID"
        guid cr_userid FK "検索者ID"
        string cr_keyword "検索キーワード"
        int cr_resultcount "検索結果数"
        boolean cr_found "見つかったフラグ"
        datetime cr_searchdate "検索日時"
        string cr_ipaddress "IPアドレス"
    }

    cr_faqsearchresult {
        guid cr_faqsearchresultid PK "検索結果ID"
        guid cr_searchlogid FK "検索ログID"
        guid cr_faqid FK "FAQ ID"
        int cr_rank "表示順位"
        decimal cr_relevancescore "関連度スコア"
        boolean cr_clicked "クリックフラグ"
    }

    %% システム設定
    cr_systemsetting {
        guid cr_systemsettingid PK "システム設定ID"
        string cr_settingkey "設定キー"
        text cr_settingvalue "設定値"
        text cr_description "説明"
        boolean cr_isactive "有効フラグ"
        datetime modifiedon "更新日時"
    }

    cr_notification {
        guid cr_notificationid PK "通知ID"
        guid cr_userid FK "通知先ユーザーID"
        guid cr_faqid FK "関連FAQ ID"
        choice cr_notificationtype "通知種別"
        string cr_title "通知タイトル"
        text cr_message "通知メッセージ"
        boolean cr_isread "既読フラグ"
        datetime cr_sentdate "送信日時"
        datetime cr_readdate "既読日時"
    }

    %% 関係性の定義
    cr_faq ||--o{ cr_faqtag : "has"
    cr_faq ||--o{ cr_faqrating : "receives"
    cr_faq ||--o{ cr_faqview : "viewed_by"
    cr_faq ||--o{ cr_faqapproval : "requires"
    cr_faq ||--o{ cr_notification : "generates"
    cr_faq }o--|| cr_category : "belongs_to"
    
    cr_category ||--o{ cr_category : "parent_child"
    cr_category ||--o{ cr_userrole : "managed_by"
    
    systemuser ||--o{ cr_userrole : "has"
    systemuser ||--o{ cr_faqrating : "gives"
    systemuser ||--o{ cr_faqview : "performs"
    systemuser ||--o{ cr_faqapproval : "requests"
    systemuser ||--o{ cr_faqapproval : "approves"
    systemuser ||--o{ cr_searchlog : "performs"
    systemuser ||--o{ cr_notification : "receives"
    systemuser ||--o{ cr_faq : "creates"
    systemuser ||--o{ cr_faq : "modifies"
    
    cr_searchlog ||--o{ cr_faqsearchresult : "contains"
    cr_faqsearchresult }o--|| cr_faq : "references"
