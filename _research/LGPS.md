---
title: "Staged Development Strategy for Halo Orbit based Lunar Navigation Satellite System"
excerpt: "Optimization of staged development strategy for lunar navigation satellite system considering uncertainties in future area of interest"
period: "2019/4 - Present"
image: 
  url: '/images/lgps/halo-orbit-291x392.png'
  width: '291'
  height: '392'
collection: project
---

| ![lnss_concept-1064x546.png](/images/lgps/lnss_concept-1064x546.png)|
|:==:|
| *Figure 1. Concept of the Research* |

Conventional positioning method on lunar surface mainly relies on captured images from lunar orbiters and lacks real-time property. For advanced missions on the lunar surface in the future, it is necessary to achieve high user positioning accuracy and instant positioning simultaneously. A Lunar Navigation Satellite System (LNSS) is an effective solution to this problem. Previous studies have shown that the number of navigation satellites needed to cover the full moon surface could be reduced by depoying them at the Halo Orbits. My undergraduate study investigated the user positioning performance in detail, and also suggested that the positining performance at low latitude regions could be improved by mixing Distant Retrograde Orbits (DROs) and Near Rectlinear Halo Orbits (NRHOs). 

However over 16 satellites are required to cover the entire surface. Considering the limited area of interest in the initial phase of lunar development and uncertainties in future area of interest, it is not practical to build the entire system all at once. The effective way to develop the LNSS is to start from small number of navigation satellites that could cover restricted area of interest in initial development phase, and gradually increase its capacity through additional satellite deployment. This study aims to optimize the arrangement and staged development strategy of navigation satellites for halo-orbit based LNSS, considering deep uncertainties in future area of interest. The concept is shown in Fig.1.

The idea of the proposed method is to formulate the staged development process as a multi-objective markov decision process, where each objective corresponds to the navigation performance at possible area of interest. We presented an optimization framework that utilizes multi-objective monte-carlo tree search (MO-MCTS) along with the LNSS simulator. A search tree is constructed where nodes correpsponds to constellation arrangement patterns and edges correspond to the addition of navigation satellites. The search tree is constructed by MO-MCTS algorithm that repeats the process of selection, expansion, simulation, and back progation. In MO-MCTS, all pareto solutions are back-propagated towards the root of the search-tree. Therefore, we proposed to use the hypervolume of the stored pareto solutions as an indicator of "flexibility" of the arragment. The MO-MCTS looks for new nodes with high flexibility considering the trade-off of exploration and exploitation. The node that has the highest hypervolumes among all nodes with depth N is considered as the most flexible first stage architecture with depth N. The overall framework is illustrated in Fig.2.

The proposed algorithm is applied on a 2-staged development scenerio where five satellites are deployed to provide positiong service in the south pole region of the Moon in the first phase, and then three satellites are added in the second phase to (objective-A) improve positioning performance at south pole or (objective-B) provide additional positioning service at the north pole. By applying our algorithm, we were able to obtain a first stage architecture with high flexibility that adjust to arbitrary weights on both area of interest in the second stage. Results are shown in Fig.3.

We are currently working on incorpating deployment and station keeping cost of navigation satellite into the optimization module.

| ![lnss_method-1073x613.png](/images/lgps/lnss_method_1073x613.png)|
|:==:|
| *Figure 2. Overall Framework* |

| ![lnss_result-1069x674.png](/images/lgps/lnss_result-1069x674.png)|
|:==:|
| *Figure 3. Result of the Research* |

---
Related Publications:
1. **Iiyama, K.**, Ozaki, N., Kawabata, Y., Funase, R., and Nakasuka, S., “The Optimization of Staged Development of Lunar Navigation Satellite System”, Space Sciences and Technology Conference, Tokushima, Japan, 2019 (Written in Japanese)
2. **Iiyama, K**., “Optimization of the Navigation satellite constellation and Lunar Monitoring Station for Lunar Global Navigation Satellite System”, 32nd International Symposium on Space Technology and Science, Fukui, Japan, 2019 (**Student session finalist**)