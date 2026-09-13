#!/usr/bin/env python3
"""Run batch image inference with a Qwen3-VL base model and a SkyThink LoRA adapter."""

from __future__ import annotations

import argparse
import os
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-model", required=True, help="Path to the local Qwen3-VL base model")
    parser.add_argument("--adapter", required=True, help="Path to the SkyThink LoRA checkpoint")
    parser.add_argument("--input-dir", required=True, help="Directory containing input images")
    parser.add_argument("--output-file", required=True, help="Text file for generated responses")
    parser.add_argument("--prompt", default="Please explain the image from a remote-sensing perspective.")
    parser.add_argument("--model-type", default="qwen3_vl")
    parser.add_argument("--max-tokens", type=int, default=2048)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--cuda-visible-devices", default=None, help="For example: 0,1")
    return parser.parse_args()


def load_swift_components():
    try:
        from swift.plugin import InferRequest, RequestConfig
        from swift.llm import PtEngine, load_model, load_template
        from swift.tuners import Swift
    except ImportError:
        from swift.llm import InferRequest, PtEngine, RequestConfig, load_model, load_template
        from swift.tuners import Swift
    return InferRequest, RequestConfig, PtEngine, Swift, load_model, load_template


def main() -> None:
    args = parse_args()
    if args.cuda_visible_devices is not None:
        os.environ["CUDA_VISIBLE_DEVICES"] = args.cuda_visible_devices

    InferRequest, RequestConfig, PtEngine, Swift, load_model, load_template = load_swift_components()
    input_dir = Path(args.input_dir)
    output_file = Path(args.output_file)
    image_paths = sorted(
        path for path in input_dir.iterdir() if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}
    )
    if not image_paths:
        raise FileNotFoundError(f"No supported images found in {input_dir}")

    model, tokenizer = load_model(args.base_model, args.model_type, torch_dtype="auto", device_map="auto")
    model = Swift.from_pretrained(model, args.adapter)
    template = load_template(args.model_type, tokenizer)
    engine = PtEngine.from_model_template(model, template, max_batch_size=1)
    request_config = RequestConfig(max_tokens=args.max_tokens, temperature=args.temperature)

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open("w", encoding="utf-8") as handle:
        for index, image_path in enumerate(image_paths, start=1):
            request = InferRequest(
                messages=[{"role": "user", "content": args.prompt}], images=[str(image_path)]
            )
            response = engine.infer([request], request_config)[0].choices[0].message.content
            handle.write(f"--- {image_path.name} ---\\n{response}\\n\\n")
            print(f"[{index}/{len(image_paths)}] {image_path.name}")


if __name__ == "__main__":
    main()
