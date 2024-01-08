---
permalink: /photos/
title: "Some highlighted photos"
images:
  - 20230611_235731_E2232E5E.jpg
  - 20230612_003706_0FB7E0B1.jpg
  - DSC02409.JPG
  - DSC02566.JPG
  - DSC02604.JPG
  - DSC04099.JPG
  - DSC04163.JPG
  - DSC04181.JPG
  - DSC04210.JPG
---

<ul class="">
{% for image in page.images %}
  <li class="">
    <img src="/images/photos/{{ image }}" />
  </li>
{% endfor %}
</ul>
