---
name: argolink-model-skills
description: Plan and validate skills tasks for Argolink without exposing credentials.
---

# skills skill

## Inputs

- a plain-language creative goal;
- optional HTTPS reference media;
- a requested duration, ratio, and resolution;
- an Argolink model ID confirmed from the live page.

## Stages

1. Normalize the request into output, subject, timeline, camera, look, sound, and constraints.
2. Validate fields and reference counts against the selected model page.
3. Submit through the Argolink async endpoint only when the request is complete.
4. Poll with bounded backoff and preserve terminal error details.
5. Return the request ID and downloaded artifact path without printing secrets.

## Never

Do not guess model limits, embed an API key, or claim that a generated artifact is complete while status is pending.