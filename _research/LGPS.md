---
title: "Optimization of Satellite Arrangement and Staged Development Strategy for Halo Orbit based Lunar Navigation Satellite System"
excerpt: "Optimization of Satellite Arrangement and Staged Development Strategy for Halo Orbit based Lunar Navigation Satellite System"
period: "2019/4 - Present"
image: 
  url: '/images/lgps/halo-orbit-291x392.png'
  width: '291'
  height: '392'
collection: project
---

Conventional positioning method on lunar surface mainly relies on captured images from lunar orbiters and lacks real-time property. For advanced missions on the lunar surface in the future, it is necessary to achieve high user positioning accuracy and instant positioning simultaneously. A Lunar Navigation Satellite System (LNSS) is an effective solution to this problem. The aim of the research is to 

## System design and optimization
The aim of the research is to obtain optimal configuration (e.g. navigation satellite and lunar monitoring station arrangement, navigation satellite design) that could minimize cost while achieving required performance. I am developing a LNSS simulator and optmizer in MATLAB and python to tackle this problem. 

Previous studies have shown that the required number of navigation satellites to cover the entire lunar surface could be reduced by deploying them on Halo Orbits. My undergraduate  research demonstrated that the global positining performance could be improved by deploying satellites on two stable periodic orbits: Distant Retrograde Orbits (DROs) and Near Rectlinear Halo Orbits (NRHOs). 

I am currently working on adding additional features to the LNSS simulator such as:
- navigation satellite cost model (based on required power, communication, required propellant)
- using inter-satellite links to improve orbit determination accurary of the navigation satellites
- clock-bias correction of navigation satellites using terrestial GNSS signals


## Optimization of staged development strategy 

| ![lnss_concept-1064x546.png](/images/lgps/lnss_concept-1064x546.png)|
|:==:|
| *Figure 1. Concept of the Research* |

More than 15 satellites are required to provide continuous navigation to the entire lunar surface. An effective way to develop the LNSS is to start from small number of navigation satellites that could cover area of interest in initial lunar development (e.g. south pole), and gradually increase its capacity through additional satellite deployment. The goal of this study is to optimize the staged development strategy of navigation satellites for halo-orbit based LNSS, considering uncertainties in future area of interest. The concept is shown in Fig.1.

The idea of the proposed method is to formulate the staged development process as a multi-objective markov decision process, where each objective corresponds to the navigation performance at possible area of interest. We presented an optimization framework that utilizes multi-objective monte-carlo tree search (MO-MCTS) along with the LNSS simulator. A search tree is constructed where nodes correpsponds to constellation arrangement patterns and edges correspond to the addition of navigation satellites. The search tree is constructed by MO-MCTS algorithm that repeats the process of selection, expansion, simulation, and back progation. In MO-MCTS, all pareto solutions are back-propagated towards the root of the search-tree. Therefore, we proposed to use the hypervolume of the stored pareto solutions as an indicator of "flexibility" of the arragment. The MO-MCTS looks for new nodes with high flexibility considering the trade-off of exploration and exploitation. The node that has the highest hypervolumes among all nodes with depth N is considered as the most flexible first stage architecture with depth N. The overall framework is illustrated in Fig.2.

The proposed algorithm is applied on a 2-staged development scenerio: In the first phase, five satellites are deployed to provide positiong service in the south pole region, in the second phase, three satellites are added to (objective-A) improve positioning performance at south pole or (objective-B) provide additional positioning service at the north pole. By applying our algorithm, we could obtain a "flexible" first stage architecture that could adjust to arbitrary weights on both area of interest in the second stage. Results are shown in Fig.3.

| ![lnss_method-1073x613.png](/images/lgps/lnss_method_1073x613.png)|
|:==:|
| *Figure 2. Overall Framework* |

| ![lnss_result-1069x674.png](/images/lgps/lnss_result-1069x674.png)|
|:==:|
| *Figure 3. Result of the Research* |

---
Related Publications:
1. **Iiyama, K.**, Ozaki, N., Kawabata, Y., Funase, R., and Nakasuka, S., “The Optimization of Staged Development of Lunar Navigation Satellite System”, Space Sciences and Technology Conference, Tokushima, Japan, 2019 (Written in Japanese)
2. **Iiyama, K**., “[Optimization of the Navigation satellite constellation and Lunar Monitoring Station for Lunar Global Navigation Satellite System](/files/ISTS2019.pdf)", 32nd International Symposium on Space Technology and Science, Fukui, Japan, 2019 (**Student session finalist**)