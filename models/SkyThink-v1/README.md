# SkyThink-v1 final LoRA adapter

This directory contains the final LoRA adapter exported at training checkpoint `19884`.

| File | Purpose |
| --- | --- |
| `adapter_model.safetensors` | LoRA adapter weights, stored with Git LFS |
| `adapter_config.json` | PEFT LoRA configuration |
| `additional_config.json` | Additional adapter settings |

Use a compatible local Qwen3-VL base model with MS-Swift, then pass this directory to `scripts/infer_images.py` with `--adapter`.

The base model and optimizer/restart artifacts are deliberately not included.
