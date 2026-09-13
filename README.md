# SkyThink-v1

SkyThink-v1 is a multimodal large language model (MLLM) for undergraduate Remote Sensing (RS) education. It is built around SkyBrain, a 1M+ entry educational corpus spanning language, vision-language, and mathematical-language tasks, and a Collaborative Adaptive Training Framework that uses adaptive gradient modulation to reduce negative transfer between tasks.

The accompanying evaluation suite, **RSEdu-Bench**, is derived from and expanded with authoritative RS exercises to cover undergraduate RS curricula. In the paper's reported experiments, SkyThink-v1 exceeded GPT-5 on RSEdu-Bench by **8.40 percentage points** in average accuracy.

## What this repository provides

* A parameterized LoRA training launcher for Qwen3-VL with [MS-Swift](https://github.com/modelscope/ms-swift)
* A batch image-inference utility that loads a base model and a SkyThink LoRA adapter
* Documentation for the model, data format, benchmark, and reproducibility boundaries

Model weights, raw educational data, benchmark images, and training logs are intentionally not committed. See [Dataset and benchmark notes](docs/DATASET.md) for the expected record format and access considerations.

## Repository layout

```text
.
├── docs/
│   ├── DATASET.md             # SkyBrain and RSEdu-Bench format and access notes
│   └── MODEL_CARD.md          # intended use, training configuration, and limitations
├── scripts/
│   ├── infer_images.py        # batch multimodal inference with a LoRA adapter
│   └── train_lora.sh          # reproducible MS-Swift training launcher
├── requirements.txt
└── README.md
```

## Setup

Create an environment compatible with your CUDA stack, then install the Python dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Prepare three local paths that are not tracked by Git:

* `BASE_MODEL`: a compatible local Qwen3-VL base-model directory
* `TRAIN_DATA`: a SkyBrain-format JSON training file, or a dataset specification accepted by MS-Swift
* `ADAPTER_PATH`: a trained SkyThink LoRA checkpoint

## Train a LoRA adapter

The launcher preserves the key settings used in the local experiment: LoRA training, `qwen3_vl`, bfloat16, a learning rate of `5e-5`, rank `8`, alpha `64`, and gradient accumulation of `18`. Adapt the device count, DeepSpeed configuration, and dataset path to your hardware.

```bash
export BASE_MODEL=/path/to/Qwen3-VL-32B-pretrain
export TRAIN_DATA=/path/to/SkyBrain/train.json
export OUTPUT_DIR=outputs/skythink-v1
export DEEPSPEED_CONFIG=/path/to/ds_config.json
export CUDA_VISIBLE_DEVICES=0,1

bash scripts/train_lora.sh
```

## Run image inference

```bash
python scripts/infer_images.py \
  --base-model /path/to/Qwen3-VL-32B-pretrain \
  --adapter /path/to/SkyThink-v1 \
  --input-dir /path/to/images \
  --output-file outputs/image_predictions.txt \
  --prompt "Please explain the image from a remote-sensing perspective."
```

The script supports PNG, JPG, JPEG, and WebP inputs and writes one response per image.

## Released LoRA adapter

The final LoRA adapter is published directly under `models/SkyThink-v1/` through Git LFS. Clone the repository with Git LFS enabled and retrieve the weight file before inference:

```bash
git lfs install
git clone https://github.com/Shukvee/skythink-v1.0.git
cd skythink-v1.0
git lfs pull
```

Use the adapter directory as the `--adapter` value in `scripts/infer_images.py`. The Qwen3-VL base model is not redistributed here; obtain it separately under its own license.

## Data and benchmark

SkyBrain records use chat-style `messages`, an optional `images` list, and a `task` label (`text`, `image`, or `math`). The local RSEdu-Bench release contains 2,198 records. Details, including why data are not redistributed here, are in [docs/DATASET.md](docs/DATASET.md).

## Reproducibility and limitations

Results depend on the exact base model, data split, image assets, prompts, hardware, and MS-Swift version. The reported 8.40-point result is a paper result, not a claim that every local deployment will reproduce the same score. This repository contains implementation utilities and documentation rather than a complete public release of third-party or source-restricted materials.

## License

This repository is released under the existing Apache-2.0 license. Use the Qwen base model, educational-source material, and any separately obtained data according to their respective licenses and permissions.
