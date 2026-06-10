import json

def load_candidates(filepath):

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            yield json.loads(line)