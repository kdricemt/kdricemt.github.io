---
layout: splash
title: "Projects"
permalink: /research/
author_profile: true
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: https://dl.dropboxusercontent.com/s/y426s802k93sote/volcano.jpg?dl=0
  caption: "Photo by Keidai Iiyama / Volcano, Hawaii"
excerpt: "Selected research, enginnering, and class projects"
intro: 
  - excerpt: ''
feature_row_lunar_pnt1:
  - image_path: https://dl.dropboxusercontent.com/s/1rcox0ptjthd6len9wqdk/dtn_nav_23.png?rlkey=uqw4vjrztrsedj2d7jtx3yen9&dl=0
    alt: "ephemeris"
    title: "Contact Plan Optimization and Distributed State Estimation for Delay Torelant Satellite Network"
    excerpt: "**Period:** 2023/1-Present <br>
    **With:** Guillem Casadesus Vila, Prof.Gao (Stanford University) <br><br> 
    
    Space agencies are seeking to utilize delay torelant satellite networks that provides both communication and navigation service to support future deep space missions. We propose an integrative solution that optimizes contact plan of these networks, considering both navigation and communication performance. Additionally, we propose a distributed orbit and clock bias estimation algorithm using covariance intersection. <br><br>
    **Related Publication:** Contact Plan Optimization and Distributed State Estimation for Delay Tolerant Satellite Networks, *IEEE Aerospace Conference*, 2024 (Abstract Accepted) [[Paper](https://drive.google.com/file/d/181gwBOnjbX3qSOpsu7iM-QQoA-GE1gXm/view?usp=sharing)]
    "
  - image_path: https://dl.dropboxusercontent.com/s/f6vkb0gsvypb88e4cybft/simulator_landscape.png?rlkey=0c65f7rtfwt0jqr62isc8asy5&dl=0
    alt: "simulator"
    title: "LuPNT: Open Source Simulator for Lunar PNT"
    excerpt: "**Period:** 2023/4-Present <br>
    **With** Guillem Casadesus Vila, Prof.Gao (Stanford University) <br><br>
    
    The growing focus on missions to the Moon necessitates reliable Positioning, Navigation, and Timing (PNT) services in cis-lunar space. We are developing a comprehensive, open-source simulation framework to address the growing research need in this field. Implemented primarily in C++ for computational efficiency, the simulation core employs an event-based architecture to model asynchronous onboard applications and inter-satellite communication. The framework also includes Python bindings to facilitate rapid algorithmic development and user interaction. <br><br>
    **Related Publication:** LuPNT: Open-Source Simulator for Lunar Positioning, Navigation, and Timing, *ION GNSS+ 2023*, 2023 [[Paper](https://drive.google.com/file/d/1mdIEUHOrfckKYSbwEAUoubVuhX13GNV_/view)] [[Slides](https://drive.google.com/file/d/1skQkY_pcZwauKjDcvAk_734lyzUmuOUt/view)] [[Code](https://github.com/Stanford-NavLab/LuPNT)]
    "
  - image_path: https://dl.dropboxusercontent.com/s/kkdr6ysq4cuf6mz9f6b29/Sidelobe_32.png?rlkey=ug0zf436mgxacldh1i0xmv86t&dl=0
    alt: "Sidelobe"
    title: "Lunar PNT using GPS Sidelobe signals"
    excerpt: "**Period:** 2021/9-Present <br>
    **With** Sriramya Bhamidipati, Tara Mina, Prof.Gao (Stanford University) <br><br>
    
    We develop various algorithms to conduct orbit determination and time-transfer in the lunar orbit and on lunar surface, that utilize the weak GPS sidelobe signals. We consider both single-agent and multi-agent scenarios at lunar surface and lunar orbit. Our proposed framework uses differential carrier phase measurements and/or crosslinks between lunar satellites to improve PNT performance under challenging GPS geometry. "
    url: /research/LGPS/
    btn_label: "Read More"
    btn_class: "btn--primary"
feature_row_astrodynamics:
  - image_path: https://dl.dropboxusercontent.com/s/cn4qe0l62w07uz9sp6yoo/Ephemeris_32.png?rlkey=o78zx27m31gey0oy9a6whdkce&dl=0
    alt: "ephemeris"
    title: "Ephemeris Design for LunaNet Satellites"
    excerpt: "**Period:** 2023/1-Present <br>
    **With:** Marta Cortinovis, Prof.Gao (Stanford) <br> <br>
    
    Plans to establish a satellite network around the Moon to support communication, position, navigation, and timing services are rapidly evolving. Satellites that are part of this system broadcast their ephemeris as finite parameters to lunar users for user state estimation. In this work, We investigate lunar satellite ephemeris parameterization to identify the optimal parameterization to broadcast to a lunar user.
    <br><br>
    **Related Publication:** Satellite Ephemeris Approximation Methods to Support Lunar Positioning, Navigation, and Timing Services, ION GNSS+ 2023, 2023 **Best Presentation of the Session** [[Paper](https://drive.google.com/file/d/1z-j70jBJPtMAQ6cpA_ig5yjbLJkotSEX/view)]  [[Slides](https://drive.google.com/file/d/1HG9RaoZfY6DoCg29m-v_fsy_l1IcnqVM/view)] [[Video](https://www.youtube.com/watch?v=9dV94dEMBbA)]  
    "
  - image_path: https://dl.dropboxusercontent.com/s/oqeju8jugcqt1yrvtynzw/gecco_32.png?rlkey=u3evslv1tas0nr5s3pr06js9l&dl=0
    alt: "gecco"
    title: "Dual-Objective High Energy Tour Design"
    excerpt: "**Period:** 2022/5-2022/8 <br>
    **With:** Yuri Shimane (Georgia Tech) <br> <br>
    **Abstract:** The 2022 edition of the <a href='https://www.esa.int/gsp/ACT/projects/gecco-2022-competition/'>Space Optimisation Competition (SpOC)</a> organized by the Advanced Concepts Team included a problem involving a ∆V and time of flight optimization of a moon tour visiting the seven planets of the Trappist-1 star system. We participated in this competition (5th place), and developed metrics to analyze effictive planets to flyby, as well as heuristics to solve the multiobjective trajectory optimization problem. <br><br>
    **Related Publication:** Methods for Dual-Objective High Energy Tour Design, *AAS/AIAA Astrodynamics Specialist Conference*, 2023 [[Paper](https://www.dropbox.com/scl/fi/n7kf8ohdq3q3a7ukw2u79/AAS_202308_gecco_spoc1.pdf?rlkey=1nvdlpd1sqvxq37554msyba6p&dl=0)]
    "
feature_row_gnc:
  - image_path: https://dl.dropboxusercontent.com/s/4j8zsl5ykc0lcxigvs37u/ARTMS_32.png?rlkey=750qz3qu2yp7w2yiqfolgknrl&dl=0
    alt: "ARTMS"
    title: "Vision Based Distributed Angles-only Navigation in Satellite Swarms (ARTMS)" 
    excerpt: "**Period:** 2021/9-2022/5 <br>
    **With:** Justin Kruger, Prof.D'Amico (Stanford University) <br> <br>
    **Abstract:** We developed The Absolute and Relative Trajectory Measurement System (ARTMS), an algorithmic framework for autonomous, distributed navigation and timekeeping for spacecraft swarms and constellations using angles-only measurements from onboard cameras. I worked on augmenting ARTMS for lunar navigation, and verified its performance via a star tracker in the loop simulations of swarms and constellations in various lunar orbits. <br>
    The performance of ARTMS will be tested in LEO in the [NASA's Starling Mission](https://www.nasa.gov/centers-and-facilities/nasas-starling-mission-sending-swarm-of-satellites-into-orbit/). <br><br>

    **Related Publication:** Autonomous Distributed Angles-Only Navigation and Timekeeping in Lunar Orbit, *ION ITM*, 2022 [[Paper](https://www.dropbox.com/s/rmg7advab2m4j1c/ION_ITM_Lunar_Navigation_Paper_Rev3.pdf?dl=0)] [[Slides](https://www.dropbox.com/s/1ocz6mt59xswasl/Keidai_ION_ITM_2022_rev2_slideonly.pdf?dl=0)] [[Video](https://www.youtube.com/watch?v=KsUHGfXN5bM&t=241s)]
    "

  - image_path: https://dl.dropboxusercontent.com/s/k9jx2f61223hlmc6r1mke/landing_trajectory_32.png?rlkey=4zomxszw1hlrta4rhjna3ihfj&dl=0
    alt: "Landing Trajectory"
    title: "Landing Site Selection and Divert Maneuver Planning with Reinforcement Learning"
    excerpt: '**Period:** 2020/1-2020/8 <br>
    **With:** Kento Tomita, Prof.Ho (Georgia Tech) <br> <br>
    **Abstract:** This research proposes a new integrated framework for identifying safe landing locations and planning in-flight divert maneuvers. I built a reinforcement learning framework that optimizes a landing site selection strategy concurrently with a guidance and control strategy to the target landing site to achieve a safe and efficient landing trajectory at system-level.'
    url: /research/landing/
    btn_label: "Read More"
    btn_class: "btn--primary"
feature_row_cubesat:
  - image_path: https://dl.dropboxusercontent.com/s/zkj0ej1hf8g1mqjk4i5fh/equuleus_32.jpg?rlkey=40ywuodkeehptvjamdeypyct0&dl=0
    alt: "equuleus"
    title: "EQUULEUS (EQUilibriUm Lunar-Earth point 6U Spacecraft) "
    excerpt: '**Period:** 2018/9-2021/8 <br>
    **With:** EQUULEUS Project Team (University of Tokyo, JAXA) <br> <br>
    **Abstract:** EQUULEUS is a 6U CubeSat project for cis-lunar region exploration, developed by JAXA and The University of Tokyo. I worked on thermal analysis, simulator implementation, and on-board software development. The cubesat succesfully completed its DV1 manuever and lunar flyby.'
    url: /research/equuleus/
    btn_label: "Read More"
    btn_class: "btn--primary"
  - image_path: https://dl.dropboxusercontent.com/s/532lafznf27g10vsyrim7/arliss.jpg?rlkey=lxccz3710dzs2tjyn0hxfofym&dl=0
    alt: "arliss"
    title: "CanSat Project in Black Rock Desert (ARLISS)  "
    excerpt: '**Period:** 2017/4-2017/9 <br>
    **With:** ARLISS Project Team (University of Tokyo) <br> <br>
    **Abstract:** ARLISS is a cansat competition in Black Rock, Nevada. Cansats developed by the participants are launched by rockets, going up high to 4km. In the "comeback competition", the participating teams integrate an autonomous system (including cases, parachutes, and rovers) to direct the CanSat to a designated location. Our team won the overall winner and best accuracy award (0 m), which is given to the team that successfully controlled the rover closest to the designated target. 
'
feature_row_class:
  - image_path: https://dl.dropboxusercontent.com/s/fe1yrx90avsgeo324a8uc/entropy_map_32.png?rlkey=zktoyiqlxyw9fhur75xsqv8s8&dl=0
    alt: "entropy_map"
    title: "Multi-Robot Semantic Mapping and Coverage Planning on Occupancy Grids"
    excerpt: "**Class** AA277: Multi-Robot Control and Distributed Optimization (taught by Prof.Schwager) <br>
    **With:** Muhammad Fadhil Ginting (Stanford University) <br><br>
    **Abstract:** We proposed a method for multi-robot mapping and coverage on 2D occupancy grids using high-level semantic information. We represented the distribution of semantic information on occupancy grid map with Dirichlet distribution. Using the semantic distribution, we performed information consensus among robots to build a globally consistent map. Then using the entropy of the semantic information, we develop multi-robot coverage planning algorithm to explore and map the environment efficiently. <br>
    [[Paper](https://www.dropbox.com/scl/fi/9q4aju3qiiuzk42af0nyc/AA277_Mapping.pdf?rlkey=xwh4os7v1kgmbivq9mwumtwng&dl=0)]"
  - image_path: https://dl.dropboxusercontent.com/s/hha66ifeuhe2vhkm1yf4j/Factor_Graph_32.png?rlkey=cxhmk0eubqflii8uw4zes6r3z&dl=0
    alt: "factor_graph"
    title: "Distributed Angles Only Navigation of Spacecraft Swarms via Factor-Graph Optimaization "
    excerpt: "**Class** AA222: Engineering Design Optimization (taught by Prof.Kochenderfer) <br><br>
    **Abstract:** In this work, we propose a factor-graph-based approach to perform batch orbit determination (BOD)using bearing angle measurements from multiple observers. Factor graphs have advantages over the filtering approach in 1) capability to apply sparse optimization algorithms to solve large-scale problems, 2) flexibility to accommodate asynchronous measurements, and 3) improved robustness to highly non-linear systems. We investogate the performance of the proposed factor-graph-based BOD via simulations on low earth orbits, sun-synchronous orbits, and highly elliptical orbits. <br>
    [[Paper](https://www.dropbox.com/scl/fi/agqk78vkrn06gjgwx86xm/AA222_Factor_Graph.pdf?rlkey=b16q46a8nk3ti4we0tu9qg8dj&dl=0)]"
---

{% include feature_row id="intro" type="center" %}

# 1. Research Projects
## 1-1. Lunar Positioning, Navigation, and Timing (PNT)
{% include feature_row id="feature_row_lunar_pnt1" %}

## 1-2. Astrodynamics and Spacecraft Trajectory Design
{% include feature_row id="feature_row_astrodynamics" %}

## 1-3. Spacecraft Guidance, Navigation, and Control (GNC) 
{% include feature_row id="feature_row_gnc" %}

# 2. Engineering Projects
{% include feature_row id="feature_row_cubesat" %}

# 3. Class Projects
{% include feature_row id="feature_row_class" %}