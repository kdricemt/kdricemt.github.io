---
title: "Landing Site Selection and Divert Maneuver Planning with Deep Reinforcement Learning"
excerpt: "Applying reinforcement learning algorithms to design landing site selection policy and closed-loop controller for hazard detection and avoidance"
period: "2020/1 - Present"
image: 
  url: '/images/landing/landing_trajectory.png'
  width: '464'
  height: '428'
collection: project
---

| ![landing_concept_972x493.png](/images/landing/landing_concept_972x493.png)|
|:==:|
| *Concept of the Research* |

This research proposes a new integrated framework for identifying safe landing sites and planning in-flight divert maneuvers. Conventional landing site selection algorithms use only local terrain features such as slope and unevenness to determine landing site priority, and are not able to select landing site selection that maximizes the expected landing success rate when multiple chances of landing site selection and divert maneuver is considered. This study aims to optimize the landing site selection strategy concurrently with guidance and control policy by reinforcement learning in order to maximize the expected ratio of successful landing. 

Currently we are investigating the performance of the reinforcement learning algorithm in a 3-DOF lunar landing setting. By combining the auto-encoder and a ZEM-ZEV feedback controller with the reinforcement learning agent, a high success rate of more than 94% was achieved.

| ![landing_method-970x613.png](/images/landing/landing_method_970x613.png)|
|:==:|
| *Framework* |


---
Related Publications:
1. **Iiyama, K**, Tomita, K., Jagatia, B.A., Nakagawa, T., and Ho, K. (2020), “Deep Reinforcement Learning for Safe Landing Site Selection with Concurrent Consideration of Divert Maneuvers”, 2020 AAS/AIAA Astrodynamics Specialist Conference, Lake Tahoe, CA, The United States, 2020
2. Tomita, K., Jagatia, B.A., Nakagawa, T., **Iiyama, K.**, and Ho, K., “Real-Time Terrain Mapping and Processing for Safe Landing via Deep Neural Networks”, ASCEND, Las Vegas, NV, The United States, 2020 (Scheduled)