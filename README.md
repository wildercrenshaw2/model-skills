# AI model skills

Four narrowly triggered Agent Skills procedures for concrete model work: GPT Image 2 image generation, Seedance 2.5 video, MiniMax H3 video, and OpenAI-compatible GPT-6 Sol Responses text. Each SKILL.md has YAML frontmatter, model-specific validation, a runnable request example, and an explicit failure boundary. They are community-maintained procedures, not official vendor packages.

[Open the live model directory](https://argolink.io/gh-model-skills) before using a procedure. Last checked: 2026-10-07.

## Skill index

| Directory | Trigger | Model-specific checks |
| --- | --- | --- |
| skills/image-generation | concrete GPT Image 2 image or edit | pixel size, quality, n, 1–16 edit references, output format |
| skills/video-generation | Seedance 2.5 video | 4–30 seconds, adaptive frame/edit ratio, 30/10/10/50 references |
| skills/minimax-h3-video | MiniMax H3 video | 768p versus 2k, 7,000-character prompt, audio requires visual reference |
| skills/text-responses | tool-enabled text request | gpt-6-sol Responses endpoint, effort, context and usage |

The index is intentionally not a generic model catalog. The examples use https://argolink.io/v1 as the API base, but the provider identity and model IDs remain explicit.

## Installation

An Agent Skills package keeps a directory and its SKILL.md together. Inspect the current host documentation before copying:

- Claude Code commonly discovers project skills in .claude/skills/<name>/SKILL.md and user skills in ~/.claude/skills/<name>/SKILL.md.
- Codex uses the configured CODEX_HOME/skills directory or a supported project skills directory.
- Cursor's Agent Skills discovery and global/project settings can change between releases.

Install only the directories the host should be allowed to select. Secrets go in the host environment, never in frontmatter, sample prompts or source control.

## Shared request discipline

Before an external side effect, read the current model page, confirm the exact model ID, validate fields, show the body when an approval step exists, and choose an output path. Every urllib or HTTP request in these examples uses a descriptive User-Agent. An ambiguous POST is not evidence of failure; preserve the request record and investigate before submitting again.

Video lifecycle is POST /v1/videos/generations, persist request_id, GET /v1/videos/{request_id} until pending becomes done/failed/expired, then GET /v1/videos/{request_id}/content. Image and text requests preserve their response and usage fields. Unknown statuses are errors.

## Model facts and costs

The values were checked on 2026-10-07:

- GPT Image 2: 1K and 2K are 0.015 USD per returned image; 4K is 0.02. The requested size is actual pixels and the returned longest edge determines the billed tier.
- Seedance 2.5: 4–30 seconds; 480p/720p/1080p; 0.0874/0.196/0.483 USD per output second. Frame and edit modes use adaptive ratio; reference video seconds add to billing.
- MiniMax H3: 4–15 seconds; 768p or 2k; 0.039/0.064 USD per second. Reference audio must accompany an image or video.
- GPT-6 Sol: 0.60 USD per million input tokens and 3.00 USD per million output tokens; use Responses for reasoning and tools.

These are dated service-catalog facts, not universal defaults. If a field is omitted by a live page, the skill says to stop and verify rather than fill it from another model.

## Testing

~~~sh
python -m unittest discover -s tests -v
~~~

The test checks all four frontmatters and model-specific content. The skills themselves do not contact a provider and do not require a key.

## FAQ

**Are these official skills?** No. They are reviewable procedures. **Why separate them?** A narrow trigger prevents an image request from selecting a video workflow. **Can I install all four?** Yes if the host's discovery rules and review policy allow it. **What if a field changes?** Update only after reading the current primary model page and record a new check date. **Can I use a private media URL?** Only through an authenticated, documented upload or fetch flow; do not publish private URLs.
