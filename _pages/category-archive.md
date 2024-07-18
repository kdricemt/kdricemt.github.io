---
layout: archive
permalink: /categories/
title: "Blog Posts"
author_profile: true
---


{% include base_path %}
{% include group-by-array collection=site.posts field="categories" %}

{% assign __empty_array = '' | split: ',' %}
{% assign group_names_manual = __empty_array %}
{% assign group_items_manual = __empty_array %}
<!-- Add "海外大学院出願"-->
{% assign group_names_manual = group_names_manual | push: "海外大学院出願" %}
<!-- Add "スタンフォード講義録"-->
{% assign group_names_manual = group_names_manual | push: "スタンフォード講義録" %}
<!-- Add "研究関連"-->
{% assign group_names_manual = group_names_manual | push: "研究関連" %}
<!-- Add "その他エッセイ"-->
{% assign group_names_manual = group_names_manual | push: "雑記事" %}

<!-- group_items -->
{% for name in group_names_manual %}
<!-- Collect if contains -->
{% assign __item = __empty_array %}
{% for __element in site.posts %}
{% if __element["categories"] contains name %}
{% assign __item = __item | push: __element %}
{% endif %}
{% endfor %}

<!-- Push to group_items -->
{% assign group_items_manual = group_items_manual | push: __item %}
{% endfor %}

{% for category in group_names_manual %}
{% assign posts = group_items_manual[forloop.index0] %}
<h4 id="{{ category | slugify }}" class="archive__subtitle">{{ category }}</h4>
{% for post in posts %}
{% include blog_feature.html type="left"%}
{% endfor %}
{% endfor %}