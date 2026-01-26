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

There is growing interest in leveraging terrestrial GNSS signals for lunar PNT to enable
autonomous navigation in cislunar space and reduce reliance on Earth-based tracking. In February 2025, the
Lunar GNSS Receiver Experiment (LuGRE) demonstrated the acquisition of GPS and Galileo signals in lunar
orbit. However, achieving the meter-level accuracy required for Lunar Augmented Navigation Services (LANS)
remains challenging due to unmodeled ionospheric and plasmaspheric delays, relativisitc effects, weak signal power, and poor
satellite geometry. I have developed a suite of new algorithms to address these challenges.

While I have published several papers in this area, my most recent publication, [GNSS-based Lunar Orbit and Clock Estimation With Stochastic Cloning UD Filter](https://arxiv.org/abs/2601.16393) is the culmination of my work in this area.

## Ionospheric and Plasmaspheric Delay Characterization and Mitigation:
I proposed a ray-tracing algorithm to quantify ionospheric and plasmaspheric delays for GNSS signals that reach lunar orbit using the Global Core Plasma Model (GCPM), and evaluated delay mitigation strategies, including altitude masking, frequency combinations, and single-difference techniques between receivers.
This work received the Best Presentation of the Session Award at the 2025 ION GNSS+ conference.

**Related Publications:** 

[J6] Iiyama, K., Gao, G., “[Ionospheric and Plasmaspheric Delay Characterization for Lunar Terrestrial GNSS Receivers with Global Core Plasma Model](https://arxiv.org/abs/2510.10059)”, Submitted to NAVIGATION: Journal of the Institute of Navigation, Under Review

[C22] Iiyama, K., Gao, G., “[Ionospheric and Plasmaspheric Delay Characterization and Mitigation Methodologies for Lunar Terrestrial GNSS Receivers]()”, Proceedings of the Institute of Navigation GNSS+ conference (ION GNSS+ 2025), 2025, Best Presentation of the Session

## Use of Precise Time-Differenced Carrier Phase (TDCP) Measurements:
To overcome the high noise of pseudorange measurements at lunar distances, I developed ODTS algorithms that fuse precise TDCP measurements
in combination with pseudorange measurements. I extended this framework to lunar surface navigation and inter-satellite relative navigation.

**Related Publications:** 

[J9] Iiyama, K., Gao G.. "[GNSS-based Lunar Orbit and Clock Estimation With Stochastic Cloning UD Filter](https://arxiv.org/abs/2601.16393)", Submitted to Journal of Guidance, Control, and Dynamics, Under review

[J2] Iiyama, K., Bhamidipati, S., Gao, G., “[Precise Positioning and Timekeeping in a Lunar Orbit via Terrestrial GPS Time-Differenced Carrier-Phase Measurements](https://navi.ion.org/content/71/1/navi.635)”, NAVIGATION: Journal of the Institute of Navigation, Vol. 71, No. 1, 2024

[C15] Iiyama, K., Gao, G., “[Positioning and Timing of Distributed Lunar Satellites via Terrestrial GPS Differential Carrier Phase Measurements](https://drive.google.com/file/d/1cL5lgkM0RPiFzZyaT2CpQ2vhyATat6S7/view)”, Proceedings of the Institute of Navigation GNSS+ conference (ION GNSS+ 2023), 2023

[C12] Iiyama, K., Bhamidipati, S., Gao, G., “[Terrestrial GPS time-differenced carrier-phase positioning of lunar surface users](https://drive.google.com/file/d/1KULYi3P5_tvvuyoWFqoC_dM_is_1V7Cz/view)”, 2023 IEEE Aerospace Conference, 2023


## Numerically Stable Filtering via UD Factorization: 
Processing high-precision TDCP measurements under poor satellite geometry can lead to ill-conditioned covariance matrices. 
To address this, I proposed a new UD-factorized filtering framework capable of processing TDCP measurements, ensuring positive
definiteness of the covariance matrix while overcoming limitations of classical Markov-based formulations.
In addition, we derived recursive equations for fixed-interval smoothers when we process delayed-state measurements.

High-fidelity Monte Carlo simulations demonstrate that processing TDCP measurements and dual-frequency pseudorange with this approach improves positioning and timing accuracy by approximately 15% relative to processing pseudorange-only, meeting stringent LunaNet performance requirements.

[J9] Iiyama, K., Gao G.. "[GNSS-based Lunar Orbit and Clock Estimation With Stochastic Cloning UD Filter](https://arxiv.org/abs/2601.16393)", Submitted to Journal of Guidance, Control, and Dynamics, Under review


## Improving Geometrical Diversity with Crosslinks and Multi-GNSS: 
I also proposed algorithms to enhance the geometrical diversity of observations by incorporating crosslinks among multiple satellites and surface stations, and utilizing multiple GNSS constellations (e.g., GPS, Galileo, QZSS).

**Related Publications:** 

[J9] Iiyama, K., Gao G.. "[GNSS-based Lunar Orbit and Clock Estimation With Stochastic Cloning UD Filter](https://arxiv.org/abs/2601.16393)", Submitted to Journal of Guidance, Control, and Dynamics, Under review

[C9] Bhamidipati, S., Iiyama*, K., Mina*, T., Gao, G., “[Time-transfer from terrestrial GPS for distributed lunar surface communication networks](https://drive.google.com/file/d/1W_xPTOMYv0S4eohT65VnOtKAQF2ah9tH/view)”, 2022 ieee aerospace conference (aero), 2022

[C7] Iiyama, K., Kawabata, Y., Funase, R., “[Autonomous and decentralized orbit determination and clock offset estimation of lunar navigation satellites using GPS signals and inter-satellite ranging](https://www.dropbox.com/scl/fi/l8hvhv1xge4xd2rs00ahy/ION_GNSS_2021_Iiyama.pdf?rlkey=hr9z2qxw8dhusosicexiyl99s&e=1&dl=0)”, Proceedings of the Institute of Navigation GNSS+ conference (ION GNSS+ 2021), 2021