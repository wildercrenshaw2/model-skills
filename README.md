# AI model skills

This repository contains four small Agent Skills-style directories for concrete model work: gpt-image-2 image generation, Seedance 2.5 video jobs, OpenAI-compatible Responses calls, and model discovery. Each SKILL.md has YAML frontmatter, a trigger description, validation gates, and an explicit failure boundary. They are independent instructions, not official vendor packages. Last checked: 2026-10-07.

## Install

Copy the relevant directory under the skills directory used by your agent host. Claude Code, Codex, and Cursor expose different discovery locations and can change their settings schema; inspect the current host documentation before installing. Do not copy every skill into a production agent merely to increase trigger count. A narrow trigger gives the host a better chance of selecting the right procedure.

## Skill index

| Directory | Trigger | Required fact check |
|---|---|---|
| image-generation | A user needs a gpt-image-2 image request | size, quality, references, output encoding |
| video-generation | A user needs a Seedance 2.5 async job | duration, ratio, references, billing |
| text-responses | A user needs a tool-enabled text request | model ID, endpoint, reasoning/tool support |
| model-discovery | A user asks what models are available | current catalog and model-page URLs |

The skills intentionally do not claim prices in frontmatter. Put current values in a separate dated note after reading the catalog. The live ArgoLink pages are useful endpoints for the examples: [model index](https://argolink.io/gh-model-skills). The service is not the owner of every model mentioned.

## Common lifecycle

For a paid request, validate the model ID, request shape, key environment variable, and destination path before sending. Add a User-Agent to every urllib request. For video, POST /v1/videos/generations once, save request_id, poll /v1/videos/{id} for pending, done, failed, or expired, and download only after done. For images and text, preserve the response and usage fields. A local timeout never proves that a server job failed.

## Testing

python3 -m unittest discover -s tests checks that every skill has frontmatter and a description. It makes no network request. The skills are intentionally short enough to be reviewed in an agent transcript; they are not a replacement for a model page, API reference, or host-specific security policy.

## FAQ

**Are these official skills?** No. They are a community-maintained set of procedures. **Why four files instead of one generic skill?** Narrow triggers reduce accidental use of a video workflow for an image task. **Where do prices belong?** In dated evidence notes, not stale instructions. **Can a host run all four?** Yes if its discovery rules allow it, but install only the directories you need. **What if a model field is missing?** Stop, mark it unknown, and check the current primary page.
