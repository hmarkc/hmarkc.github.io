---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am a second-year PhD student at [Imperial College London](https://www.imperial.ac.uk/), advised by Prof. [Wayne Luk](https://www.imperial.ac.uk/people/w.luk) and Dr. [Hongxiang Fan](https://os-hxfan.github.io). I hold the [President's PhD Scholarship](https://www.imperial.ac.uk/study/fees-and-funding/postgraduate-doctoral/grants-scholarships/presidents-phd/) and previously completed both my Bachelor's and Master's degrees here. For more details, please see my [CV](files/research_CV.pdf).

My research focuses on democratizing AI through efficient ML algorithms (e.g., LLM quantization, speculative decoding, model merging, expert skipping) and systems (e.g., memory management, request scheduling, heterogeneous computing).


# 🔥 News
- *2026.03*: &nbsp;📖📖 Named as Microsoft Research Fellow for the research challenge "Steering reasoning models with test-time verification".
- *2026.01*: &nbsp;🎉🎉 [AdaBlock-dLLM](https://arxiv.org/pdf/2509.26432), our work on automated block size optimization for diffusion language models, was accepted to ICLR 2026!
- *2025.11*: &nbsp;🎉🎉 [FastTTS](https://arxiv.org/pdf/2509.00195), our work on fast test-time scaling for edge devices, was accepted to ASPLOS 2026!
- *2025.09*: &nbsp;🎉🎉 Our [paper](https://arxiv.org/pdf/2505.11730) on optimal verification granularity for test-time scaling was accepted to NeurIPS 2025!
- *2025.08*: &nbsp;🎉🎉 [PPD](https://arxiv.org/pdf/2405.18628), our edge-friendly speculative decoding method, was accepted to EMNLP 2025!
- *2025.06*: &nbsp;🎉🎉 [FW-Merging](https://arxiv.org/abs/2503.12649), our work on scalable multi-LLM/agent merging, was accepted to ICCV 2025!
- *2025.01*: &nbsp;🎉🎉 [PMPD](https://arxiv.org/pdf/2410.13461), which proposes adaptive LLM quantization, was accepted to ICLR 2025!
- *2024.10*: &nbsp;😊😊 Started my PhD at Imperial College London with the President's PhD Scholarship!


# 📝 Selected Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ASPLOS 2026</div><img src='images/asplos26.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Democratizing Agentic AI with Fast Test-Time Scaling on the Edge](https://arxiv.org/pdf/2509.00195)

**Hao Mark Chen**, Zhiwen Mo, Guanxi Lu, Shuang Liang, Lingxiao Ma, Wayne Luk, Hongxiang Fan

<span style="color: red;">ASPLOS 2026</span>

[**Paper**](https://arxiv.org/pdf/2509.00195)
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025</div><img src='images/neurips25.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling](https://arxiv.org/pdf/2505.11730)

**Hao Mark Chen**, Guanxi Lu, Yasuyuki Okoshi, Zhiwen Mo, Masato Motomura, Hongxiang Fan

<span style="color: red;">NeurIPS 2025</span>

[**Paper**](https://arxiv.org/pdf/2505.11730) <strong>|</strong> [**Code**](https://github.com/hmarkc/VG-Search)
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2025</div><img src='images/emnlp25.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Hardware-Aware Parallel Prompt Decoding for Memory-Efficient Acceleration of LLM Inference](https://arxiv.org/pdf/2405.18628)

**Hao (Mark) Chen**, Wayne Luk, Ka Fai Cedric Yiu, Rui Li, Konstantin Mishchenko, Stylianos I. Venieris, Hongxiang Fan

<span style="color: red;">EMNLP 2025</span>

[**Paper**](https://arxiv.org/pdf/2405.18628) <strong>|</strong> [**Code**](https://github.com/hmarkc/parallel-prompt-decoding)
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICCV 2025</div><img src='images/iccv25.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[FW-Merging: Scaling Model Merging with Frank-Wolfe Optimization](https://arxiv.org/abs/2503.12649)

**Hao Mark Chen**, Shell Xu Hu, Wayne Luk, Timothy Hospedales, Hongxiang Fan

<span style="color: red;">ICCV 2025</span>

[**Paper**](https://arxiv.org/abs/2503.12649) <strong>|</strong> [**Code**](https://github.com/hmarkc/FW-Merging)
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2025</div><img src='images/iclr25.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Progressive Mixed-Precision Decoding for Efficient LLM Inference](https://arxiv.org/pdf/2410.13461)

**Hao Mark Chen**, Fuwen Tan, Alexandros Kouris, Royson Lee, Hongxiang Fan, Stylianos I. Venieris

<span style="color: red;">ICLR 2025</span>

[**Paper**](https://arxiv.org/pdf/2410.13461) <strong>|</strong> [**Code**](https://github.com/SamsungLabs/PMPD)
</div>
</div>

<p style="text-align: center; margin-top: 20px;">
  📚 Full list of publications available on <a href="https://scholar.google.com/citations?user=O6ajbEoAAAAJ&hl">Google Scholar</a>
</p>


# 🎖 Honors and Awards
- *2026* Microsoft Research Fellow, co-named with supervisor, research challenge: "Steering reasoning models with test-time verification"
- *2024* President's PhD Scholarship, Imperial College London
- *2024* Governors' MEng Prize in Computing (best overall performance in MEng programme), Imperial College London
- *2024* Winton Capital Applied Undergraduate Project Computing Prize, Imperial College London
- *2024* Dean's List (Year 4), Imperial College London
- *2023* Dean's List (Year 3), Imperial College London
- *2022* Dean's List (Year 2), Imperial College London
- *2021* Dean's List (Year 1), Imperial College London
- *2021* G-Research Ltd Prize, G-Research Ltd
- *2015 - 2019* Singapore SM1 Scholarship, Ministry of Education Singapore


# 📖 Educations
- *2024 - 2028 (expected)*, Ph.D in Computer Science, Imperial College London
- *2020 - 2024*, MEng in Computing, Imperial College London


# 💼 Industry Experience
- *2025.07 - 2025.12*, **Samsung AI Center**, Research Intern. Worked on efficient diffusion language model.
- *2024.07 - 2024.12*, **Samsung AI Center**, Research Intern. Worked on efficient LLM inference involving quantization, leading to a publication at ICLR 2025.
- *2023.04 - 2023.09*, **Qube RT**, Quantitative Technologist Intern. Developed C++ performance monitoring system for low-latency trading platform.
<!-- - *2022.03 - 2022.09*, **Huawei Technologies R&D**, Graphics Modelling Intern. Worked on automatic GPU API generation. -->
- *2021.06 - 2021.09*, **Ampere Computing**, Java Software Developer. Developed a log search engine for Jenkins based on Lucene Search.


# 💻 Academic Service
- Conference Reviewer: ICLR (2025), NeurIPS (2025)
- Journal Reviewer: TMLR


# 🍞 Teaching Experience
- *2023 - 2024*, Personal Math Tutor, Imperial College London
