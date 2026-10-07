---
name: text-responses
description: Make OpenAI-compatible Responses requests through the live gpt-6-sol contract, including tool calls and reasoning effort validation.
---

# OpenAI-compatible text Responses

Use this skill for a text model request that needs the Responses API. The current example uses model gpt-6-sol and POST https://argolink.io/v1/responses. This is a text workflow; do not send image or video fields to it.

## Current model facts

The live catalog checked 2026-10-07 lists gpt-6-sol at 0.60 USD per million input tokens and 3.00 USD per million output tokens, with a 1,050,000-token context window and 128,000-token maximum output. The effective rates shown here are service prices, not a claim about the upstream provider.

Use the Responses endpoint for reasoning and tools. The documented reasoning effort values are low, medium, high, xhigh and max, with medium as the default. A tool-enabled request carries a tools array and the model may return function_call items. Send each function result back with its call_id and continue until the response has no pending calls or a local turn limit is reached.

## Minimal Python request

~~~python
import os, requests

payload = {
    "model": "gpt-6-sol",
    "input": [{"role": "user", "content": [
        {"type": "input_text", "text": "Summarize the release notes in three bullets."}
    ]}],
    "reasoning": {"effort": "medium"},
}
response = requests.post(
    "https://argolink.io/v1/responses",
    headers={"Authorization": f"Bearer {os.environ['TEXT_API_KEY']}",
             "User-Agent": "model-skills-text/1.0",
             "Content-Type": "application/json"},
    json=payload,
    timeout=90,
)
response.raise_for_status()
print(response.json())
~~~

For a tool loop, validate the function name and JSON arguments against an allow-list. Never execute arbitrary code returned by a model. Keep a maximum turn count and preserve the response ID or call IDs in a private run record. Do not retry a POST whose outcome is unknown.

## Endpoint boundaries

The request base is https://argolink.io/v1. An OpenAI-compatible chat endpoint is not automatically identical to Responses: use the current API reference for fields, streaming, usage and errors. Preserve usage.input_tokens and usage.output_tokens when returned. A 401 is an environment credential problem; 402 is billing; 429 and 503 need bounded handling; other errors should retain the response body.

## Host installation

This SKILL.md is a reusable procedure, not an official OpenAI package. Install it in the current Agent Skills directory for Claude Code, Codex or Cursor after reading that host's discovery documentation. Secrets belong to the host environment, never in frontmatter or examples.
