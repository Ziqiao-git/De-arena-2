import torch
import json
import sys

if torch.cuda.is_available():
    print(f"Total CUDA devices: {torch.cuda.device_count()}")
    for i in range(torch.cuda.device_count()):
        print(f"Device {i}: {torch.cuda.get_device_name(i)}")
else:
    print("No CUDA devices are available.")

existing_model_paths = {
    # 'gpt-4o-mini-2024-07-18' : "OPENAI", # 1 finish old
    # 'gpt4-1106' : "OPENAI",
    # 'gpt3.5-turbo-0125' : "OPENAI", # 2 finish old
    # "o1-preview" : "OPENAI", 
    # "o1-mini" : "OPENAI", 
    # "ChatGPT-4o-latest (2024-09-03)" : "OPENAI", # 4
    "gpt-4o-2024-08-06" : "OPENAI", # 3 running old
    # "gpt-4-turbo-2024-04-09" : "OPENAI",
    "gpt-4o-2024-05-13" : "OPENAI",

    # "gemma-2-9b-it-simpo" : "/data/shared/huggingface/hub/gemma-2-9b-it-simpo",
    # "google-gemma-2-9b-it" : "/data/shared/huggingface/hub/google-gemma-2-9b-it",
    # "llama-3.1-tulu-8b" : "/data/shared/huggingface/hub/llama-3.1-tulu-8b",
    # "zephyr-7b-beta": "/data/shared/huggingface/hub/zephyr-7b-beta",
    # "qwen2.5-3b" : "/data/shared/huggingface/hub/models--Qwen--Qwen2.5-3B/snapshots/3aab1f1954e9cc14eb9509a215f9e5ca08227a9b",
    # "vicuna-7b" : "/data/shared/huggingface/hub/vicuna-7b",
    # "mistral-7b-instruct-2" : "/data/shared/huggingface/hub/mistral-7b-instruct-2",


    # "llama3-8b-instruct" : "/data/shared/huggingface/hub/models--meta-llama--Meta-Llama-3-8B-Instruct/snapshots/a8977699a3d0820e80129fb3c93c20fbd9972c41",
    # "meta-llama-3.3-8b-instruct" : "/data/shared/huggingface/hub/models--meta-llama--Meta-Llama-3.1-8B-Instruct/snapshots/07eb05b21d191a58c577b4a45982fe0c049d0693",
    "AceGPT-v2-32B-Chat": "/lustre/scratch/users/guangyi.liu/ziqiao/models/AceGPT-v2-32B-Chat",
    "AceGPT-v2-70B-Chat": "/lustre/scratch/users/guangyi.liu/ziqiao/models/AceGPT-v2-70B-Chat",
    "Awqward2.5-32B-Instruct": "/lustre/scratch/users/guangyi.liu/ziqiao/models/Awqward2.5-32B-Instruct",
    "calme-2.1-qwen2.5-72b": "/lustre/scratch/users/guangyi.liu/ziqiao/models/calme-2.1-qwen2.5-72b",
    "Cogito-R1": "/lustre/scratch/users/guangyi.liu/ziqiao/models/Cogito-R1",
    "calme-2.2-qwen2.5-72b": "/lustre/scratch/users/guangyi.liu/ziqiao/models/calme-2.2-qwen2.5-72b",
    "free-evo-qwen72b-v0.8-re": "/lustre/scratch/users/guangyi.liu/ziqiao/models/free-evo-qwen72b-v0.8-re",
    "lambda-qwen2.5-32b-dpo-test": "/lustre/scratch/users/guangyi.liu/ziqiao/models/lambda-qwen2.5-32b-dpo-test",
    "Llama-3.3-70B-Instruct": "/lustre/scratch/users/guangyi.liu/ziqiao/models/Llama-3.3-70B-Instruct",
    "Qwen2-72B": "/lustre/scratch/users/guangyi.liu/ziqiao/models/Qwen2-72B",
    "Qwen2.5-32B-Instruct": "/lustre/scratch/users/guangyi.liu/ziqiao/models/Qwen2.5-32B-Instruct",
    "Qwen2.5-32B-Instruct-abliterated-v2": "/lustre/scratch/users/guangyi.liu/ziqiao/models/Qwen2.5-32B-Instruct-abliterated-v2",
    "Qwen2.5-32B-Instruct-CFT": "/lustre/scratch/users/guangyi.liu/ziqiao/models/Qwen2.5-32B-Instruct-CFT",
    "Qwen2.5-72B-Instruct": "/lustre/scratch/users/guangyi.liu/ziqiao/models/Qwen2.5-72B-Instruct",
    "Qwentile2.5-32B-Instruct": "/lustre/scratch/users/guangyi.liu/ziqiao/models/Qwentile2.5-32B-Instruct",
    "Rombos-LLM-V2.5-Qwen-72b": "/lustre/scratch/users/guangyi.liu/ziqiao/models/Rombos-LLM-V2.5-Qwen-72b",
    "Saka-14B": "/lustre/scratch/users/guangyi.liu/ziqiao/models/Saka-14B",
    "SakaMoe-3x14B-Instruct": "/lustre/scratch/users/guangyi.liu/ziqiao/models/SakaMoe-3x14B-Instruct",
    "tempmotacilla-cinerea-0308": "/lustre/scratch/users/guangyi.liu/ziqiao/models/tempmotacilla-cinerea-0308",
    "Ultiima-72B": "/lustre/scratch/users/guangyi.liu/ziqiao/models/Ultiima-72B"
}