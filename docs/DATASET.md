# SkyBrain and RSEdu-Bench

## SkyBrain

SkyBrain is the training corpus for SkyThink-v1. The paper describes more than one million RS educational entries across three task families:

* **Text:** RS concepts, questions, explanations, and structured responses
* **Vision-language:** RS imagery paired with questions or explanatory responses
* **Mathematical language:** calculations, formulas, and reasoning tasks used in RS coursework

The local training material uses JSON lists whose records follow a chat-style schema:

```json
{
  "task": "image",
  "messages": [
    {"role": "user", "content": "<image>\\nExplain this remote-sensing image."},
    {"role": "assistant", "content": "..."}
  ],
  "images": ["/absolute/or/relative/path/to/image.png"]
}
```

Text-only and mathematical records may omit `images`. Ensure image paths are valid in the training environment before starting MS-Swift.

## RSEdu-Bench

RSEdu-Bench is the evaluation benchmark introduced for undergraduate RS education. The local benchmark file inspected for this release contains **2,198** records using the same `messages`, optional `images`, and `task` fields. It is intended to cover core undergraduate RS curricula, including text, image, and mathematical tasks.

## Distribution boundary

The raw SkyBrain corpus, RSEdu-Bench items, benchmark images, and source exercises are not included in this repository. They may contain third-party educational material, images, or source-restricted content. Before releasing any subset, verify the applicable copyright, data-use, and redistribution permissions.

To reproduce a permitted experiment, place the data outside the repository, confirm the JSON schema and image paths, and pass the resulting local paths to `scripts/train_lora.sh` or `scripts/infer_images.py`.
