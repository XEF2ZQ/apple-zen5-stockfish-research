# Evidence notes

Reviewed 13 November 2026. The README is the complete article and contains the source index.

- Stockfish data: 17.1 Chess Benchmark public aggregate, reported cutoff 22 October 2026. The published plus/minus fields are not interpreted as confidence intervals.
- LLVM data: 16.0 Ninja, cutoff 7 October 2026; 21.1 Ninja, cutoff 11 November 2026. The versions are never pooled.
- Apple Stockfish numeric charts and the reported 233/192-second LLVM pair were not fully recovered. They are not included as verified measurements in the charts.
- PassMark selection: exactly five exposed recent M5 Pro 18-core baselines were read individually. BL5128734 leads that set in CPU Mark, integer and FP. All-time historical supremacy was not verified; comparable-systems browser search did not expose an exhaustive ranking.
- Both selected M5 Pro arithmetic numbers belong to BL5128734, PerformanceTest 11.0.1004. Historical M4 Max averages were labeled as V10 aggregate reporting. Their ratio is asymmetric and not a matched version-controlled test.
- An M5 Pro result is not substituted for an M5 Max Stockfish or LLVM result. Apple confirms the same 6-super/12-performance composition for the full eighteen-core CPU configurations, not identical measured system behavior.
- No software from PassMark was installed and no hardware tests were performed by this review.

## Source-code retrieval identities

| Source | Tag / path | Retrieved blob SHA |
|---|---|---|
| Stockfish | sf_17 / src/nnue/layers/affine_transform.h | 59a6149f0c40dd6d379fba733354776ee3f7417b |
| Stockfish | sf_17.1 / src/nnue/layers/simd.h | 70ca68a0c708596e8447cb53c716500179467b6d |
| Stockfish | sf_17.1 / src/bitboard.h | df15113bda3428b32721893f891d7dc748ae4440 |
| Stockfish | sf_17.1 / src/Makefile | 76b94785ecb59a3e58a57325091e1d6cff66723d |
| Stockfish | sf_17.1 / src/benchmark.cpp | a9f70f10d1a715fd1ce4f365c826a03c2ce8575e |
| PTS profiles | master / pts/stockfish-1.6.0/install.sh | 381d44906b63626bdad9f55e7fa3d7293c066197 |
| PTS profiles | master / pts/build-llvm-1.5.0/pre.sh | 70dae5cc6437b96ca593091cb71a29104695f607 |
| PTS profiles | master / pts/build-llvm-1.5.0/install.sh | 6177d7fa56701c039869fe143147407ab12f78e4 |
| m5-uarch | main / README.md | 037aeef763c884574474717ac2cb045d2467d6ea |

Blob SHAs identify file contents, not repository commits. The m5-uarch source concerns the base M5; its E-core is not the new M5 Pro/Max secondary performance core.
