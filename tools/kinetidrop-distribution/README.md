# KinetiDrop marketplace preparation (local-first)

Experimental production tooling for **Adobe Stock / Pond5 / itch.io**. It does NOT log in to accounts, submit anything, or promise marketplace acceptance. Source archive remains on the creator's PC.

## One source, two commercial candidates
Use **PrecisionAssemblyV2.zip** or the extracted project folder as the source. Run from any directory with Python 3.10+.

```powershell
python tools/kinetidrop-distribution/prepare.py inspect --source "D:\\KinetiDrop\\PrecisionAssemblyV2.zip" --out "D:\\KinetiDrop\\marketplace\\audit"
python tools/kinetidrop-distribution/prepare.py stock --source "D:\\KinetiDrop\\PrecisionAssemblyV2.zip" --out "D:\\KinetiDrop\\marketplace\\stock"
python tools/kinetidrop-distribution/prepare.py asset --source "D:\\KinetiDrop\\PrecisionAssemblyV2.zip" --out "D:\\KinetiDrop\\marketplace\\assets"
```

- **inspect** creates `inventory.json` (file counts, extensions, videos, Blender scenes).
- **stock** requires FFmpeg and ffprobe on PATH; outputs silent H.264 MP4 technical candidates and `stock_review.csv`. The conservative 1080p / 5–60 second filters are not proof of upload suitability.
- **asset** creates `blender_pack_candidate.zip` including discovered .blend and texture files and a DRAFT listing. It is **not** proof that Blender references are packed or that assets are sale-ready.
- To embed files into a separate Blender copy, use `blender -b original.blend --python tools/kinetidrop-distribution/blender_pack.py -- --out packed_copy.blend`. Check the pack report and visually render the packed scene in Blender before replacing raw source files in the sale package.

## Rights, creative provenance and quality gates
1. Verify exclusive/redistribution rights to geometry, models, fonts, textures, music and footage. **A commercial-use license is not automatically a resale-of-source license.**
2. Review whether any actual footage was synthesized by a generative AI model. **Pond5 currently does not accept AI-generated content**. Procedural Blender simulations require a truthful provenance assessment, not an invented label.
3. Adobe Stock generative AI footage must use the platform's generative AI declaration where applicable. Review current rules and labels.
4. No commercial soundtracks. All stock candidates are rendered without audio tracks.
5. Check actual frames for banding, motion artifacts, logos, IP/trademarks, watermarks, focus and lighting. A technically valid MP4 can still be refused.
6. All titles and keywords must describe **visible actual content**, not guessed content from filenames.
7. Confirm payment/tax/identity setup directly in each contributor account. No banking details or login secrets in this repo.
8. Do not upload duplicate or near-duplicate clips just to increase the catalog.
9. Keep Blender source and preview files separate from stock deliverables; sell only materials the creator can legally redistribute.

## Codex task — proceed on the creator's Windows computer
> Work in `D:\\KinetiDrop` with the uploaded archive `PrecisionAssemblyV2.zip`. First run `inspect`. Open and render the real Blender scenes using the installed portable Blender 3.6 (do not assume the executable path). Inspect footage visually and verify no third-party models/audio. Run `stock` and `asset`, correct errors, pack source textures, produce a polished English itch.io listing and factual Adobe Stock/Pond5 metadata for each approved clip. Ensure a 16:9 Full HD or better export where feasible. Write a release report with exact filenames, durations, resolutions, SHA256s, provenance and QA evidence. Do not upload or publish to any platform without a separate explicit instruction. Do not touch YouTube uploads or published game releases.

## Distribution and payment reality
- itch.io: upload downloadable ZIP as an asset/product only after file/package QA and finishing tax/payment setup.
- Adobe Stock: upload individual approved video files; complete titles, accurate keywords, AI labeling when required, and relevant releases.
- Pond5: only original human-authored/computer-generated footage compliant with its current anti-generative-AI policy; creator confirms provenance before submission.
- Product and clip sales are **not guaranteed**.
