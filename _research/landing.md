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

Autonomous hazard detection and avoidance (HD&A) is of great importance in future planetary landing missions. This research proposes a new integrated framework for identifying safe landing sites and planning in-flight divert maneuvers. Conventional landing site selection algorithms relies on calculated local terrain features (e.g.: slope and roughness) to determine the priority of the landing sites. However, they are not able to select landing site selection that maximizes the expected probability of successful landing with explicit consideration of multiple chances of landing site selection and divert maneuver. This study aims to optimize the landing site selection strategy concurrently with guidance and control policy by reinforcement learning in order to maximize the expected ratio of successful landing.

The developed framework is applied to a 3-DOF lunar landing with Lidar observation scenario. The high dimemsion of Lidar DEM data is reduced with the trained auto-encoder, while stability is guranteed by utilizing the ZEM-ZEV feedback controller as a baseline control law. The target landing position and control gain of the ZEM-ZEV controller is adjusted by the reinfocement learning agent trained by both memory-based and memory-less algorithms. The investigation of the obtained result showed the capability of the agent to effectively adjust the control gain to achieve both long and short divert maneuvers. 

We are currently working on extending the framework to 6-DOF scenario with state estimation errors.

| ![landing_method-970x613.png](/images/landing/landing_method_970x613.png)|
|:==:|
| * Overall Framework* |

---
Related Publications:
1. **Iiyama, K**, Tomita, K., Jagatia, B.A., Nakagawa, T., and Ho, K. (2020), “Deep Reinforcement Learning for Safe Landing Site Selection with Concurrent Consideration of Divert Maneuvers”, 2020 AAS/AIAA Astrodynamics Specialist Conference, Lake Tahoe, CA, The United States, 2020
2. Tomita, K., Jagatia, B.A., Nakagawa, T., **Iiyama, K.**, and Ho, K., “Real-Time Terrain Mapping and Processing for Safe Landing via Deep Neural Networks”, ASCEND, Las Vegas, NV, The United States, 2020 (Scheduled)