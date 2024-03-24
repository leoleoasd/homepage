import datetime
import json

import pandas as pd
import plotly.graph_objects as go
from pytz import timezone
from scholarly import scholarly

cited_by = scholarly.search_author_id("t_KJvIYAAAAJ")
with open("_data/scholar.json", "r") as f:
    data = json.load(f)
today = datetime.datetime.now(timezone("America/New_York")).strftime("%Y-%m-%d")
print(today, cited_by)
data[today] = cited_by["citedby"]
with open("_data/scholar.json", "w") as f:
    json.dump(data, f)

df = pd.DataFrame(data.items(), columns=["date", "citedby"])
df = df.sort_values("date")
fig = go.Figure(data=go.Scatter(x=df["date"], y=df["citedby"], mode="lines+markers"))
fig.update_layout(xaxis_title="Date", yaxis_title="Cited by", xaxis_type="category")
fig.write_html("_includes/scholar.html")
