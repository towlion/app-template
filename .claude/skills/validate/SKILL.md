---
disable-model-invocation: true
allowed-tools: Bash, Read
description: Run the Towlion spec validator against this app
---

# /validate — Run Spec Validator

Run the Towlion spec conformance validator against this application repository.

## Instructions

1. Check if the platform validator is available locally:
   - Look for `../platform/validator/validate.py` or `~/towlion/platform/validator/validate.py`
   - If not found, clone it: `git clone --depth 1 https://github.com/towlion/platform.git /tmp/towlion-platform`
2. Run the validator against the current directory:
   ```
   python <path-to-validator>/validate.py --tier 2 --dir .
   ```
3. Show the output to the user
4. If there are failures, summarize what needs to be fixed
