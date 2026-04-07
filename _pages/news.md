---
layout: archive
title: "News"
permalink: /news/
author_profile: true
---

{% assign sorted_news = site.news | sort: 'date' | reverse %}
{% for item in sorted_news %}
  {% include news-item.html %}
{% endfor %}
