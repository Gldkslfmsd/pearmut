import sys
import json

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

campaign = {
  "info": {
    "assignment": "task-based",
    "protocol": "STEL",
    "assets": {
      "source": "robothon/short-audio/",
      "destination": "assets/robothon"
    },
    "users": ["dm"] #, "user1", "user2"],
  },
  "campaign_id": "robothon-stel-1",
}


segments = {}

SYSTEMS = [
    ("canary","selected/canary-script.short.jsonl"),
    ("gemma3+whisper","selected/merged_gemma3.whisperx-asr.seg3000.short.jsonl"),
    ("simulstreamingwhisper","selected/simulstreamingwhisper-aware.short.jsonl"),
]

for n,fn in SYSTEMS:
    segments[n] = []
    with open(fn) as f:
        for line in f:
            d = json.loads(line)
            segments[n].append(d["output"])

ref_manifest = "ref/robothon-short.jsonl"

data = [[]]
duration_buffer = 0
with open(ref_manifest) as f:
    for i,ref in enumerate(f):
       d = json.loads(ref)
       audio = d["doc_id"]+"_"+str(d["sample_id"])+".wav"
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
       if duration_buffer + duration > 60:
          data.append([])
          duration_buffer = 0
       data[-1].append(o)
       duration_buffer += duration
campaign["data"] = [data]
print(json.dumps(campaign, indent=2, ensure_ascii=False))
