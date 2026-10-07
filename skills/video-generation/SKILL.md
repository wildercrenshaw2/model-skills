---
name: video-generation
description: Generate Seedance 2.5 video jobs with model-specific validation and an explicit submit, status, and content lifecycle.
---

# Seedance 2.5 video generation

Use this skill for a Seedance 2.5 video request. The current model ID is seedance-2.5 and the API base in examples is https://argolink.io/v1. Submit once with POST /v1/videos/generations, persist request_id, read GET /v1/videos/{request_id}, and request content only after status done.

## Contract checked 2026-10-07

- duration is an integer from 4 through 30 seconds.
- resolution is 480p, 720p or 1080p.
- text and multimodal reference ratios are 21:9, 16:9, 4:3, 1:1, 3:4 or 9:16.
- start_image and first_last_frames use adaptive ratio; an edit omits duration and ratio and takes one 4–30 second source video.
- reference mode accepts up to 30 images, 10 videos, and 10 audio tracks, 50 total; audio-only reference input is valid. Reference video and audio clips are 2–30 seconds per clip and 30 seconds total per type.
- every request returns one 24 fps H.264 MP4; generate_audio defaults true.
- effective rates are 0.0874/0.196/0.483 USD per output second at 480p/720p/1080p. Reference video seconds are additional billable input seconds.

Use only HTTPS media URLs. For a local asset, request a media ticket from POST /v1/media/uploads, PUT bytes to its upload_url with the declared Content-Type and a User-Agent, then place the returned media_url in the generation body. Never send a bearer key to the presigned storage host.

## Minimal cURL lifecycle

~~~sh
BASE=https://argolink.io/v1
AUTH="Authorization: Bearer $VIDEO_API_KEY"
JOB=$(curl --fail-with-body -sS "$BASE/videos/generations" \
  -H "$AUTH" -H 'User-Agent: model-skills-video/1.0' \
  -H 'Content-Type: application/json' \
  -d '{"model":"seedance-2.5","prompt":"A paper kite crosses a sunset city","duration":5,"resolution":"720p","aspect_ratio":"16:9","generate_audio":true}')
ID=$(python3 -c 'import json,sys; print(json.load(sys.stdin)["request_id"])' <<< "$JOB")
curl --fail-with-body -sS "$BASE/videos/$ID" -H "$AUTH" -H 'User-Agent: model-skills-video/1.0'
curl --fail-with-body -sS "$BASE/videos/$ID/content" -H "$AUTH" -H 'User-Agent: model-skills-video/1.0' -o output.mp4
~~~

The final command is valid only after status reports done. The only terminal states are failed and expired; pending is not success. A 409 means content is not ready and 424 means the job failed.

## Host and safety

Keep the key in the host environment and keep request IDs in a private manifest. A local timeout is not proof of provider failure. Preserve response bodies and inspect the existing ID before considering another request. This skill is not an official vendor package. Install it under the host's current Agent Skills directory after checking Claude Code, Codex or Cursor discovery rules.
