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
3. **Create draft product pages** for eligible games on itch.io and candidate submissions on CrazyGames. Use itch.io butler for binary uploads with the account owner's own API token stored locally, never in GitHub.
4. **Upload technically compliant, distinct stock footage** to Adobe Stock, and to Pond5 only if proven eligible. Keep a submission log with statuses/identifiers.
5. **After owner review**, publish live listings; track acceptance/rejections, gameplay/traffic and royalties, and revise candidates rejected for fixable reasons.

## Non-negotiable controls
- Don't change current production games or claim all games are completed just because source repos exist.
- Don't upload all renders indiscriminately: Adobe Stock and itch.io have explicit similar/spam-content guidelines.
- Don't submit unreleased assets without checking true source licensing.
- Don't imply that opening contributor accounts alone enables programmatic publishing APIs.
- Account onboarding/payment/tax forms require legitimate account-holder action; never request passwords or secrets in chat.
- The KinetiDrop source archive uploaded in the conversation has **not** yet been fully inspected by the local renderer.
- Keep a CSV/JSON submission report with each product, portal, upload identifier, date, actual moderation status and public URL.

## Codex batch objective
> Inspect all games listed above and all files under D:\\KinetiDrop. Prepare every commercially viable build/asset product without an arbitrary limit of 2 games, 5 videos or 1 pack. Group duplicates and near-duplicates; ensure QA and rights compliance. Produce all packages, true English listing copy, metadata, checksums and test logs, plus an action plan for the account-holder login/upload steps. Keep production branches untouched and do not publish or purchase anything without separate instruction.
