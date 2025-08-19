**🐍 Power BI + Python でサンキーダイアグラム実現！**

素晴らしいアプローチです！Power BIのPython visualを使えば、plotlyで高品質なサンキーダイアグラムが作成できます。

---

## 🎯 実装方法

### **📋 前提条件**
```python
# Power BI Desktop設定
# ファイル → オプション → Pythonスクリプト
# Python環境: Anaconda/miniconda推奨
# 必要ライブラリ: pandas, plotly
```

---

## 📊 1. プロセスフロー サンキーダイアグラム

### **Power BI側データ準備**
```dax
# DAX計算テーブル作成
ProcessFlow = 
SUMMARIZE(
    ActivityTransition,
    "Source", RELATED(ActivityDefinition[name]),
    "Target", RELATEDTABLE(ActivityDefinition[name]),
    "Value", COUNT(ActivityTransition[activitytransitionid]),
    "AvgWaitTime", AVERAGE(ActivityTransition[waitingduration])
)
```

### **Pythonビジュアル実装**
```python
# Power BI Python Visual
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Power BIからデータ取得（dataset変数に自動格納）
df = dataset.copy()

# ユニークなノード一覧作成
nodes = list(set(df['Source'].tolist() + df['Target'].tolist()))
node_dict = {node: i for i, node in enumerate(nodes)}

# サンキーダイアグラム用データ準備
source_indices = [node_dict[source] for source in df['Source']]
target_indices = [node_dict[target] for target in df['Target']]
values = df['Value'].tolist()

# 待機時間による色付け
colors = []
for wait_time in df['AvgWaitTime']:
    if wait_time <= 30:
        colors.append('rgba(50, 160, 44, 0.8)')  # 緑: 正常
    elif wait_time <= 60:
        colors.append('rgba(255, 127, 14, 0.8)')  # 橙: 注意
    else:
        colors.append('rgba(214, 39, 40, 0.8)')   # 赤: 問題

# ノード色設定（アクティビティタイプ別）
node_colors = []
for node in nodes:
    if '申込' in node or '受付' in node:
        node_colors.append('rgba(31, 119, 180, 0.8)')  # 青: 受付
    elif '確認' in node:
        node_colors.append('rgba(255, 127, 14, 0.8)')  # 橙: 確認
    elif '審査' in node:
        node_colors.append('rgba(44, 160, 44, 0.8)')   # 緑: 審査
    elif '承認' in node:
        node_colors.append('rgba(214, 39, 40, 0.8)')   # 赤: 承認
    else:
        node_colors.append('rgba(148, 103, 189, 0.8)') # 紫: その他

# サンキーダイアグラム作成
fig = go.Figure(data=[go.Sankey(
    node = dict(
        pad = 15,
        thickness = 20,
        line = dict(color = "black", width = 0.5),
        label = nodes,
        color = node_colors
    ),
    link = dict(
        source = source_indices,
        target = target_indices, 
        value = values,
        color = colors,
        # ホバー情報
        customdata = df['AvgWaitTime'],
        hovertemplate = 'フロー: %{source.label} → %{target.label}<br>' +
                       '件数: %{value}<br>' +
                       '平均待機時間: %{customdata:.0f}分<extra></extra>'
    )
)])

# レイアウト設定
fig.update_layout(
    title_text="カードローン審査プロセスフロー",
    title_x=0.5,
    font_size=12,
    height=600,
    margin=dict(l=0, r=0, t=50, b=0)
)

# Power BIに表示
fig.show()
```

---

## 🔄 2. リワークループ可視化

### **リワーク専用サンキー**
```python
# リワークパターン特化版
import pandas as pd
import plotly.graph_objects as go

df = dataset.copy()

# リワークデータのみ抽出
rework_data = []
for index, row in df.iterrows():
    if row['IsRework'] == True:
        # 元のアクティビティ → リワーク版
        rework_data.append({
            'Source': row['ActivityName'] + '(初回)',
            'Target': row['ActivityName'] + '(リワーク)',
            'Value': 1,
            'ReworkReason': row['ReworkReason']
        })

rework_df = pd.DataFrame(rework_data)
rework_summary = rework_df.groupby(['Source', 'Target', 'ReworkReason']).size().reset_index(name='Value')

# リワーク理由別色分け
reason_colors = {
    '書類不備': 'rgba(214, 39, 40, 0.6)',   # 赤
    'システムエラー': 'rgba(255, 127, 14, 0.6)', # 橙  
    '手続きミス': 'rgba(44, 160, 44, 0.6)',   # 緑
    '顧客要求': 'rgba(31, 119, 180, 0.6)'    # 青
}

# サンキーダイアグラム実装
# ... (上記と同様のコード構造)

fig.update_layout(
    title_text="リワークフロー分析 - 原因別可視化",
    title_x=0.5
)

fig.show()
```

