# LuSor Games + KinetiDrop — portfolio distribution register

Goal: **evaluate every previously created game and every reusable original asset for publication**. This is a candidate register, not a declaration that the assets have been published.

## Games found in the owner's connected GitHub

| Title | Repository | Engine | Initial route | Current gate |
|---|---|---|---|---|
| LookTwist: Hidden Objects | lusor83/looktwist | Godot 4.6.3 | CrazyGames + itch.io HTML5 | HTML5 artifact generated; browser functional QA outstanding |
| Nerelune: Secrets of the Cove | lusor83/Nerelune | Godot 4.6.3 | CrazyGames + itch.io HTML5 | HTML5 artifact generated; browser functional QA outstanding |
| Hacker Game | lusor83/hacker-game | Godot 4 (4.3 metadata) | CrazyGames + itch.io HTML5 | HTML5 workflow in draft PR; awaiting result + QA |
| Baggage Color Flow | lusor83/baggage_color_flow | Unity 2022 LTS | Unity WebGL for portals, Android package for itch.io where permitted | Port / export + gameplay QA needed |
| Astral Fusion (StellarMerge) | lusor83/StellarMerge | Flutter/Flame/Forge2D | Flutter web or packaged Android build on itch.io | Web support, Forge2D compatibility and controls QA needed |
| Life Unwritten | lusor83/newhand | Expo / React Native | Web build or Android on itch.io | Web parity and UI testing needed |
| Ruinshot | lusor83/Ruinshot | Godot planned | itch.io when playable | Repository README describes vertical-slice direction; playable runnable build not yet evidenced |

Other GitHub projects (e.g. PartySketch Studio, SafePath and FoodPilot) are not part of the **games** catalog; assess separately if the owner wants to distribute standalone software.

## KinetiDrop and production assets

- Run `tools/kinetidrop-distribution/prepare.py inspect` against the complete on-disk KinetiDrop tree, not just a single ZIP, to inventory all `.blend`, original `.mp4`, textures and dependencies.
- Record each distinct creative concept once in the inventory. **One project may have several truly different footage clips**, but avoid submitting near-identical versions to stock sites.
- For each video: source project, authorship/provenance, third-party rights, original source, duration, dimensions, codec, QC decision, Adobe Stock readiness and Pond5 eligibility decision.
- For each Blender source: dependencies packaged, smoke-open/render, rights to redistribute source files, correct license, product preview, version and archive checksum.
- For product packaging, prefer a coherent product per asset family or project, and bundles for related materials; **do not create many near-identical itch.io pages**.
- Pure Blender procedural animation is not necessarily generative-AI-generated footage. However, renders of AI-synthesized footage must not be mislabeled. Pond5's prohibition on AI-generated materials requires individual provenance checks.
- Exclude licensed soundtracks, third-party logos and models without source redistribution rights.

## Batch distribution in stages

1. **Inventory** every game, render and Blender project.
2. **Build/QA** every viable web candidate and commercial bundle; gather genuine screenshots/previews and metadata.
3. **Create and publish eligible game/product pages** on itch.io and submit verified browser candidates to CrazyGames using authorized authenticated accounts. Use itch.io butler where supported, with credentials held locally, never in GitHub.
4. **Submit all distinct, eligible stock footage** to Adobe Stock; submit to Pond5 only where confirmed compliant. Log actual submission IDs and statuses.
5. **No per-item approval required** for validated, original, free-to-publish listings. Keep track of acceptance, moderation, rejections, analytics, and revenue. Report every published, submitted or blocked item with actual evidence.

## Non-negotiable controls
- Don't change current production games or claim all games are completed just because source repos exist.
- Don't upload all renders indiscriminately: Adobe Stock and itch.io have explicit similar/spam-content guidelines.
- Don't submit unreleased assets without checking true source licensing.
- Don't imply that opening contributor accounts alone enables programmatic publishing APIs.
- Account onboarding/payment/tax forms require legitimate account-holder action; never request passwords or secrets in chat.
- The KinetiDrop source archive uploaded in the conversation has **not** yet been fully inspected by the local renderer.
- Keep a CSV/JSON submission report with each product, portal, upload identifier, date, actual moderation status and public URL.

