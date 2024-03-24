---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

[PDF version](/files/resume.pdf)

Education
======
* Ph.D. in Computer Science, Northeastern University, 2023 -- ?
  * Honored to be advised by [Prof. Dakuo Wang](https://dakuowang.com)
* B.S. in Computer Science, Beijing University of Technology, 2019 -- 2023
  * Principle of Compiling 96, Formal Language 96,  Principle of Operating System 95,  Operations Research 97,  Probability Theory 97, Design and Analysis of Algorithms 99
  * GPA 3.84, Major GPA 3.96
  * **Graduated with Honor**

Awards
=====
* *Bronze Medal*, 2021 ICPC Asia Regional Contest Shenyang Site
* *Bronze Medal*, 2020 ICPC Asia Regional Contest Yichuan Site
* *Bronze Medal*, 2019 ICPC Asia Regional Contest Yichuan Site
* *Global Rank 42 (top 2%)*, IEEE Xtreme 14.0 (2020)
* *Global Rank 85 (top 3.5%)*, IEEE Xtreme 14.0 (2021)

Publications
======
{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

<div class="publications">

{% bibliography %}

</div>

Work experience
======
* Jul. 2022 -- Present: Machine Learning Researcher
  * Contextual Summary for User Profile Regarding Job Description
    * Contextual summarization research on LinkedIn data. Generate a summary for each candidate profile regarding each job description to help HR to know the candidates faster.
    * As the main contributor to this project, I'm responsible for collecting data, designing and evaluating the method, and designing experiments.
  * Heterogeneous Knowledge-based Person-Job Fit
    * Person-Job Fit research using heterogeneous GNN pre-training. 
    * We are the first work to **leverage social knowledge among members** to help enhance the performance of Person-Job Fit.
    * Participated in method designing and I'm responsible for collecting data and running baseline experiments.
    * Submitted to WWW 2023.
* Dec. 2021 -- Jun. 2022: Intern Research Assistant
  * Tsinghua University, Natural Language Processing Lab
  * Big Model for Knowledge Graph (BMKG)
    * Develop a toolkit to help **train large Knowledge Embedding models** on **large KGs** and **run various downstream tasks**. 
    * Supports **4 levels of parallel** during the training process of **translation-based or context-based** Knowledge Embedding models.
    * I'm responsible for designing the framework and writing code that need high performance.
  * Design / Develop / Maintain multiple demos for NLP models
    * I designed and maintain multiple demos for NLP models to show their performance to non-specialists.
* Dec. 2020 -- Present: Research Assistant
  * Machine Reading Comprehension research in Biomedical Domain.
  * Supported by a **National-level undergraduate research program**.
  * Designed a **contextual embedding** and **model weighting** strategy to **learn domain knowledge ** in Biomedical Question Answering task. **Outforms SOTA models by a large margin**
  * Published in ACM BCB 2022. I'm the leader of this project, and I'm responsible for designing the model, conducting experiments and writing the paper.

Teaching Assistant Experiences
======
* Advanced Language & Programming Design -- 2019
* Advanced Language & Programming Design Course Design -- 2020
* Data Structure & Algorithm -- 2021
* Operating System Course Design -- 2021

Projext Experiences
=====
* Apr. 2020 -- Jun. 2022 Course Grading and Feedback System based on Fault-Cause analysis
  * An **autograding system** that can help daily teaching and **give accurate scores and feedback** based our **automatic fault-cause clustering method**. 
  * Supported by a **National-level undergraduate research program**.
  * Capable of handling **500+ QPS** while other similar systems can only do 20+. There are 60k+ lines of code and 72\% of them are covered by unit tests.
  * We even **found a bug in the go compiler** (see [golang/go\#44614](https://github.com/golang/go/issues/44614)). Check [project introduction](/opensource#eduoj) to see more.
  * I'm the leader of this project, and I'm responsible for designing the system architecture, code reviewing, and full stack developing. 

Skills
=====
* Programming: Multilingual. Fluent in python, rust, go, c++, php, JavaScript, etc.
* English: Fluent (TOEFL 105, best scores 30/29/24/25)

Citations
=====
{% include /scholar.html %}