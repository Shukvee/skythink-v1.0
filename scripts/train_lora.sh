#!/usr/bin/env bash
set -euo pipefail

: "${BASE_MODEL:?Set BASE_MODEL to a local Qwen3-VL checkpoint directory.}"
: "${TRAIN_DATA:?Set TRAIN_DATA to a SkyBrain-format JSON file or MS-Swift dataset specification.}"
: "${OUTPUT_DIR:=outputs/skythink-v1}"
: "${DEEPSPEED_CONFIG:?Set DEEPSPEED_CONFIG to a DeepSpeed configuration file.}"
: "${CUDA_VISIBLE_DEVICES:=0,1}"

export CUDA_VISIBLE_DEVICES
export PYTORCH_CUDA_ALLOC_CONF="${PYTORCH_CUDA_ALLOC_CONF:-expandable_segments:True}"

IFS=',' read -r -a DEVICES <<< "$CUDA_VISIBLE_DEVICES"
NPROC_PER_NODE="${NPROC_PER_NODE:-${#DEVICES[@]}}"

torchrun \
  --nproc_per_node="$NPROC_PER_NODE" \
  --master_port="${MASTER_PORT:-29500}" \
  -m swift.cli.sft \
  --model "$BASE_MODEL" \
  --model_type qwen3_vl \
  --deepspeed "$DEEPSPEED_CONFIG" \
  --train_type lora \
  --dataset "$TRAIN_DATA" \
  --torch_dtype bfloat16 \
  --num_train_epochs "${NUM_TRAIN_EPOCHS:-2}" \
  --per_device_train_batch_size "${TRAIN_BATCH_SIZE:-1}" \
  --per_device_eval_batch_size "${EVAL_BATCH_SIZE:-1}" \
  --learning_rate "${LEARNING_RATE:-5e-5}" \
  --lora_rank "${LORA_RANK:-8}" \
  --lora_alpha "${LORA_ALPHA:-64}" \
  --target_modules all-linear \
  --gradient_accumulation_steps "${GRADIENT_ACCUMULATION_STEPS:-18}" \
  --eval_steps "${EVAL_STEPS:-1000}" \
  --save_steps "${SAVE_STEPS:-1000}" \
  --save_total_limit "${SAVE_TOTAL_LIMIT:-10}" \
  --logging_steps "${LOGGING_STEPS:-10}" \
  --max_length "${MAX_LENGTH:-2000}" \
  --output_dir "$OUTPUT_DIR" \
  --system "${SYSTEM_PROMPT:-You are a remote-sensing expert helping students answer domain questions.}" \
  --warmup_ratio "${WARMUP_RATIO:-0.03}" \
  --dataloader_num_workers "${DATALOADER_NUM_WORKERS:-2}" \
  --model_name "${MODEL_NAME:-SkyThink-v1}"
