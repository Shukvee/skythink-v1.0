# SkyThink-v1

SkyThink-v1 is a LoRA adapter for a compatible Qwen3-VL base model, developed for undergraduate Remote Sensing (RS) education. It is designed for text, image, and mathematical-language questions in the RS domain, and performs well in relevant educational tasks.

The project follows a Collaborative Adaptive Training Framework, using adaptive gradient modulation to support interaction across heterogeneous RS tasks and reduce negative transfer.

## Released adapter

The released adapter is stored directly in `models/SkyThink-v1/` with Git LFS:

| File | Description |
| --- | --- |
| `adapter_model.safetensors` | LoRA adapter weights |
| `adapter_config.json` | LoRA configuration |
| `additional_config.json` | Additional adapter settings |

The configuration identifies this release as a PEFT LoRA adapter with rank `8`, alpha `64`, and a `0.05` dropout rate.

## Download

```bash
git lfs install
git clone https://github.com/Shukvee/skythink-v1.0.git
cd skythink-v1.0
git lfs pull
```

Load `models/SkyThink-v1/` as the adapter directory with a compatible, separately obtained Qwen3-VL base model. The base model is not redistributed in this repository and remains subject to its own license.

## License

This repository is released under the existing Apache-2.0 license. Use the base model and any separately obtained materials in accordance with their respective licenses and permissions.
