---
layout: single
permalink: /year-archive/
title: "Blog Posts (Year)"
excerpt: " "
author_profile: true
header:
overlay_color: "#000"
overlay_filter: "0.5"
overlay_image: https://dl.dropboxusercontent.com/s/8j2t9kglf5n8cjd/dish.jpg?dl=0
caption: "Photo by Keidai Iiyama / The Dish, Stanford"
redirect_from:
- /wordpress/blog-posts/
---

カテゴリ別は[こちら](/categories/)

{% include base_path %}
{% capture written_year %}'None'{% endcapture %}
{% for post in site.posts %}
{% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
{% capture articletype %}{{ post.type }}{% endcapture %}
{% if year != written_year %}
<h2 id="{{ year | slugify }}" class="archive__subtitle">{{ year }}</h2>
{% capture written_year %}{{ year }}{% endcapture %}
{% endif %}
{% include blog_feature.html type="left"%}
{% endfor %}