# SkyThink-v1 model card

## Model summary

SkyThink-v1 is an MLLM tailored to undergraduate Remote Sensing education. It is trained from a local Qwen3-VL 32B pretraining checkpoint with LoRA adaptation and is designed to answer text, vision-language, and mathematical-language questions in the RS domain.

## Training approach

The paper introduces a Collaborative Adaptive Training Framework. Adaptive gradient modulation is used to improve interaction and robustness across heterogeneous RS tasks and to reduce negative transfer.

The local training configuration used the following key settings:

| Setting | Value |
| --- | --- |
| Model type | `qwen3_vl` |
| Training method | LoRA |
| Precision | bfloat16 |
| Learning rate | `5e-5` |
| LoRA rank / alpha | `8` / `64` |
| Target modules | all linear layers |
| Gradient accumulation | `18` |
| Maximum sequence length | `2000` |
| Epochs | `2` |

## Performance

SkyThink-v1 performs well on relevant undergraduate RS educational tasks across text, image, and mathematical modalities. Results can vary with the base model, prompt, data, and deployment environment.

## Intended use

* Undergraduate RS teaching support
* Guided explanation of RS concepts and images
* Practice-question assistance and educational exploration

## Limitations and responsible use

SkyThink-v1 is an educational assistant, not a substitute for instructors, verified course material, operational geospatial analysis, or safety-critical decisions. Its responses can be incorrect, incomplete, or sensitive to prompt and image quality. Users should verify technical claims with authoritative sources and avoid supplying private, restricted, or copyrighted material without permission.

The base model, LoRA adapter, data, and evaluation assets may each have separate terms of use. Check their licenses and access restrictions before training, redistribution, or deployment.
