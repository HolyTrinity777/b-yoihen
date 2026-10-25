# Contributing to b-yoihen

I welcome careful code fixes, data corrections, reproducibility work, and documented improvements to b.yoihen. I am Yoihenba Sougaijam, maintaining this project from Imphal, Manipur.

## 1. Start with the applicable terms

Read `LICENSE.md`, `SECURITY.md`, and `docs/FORMAT.md`. Public availability is not an unrestricted licence. This guide does not grant commercial rights or override third-party terms.

For security-sensitive issues, use the private route described in `SECURITY.md`. Do not put credentials, personal data, or a working exploit in a public issue or pull request.

## 2. Good contributions

- Reproducible parser, converter, and verifier bug fixes.
- Bounded-memory handling and no-overwrite protections.
- Tests using clearly identified synthetic fixtures.
- Corrections linked to exact source fields or records.
- Provenance, licensing, privacy, and data-quality improvements.
- Measured experiments with complete inputs and failure reporting.

## 3. Evidence required for a data change

Identify the affected release, file digest, source record or report path, proposed change, reason, and verification method. Distinguish captured, authored, templated, and synthetic content.

Do not fabricate screenshots, success results, approvals, task histories, or benchmark logs. Do not replace a missing asset with a generated one while calling it recovered evidence.

Historical proof reports are immutable evidence inputs. Propose an explicitly identified new revision instead of silently reformatting or overwriting the old bytes.

## 4. Code boundaries

- Use the standard library unless a dependency is genuinely required and documented.
- Preserve fields exactly; split at the first three pipes.
- Preserve topic-ID case.
- Fail clearly on malformed input; do not use `errors="ignore"`.
- Bound record reads, decompression, and resource consumption.
- Refuse to overwrite or delete files not created by the current operation.
- Keep dataset text inert. No `eval`, `exec`, shell execution, uncontrolled replication, or automatic self-update.
- Do not infer evaluation success from annotation suffixes.

Include a minimal fixture, expected behavior, actual behavior, and a regression test with a code fix. State which tests you actually ran. CI is not a substitute for evidence of an unrelated capability claim.

## 5. Contribution rights

Before I merge code or data, the submission must state its proposed inbound licence and confirm that the submitter has the necessary rights and any required employer or third-party permissions. Do not assume the repository licence automatically covers all contributed material.

A contributor retains ownership unless a separate written agreement provides otherwise. Any permission for me to distribute the contribution under the public track and offer it under the commercial track must be expressly documented before merge. A public pull request alone is not treated here as a copyright assignment or an unstated relicensing agreement.

Do not submit material you cannot authorize under the intended arrangement. Ordinary issue reports do not require transferring ownership of unrelated work.

## 6. Pull-request checklist

- [ ] I identified the problem and affected files.
- [ ] I provided a minimal, non-sensitive reproduction where appropriate.
- [ ] I described source provenance and applicable permissions.
- [ ] I did not alter historical proof bytes without an explicit revision plan.
- [ ] I preserved inert ingestion and no-overwrite behavior.
- [ ] I included tests and stated which ones I ran.
- [ ] I documented actual measurements separately from expectations.
- [ ] I stated the proposed inbound licence/permissions for code or data.

I may request revisions or decline a change that weakens safety, obscures evidence, or has unclear rights. A proposal is not permission to test third-party systems or deploy autonomous code against real resources.

Soli Deo Gloria â Yoihenba Sougaijam â Imphal, Manipur.
