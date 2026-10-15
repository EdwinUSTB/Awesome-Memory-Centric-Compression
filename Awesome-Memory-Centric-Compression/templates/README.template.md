<div align="center">

# Awesome Memory-Centric Compression for LLMs

**A curated paper list for the survey**<br>
*From Long Context to Selective Memory: A Survey of Memory-Centric Compression for Large Language Models*

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![arXiv](https://img.shields.io/badge/arXiv-coming_soon-b31b1b.svg)](#-citation)
[![Papers](https://img.shields.io/badge/Papers-{{COUNT}}-2ea44f)](#-paper-list)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

## 📢 News

- **[2026-10]** Repository released together with the paper list of the survey. The preprint will be linked here once it is available on arXiv.

## 📖 Overview

Longer context windows do not remove the computational, storage, and information-selection pressures of long-context inference. This survey treats long-context compression as **memory management for inference-time computation**: the central question is which information should enter the expensive attention path, when, and in what form.

| Memory state | What it contains | Main cost |
|---|---|---|
| **Compute-active memory** | Prompt tokens, compressed representations, KV caches, serving caches | Prefill computation, KV memory, decoding bandwidth |
| **Intermediate states** | Offloaded KV caches, persistent prefix caches, materialized KV | Storage and data movement; recoverable without re-encoding |
| **Compute-inactive memory** | Documents, vector and graph memory, episodic and reflective memory | Retrieval, compression, and re-encoding before use |

Methods are organized by the state they operate on and by the **state transitions** they perform: writing, offloading, recall, retrieval-and-injection, materialization, eviction, consolidation, and forgetting.

<p align="center">
  <img src="assets/lifecycle.png" width="78%" alt="Memory-centric lifecycle view of long-context compression">
</p>

## 🗂️ Taxonomy

<p align="center">
  <img src="assets/taxonomy.png" width="95%" alt="Taxonomy of memory-centric long-context compression">
</p>

## 📑 Table of Contents

{{TOC}}

## 📚 Paper List

Papers are listed in the section of the survey where they are primarily discussed; within each group, newer papers come first. Venues follow the published version when available.

{{LISTS}}

## 📝 Citation

If you find this survey or repository useful, please cite:

```bibtex
@article{memorycentric2026survey,
  title   = {From Long Context to Selective Memory: A Survey of Memory-Centric Compression for Large Language Models},
  author  = {Author Name and others},
  journal = {arXiv preprint},
  year    = {2026}
}
```

The complete bibliography of the survey is available in [`papers.bib`](papers.bib).

## 🤝 Contributing

Suggestions of missing papers, corrections, and discussions are welcome through issues and pull requests. Please see [CONTRIBUTING.md](CONTRIBUTING.md) for the entry format; the paper list above is generated from [`data/papers.json`](data/papers.json).

## 📄 License

This repository is released under the [MIT License](LICENSE).
