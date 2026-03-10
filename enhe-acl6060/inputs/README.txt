src_ref.txt
- source transcript, segmented to 86 lines corresponding to ../short-audio/*wav


offline-whisperx+llama3-70b.txt
simul-whisper+gemma2-9b-it.txt
- en-he translations with two system
- not segmented to sentences!
- expected first step is to manually segment them to lines corresponding to src_ref.txt, then convert to campaign.json in a script adapted from ../../robothon/prepare-robo-stel.py

