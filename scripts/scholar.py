import datetime
import json

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
