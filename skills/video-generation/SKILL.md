---
name: video-generation
description: Seedance 2.5 video generation. Trigger only when the user asks for this concrete capability, and validate current model fields before a request.
---

# Seedance 2.5 video generation

Collect the user's goal, input assets, output constraints, and acceptance test. Read the live model page before selecting an ID or claiming a limit. Put secrets in the host environment, not in a prompt or skill file.

## Procedure

1. Build a small, reviewable request plan.
2. Validate fields against the current catalog and model page.
3. Show the request body or tool schema before an external side effect.
4. Use the documented endpoint and preserve the response ID.
5. Record the terminal result, output path, and any omitted fact.

## Failure discipline

Do not retry an ambiguous POST. Treat authentication, rate limits, capacity, and model validation as separate failures. Keep user content and media URLs out of committed examples. If a fact is unknown, say so and link the page that must be checked.

This skill is a reusable procedure, not an official vendor package.
