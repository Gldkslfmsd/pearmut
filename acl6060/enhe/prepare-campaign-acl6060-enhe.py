import sys
import json
sys.stdout.reconfigure(encoding="utf-8")

# Usage:

# 0) ensure that files on the following path exist, or change the paths in this script to your paths:

#   Reference:
# - ref/robothon-short.jsonl : input in hearing2translate format, converted from iwslt2024_cs_en_dev.zip , removed segments that had empty target.
#    - only the textfields are needed, the src_audio_path does not matter

#   Source audio:
# - robothon/short-audio/ : contains segmented audio wavs, named like robothon-debate_1.wav . They origin in the IWSLT24 dev, split by timestamps in this dev, removed segments that had empty target.
    # (TODO for next time: would be better to include gaps between the segments)

#   System outputs:
# - selected/*jsonl : candidate system outputs in hearing2translate output jsonl format, segmented by mweralign to match the reference segments

# 1) python3 prepare-robo-stel.py > ../campaign.json

# 2) cd .. ; pearmut add campaign.json

START_WAV_NUM = 330
END_WAV_NUM = 415

wav_numbers = list(range(START_WAV_NUM, END_WAV_NUM + 1))

campaign = {
  "info": {
    "assignment": "task-based",
    "protocol": "STEL",
    "assets": {
      "source": "../pearmut/enhe-acl6060/short-audio/",
      "destination": "assets/robothon"
    },
    "users": ["dm"] #, "user1", "user2"],
  },
  "campaign_id": "esa_validation",
}

segments = {}


SYSTEMS = [
    ("offline-whisperx+llama3-70b","selected/offline_whisper.jsonl"),
    ("simul-whisper+gemma2-9b-it","selected/simul_whisper.jsonl"),
]

for n,fn in SYSTEMS:
    segments[n] = []
    with open(fn, encoding="utf-8") as f:
        for line in f:
            d = json.loads(line)
            segments[n].append(d["output"])

ref_manifest = "ref/offline-short.jsonl"

data = [[]]
duration_buffer = 0
with open(ref_manifest, encoding="utf-8") as f:
    for i,ref in enumerate(f):
       d = json.loads(ref)
       audio = str(wav_numbers[i])+".wav"
       duration = d["timestamps"][1] - d["timestamps"][0]
       src_tgt = "<br> SOURCE: " + d["src_ref"] + "<br>REFERENCE: " + d["tgt_ref"]
       o = {
          "langs": f"{d['src_lang']}-{d['tgt_lang']}",
          "dataset": d["dataset_id"] + "-" + d["doc_id"],
          "sample_id": d["sample_id"],
          "src": f'<audio controls="" src="assets/robothon/{audio}"></audio>' + src_tgt,
          "tgt": {
            k: segments[k][i] for k in segments.keys()
          }
       }
       # every annotation task will contain appx 1 minute of audio:
       if duration_buffer + duration > 60:
          data.append([])
          duration_buffer = 0
       data[-1].append(o)
       duration_buffer += duration

campaign["data"] = [data]
# print(json.dumps(campaign, indent=2, ensure_ascii=False))

with open("../campaign.json", "w", encoding="utf-8") as f:
    json.dump(campaign, f, indent=2, ensure_ascii=False)

print("Wrote ../campaign.json")
