ACL6060, one randomly selected document nr. 111
- en-de STEL annotation

1) Dominik selected 3 ST systems and processed them. The candidate translations are in inputs/ dir.

2) Segmentation and alignment.

Using the de ref translation and mwerlign.
Visual check: it's more or less ok, let's not fix it manually.

3) then adapted the provided script to generate campaign.json:

prepare-campaign-acl6060-ende.py

4) annotation of STEL in pearmut, in the robo-stel branch. Results are (or will be) in annotated/  dir.
