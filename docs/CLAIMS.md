# Claims and Evidence — b.yoihen

I keep my README in my own voice. I use this document to connect technical claims to their actual evidence and identify what would strengthen them.

## 1. Evidence categories

- Recorded: a field or statement present in a supplied run report.
- Measured locally: computed from identified bytes by a named tool/configuration.
- Demonstrated: supported by an execution package with inputs, actions, outcomes, and environment.
- Reproduced independently: obtained by a separate reviewer using the stated protocol.
- Architecture / positioning: my intended design or project claim, not an execution result by itself.

One category does not automatically imply the next.

## 2. Claim-to-evidence map

| Claim | Present source | Current boundary / next evidence |
| --- | --- | --- |
| V25 reports 500002 records and 1147108255 raw bytes | `proof/benchmark_500002_real_measured.json` | Run the manifest generator against the actual archive |
| Gzip release size is 19785162 bytes | My release specification | Measure the local archive and publish its digest |
| V25 records 367/369 completion | V25 aggregate fields | Publish runner, task IDs, environment, evaluator, and per-task results |
| Earlier runs show an evaluation progression | V22–V25 reports | Separate report continuity from independent benchmark reproduction |
| V23 includes code/self-healing content | V23 `self_collected` | Inspect source topics and demonstrate a bounded code-repair experiment |
| V24 already includes 11051 self-rewrite/world-model entries | V24 `self_collected`, retained in V25 | Identify corresponding dataset records; do not assume all are new in V25 |
| My V21 configuration uses eight 1.6 GB active allocations | V21 `moe.warehouse` | Measure actual artifacts and resident runtime allocations |
| My intended routing uses eight active positions | Configuration and architectural clarification | Separate 8/250 = 3.2% from 8/256 = 3.125%; supply the actual routing implementation |
| My architecture records 193 shards | V21 and later method/discovery fields | Do not claim 193 physical national deployments from those fields |
| My total knowledge MAP is 10T+ | My architecture/positioning | Define the unit, inventory, coverage, and verification method |
| My model can execute a governed self-update | Learning objective / architecture | Provide an actual proposal-to-approval-to-change-to-evaluation experiment |
| My architecture can self-replicate across 11 CPU nodes | My design claim | Demonstrate a bounded multi-node run with actual resource measurements |
| This is first globally | My novelty claim | Define the contribution and conduct a related-work/priority analysis |

## 3. What the supplied sample proves

The proof sample preserves values present in seven V25 report objects and maps them to their JSON locations. It demonstrates that a reader can parse and inspect those values without executing them.

It does not establish captured screenshots, actual raw-dataset line numbers, complete category counts, successful self-replication, or a fresh benchmark run.

The two reported failures have failure result fields despite success-marker text in their annotations. Structured reported outcomes are retained in the sidecar; an inspector must not infer them from the four-field suffix.

## 4. Build-history views

The author-approved endpoint/checkpoint chain is:

```text
31695+6525=38220 -> 38220+6525=44745 -> 44745+125000=169745
-> 169745+130255=300000 -> 300000+112972=412972
-> 412972+87030=500002
```

The V24 report separately records its actual batch base:

```text
282717+130255=412972
```

I preserve both and do not present them as the same chronological batch ordering.

## 5. What I will not infer

- A `real` class is not a provenance audit.
- A success annotation is not an execution outcome.
- A topic count is not a parameter count.
- Configured storage is not measured resident memory.
- Eight of 250 is not 3.125%.
- A hash is not publisher authentication without a trusted reference.
- A hash chain alone does not establish who authorized an event or whether its contents are true.
- A data file describing self-update is not an already running autonomous system.
- A green tooling CI job is not benchmark replay or training.

## 6. Next experiment package

Before claiming demonstrated governed self-update, I should preserve:

1. Exact source data and code identities.
2. Model/runtime version and permissions.
3. Proposed change and its scope.
4. Actual approval identity and approved arguments.
5. Isolated execution record.
6. Before/after tests, including regressions and failures.
7. Audit evidence outside the agent's write authority.
8. Persistence decision or rollback outcome.

I publish real run artifacts only after performing the run. I do not create success-shaped placeholder logs to fill this checklist.