---

## ⏱️ 3. 時間軸付きプロセスフロー

### **時系列サンキー（アニメーション対応）**
```python
# 時系列プロセス可視化
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

df = dataset.copy()
df['StartDate'] = pd.to_datetime(df['StartedAt'])
df['Week'] = df['StartDate'].dt.isocalendar().week

# 週別フロー作成
weeks = sorted(df['Week'].unique())
fig = make_subplots(
    rows=len(weeks), cols=1,
    subplot_titles=[f'第{w}週' for w in weeks],
    specs=[[{"type": "sankey"}] for _ in weeks],
    vertical_spacing=0.02
)

for i, week in enumerate(weeks):
    week_data = df[df['Week'] == week]
    
    # 週別サンキーデータ準備
    week_summary = week_data.groupby(['Source', 'Target']).agg({
        'Value': 'sum',
        'AvgWaitTime': 'mean'
    }).reset_index()
    
    # ノード・リンク設定
    nodes = list(set(week_summary['Source'].tolist() + week_summary['Target'].tolist()))
    node_dict = {node: j for j, node in enumerate(nodes)}
    
    source_indices = [node_dict[source] for source in week_summary['Source']]
    target_indices = [node_dict[target] for target in week_summary['Target']]
    values = week_summary['Value'].tolist()
    
    # サンキー追加
    fig.add_trace(
        go.Sankey(
            node=dict(
                pad=10,
                thickness=15,
                label=nodes,
                color="rgba(31, 119, 180, 0.8)"
            ),
            link=dict(
                source=source_indices,
                target=target_indices,
                value=values,
                color="rgba(31, 119, 180, 0.4)"
            )
        ),
        row=i+1, col=1
    )

fig.update_layout(
    title_text="週別プロセスフロー推移",
    height=300 * len(weeks),
    showlegend=False
)

fig.show()
```

---

## 📊 4. 対話的高度サンキー

### **ドリルダウン対応サンキー**
```python
# 対話的サンキーダイアグラム
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

df = dataset.copy()

# 顧客種別・金額帯別のフロー分析
df['AmountCategory'] = pd.cut(df['CaseAmount'], 
                             bins=[0, 500000, 1000000, 2000000, float('inf')],
                             labels=['50万以下', '51-100万', '101-200万', '200万超'])

# メインサンキー
main_flow = df.groupby(['Source', 'Target']).agg({
    'Value': 'sum',
    'AvgWaitTime': 'mean'
}).reset_index()

# 詳細フロー（金額帯別）
detail_flows = {}
for category in df['AmountCategory'].unique():
    detail_flows[category] = df[df['AmountCategory'] == category].groupby(['Source', 'Target']).agg({
        'Value': 'sum', 
        'AvgWaitTime': 'mean'
    }).reset_index()

# ... サンキー実装 ...

# ボタンによる切り替え機能
updatemenus = [
    dict(
        type="buttons",
        direction="left",
        buttons=list([
            dict(label="全体", method="restyle", args=["visible", [True, False, False, False]]),
            dict(label="50万以下", method="restyle", args=["visible", [False, True, False, False]]),
            dict(label="51-100万", method="restyle", args=["visible", [False, False, True, False]]),
            dict(label="200万超", method="restyle", args=["visible", [False, False, False, True]])
        ]),
        pad={"r": 10, "t": 10},
        showactive=True,
        x=0.01,
        xanchor="left",
        y=1.02,
        yanchor="top"
    ),
]

fig.update_layout(updatemenus=updatemenus)
fig.show()
```

---

## 🎯 実装手順

### **Step 1: 環境準備**
```bash
# Anaconda Prompt
conda install plotly pandas
# または
pip install plotly pandas
```

### **Step 2: Power BI設定**
```
1. Power BI Desktop起動
2. ファイル → オプション → Pythonスクリプト
3. Python IDEパス設定
4. 「ホーム」→「Pythonビジュアル」選択
```

### **Step 3: データ接続**
```dax
# 必要な列をPythonに渡す
- ActivityTransition[fromactivity] → Source
- ActivityTransition[toactivity] → Target  
- COUNT(ActivityTransition) → Value
- AVERAGE(waitingduration) → AvgWaitTime
```

### **Step 4: Python実装**
```python
# 上記コードをPythonビジュアルにペースト
# Power BIのdataset変数が自動的に利用可能
```

**この方法で、動的で美しいサンキーダイアグラムによるプロセス可視化が実現できます！** 🐍📊✨
