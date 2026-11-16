# Revision audit — 16 November 2026

This revision applies the user's pasted engineering review to the existing front-page paper. Its praise is not a certification: there is no single published “FAANG standard” against which this document has been formally approved.

## Review request and disposition

| Review item | Disposition in this revision |
|---|---|
| Truncated “Fetc” under Section 3.1 | The current repository already contained a complete Fetch row. Checked again; no fragment remains. |
| Missing visualization panels | Existing SVG was present. Added a PNG preview, explicit image links, and a separate LLVM 16 panel. Exact tables remain available to text-only readers. |
| Explicit SIMD paths | Added source-selected VNNI512, VNNI256 / AVX-VNNI, AVX2 emulation, NEON dot and fallback descriptions. |
| Cache structure and latency | Added cache scope, three-/four-cycle L1 distinctions, sourced desktop latency values, and capacity-versus-hit-time accounting. |
| SMT penalty and efficiency | Added aggregate gain, per-worker efficiency, shared-window detail, and same-system worker/core-placement comparisons. |
| New M5 performance cores | Inspected machine identity and actual instruction results; separated base-M5 P/E measurements from unmeasured Pro/Max secondary-core claims. |
| LLVM depth | Added phase-specific mechanisms, critical-path reasoning and a comparison manifest. |
| Reproducibility | Retained inputs, added architecture evidence, extended calculation output and a controlled-run template. |
| Highest M5 Pro PassMark | Retained BL5128734 and the exact five-submission scope; no replacement with model averages. |

## Review statements corrected during integration

The review is useful feedback, but some technical conclusions exceed its evidence:

- The 17% X3D aggregate advantage is not proven to be entirely caused by L3 cache.
- NEON and AMX are distinct resources; an AMX block must not be called a 128-bit NEON execution unit.
- The audited Stockfish 17.1 files expose explicit NEON and x86 SIMD implementations, not automatic matrix-accelerator offload.
- Zen 5's relevant dot-product path is AVX-512 VNNI; AVX10 is not needed to name this implementation.
- Desktop all-core clocks above 5 GHz are not assumed from an advertised boost maximum.
- Compilation can be limited by several phases; it is not universally memory-bandwidth-bound.
- A base-M5 instruction table cannot establish the new M5 Pro/Max performance-core port map.

## What this revision establishes

The paper is a source-backed research synthesis with reproducible arithmetic. It preserves the originating architecture calculations, distinguishes measured instruction evidence from extrapolation, and describes experiments that could identify causal contributions.

It does not contain a new controlled hardware campaign. The missing Apple Stockfish chart values and unmatched Apple LLVM pair remain explicit evidence gaps. Public means are still the 13 November snapshot, not a silently refreshed 16 November dataset.

## Closure criteria for a stronger empirical paper

| Open item | Evidence needed |
|---|---|
| Exact Apple Stockfish gap | Matching engine, network, procedure and numeric native Apple result |
| Cache-only contribution | Controlled system/placement comparison plus misses/stall evidence |
| SMT contribution | Same Ryzen 16/32-worker repeated runs, clocks and placement |
| M5 Pro/Max new-core port map | Core-type-verified independent and contention loops, disassembly, raw cycles |
| Apple LLVM ranking | Exact source/configuration/compiler/job policy and repeated raw timings |
| Independent review | Named reviewer, scope, review date and recorded findings |

## Verification performed

The publication workflow regenerates all arithmetic and charts, validates image dimensions and source links inside the repository, checks section structure and key retained PassMark values, and verifies the committed front page. It does not claim hardware-test results from these document checks.
