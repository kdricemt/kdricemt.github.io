---
title: "Fault Detection from Intersatellite Ranges Using Reduntly Rigid Graphs"
excerpt: "Fault Detection from Intersatellite Ranges Using Reduntly Rigid Graphs"
period: "2024/6 - Present"

---
**With** Daniel Neamati, Prof.Gao (Stanford University) <br>

<div style="text-align: center;">
<img src = "https://dl.dropboxusercontent.com/s/24tnmg7uc25dcy8hujx7d/fault_singular_values.png?rlkey=oah1a2mh3duqhk1111gkd59gw&st=r5p149jw&dl=0"
style="height: 248px; width:717px;">
</div>
<br>
<div style="text-align: center;">
</div>

Navigation systems must be able to detect satellite faults and provide timely alerts when they fail to meet their stated accuracy, which is referred to as integrity monitoring.
I designed a satellite clock fault detection and exclusion algorithm that operates within the lunar navigation satellite constellation. 
By using inter-satellite ranging, it monitors satellite faults without relying on prior ephemeris information nor monitoring from lunar surface stations, which are likely not available at the early stages of LunaNet development. 

The proposed method models navigation satellite constellations as graphs, where satellites serve as vertices and inter-satellite links serve as edges.
It detects faults by identifying biases injected into inter-satellite range measurements whenever a satellite’s onboard clock malfunctions.
I proved that we are able to detect fault nodes (satellites with fault clocks) by assessing the realizability of redundantly rigid graphs (graphs that remain rigid after removing any vertex) in 3-D space. 
The process begins by searching for redundantly rigid subgraphs within the constellation graph and then evaluating their realizability by analyzing the singular values of Euclidean distance matrices constructed from the measured inter-satellite ranges.
This work received the best presentation award at the 2024 ION GNSS+ conference.
 <br><br>

**Related Publication:** 

[J4]  Iiyama, K., Neamati, D., Gao, G., “Satellite Autonomous Clock Fault Monitoring with Inter-Satellite Ranges Using Euclidean Distance Matrice”, NAVIGATION: Journal of the Institute of Navigation, 2025, (Under Review)

[C18] Iiyama, K., Neamati, D., Gao, G., “Autonomous Constellation Fault Monitoring with Inter-satellite Links: A Rigidity-Based Approach”, Proceedings of the Institute of Navigation GNSS+ conference (ION GNSS+ 2024), 2024

