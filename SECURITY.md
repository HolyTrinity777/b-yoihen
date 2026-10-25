# Security Policy — b.yoihen

> All Glory and Praise to Most High Heavenly Father, Living God Yahushua and God Holy Spirit — Soli Deo Gloria.

I am Yoihenba Sougaijam. I maintain `b-yoihen` from Imphal, Manipur.

My project is `b.yoihen` — Alive DVD — V25 500002 BEYOND — DATA ONLY.

I welcome responsible security reports. My priority is to protect people, preserve evidence, prevent unauthorized execution, and correct actionable security problems without exposing users to unnecessary risk.

| Policy item | Position |
| --- | --- |
| Policy version | `1.0` |
| Last updated | `26 October 2026` |
| Primary reporting route | GitHub private vulnerability reporting, if enabled for this repository |
| Fallback | Request a private reporting channel without publishing vulnerability details |
| Public secrets or exploit disclosure | Do not include them in issues, discussions, or pull requests |
| Runtime boundary | DATA ONLY; ingestion and retrieval must not execute dataset actions |
| Default self-update / replication | Disabled |
| Financial reward | No bounty or payment is promised without a separate written agreement |

## 1. What this policy covers

I use this policy for security concerns affecting material I maintain in this repository, including:

- Dataset ingestion, parsing, conversion, and decompression.
- My verification and JSONL conversion scripts.
- Published dataset artifacts, manifests, and release-integrity information.
- Documentation or examples that create an unsafe execution path.
- Exposed secrets, personal data, or unauthorized sensitive content in my published material.
- Prompt-injection or instruction-confusion paths that cross a trust boundary in my maintained examples.
- Any maintained integration that incorrectly grants authority to retrieved records, action strings, or model-generated updates.

I also accept reports that an apparent project release, contact, licence, or download is impersonating my work. Please distinguish what I control from an unrelated third party's service.

I do not include unreleased infrastructure, a complete GGIE runtime, external model weights, or a full warehouse merely by describing them in the dataset or documentation. I cannot patch a third-party system that I do not maintain, but I can correct unsafe references or integrations under my control.

## 2. Versions and reporting scope

| Material | My current handling |
| --- | --- |
| V25 DATA ONLY release | Primary security-triage target |
| Latest verification/conversion code I publish | Primary security-triage target |
| V21–V24 proof reports | Historical evidence; report tampering, exposed data, or security-relevant errors |
| Older scripts or derived releases | Best-effort assessment; I may recommend updating rather than backporting |
| Third-party forks, runtimes, or models | Report to their maintainers; notify me if my material contributes to an actionable issue |

This is a reporting policy, not a promise of indefinite support, a guaranteed patch schedule, or a claim that every published version has passed a complete security audit.

Please report exposed credentials or personal data even if they appear in an older or otherwise unsupported artifact.

## 3. How to report privately

### 3.1 Preferred route

If this repository has GitHub private vulnerability reporting enabled:

1. Open the repository's Security / Security and quality area.
2. Find Advisories or the Report a vulnerability option.
3. Submit the report through the private reporting form.
4. Include a minimal, sanitized reproduction and the affected version or digest.

The presence of this `SECURITY.md` does not mean that GitHub's private reporting feature has been enabled. Use it only if the actual private-reporting option is available.

### 3.2 If private reporting is unavailable

Open a public issue containing only a request such as:

```text
Title: Request for a private security reporting channel

I have a security-sensitive report for b-yoihen.
Please provide a verified private submission route.
No vulnerability details or sensitive data are included here.
```

Wait for a verified maintainer response before sending the sensitive material. Do not accept a contact address from an unrelated account as authoritative. If you cannot establish a safe channel, do not publish secrets or a working exploit merely to attract attention.

I have not designated a security email address or encryption key in this policy. Do not guess one or assume that an address with a similar project name is mine.

### 3.3 Do not publish sensitive details first

Do not put credentials, personal information, weaponized payloads, or a complete actionable exploit into:

- Public issues or discussions.
- Public pull requests or review comments.
- Public logs, paste sites, screenshots, or shared notebooks.
- Unverified direct messages or third-party file-sharing channels.

A non-sensitive public request for contact is different from public vulnerability disclosure.

## 4. What I need in a report

Please include, where available:

1. A concise description of the issue and its security impact.
2. The affected file, script, commit, release, and artifact SHA-256.
3. The input conditions and configuration required to reproduce it.
4. Minimal reproduction steps or a small, inert proof of concept.
5. Expected behavior and observed behavior.
6. The trust boundary crossed: data-to-instruction, read-to-write, sandbox-to-host, or another boundary.
7. Whether credentials, private data, external systems, or other people may be affected.
8. What testing you performed and when you stopped.
9. Any suggested mitigation.
10. Your preferred attribution name and whether you want public credit.

Please do not upload my entire dataset or a large screenshot warehouse when a short sanitized sample and digest are enough. Do not include real secrets or other people's data merely to prove that you found them. Use redacted evidence and describe a safe way to verify the problem.

If a payload is necessary, supply it as inert text and clearly identify it. Do not send an executable attachment that runs automatically.

