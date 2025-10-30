---
title: "Landing Site Selection and Divert Maneuver Planning with Deep Reinforcement Learning"
excerpt: "Applying reinforcement learning algorithms to design landing site selection policy and closed-loop controller for hazard detection and avoidance"
image: 
  url: '/images/landing/landing_trajectory.png'
  width: '464'
  height: '428'
collection: project
---

<img src = "https://dl.dropboxusercontent.com/s/fnlga64x94mw7hh/landing_concept_972x493.png?dl=0">
<div style="text-align: center;">
<i>Figure 1. Concept of the Research</i>
</div>
<br>
Autonomous hazard detection and avoidance (HD&A) is of great importance in future planetary landing missions. This research proposes a new integrated framework for identifying safe landing sites and planning in-flight divert maneuvers. Conventional landing site selection algorithms rely on calculated local terrain features (e.g., slope and roughness) to find and prioritize candidate landing sites. However, they cannot select a target landing site that maximizes the expected probability of successful landing with explicit consideration of future divert maneuvers and observation. This study aims to optimize the landing site selection strategy concurrently with guidance and control policy by reinforcement learning to maximize the expected ratio of a successful landing by formulating the HD&A sequence as a Partially Observable Markov Decision Process (POMDP). 

The developed framework was applied to a 3-DOF lunar landing with a Lidar observation scenario. The (high) dimension of Lidar DEM data was reduced with the trained auto-encoder, while stability is guaranteed by utilizing the ZEM-ZEV feedback controller as a baseline control law. The target landing position and control gain of the ZEM-ZEV controller was adjusted by the reinforcement learning agent trained by both memory-based and memory-less algorithms. The investigation of the obtained result showed the capability of the agent to effectively adjust the control gain to achieve both long and short divert maneuvers. 

This research is a collaboration project with [Space Systems Optimization Group](https://ssog.ae.gatech.edu/) in Georgia Institute of Technology. 

<img src = "https://dl.dropboxusercontent.com/s/xlbuddt6b0iq3t5/landing_method_970x613.png?dl=0">
<div style="text-align: center;">
<i>Figure 2. Overall Framework</i>
</div>

**Related Publication:** 

[C5] Iiyama, K., Tomita, K., Jagatia, B.A., Nakagawa, T., Ho, K., "[Deep reinforcement learning for safe landing site selection with concurrent consideration of divert maneuvers](https://arxiv.org/pdf/2102.12432)”, AAS/AIAA Astrodynamics Specialist Conference, 2020,