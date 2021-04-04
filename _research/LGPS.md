---
title: "Research on Lunar Navigation Satellite System (LNSS)"
excerpt: "Research on Lunar Navigation Satellite System (LNSS)"
period: "2019/4 - Present"
image: 
  url: '/images/lgps/halo-orbit-291x392.png'
  width: '291'
  height: '392'
toc: true
toc_label: "My Table of Contents"
toc_icon: "cog"
collection: project
---

The Lunar Navigation Satellite System (LGSS) could significantly improve lunar missions' operational capability and flexibility by providing real-time, continuous, and highly accurate positioning services to lunar users. Research topics that I have been working on are listed below.

## 1. LNSS Simulator Development and Configuration Optimization
The research aims to obtain optimal configuration (e.g., arrangement of navigation satellite and lunar monitoring station) that could minimize cost while achieving the required performance. I developed an LNSS simulator and an optimizer to tackle this problem. 

Previous studies have shown that the required number of navigation satellites to cover the entire lunar surface could be reduced by deploying them on Halo Orbits. My undergraduate research demonstrated that the global positioning performance could be improved by deploying satellites on two stable periodic orbits: Distant Retrograde Orbits (DROs) and Near Rectlinear Halo Orbits (NRHOs). 

Related Publications:
1. **Iiyama, K**., “Optimization of the Navigation satellite constellation and Lunar Monitoring Station for Lunar Global Navigation Satellite System”, 32nd International Symposium on Space Technology and Science, Fukui, Japan, 2019 [[paper](/files/ISTS2019.pdf)]


## 2. Optimization of staged development strategy 
<img src = "https://dl.dropboxusercontent.com/s/132f1g15ozrcwpu/lnss_concept-1064x546.png?dl=0">
<div style="text-align: center;">
<i>Figure 1. Concept of the Research</i>
</div>  
<br>
More than 15 satellites are required to provide continuous navigation service to the entire lunar surface. Therefore, an effective way to develop the LNSS is to start from a small number of navigation satellites that could cover the area of interest in initial lunar development (e.g., south pole) and gradually increase its capacity. This study aims to optimize the staged development strategy of navigation satellites for halo-orbit-based LNSS, considering uncertainties in future areas of interest. The concept is shown in Fig.1.

The proposed method formulates the staged development process as a multi-objective Markov decision process, where each objective corresponds to the navigation performance at the possible area of interest. We presented an optimization framework that utilizes a multi-objective Monte-Carlo tree search (MO-MCTS) along with the LNSS simulator. A search tree is constructed where nodes correspond to constellation arrangement patterns, and edges correspond to the addition of navigation satellites. The search tree is gradually expanded by the MO-MCTS algorithm that repeats selection, expansion, simulation, and backpropagation. 
The algorithm searches for a development strategy with high flexibility, using the hypervolume of the stored Pareto-front at each node as an indicator of flexibility, 

The proposed algorithm is applied on a two-staged development scenario: In the first phase, five satellites are deployed to provide positioning service in the south pole region; in the second phase, three satellites are added to (objective-A) improve positioning performance at the south pole or (objective-B) provide additional positioning service at the north pole. By applying our algorithm, we could obtain a "flexible" first-stage architecture that could adjust to arbitrary weights on both areas of interest in the second stage. Results are shown in Fig.2.

<img src = "https://dl.dropboxusercontent.com/s/t6ue8zoi3ibe0sx/lnss_result-1069x674.png?dl=0">
<div style="text-align: center;">
<i>Figure 2. Result of the Research</i>
</div>  

Related Publications:
1. **Iiyama, K.**, Ozaki, N., Kawabata, Y., Funase, R., and Nakasuka, S., “The Optimization of Staged Development of Lunar Navigation Satellite System”, Space Sciences and Technology Conference, Tokushima, Japan, 2019 (Written in Japanese)

## 3. Autonomously Operated Networked Navigation Architecture
<img src = "https://dl.dropboxusercontent.com/s/fw9lvg8x300kwr9/lunanet.png?dl=0">
<div style="text-align: center;">
<i>Figure 3. Concept of the Research</i>
</div>
<br>
The development of a robust navigation infrastructure in cis-lunar space is crucial for the coming new era of advanced lunar exploration. NASA has set a goal to develop an extensible and scalable lunar communication, and navigation architecture called [LunaNet](https://directory.eoportal.org/web/eoportal/satellite-missions/l/lunanet). For the flexibility and robustness of the system, the architecture is desired to have an autonomous and decentralized operation capability. In this work, we propose a decentralized and autonomous state estimation algorithm for SmallSats that provides positioning, navigation, and timing service, each equipped with a GNSS receiver, a chip-scale atomic clock, and a steering antenna for inter-satellite communication. In our framework, each satellite individually estimates its own state and clock offset with a modified decentralized Schmidt Extended Kalman Filter by processing weak GNSS signal and inter-satellite range measurements. We also demonstrate that by deploying a total of 5 satellites on lunar frozen orbit and halo orbit, the PNT service area could be extended to regions where direct GNSS signals are not available, including the far side and pole regions of the moon.

Related Publications:
1. Iiyama, K, and Funase, R., “Autonomous and Decentralized Orbit Determination and Clock Offset Estimation of Lunar Navigation Satellites Using GPS Signals and Inter-satellite Ranging”, ION GNSS+ 2021, St.Louis, MO, The United States of America, September, 2021 (In preperation, Abstract Submitted) [[Extended Abstract](/files/ION_Conference_Extended_Abstract.pdf)]
