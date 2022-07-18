---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

Hi! 👋🏻 I'm Yuxuan (Leo) Lu, a senior undergraduate student at Beijing University of Technology. I'm currently working as an AI Intern at a joint program between LinkedIn & Microsoft Research Asia. My research interest includes Machine Reading Comprehension(MRC), Knowledge Graph Embedding (KGE) and general Natural Language Processing. I've worked as an intern research assistant at [THUNLP](https://nlp.csai.tsinghua.edu.cn/) lab, supervised by [Zhiyuan Liu(刘知远)](http://nlp.csai.tsinghua.edu.cn/~lzy/).

Education
=====
I'm currently pursuing my B.E. degree in Computer Science at Faculty of Information, Beijing University of Technology. Before that, I've finished my junior and senior high at Beijing National Day School.

I'm looking for Ph.D. opportunity starting at Fall, 2023.

Research Experience
=====
I'm currently working as an AI Intern at a joint intern program between LinkedIn & Microsoft Research Asia. My job includes designing, writing & testing AI models. My research area includes the construction and representation of Knowledge Graphs.

Before that, I've worked as an intern research assistant at [THUNLP](https://nlp.csai.tsinghua.edu.cn/) lab, supervised by Prof. [Zhiyuan Liu(刘知远)](http://nlp.csai.tsinghua.edu.cn/~lzy/). My research area here includes Knowledge Embedding.

Open source communities
=====
I've participated in many open-source communities. I'm the maintainer of the VSCode extension [LaTeX-Utilities](https://github.com/tecosaur/LaTeX-Utilities), and I'm the founder and maintainer of the [EduOJ](https://github.com/eduoj) project. Furthermore, I've contributed to many open-source projects, like [GitLab](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/20603), [UniversalOJ](https://github.com/UniversalOJ/UOJ-System), [OI-Wiki](https://github.com/OI-wiki/OI-wiki/), [nix](https://github.com/nix-rust/nix/) and others.

I've participated as mentor and community leader in the Open Source Promotion Plan 2021. All my 3 students successfully finished their projects. I've participated as a student in the OSPP 2020 in the UniversalOJ community, and successfully finished my project.

Introduction for some of my open-source projects:

EduOJ
-----
EduOJ (OJ for education) is an Online Judge (auto grader) system designed for educational needs in the Programming and Data Structure and Algorithm course. EduOJ's tech stack includes Go, Vue and Docker. It handles course scenarios well, and capable of handling 150+ QPS, thanks to its well-designed architecture.

This project is used in the daily teaching of my school's Data Structure class, and is supported by the Xing Huo (Spark) Foundation and National-level Student Innovation and Entrepreneurship Training Program of Beijing University of Technology.

LaTeX-Utilities
----
LaTeX-Utilities is a VSCode extension with more than 100,000 downloads, aiming to improve the experience of writing LaTeX files using VSCode. It supports pasting image into `.tex` file, pasting tables into `.tex` file, and more.

This project originally started by [@tecosaur](https://github.com/tecosaur), then stopped support in 2020. I'm the new maintainer of this project.

Compiler-Exp
----
The Cb compiler is a compiler that compiles a C-like language (Cb, pronounced as C-flat) to LLVM IR. This is the course experiment of my Compiler course.

The Cb compiler itself is written in Rust. It uses ANTLR4 and Inkwell (rust binding of LLVM builder library). Thanks to LLVM, the Cb compiler produces industurial level assembly and binary.

The Cb language implements a sub-set of C's features. Just like C# (C-sharp) which have more features than C, we have fewer features than C, hence the name C-flat.

Cb has full support for structs, arrays, pointers and their combinations.

The main difference between C89 and Cb is listed as follows:
1. Nested block comment
   Thanks to ANTLR4's powerful lexer, the following statement is legal in Cb:
```
/* /* 123 */ */
```
1. No support for float point numbers.
   Due to high workload, Cb have no support for float point numbers.
1. No support for `enum` and `bitfields` in `structs`.
1. No support for `register` and `volatile`.
1. No support for self-referencing types, like Linked-list nodes.
   Can be achieved by casting void-pointers.
1. Inline assembly

The report of this project (in Chinese) can be found at [here](https://github.com/leoleoasd/compiler_exp/blob/master/report/report.pdf).

