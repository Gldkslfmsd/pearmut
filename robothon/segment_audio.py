import sys
import json
for i in sys.stdin:
    d = json.loads(i)
    audio = d['src_audio'].replace("/csen-robothon","ref")
    beg, end = d["timestamps"]
    duration = end-beg
    print(f"sox {audio} short-audio/{d['doc_id']}_{d['sample_id']}.wav trim {beg} {duration}")