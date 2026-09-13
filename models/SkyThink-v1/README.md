# SkyThink-v1 LoRA adapter

This directory contains the released SkyThink-v1 LoRA adapter for a compatible Qwen3-VL base model.

| File | Purpose |
| --- | --- |
| `adapter_model.safetensors` | LoRA adapter weights, stored with Git LFS |
| `adapter_config.json` | PEFT LoRA configuration |
| `additional_config.json` | Additional adapter settings |

`adapter_config.json` records a LoRA rank of `8`, alpha of `64`, and dropout of `0.05`. Use this directory as the adapter path in your compatible inference environment.

The base model and training artifacts are not included.
