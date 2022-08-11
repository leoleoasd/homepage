---
permalink: /open_source/
title: "My open source projects"
author_profile: true
redirect_from:
  - "/open"
  - "/open.html"
---

I've participated in many open-source communities. I'm the maintainer of the VSCode extension [LaTeX-Utilities](https://github.com/tecosaur/LaTeX-Utilities), and I'm the founder and maintainer of the [EduOJ](https://github.com/eduoj) project. Furthermore, I've contributed to many open-source projects, like [GitLab](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/20603), [UniversalOJ](https://github.com/UniversalOJ/UOJ-System), [OI-Wiki](https://github.com/OI-wiki/OI-wiki/), [nix](https://github.com/nix-rust/nix/) and others.

I've participated as mentor and community leader in the Open Source Promotion Plan 2021. All my 3 students successfully finished their projects. I've participated as a student in the OSPP 2020 in the UniversalOJ community, and successfully finished my project.

## Open source projects lead by me

### EduOJ

EduOJ (OJ for education) is an Online Judge (auto grader) system designed for educational needs in the Programming and Data Structure and Algorithm course. EduOJ's tech stack includes Go, Vue and Docker. It handles course scenarios well, and capable of handling 150+ QPS, thanks to its well-designed architecture.

This project is used in the daily teaching of my school's Data Structure class, and is supported by the Xing Huo (Spark) Foundation and National-level Student Innovation and Entrepreneurship Training Program of Beijing University of Technology.

### LaTeX-Utilities
LaTeX-Utilities is a VSCode extension with more than 100,000 downloads, aiming to improve the experience of writing LaTeX files using VSCode. It supports pasting image into `.tex` file, pasting tables into `.tex` file, and more.

This project originally started by [@tecosaur](https://github.com/tecosaur), then stopped support in 2020. I'm the new maintainer of this project.

### Compiler-Exp
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

### RPing

Rping is a ping tool written in pure rust. It uses full-async system calls (through epoll), and supports ping hosts and trace routes.

- Ping hosts
- Set TTL / package size / ping interval
- Bypass routing table
- Draw ping latency graph
- Trace route using ICMP
- Draw traceroute graph

## Open source projects I've participated in:

### UniversalOJ

UniversalOJ is a universal auto grader for practicing programming competition. It supports features like Hack / Extra Tests, and support multiple rules of contest (OI / IOI / ICPC).

Before I started the EduOJ project, I worked as a member in UOJ community. I've contributed to it's CI workflow and wrote some utilities.

### GitLab

GitLab is an open-source software collaboration platform.

I found a bug in its API and helped to fix it.

### Other:
Here is an incomplete list of other open source projects I've contributed to.

- [dashmap](https://github.com/xacrimon/dashmap/pull/186)
- [gofakes3](https://github.com/johannesboyne/gofakes3/pull/50)
- [heti](https://github.com/sivan/heti/pull/47)
- [nix](https://github.com/nix-rust/nix/pull/1752)
- [xalloc-rs](https://github.com/yvt/xalloc-rs/pull/1)
- [wasm-clang](https://github.com/binji/wasm-clang/pull/6)
