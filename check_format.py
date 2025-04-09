#!/usr/bin/env python3
import json

def load_jsonl(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, start=1):
            try:
                json_data = json.loads(line.strip())
            except json.JSONDecodeError as e:
                print(f"Error parsing line {line_num}: {e}")
                continue
            yield json_data
    return json_data

def main():
    questions = load_jsonl("arabic_mt_bench_questions.jsonl")
    for question in questions:
        print(question['turns'][0])
        print("Reference:", question.get('reference', [""]))
        if 'turns' not in question:
            print(f"Warning: question {question['question_id']} has no 'turns' key at all.")
        if not question['turns']:
            print(f"Warning: Question ID {question['question_id']} has no turns.")
        
if __name__ == "__main__":
    main()
