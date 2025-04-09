#!/bin/bash

# List of models as an array
models=(
  "AceGPT-v2-32B-Chat"
  "AceGPT-v2-70B-Chat"
  "Awqward2.5-32B-Instruct"
  "calme-2.1-qwen2.5-72b"
  "calme-2.2-qwen2.5-72b"
  "Cogito-R1"
  "lambda-qwen2.5-32b-dpo-test"
  "Llama-3.3-70B-Instruct"
  "Qwen2-72B"
  "Qwen2.5-32B-Instruct-abliterated-v2"
  "Qwen2.5-32B-Instruct-CFT"
  "Qwen2.5-72B-Instruct"
  "Qwentile2.5-32B-Instruct"
  "Rombos-LLM-V2.5-Qwen-72b"
  "Saka-14B"
  "tempmotacilla-cinerea-0308"
)

# Common args
output_dir="arabic_mt_bench_responses"
path="arabic_mt_bench_questions.jsonl"
openai_api="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"
tensor_parallel_size=8

# Loop over each model
for model in "${models[@]}"; do
  echo "============================"
  echo "Running model: $model"
  echo "============================"

  python run_response.py \
    --output_dir "$output_dir" \
    --model_name "$model" \
    --path "$path" \
    --openai_api "$openai_api" \
    --tensor_parallel_size "$tensor_parallel_size"

  echo "Finished model: $model"
  pkill -9 -f reasoner
  echo "Killed reasoner process"
  echo "============================"
done