---
layout: archive
title: "Citations"
permalink: /citations/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{%- capture rawContent -%}
  {%- include scholar.html -%}
{%- endcapture -%}

{{ rawContent }}
