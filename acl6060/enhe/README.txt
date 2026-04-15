ACL6060, one randomly selected document nr. 111
- en-he STEL annotation

1) Dominik selected 2 ST systems and processed them. The candidate translations are in inputs/ dir.

BUT: we don't have Hebrew reference translation, therefore we can not have automatic sentence segmentation.

2) The English-Hebrew speaking annotator:

- splitted the translations to sentences using ChatGPT + manually reviewed the alignment

3) then adapted the provided script to generate campaign.json:

prepare-campaign-acl6060-enhe.py

- instead of REFERENCE, the annotator put there one of the candidate translations. (But then didn't put attention to it.)

4) annotation of STEL in pearmut, in the robo-stel branch. Results are in annotated/  dir.
