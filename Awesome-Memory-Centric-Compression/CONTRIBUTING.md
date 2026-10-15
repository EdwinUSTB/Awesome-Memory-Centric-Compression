# Contributing

Thank you for helping keep this list accurate and up to date. Issues and pull requests are welcome for:

- missing papers that fit the scope of the survey (see below);
- corrections to titles, venues, years, or links;
- discussion of how a paper should be categorized.

## Scope

The list covers work on how long-context LLM systems decide which information enters the inference path, how they compress its representation, and how they store, retrieve, update, or forget it. This includes prompt and representation compression, KV-cache compression and offloading, architecture- and serving-level selective computation, external and agent memory, retrieval-conditioned compression and injection, and the corresponding benchmarks. Work that only extends the context window without changing information selection, caching, or memory mechanisms is generally out of scope.

## Adding or editing a paper

The paper list in `README.md` is generated from `data/papers.json`. Please edit the JSON file rather than the README:

```json
{
  "key": "author2026keyword",
  "title": "Full Paper Title",
  "year": 2026,
  "venue": "arXiv",
  "section": "active",
  "subsection": "Input and prompt compression",
  "paper": "https://arxiv.org/abs/xxxx.xxxxx",
  "code": "https://github.com/org/repo"
}
```

- `section` must be one of `surveys`, `background`, `active`, `inactive`, `transition`, `benchmarks`.
- `subsection` should reuse an existing subsection name where possible (see `scripts/build_readme.py`).
- `venue` should be the published venue (e.g., `NeurIPS`, `ICLR`, `ACL`), or `arXiv` for preprints.
- Leave `code` empty if no official implementation is available.

Then regenerate the README:

```bash
python scripts/build_readme.py
```

When adding a paper, please also add its BibTeX entry to `papers.bib` if it is not already there.
