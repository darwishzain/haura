import json

with open('corpus/dialogue/greetings.jsonl') as f:
    for line in f:
        item = json.loads(line)
        print(f"User: {item['user']}")
        print(f"HAURA: {item['haura']}")