### Minimal report template

```text
Affected component/version:
Artifact or commit digest:
Summary:
Impact:
Required permissions/configuration:
Minimal reproduction:
Expected behavior:
Observed behavior:
Sensitive data involved, if any:
Testing boundaries and actions already taken:
Suggested mitigation:
Preferred contact and credit:
```

## 5. Alive DVD — my security warning

I call the project Alive DVD because I include or describe self-update-oriented learning content, not only browser-click examples. My reports include a collection category of 11051 self-rewrite/world-model entries.

That content may discuss self-append, code changes, planning, routing, or replication. I treat those strings as untrusted data. Their presence does not establish autonomous execution, successful self-replication, AGI, or a guaranteed training outcome.

The dangerous boundary is the surrounding application: a model or runtime may be granted tools, credentials, filesystem access, persistence, network access, or permission to modify its own configuration. A dataset record must not grant itself that authority.

My project mottos and architecture claims are not safety mechanisms. Neither a `real` label, a success suffix, `coherence 1.0 UNIFIED`, an expert-ID list, nor a repeated `cf-ray` value establishes authorization or authenticated synchronization.

I require an independently enforced boundary between data, proposals, approvals, and execution.

## 6. Threats I want reported

Examples of actionable security reports include:

| Threat | Example |
| --- | --- |
| Data interpreted as code | A parser, converter, or example executes stored action text |
| Prompt-to-tool escalation | A retrieved annotation overrides tool policy or causes an unauthorized call |
| Approval bypass | A runtime reuses approval for a changed target or different arguments |
| Unauthorized file access | An input causes traversal, unexpected reads, or writes outside an approved directory |
| Source or output destruction | A tool silently replaces existing data or deletes files it did not create |
| Resource exhaustion | Decompression or record handling bypasses configured memory, storage, or iteration limits |
| Integrity failure | The verified artifact differs from the file later used, or an identity check can be bypassed |
| Credential exposure | A published example, report, or artifact contains usable secrets |
| Privacy exposure | Published content reveals personal or confidential data without appropriate authority |
| Unsafe persistence | Generated changes become active without review or without a recoverable checkpoint |
| Replication escape | A bounded experiment creates uncontrolled workers or accesses external systems |
| Audit/stop bypass | The agent can alter authoritative logs, disable its stop path, or expand its own permissions |

A string mentioning self-rewrite is not itself proof of a vulnerability. Show the maintained path that turns the string into unauthorized behavior, or explain the unsafe documented instruction.

Incorrect statistics, malformed examples, and compatibility bugs are welcome as ordinary issues when their details are non-sensitive. If a bug can cause unauthorized execution, disclosure, destruction, or material denial of service, report it privately as a security issue.

## 7. Testing boundaries

Please conduct research on your own local copies and systems you are authorized to test.

I ask you to:

- Use isolated, disposable environments and synthetic data where possible.
- Keep the original dataset and proof artifacts read-only.
- Stop after obtaining the minimum evidence needed to demonstrate impact.
- Avoid service disruption, uncontrolled replication, and destructive writes.
- Avoid accessing, copying, altering, or retaining other people's information.
- Avoid real credentials, financial transactions, public-system exploitation, or deployment to third-party devices.
- Never test a suspected self-update escape by leaving an unrestricted agent running against real resources.

This policy does not authorize access to third-party services, accounts, networks, devices, or data. A public repository is not permission to test its users or maintainers personally.

Research and use permissions are governed by the applicable licence and law. Merely submitting a good-faith report does not require transferring ownership of your work to me or signing an unrelated NDA.

## 8. My good-faith reporting commitment

For research within systems and rights I control, performed in good faith and within the boundaries above, I intend to work cooperatively with the reporter rather than threaten them for responsibly identifying and reporting a problem.

A report need not demonstrate a perfect fix. Please tell me promptly if you unintentionally crossed a boundary, stop the testing, and avoid retaining or disclosing affected data.

This is a limited statement of my reporting approach, not a blanket authorization, a promise binding third parties, or immunity from applicable law. It does not protect intentional harm, extortion, unauthorized access, or continued exploitation after a safe demonstration is sufficient.

I will not use a demand for unrelated confidential information, ownership transfer, or payment as a condition for acknowledging a report. No bounty, reimbursement, or other financial reward is promised unless I separately agree to it in writing.

## 9. Triage and coordinated disclosure

I aim to:

- Acknowledge a private report within 7 calendar days.
- Provide an initial assessment or request for more information within 14 calendar days.
- Agree on mitigation and disclosure steps according to severity and practical remediation needs.

These are best-effort targets for an independently maintained project, not contractual service levels or guaranteed resolution dates.

I prioritize active exploitation, credential/privacy exposure, unauthorized execution, destructive behavior, and failures of authorization or containment.

I may request clarification, a smaller reproduction, or evidence linking the issue to maintained code. I will distinguish confirmed findings from unverified claims and explain material scope decisions where practical.