## Codex batch objective
> Inspect all games listed above and all files under D:\\KinetiDrop. Prepare and **actually publish/submit** every eligible commercial game build, distinct video and asset pack using the owner's authenticated marketplace accounts (CrazyGames, itch.io, Adobe Stock, Pond5 as applicable). The owner explicitly authorized publication of commercially compliant content without additional per-item review. Run actual functional and license QA, record true listing names, URLs/IDs, prices, terms, checksums, upload timestamps and moderation statuses. Do not claim completion without an actual successful remote submission, and do not confuse “pending review” with “published.” Avoid duplicate/spam uploads. Keep existing production game releases untouched unless required and safe. Never spend money, purchase ads, enroll in paid plans, grant exclusivity, accept new binding paid commitments, or publish content without verified redistribution rights. Pause only when legal identity/tax/payment verification, login/MFA, or uncertain rights require owner involvement. Deliver an evidence-backed summary at completion.


## Explicit owner authorization — 2026-11-22

The owner authorizes the operator/Codex to **publish or submit** the full set of newly prepared, verified content to the four marketplace accounts, **without a separate confirmation for each listing**. This updates the earlier “do not publish” instructions in this plan; it does not override platform law, safety, licensing or user-account authentication requirements.

- **Permitted**: technical adaptation, QA, royalty-free resale of wholly owned assets, approved creator-account listing creation, non-exclusive distribution and commercially reasonable listing prices with recorded rationale, submission and publication where allowed, correction of rejected compliant items, and final reporting.
- **Not permitted**: unverified content rights, unauthorized use of copyrighted music, reuse/resale of third-party source assets without redistribution license, AI-labeled footage incorrectly represented, duplicate flooding, purchases or ad spend, fee-bearing subscriptions, exclusive contracts, transferring IP ownership, publishing private repository source code instead of compiled games, disclosure of account/payment credentials, and bypassing moderation.
- **Needs owner action**: mandatory identity checks, tax declarations, payout account setup, login challenges, terms requiring a verified personal act, or a substantive legal/licensing uncertainty.
- **Completion report**: one row per artifact and per destination with source repo/path, release build checksum, true product title, price (if any), platform, submission/listing ID, public URL (if available), exact status (draft/submitted/in-review/approved/live/rejected/blocked), evidence reference, reason if blocked, and any immediate sales data actually available. Include a separate summary of ready-but-not-uploaded and excluded items; never invent acceptance or sales.
- **Where to save**: a dated report and machine-readable CSV in a dedicated local or GitHub report location, omitting credentials and sensitive personal data. Deliver a plain-language recap to the owner when the run ends; do not claim future monitoring unless it is actually scheduled.


## Permanent workflow for every new KinetiDrop video — owner decision 2026-11-26

**Priority and scope:** KinetiDrop video production is the primary activity. Commercial distribution is a mandatory downstream step for every new completed production, not a separate creative assignment. Apply this section to all future KinetiDrop episodes and formats in the local workspace, even when the initial request only concerns producing a video. It supersedes older destination lists and session-specific no-upload instructions for eligible commercial assets; it does not override separate social-video approval gates, rights, platform rules or safety requirements. Do not change RacingHub or game releases.

### Production-to-market deliverables
- Produce the approved social video and retain its editable Blender source, scripts, dependencies, textures/materials, reusable geometry, and render settings.
- Save clean original footage without social text, watermark, third-party music or branding; choose useful distinct commercial clips (native dimensions and frame rate, ProRes MOV or another accepted format where appropriate). Preserve the best available master; do not upscale or claim unsupported quality.
- Where the video yields a genuinely useful distinct asset, assemble a coherent Blender pack with relative/packed dependencies, a tested archive, README, license, representative actual previews, version/engine information and checksum. Optional FBX/OBJ/glTF only when compatible with the asset and tested; do not promise lossless animation/material transfer.
- Prepare English commercial title, description, relevant tags, technical specifications, pricing and provenance. Document actual human creative direction, editing and post-production and the use of AI-assisted scripting and workflow automation accurately; use the agreed wording when truthful: “Original 3D animations created in Blender, with human creative direction, editing and post-production, supported by AI-assisted scripting and workflow automation.” Complete mandatory platform declarations truthfully. Do not claim manual authorship or omit required disclosures.
- QA the actual files, archive, dependency integrity, previews, license, third-party rights and platform-specific requirements. Do not duplicate previous products or near-identical footage. If no commercially meaningful asset/clip results, record the reason rather than creating filler.

