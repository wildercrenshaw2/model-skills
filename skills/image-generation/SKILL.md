---
name: image-generation
description: Generate or edit images with the live gpt-image-2 contract. Trigger for a concrete image request; verify size, quality, references, n and output format before spending credits.
---

# GPT Image 2 image generation

Use this skill when the user asks for a GPT Image 2 image or a reference-image edit. The live model ID is gpt-image-2 and its endpoint is POST /v1/images/generations for text-to-image and POST /v1/images/edits for reference edits. The default API base in examples is https://argolink.io/v1.

## Validate first

- prompt is required; describe subject, composition and the desired ratio in words such as “16:9 composition”.
- size is actual pixels, such as 1024x1024, 2048x1152 or 3840x2160. Billing uses the returned longest edge: up to 1024 is 1K, 1025–2048 is 2K, above 2048 is 4K.
- quality is auto, low, medium or high. response_format is url or b64_json.
- n is 1–7; every returned image is billed separately.
- an edit uses multipart POST /v1/images/edits and one to sixteen image[] references (max_references: 16). A local file is uploaded or attached explicitly; never place a local path in a public JSON example.
- the response can contain data[].url or data[].b64_json. Check returned pixels when exact dimensions matter.

The current effective rates checked 2026-10-07 are 0.015 USD per image at 1K and 2K and 0.02 at 4K. A larger n is a larger bill. The model page remains authoritative.

## Safe request example

~~~python
import os, requests

body = {
    "model": "gpt-image-2",
    "prompt": "Editorial still life, 16:9 composition, soft morning light",
    "size": "1024x576",
    "quality": "auto",
    "n": 1,
    "response_format": "b64_json",
}
response = requests.post(
    "https://argolink.io/v1/images/generations",
    headers={
        "Authorization": f"Bearer {os.environ['IMAGE_API_KEY']}",
        "User-Agent": "model-skills-image/1.0",
    },
    json=body,
    timeout=180,
)
response.raise_for_status()
image = response.json()["data"][0]
~~~

Do not log the bearer header. For an edit, use the current model page's multipart field names and verify every redirect remains HTTPS.

## Failure boundaries

400 is an invalid field, 401 an authentication failure, 402 a billing problem, 429 rate limiting and 503 capacity. Preserve the response body. Do not blindly repeat an ambiguous POST. This is a procedure, not an official vendor package.

Install this directory under the Agent Skills location configured by the host. Claude Code commonly uses project .claude/skills or user ~/.claude/skills; Codex uses its configured CODEX_HOME/skills; Cursor settings vary. Check the host's current documentation before copying.
