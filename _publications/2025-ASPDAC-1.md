---
title: "Exploring Code Language Models for Automated HLS-based Hardware Generation: Benchmark, Infrastructure and Analysis"
collection: publications
date: 2025-01-01
venue: "Asia and South Pacific Design Automation Conference (ASP-DAC)"
paperurl: "https://arxiv.org/abs/2502.13921"
authors: "Jiahao Gai, <b>Hao (Mark) Chen</b>, Zhican Wang, Hongyu Zhou,
Wanru Zhao, Nicholas Lane, Hongxiang Fan"
citation: "Jiahao Gai, <b>Hao (Mark) Chen</b>, Zhican Wang, Hongyu Zhou,
Wanru Zhao, Nicholas Lane, Hongxiang Fan. Exploring Code Language Models for Automated HLS-based Hardware Generation: Benchmark, Infrastructure and Analysis. 2025 Asia and South Pacific Design Automation Conference (ASP-DAC)."
---

# Abstract

Recent advances in code generation have illuminated the potential of employing large language models (LLMs) for general-purpose programming languages such as Python and C++, opening new opportunities for automating software development and enhanc- ing programmer productivity. The potential of LLMs in software programming has sparked significant interest in exploring auto- mated hardware generation and automation. Although preliminary endeavors have been made to adopt LLMs in generating hardware description languages (HDLs) such as Verilog and SystemVerilog, several challenges persist in this direction. First, the volume of avail- able HDL training data is substantially smaller compared to that for software programming languages. Second, the pre-trained LLMs, mainly tailored for software code, tend to produce HDL designs that are more error-prone. Third, the generation of HDL requires a significantly higher number of tokens compared to software pro- gramming, leading to inefficiencies in cost and energy consumption. To tackle these challenges, this paper explores leveraging LLMs to generate High-Level Synthesis (HLS)-based hardware design. Although code generation for domain-specific programming lan- guages is not new in the literature, we aim to provide experimental results, insights, benchmarks, and evaluation infrastructure to inves- tigate the suitability of HLS over low-level HDLs for LLM-assisted hardware design generation. To achieve this, we first finetune pre- trained models for HLS-based hardware generation, using a col- lected dataset with text prompts and corresponding reference HLS designs. An LLM-assisted framework is then proposed to automate end-to-end hardware code generation, which also investigates the impact of chain-of-thought and feedback loops promoting tech- niques on HLS- design generation. Comprehensive experiments demonstrate the effectiveness of our methods.
