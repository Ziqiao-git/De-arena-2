#!/usr/bin/env bash

##########################
# Updated Bash Script
##########################

# Dimension name & input path
q_set="mt_bench"
path="mt_bench_questions.jsonl"

# -------------------------------------------------------------------------
# 1) Define the *candidate* models (the 16 that will be compared/judged)
# -------------------------------------------------------------------------
candidate_models=(
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

# Convert the list of 16 candidate models into a single comma-separated string
all_candidates="$(IFS=, ; echo "${candidate_models[*]}")"

# -------------------------------------------------------------------------
# 2) Define the *judge* models (the 5 you listed)
# -------------------------------------------------------------------------
judge_models=(
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

# -------------------------------------------------------------------------
# 3) Loop over each judge to evaluate the 16 candidate models
# -------------------------------------------------------------------------
for judge in "${judge_models[@]}"; do
  echo "======================================================"
  echo "Running judge_responses.py with judge model: ${judge}"
  echo "Comparing among all 16 models' outputs..."
  echo "======================================================"

  python /home/guangyi.liu/ziqiao/De-Arena/judge_responses.py \
    --path "${path}" \
    --model_name "${judge}" \
    --model_names "${all_candidates}" \
    --tensor_parallel_size 8 \
    --dimension "${q_set}"

  echo "Finished judging with model: ${judge}"
  pkill -9 -f reasoner
  echo
done