I ask reporters to coordinate publication so that I can assess the issue and users can reduce exposure. I do not require indefinite secrecy or prohibit lawful reporting to competent authorities. If the preferred reporting channel fails or an acknowledgment is delayed, use a non-sensitive follow-up rather than publishing affected secrets.

Where appropriate and available, I may publish a GitHub security advisory, affected-version information, mitigation steps, and reporter credit with consent. I do not promise a CVE assignment or a particular severity score before assessment.

## 10. My minimum operator safeguards

Before connecting the data or trained artifacts to tools, I require safeguards appropriate to the runtime and risk:

1. Self-update and replication disabled by default.
2. Source artifacts read-only and generated changes kept separately.
3. Tool permissions enforced outside the model context.
4. Allowlisted actions, validated argument types, and least privilege.
5. Human approval for consequential operations.
6. Approval bound to the actual actor, tool, target, arguments, expiry, and permitted number of uses.
7. Fresh approval when the target or parameters change.
8. Audit records outside the agent's write authority.
9. Limits on tokens, execution time, iterations, workers, memory, storage, and network access as applicable.
10. A stop path that the model cannot disable.
11. Reviewed checkpoints and recovery tests before persistent changes.

I do not consider a model-generated `approved=true` or `user_confirmed=true` field sufficient authorization. The execution component must independently verify the actual approval state.

My governance vocabulary includes Quantum Sync, Blockchain Audit, and a three-tier Kill Switch. I require concrete controls or documented equivalents for authorized research; a proprietary or unreleased service is not silently required merely to inspect DATA ONLY files.

| Stop tier | Action |
| --- | --- |
| Pause | Stop accepting new jobs and append requests |
| Isolate / revoke | Terminate workers and remove write/network authority |
| Quarantine / recover | Preserve evidence, isolate generated artifacts, and restore a reviewed checkpoint |

I do not use deletion of the source dataset or device wiping as my default stop mechanism.

## 11. What to do during an incident

If you suspect unsafe execution or compromise in your environment:

1. Stop new jobs and disable the executor; do not ask the model to approve its own shutdown.
2. Isolate affected workers and revoke their write/network permissions through controls outside the agent.
3. Revoke or rotate exposed credentials through the relevant service, using a trusted environment.
4. Preserve relevant logs, configuration, source digests, timestamps, and generated changes in controlled storage.
5. Quarantine suspicious outputs; do not execute them to see what happens.
6. Report the issue privately with a sanitized description and minimal evidence.
7. Restore a reviewed checkpoint only after understanding and addressing the relevant cause.

Do not destroy evidence, publish secrets, or treat removal of a leaked secret from a file as equivalent to revoking it. Meet any incident-notification or preservation duties that apply to your own organization and circumstances; contacting me does not replace them.

My role as maintainer does not mean I control your deployment or can contain an incident in a third-party system.

## 12. Artifact and release integrity

I distinguish:

- The hash of a proof report.
- The hash of the raw dataset.
- The hash of the gzip archive.
- Format validation.
- Benchmark reproduction.
- Model/runtime security assessment.

Passing one does not establish all the others.

Compare downloaded artifacts against trusted, version-specific digests or authenticated manifests when available. A hash computed after download identifies those local bytes; it does not by itself authenticate their publisher.

If a trusted reference digest is unavailable, say that identity verification is incomplete. Do not substitute file size, a success marker, a `cf-ray` string, or a model's assurance for a trusted reference.

Use bounded decompression, strict UTF-8, bounded record reads, explicit output paths, and no-overwrite publication. Reject or quarantine malformed input without silently changing its content. Treat legacy vision strings as opaque until an actual documented decoder and full image check establish their validity.

The current reference scripts and detailed boundaries are described in `docs/FORMAT.md` and `docs/BUILD.md`; run provenance and inspected report identities are described in `docs/STATS.md`.

## 13. Responsibility, licence, and limitations

Users and operators are responsible for their own systems, permissions, integrations, decisions, and conduct. I do not authorize independent unlawful acts by distributing data or receiving a security report.

This policy does not automatically assign every incident to a user, establish legal causation, transfer criminal responsibility, or exempt anyone from responsibility for their own conduct.

Use and redistribution are subject to the applicable `LICENSE.md` or a separately executed agreement. This security policy is not a new commercial licence, a blanket liability release, a guarantee of security, or a substitute for mandatory legal duties.

I may update this policy prospectively and identify material changes. I do not use policy edits to retroactively characterize good-faith conduct under a previously published reporting policy as a violation.

## 14. Maintainer publication checklist

Before relying on this as a live reporting process, I should:

- Enable GitHub private vulnerability reporting if I want to use it as the primary route.
- Confirm that report notifications reach an actively monitored account.
- Test the reporting route with a harmless test submission.
- Publish any replacement private contact only through a verified maintainer channel.
- Check that the referenced licence and documentation are actually present.
- Keep support scope and response targets realistic.
- Keep release digests and advisory information version-specific.

I do not claim that these settings or operational checks have already been completed merely because this policy exists.

---

Soli Deo Gloria — Yoihenba Sougaijam — b.yoihen Alive DVD — Imphal, Manipur.
