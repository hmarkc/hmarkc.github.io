---
permalink: /
title: "About me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I am a first-year PhD student at [Imperial College London](https://www.imperial.ac.uk/), advised by Prof. [Wayne Luk](https://www.imperial.ac.uk/people/w.luk) and Dr. [Hongxiang Fan](https://os-hxfan.github.io). I am a recipient of the [President's PhD Scholarship](https://www.imperial.ac.uk/study/fees-and-funding/postgraduate-doctoral/grants-scholarships/presidents-phd/) at Imperial. Previously, I completed both my bachelor's and master's degrees at Imperial College London.

My research focuses on bridging the gap between advanced AI algorithms and hardware platforms through efficient hardware-aware algorithms, cost-effective model merging, ML-assisted hardware design, and algorithm-system co-design. My current research directions include:

- Multi-token generation for LLMs
- LLM quantization for edge deployment
- Model merging
- Code agents for hardware design

<br>

# Education

- Ph.D in Computing Research, Imperial College London, 2024 - 2028 (expected)
- MEng in Computing, Imperial College London, 2020 - 2024

<br>

# Selected Publications

{% for post in site.publications reversed %}
{% include archive-single-cv.html %}
{% endfor %}
