---
title: "EQUULEUS"
excerpt: "EQUULEUS is a 6U cubesat project for cis-lunar region exploration, developed by JAXA and The University of Tokyo"
image: 
  url: '/images/equuleus/equuleus.jpg'
  width: '512'
  height: '270'
collection: "project"
---

[EQUULEUS](https://www.space.t.u-tokyo.ac.jp/equuleus/en/) is a 6U CubeSat project for cis-lunar region exploration, scheduled to be launched in 2020 by NASA's Space Launch System (SLS) Exploration Mission 1 (EM-1). I mainly worked on thermal analysis and onboard software/simulator development for the thermal and propulsion subsystem.

EQUULEUS adopts a Water Resistojet Propulsion System for trajectory control for trajectory design control and angular momentum unloading. A large amount of heat required for vaporization and severe power constraint makes the thermal design and control tightly coupled with other subsystems. 
Through thermal vacuum tests and propulsion system operation tests followed by thermal analysis using Thermal Desktop models, we analyzed the feasibility of the entire mission phase.

In addition, due to the severe time-constraint and importance of the initial Delta-V maneuver phase, a robust FDIR (Fault Detection, Isolation, and Recovery) system is required. I was responsible for the FDIR design and software implementation for the thermal management system of both the bus-system and the propulsion module.

EQUULEUS succesfully completed the lunar flyby with water-based propulsion.

<div style="text-align:center">
<img src = "https://dl.dropboxusercontent.com/s/sc3n4us4bkfkiaw/chamber.png?dl=0">
<br><i>Figure 1. Flight Model Thermal Vacuum Chamber Test</i>
</div>
<br>


<div style="text-align:center">
<img src = "https://dl.dropboxusercontent.com/s/rxihafqzod8zk1hfnety6/equ_moon.jpg?rlkey=488bl6vin5u9bgm3pcwz1j98n&st=xlf9mxm0&dl=0">
<br><i>Figure 2. Image taken from EQUULEUS (far-side of the Moon)</i>
</div>
<br>

***Related Publications:***

[J1] Funase, R., et al., “[Mission to earth--moon lagrange point by a 6u cubesat: Equuleus](https://ieeexplore.ieee.org/document/9076200)”, IEEE Aerospace and Electronic Systems Magazine, Vol. 35, No. 3, pp. 30--44, 2020

[C4] Shibukawa, T., Matsushita, S., Iiyama, K., Ishikawa, A., Nishii, K., Funase, R., “[Flight Model Thermal Design and Verification for the 6U Deep Space CubeSat EQUULEUS](https://ttu-ir.tdl.org/server/api/core/bitstreams/681d6ff8-9401-4a80-ba10-604d53648411/content)”, 2020 International Conference on Environmental Systems, 2020

[C3] Matsushita, S., Shibukawa, T., Iiyama, K., Funase, R., “[Thermal Design and Validation for a 6U Deep Space CubeSat EQUULEUS under Constraints Tightly Coupled with Orbital Design and Water Propulsion System](https://ttu-ir.tdl.org/server/api/core/bitstreams/3e7f245a-80b7-4542-86de-1e884547c760/content)”, 49th International Conference on Environmental Systems, 2019