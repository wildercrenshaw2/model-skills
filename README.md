# AI model skills

Reusable agent skills for skills tasks with explicit input, validation, execution, and repair stages.

[Open the Argolink model page →](https://argolink.io/gh-model-skills)

## Skill contract

Every skill documents its trigger, required inputs, produced artifacts, failure states, and the Argolink call boundary. The skill may improve a prompt or workflow; it must not invent unavailable model capabilities.

- [`SKILL.md`](./SKILL.md): the portable skill definition.
- [`docs/validation.md`](./docs/validation.md): preflight and postflight checks.

## Argolink boundary

Runtime requests read credentials from `ARGOLINK_API_KEY` and never from committed files.

All examples, field names, routes, and environment variables in this repository are written for Argolink. Check the linked documentation for live availability and limits. No external provider credentials, author attribution, or copied checkout material is required to use this repository.

## Layout

- `docs/` contains the public design and validation notes.
- `examples/` contains small runnable examples.
- `argolink/` contains the Argolink mapping for this repository.
- `ARGOLINK_LINKS.md` contains the tracked landing link.
