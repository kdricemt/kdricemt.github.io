---
title: "LunaNet Constellation Design with Staged Development"
excerpt: "Framework to jointly optimize lunar navigation satellite constellation and staged development sequence"
---
**With** Prof.Gao (Stanford University) <br>

<div style="text-align: center;">
<img src = "https://dl.dropboxusercontent.com/s/p2yfx6pwdewwyx6olj8hs/constellation_overview_white.png?rlkey=gx55gelcq5qiwqssy1qkbhzk9&st=qt67s7ae&dl=0"
style="height: 320px; width:717px;">
</div>
<br>
<div style="text-align: center;">
</div>

Lunar navigation constellations must evolve strategically—beginning with service near the lunar south pole, where most early landing and surface exploration activities are planned, and eventually expanding toward full global coverage. 
Designing this type of constellation requires the integration of space-segment design, user positioning performance evaluation, and deployment sequencing to balance coverage, accuracy, and resource constraints (cost) throughout its evolution.
My research provides a systematic framework to address these challenges through two complementary studies: a comprehensive trade-off analysis of lunar frozen-orbit constellations and a staged-development optimization framework that jointly designs constellation architecture and deployment sequence.

I conducted an extensive analysis of lunar frozen-orbit Walker constellations to characterize the trade space of the Lunar Augmented Navigation Service (LANS) design.
This study quantified how key orbital parameters—such as semi-major axis and inclination—affect coverage, position dilution of precision (PDOP), orbit determination (OD) accuracy, receiver noise, and orbit insertion $\Delta V$.
Building on these findings, I developed a staged-deployment optimization algorithm that integrates coverage, PDOP, user range error, and robustness to satellite failure into a unified metric to optimize both constellation configuration and deployment sequencec. 
Simulations produced Pareto-optimal architectures that achieve early south-pole service with limited number of satellites, then scale efficiently to global coverage while meeting stage-specific performance targets. 
 <br><br>

**Related Publication:** 

[J5] Iiyama, K., Gao, G., “[Trade-off Analysis for Lunar Augmented Navigation Service (LANS) Constellation Design](https://arxiv.org/abs/2510.16030)”, Submitted to NAVIGATION: Journal of the Institute of Navigation, Under Review

[C21] Iiyama, K., Gao, G., “[Constellation Design and Staged Development for the Lunar Navigation Satellite System](https://drive.google.com/file/d/14dKsXmlO7jR0pz3i6h72kJFxZAkjdSG_/view)”, Proceedings of the Institute of Navigation GNSS+ conference (ION GNSS+ 2025), 2025