### Routing and current marketplace gates
| Marketplace | Material | Operational rule |
|---|---|---|
| itch.io | Blender packs and relevant bundles | Active; publish eligible new products. |
| Gumroad | Blender packs, bundles and clean downloadable footage packs | Active; publish eligible products, use EUR and coherent pricing. |
| CGTrader | Compatible 3D models/Blender packs | Active; publish eligible assets with accurate mandatory disclosures. Do not relist a suspended item or bypass review. |
| Superhive | Blender assets/templates | Creator and PayPal configured; first product Kinetic Wave Studio in review as of 2026-11-26. Submit subsequent assets only when permitted; queue eligible packages locally meanwhile. Verify current Blender/version and creator rules. |
| Fab | Compatible 3D assets | Trader verification currently Retry required. Queue locally until onboarding, tax and payout are complete and upload is enabled. |
| MotionElements | Distinct original stock footage | Contributor application submitted; wait for approval and verify current content/disclosure policy. |
| Adobe Stock | Eligible stock footage | Contributor onboarding blocked by SMS; queue compliant footage until resolved. |
| Shutterstock | Eligible stock footage | Contributor setup incomplete; verify content policy and eligibility before any submission. |
| Pond5 | Only independently eligible material | Support explicitly confirmed on 2026-11-25 that both AI-generated and AI-assisted content are not approved. Do not submit the current AI-assisted KinetiDrop workflow to Pond5. Retain the verified account for genuinely eligible future material only, unless written policy clarification changes. |

These are the recorded gates as of 2026-11-26, not permanent assumptions. Refresh relevant remote status and policy before submission. No need to recheck an unchanged blocked destination repeatedly during a single run. Keep a local queue and resume when the gate is legitimately cleared.

### Execution and acceptance
1. Once a new video is finalized, automatically carry out the commercial packaging and distribution step in the same workflow. The owner authorizes actual upload, submission and publication of eligible commercial derivatives on the listed authorized marketplaces without per-item confirmation. If a destination is blocked, continue on the others. Use authenticated authorized sessions, no new paid services, spend, exclusivity or changes to personal, tax or banking data.
2. Request owner intervention only for genuinely required authentication, identity, legal attestations, new binding terms, payment setup, unresolved rights/compliance or expenditure. Never bypass moderation or eligibility gates. Do not treat a draft, upload or moderation submission as a live product.
3. Use existing commercial prices as reference, avoid needless price changes, and record a rationale for new prices. Where appropriate use commercial product links in social captions/descriptions with the platform's permitted link format; preserve any existing separate social publishing approvals.
4. Update the existing Google Drive operational tracker (LuSor / DLF — Tracker operativo: https://docs.google.com/spreadsheets/d/1rZ3Wa9FzF09frPpNncgTeVPs5g79zowD3u8mGEhR6Xs/edit) in Catalogo, Canali, Roadmap and Log Codex. Preserve formulas and append-only history. For each asset and destination, record source project, archive/checksum, price/currency, listing/submission ID, public URL, status, date and evidence. Record actual sales only with evidence.
5. Deliver a short release report per video: social deliverable, commercial derivatives, products live/acquirable, in review, queued, excluded or blocked, prices and URLs, and only the actions genuinely requiring the owner. Never invent sales or acceptance. Keep binary files, credentials, account documents and sensitive data local, outside Git.

**Definition of done:** a finished video is not the end of the commercial workflow. Every meaningful eligible derivative must be prepared and actually published/submitted on available compatible marketplaces, or have a documented reason and queue entry for an unavailable destination. Do not delay new video production solely because a marketplace is awaiting external review.
