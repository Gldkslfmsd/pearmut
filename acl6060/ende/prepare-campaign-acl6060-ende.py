import sys
import json
import librosa
import os

# Usage:

# 0) ensure that files on the following path exist, or change the paths in this script to your paths:

#   Reference:
# - ref/robothon-short.jsonl : input in hearing2translate format, converted from iwslt2024_cs_en_dev.zip , removed segments that had empty target. 
#    - only the textfields are needed, the src_audio_path does not matter

#   Source audio:
# - ../short-audio/ : contains segmented audio wavs, named like robothon-debate_1.wav . They origin in the IWSLT24 dev, split by timestamps in this dev, removed segments that had empty target.
    # (TODO for next time: would be better to include gaps between the segments)

#   System outputs:
# - selected/*txt : candidate system outputs, sentence-level segmented (automatically), in txt format, one segment per line

# 1) python3 prepare-*.py > campaign.json

# 2) cd ../.. ; pearmut add $PATH-HERE/campaign.json

USERS =  ["mz", "dm", "annotator3", "annotator4"]
AUDIO_SRC_DIR = "acl6060/short-audio/"  # from main dir
campaign = {
  "info": {
    "assignment": "task-based",
    "protocol": "STEL",
    "assets": {
      "source": AUDIO_SRC_DIR,
      "destination": "assets/acl6060"
    },
    "users": USERS,
  },
  "campaign_id": "stel-acl6060.111-ende",
}


segments = {}

SYSTEMS = [
    ("canary","selected/canary.txt"),
    ("whisper+gemma","selected/whisper+gemma.txt"),
    ("simulstreamingwhisper+tower","selected/simulstreaming_whisper+tower.txt"),
]

for n,fn in SYSTEMS:
    segments[n] = []
    with open(fn) as f:
        for line in f:
            segments[n].append(line.strip())

ref_manifest = "ref/2022.acl-long.111.short.jsonl"

data = [[]]
duration_buffer = 0
with open(ref_manifest) as f:
    for i,ref in enumerate(f):
       d = json.loads(ref)
       audio = str(d["sample_id"])+".wav"
       duration = librosa.get_duration(path=f"../short-audio/{audio}")
       src_tgt = "<br> SRC: " + d["src_ref"] + "<br>REF: " + d["tgt_ref"]
       o = {
          "langs": f"{d['src_lang']}-{d['tgt_lang']}",
          "dataset": d["dataset_id"],
          "sample_id": d["sample_id"],
          "src": f'<audio controls="" src="assets/acl6060/{audio}"></audio>' + src_tgt,
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
campaign["data"] = [data for _ in range(len(USERS))]
print(json.dumps(campaign, indent=2, ensure_ascii=False))
