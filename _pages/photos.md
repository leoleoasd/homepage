---
permalink: /photos/
title: "Some highlighted photos"
images:
  - DSC02409.JPG
  - DSC02566.JPG
  - DSC02604.JPG
  - DSC03674.JPG
  - DSC03963.JPG
  - DSC04099.JPG
  - DSC04163.JPG
  - DSC04181.JPG
  - DSC04210.JPG
  - DSC04214.JPG
  - DSC04527.JPG
  - DSC04756.JPG
  - DSC04840.JPG
  - DSC04910.JPG
---

<ul class="">
{% for image in page.images %}
  <li class="">
    <img src="/images/photos/{{ image }}" />
  </li>
{% endfor %}
</ul>
