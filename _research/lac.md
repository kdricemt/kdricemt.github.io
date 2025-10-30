---
title: "Lunar Autonomy Challenge" 
excerpt: "Lunar Autonomy Challenge" 

---
**With** Stanford NAV Lab (Stanford University) <br>

<div style="text-align: center;">
<img src = "https://dl.dropboxusercontent.com/s/ebmiaipar7f29iymh3n2l/lac_overview.png?rlkey=d5flctxlxplcsyajkiti9x8r5&st=eexb0fug&dl=0"
style="height: 400px; width:717px;">
</div>
<br>
<div style="text-align: center;">
</div>

We developed a full-stack autonomous agent for lunar rover navigation and mapping designed for the [Lunar Autonomy Challenge competition](https://lunar-autonomy-challenge.jhuapl.edu/), hosted by NASA and Johns Hopkins University Applied Physics Laboratory (APL). 
This challenge directly supports NASA’s Lunar Surface Innovation Initiative (LSII), which seeks to develop foundational technologies and approaches needed to fulfill the Artemis
missions. 

The goal of the challenge is to virtually explore and map the lunar surface using a digital twin of NASA’s lunar In-Situ Resource Utilization (ISRU) Pilot Excavator (IPEx) robot. 
The challenge provides a high-fidelity lunar simulation environment based on Unreal Engine and built using CARLA (Dosovitskiy et al., 2017), which is capable of photorealistic imagery and
simulating vehicle dynamics over complex terrain. 

We leverage lightweight learning-based perception models for real-time segmentation and feature tracking, and use a factor-graph backend to maintain globally consistent localization. High-level waypoint planning is designed to promote mapping coverage while encouraging
frequent loop closures, and local motion planning uses arc sampling with geometric obstacle checks for efficient, reactive
control. We evaluate our approach in the competition’s high-fidelity lunar simulator, demonstrating centimeter-level localization
accuracy, high-fidelity map generation, and strong repeatability across random seeds and rock distributions. 

[Our solution achieved first place](https://www.nasa.gov/directorates/stmd/top-prize-awarded-in-lunar-autonomy-challenge-to-virtually-map-moons-surface/) in the final competition evaluation.


**Related Publication:** 

[C23] Dai, A., Wu, A., Iiyama, K., Vila, G.C., Coimbra, K., Deng, T., Gao, G., “[Full Stack Navigation, Mapping, and Planning for the Lunar Autonomy Challenge](https://drive.google.com/file/d/1T90LuymHHbPKRx4QeSBnXULjS5RcOBb0/view)”, Proceedings of the Institute of Navigation GNSS+ conference (ION GNSS+ 2025), 2025 [[Slides](https://drive.google.com/file/d/1oiCwl1F3BmPP4-8lYbAemcrtMgLHHbIp/view)]