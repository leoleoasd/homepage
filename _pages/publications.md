---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

Preprints
======
{% include base_path %}

<div class="publications">

{% bibliography --file preprint %}

</div>

Publications
======

<div class="publications">

{% bibliography %}

</div>