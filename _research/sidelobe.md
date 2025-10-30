---
title: "Lunar PNT using GPS Sidelobe Signals"
excerpt: "Lunar PNT using GPS Sidelobe Signals"
---
**With** Sriramya Bhamidipati, Tara Mina, Prof.Gao (Stanford University) <br>

<div style="text-align: center;">
<img src = "https://dl.dropboxusercontent.com/s/3983cccoobov71ttnilqu/sidelobe.png?rlkey=mujdzj9f1ggnxeigpbubh5499&st=vnba9f4o&dl=0"
style="height: 300px; width:420px;">
</div>
<br>
<div style="text-align: center;">
</div>

There is growing interest in exploiting terrestrial GNSS signals for lunar PNT with the goal of enabling real-time, autonomous navigation in cislunar space and reducing reliance on Earth-based tracking. 
In February 2025, NASA and the Italian Space Agency’s Lunar GNSS Receiver Experiment (LuGRE) successfully demonstrated the acquisition of GPS and Galileo signals in lunar orbit. 
Yet achieving meter-level accuracy required for LunaNet remains challenging due to low signal power, unmodeled ionospheric and plasmaspheric delays, and poor satellite geometry.
To address these challenges, I have proposed a suite of new algorithms tailored for lunar ODTS.

## Use of Time-Differenced Carrier Phase (TDCP) Measurements:
I developed ODTS algorithms for lunar satellites that fuse precise TDCP measurements with pseudorange measurements and orbital dynamics models. 
The algorithm employs adaptive process-noise tuning and onboard cycle-slip detection enabling robust performance under varying dynamics in ELFOs. 
Monte Carlo simulations demonstrated that the proposed algorithm achieved 14.0 m (3$\sigma$) position accuracy in an ELFO after convergence, compared to 50 m (3$\sigma$) for the pseudorange-only baseline. 
I further extended this framework for additional applications, including lunar rovers (integrating inertial measurement unit (IMU) data) and relative navigation between satellites using TDCP and single-difference measurements.

**Related Publications:** 

[J2] Iiyama, K., Bhamidipati, S., Gao, G., “[Precise Positioning and Timekeeping in a Lunar Orbit via Terrestrial GPS Time-Differenced Carrier-Phase Measurements](https://navi.ion.org/content/71/1/navi.635)”, NAVIGATION: Journal of the Institute of Navigation, Vol. 71, No. 1, 2024

[C15] Iiyama, K., Gao, G., “[Positioning and Timing of Distributed Lunar Satellites via Terrestrial GPS Differential Carrier Phase Measurements](https://drive.google.com/file/d/1cL5lgkM0RPiFzZyaT2CpQ2vhyATat6S7/view)”, Proceedings of the Institute of Navigation GNSS+ conference (ION GNSS+ 2023), 2023

[C12] Iiyama, K., Bhamidipati, S., Gao, G., “[Terrestrial GPS time-differenced carrier-phase positioning of lunar surface users](https://drive.google.com/file/d/1KULYi3P5_tvvuyoWFqoC_dM_is_1V7Cz/view)”, 2023 IEEE Aerospace Conference, 2023


## Ionospheric and Plasmaspheric Delay Characterization and Mitigation:
I proposed a ray-tracing algorithm to quantify ionospheric and plasmaspheric delays for GNSS signals that reach lunar orbit using the Global Core Plasma Model (GCPM), and evaluated delay mitigation strategies, including altitude masking, frequency combinations, and single-difference techniques between receivers.
This work received the Best Presentation of the Session Award at the 2025 ION GNSS+ conference.

**Related Publications:** 

[J6] Iiyama, K., Gao, G., “[Ionospheric and Plasmaspheric Delay Characterization for Lunar Terrestrial GNSS Receivers with Global Core Plasma Model](https://arxiv.org/abs/2510.10059)”, Submitted to NAVIGATION: Journal of the Institute of Navigation, Under Review

[C22] Iiyama, K., Gao, G., “[Ionospheric and Plasmaspheric Delay Characterization and Mitigation Methodologies for Lunar Terrestrial GNSS Receivers]()”, Proceedings of the Institute of Navigation GNSS+ conference (ION GNSS+ 2025), 2025, Best Presentation of the Session

## Improving Geometrical Diversity with Crosslinks and Multi-GNSS: 
I also proposed algorithms to enhance the geometrical diversity of observations by incorporating crosslinks among multiple satellites and surface stations, and utilizing multiple GNSS constellations (e.g., GPS and Galileo).

**Related Publications:** 

[C20] Vila, G.C., Iiyama, K., Gao, G., “[LuPNT: An Open-Source Simulator for Lunar Communications, Positioning, Navigation, and Timing](https://drive.google.com/file/d/1t4BDd2MEI5CnjsShM9xezC0Y28_xfL63/view)”, 2025 IEEE Aerospace Conference, 2025

[C9] Bhamidipati, S., Iiyama*, K., Mina*, T., Gao, G., “[Time-transfer from terrestrial GPS for distributed lunar surface communication networks](https://drive.google.com/file/d/1W_xPTOMYv0S4eohT65VnOtKAQF2ah9tH/view)”, 2022 ieee aerospace conference (aero), 2022

[C7] Iiyama, K., Kawabata, Y., Funase, R., “[Autonomous and decentralized orbit determination and clock offset estimation of lunar navigation satellites using GPS signals and inter-satellite ranging](https://www.dropbox.com/scl/fi/l8hvhv1xge4xd2rs00ahy/ION_GNSS_2021_Iiyama.pdf?rlkey=hr9z2qxw8dhusosicexiyl99s&e=1&dl=0)”, Proceedings of the Institute of Navigation GNSS+ conference (ION GNSS+ 2021), 2021