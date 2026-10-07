---
name: minimax-h3-video
description: Generate MiniMax H3 video with its 768p/2k and reference-audio constraints. Trigger only for a MiniMax H3 request.
---

# MiniMax H3 video

The live model ID is minimax-h3. Use POST /v1/videos/generations at https://argolink.io/v1, then GET /v1/videos/{request_id} and GET /v1/videos/{request_id}/content. It is a video skill with facts specific to H3; do not borrow Seedance or Wan fields.

## Model-specific limits

Facts checked against the model page and catalog on 2026-10-07:

- 4–15 whole seconds; one output per request.
- 768p or 2k. There is no 720p tier.
- Prompt is required and limited to 7,000 characters.
- Text ratios are 21:9, 16:9, 4:3, 1:1, 3:4 or 9:16. Reference mode also allows adaptive.
- A first frame or first-and-last-frame request follows the first frame and uses adaptive ratio.
- Reference mode accepts up to 9 images, 3 videos and 3 audio tracks, 12 total. Each reference video/audio is 2–15 seconds and the type total is 15 seconds.
- Reference audio needs an image or video alongside it; audio-only reference is not valid for H3.
- Every result carries a generated soundtrack. The reference-video seconds are billed like output seconds.
- The effective catalog rate is 0.039 USD/s at 768p and 0.064 USD/s at 2k.

Validate these values again before a paid request. They are not a generic video schema.

## Request example

~~~python
import os, requests

payload = {
    "model": "minimax-h3",
    "prompt": "A child follows a lantern through a quiet forest",
    "duration": 5,
    "resolution": "768p",
    "aspect_ratio": "16:9",
    "generate_audio": True,
    "reference_images": [{"url": "https://cdn.example.test/lantern.png"}],
}
response = requests.post(
    "https://argolink.io/v1/videos/generations",
    headers={"Authorization": f"Bearer {os.environ['VIDEO_API_KEY']}",
             "User-Agent": "model-skills-minimax-h3/1.0"},
    json=payload,
    timeout=90,
)
response.raise_for_status()
request_id = response.json()["request_id"]
~~~

Persist request_id before polling. Poll explicitly and stop on pending, done, failed or expired. Download content only after done. Never claim that a “running” or “completed” status belongs to this contract.

## Reference media

A local image, video or audio file must go through the documented media upload ticket first. The PUT to a presigned upload URL carries Content-Type and User-Agent but no API bearer token. An HTTPS URL in a public example must be a URL the provider can fetch without private cookies.

## Errors and host installation

400 is invalid model input; 401 is authentication; 402 is billing; 409 means content is not ready; 424 means the job failed; 429 and 503 are transient service conditions. Preserve the ID and response body. Do not repeat an ambiguous POST. Install this SKILL.md in the host's current Agent Skills directory; check Claude Code, Codex and Cursor docs instead of assuming one path. This skill is not a MiniMax official package.
