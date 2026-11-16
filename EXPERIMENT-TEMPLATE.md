# Controlled-run reporting template

This template describes future measurements. No values below are new benchmark results.

## Experiment identity

| Field | Record |
|---|---|
| Run ID / UTC date / operator | |
| Question and single intervention | |
| CPU SKU / core types / enabled SMT | |
| Motherboard or Mac model / firmware / OS | |
| Memory capacity / rate / timing / swap policy | |
| Power limits / cooling / ambient conditions | |
| Baseline and intervention run order | |

## Stockfish manifest

| Field | Record |
|---|---|
| Engine tag and full commit | |
| NNUE filenames and cryptographic hashes | |
| Compiler / version / PGO workflow / flags | |
| Build architecture and enabled VNNI / PEXT / NEON dot paths | |
| Binary hash / architecture / disassembly evidence | |
| Exact command, positions, search limits | |
| Explicit threads / hash / tablebase policy | |
| Worker-to-core placement or measured residency | |
| Warm-up and repetitions | |

Compare one change at a time. Keep the compiler and PGO policy fixed for an ISA comparison. Disabling PEXT must not inadvertently select a different vector kernel. Sixteen Ryzen workers must occupy sixteen distinct physical cores before comparing against thirty-two workers. Report worker-count sweeps separately from confirmed core-type subsets on Apple/Intel.

| Individual run | Workers / placement | Nodes | Elapsed s | NPS | Effective clocks | Temperature / power | Notes |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Retain raw standard output. Add cycles, retired instructions, branch misses, cache/TLB misses and memory stalls where supported. Record counter scope and multiplexing. Do not compare differently defined counters as though they were identical across ISAs.

## LLVM manifest

| Field | Record |
|---|---|
| Source commit / archive hash / patches | |
| Bootstrap C / C++ compiler and linker | |
| CMake generator / build type / assertions | |
| Enabled projects / runtimes / target backends | |
| Complete CMake cache and command | |
| Ninja command / jobs / parallel link limit | |
| Fresh build / disabled compiler cache evidence | |
| Filesystem and warm/cold cache policy | |
| Profiling mode and its overhead | |

| Individual run | Jobs | Total wall s | Compile phase s | Link phase s | Critical-path observations | Peak RSS / swap | Effective clocks |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Archive build logs, CMakeCache.txt, .ninja_log and timing traces where used. Phase times may overlap: do not add overlapping process CPU times and call the result wall time.

## Analysis and acceptance

- Publish individual repeated runs and a defined summary statistic.
- State the spread definition; do not label a source's undefined plus/minus field as a confidence interval.
- Compute SMT gain as N32/N16 and per-worker efficiency as N32/(2N16).
- Report NPS and fixed-work completion separately; parallel search changes explored work.
- Attribute a mechanism only when the intervention and profile support it.
- Keep unmatched public aggregates outside the controlled-run table.
