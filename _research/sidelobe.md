---
title: "Lunar PNT using GPS Sidelobe Signals"
excerpt: "Lunar PNT using GPS Sidelobe Signals"
period: "2021/9 - Present"
image: 
  url: '/images/lgps/halo-orbit-291x392.png'
  width: '291'
  height: '392'
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
toc_sticky: true
collection: project
---
**With** Sriramya Bhamidipati, Tara Mina, Prof.Gao (Stanford University) <br>

We develop various algorithms to conduct orbit determination and time-transfer in the lunar orbit and on lunar surface, that utilize the weak GPS sidelobe signals. We consider both single-agent and multi-agent scenarios at lunar surface and lunar orbit. Our proposed framework uses differential carrier phase measurements and/or crosslinks between lunar satellites to improve PNT performance under challenging GPS geometry. 

## 1. Time Transfer to Distributed Lunar Surface Communication Networks
Reliable lunar communication infrastructure will be instrumental in building a sustainable human presence on the Moon. There has been a great emphasis on designing a low-power and an ultra-compact LTE solution for the future Lunar Surface Communication Network (LSCN) due to its ease of transportation and potential for scalable deployment on the lunar surface. Ensuring a reliable LSCN design requires the base stations to be time-synchronized, and to maintain a precise globally referenced timing standard. 

In this work, we propose an LSCN design with distributed time-transfer from Earth-GPS to maintain precise timing across the network. We design a diffusion Kalman filter framework that utilizes the intermittently available Earth-GPS signals and the crosslink signals exchanged among the LSCN base stations to facilitate global time synchronization, while alleviating the timing stability and SWaP requirements for the on-site clocks. We validate our proposed technique by simulating the Earth-GPS satellites and multiple base stations near the Moon's Haworth Crater.

<div style="text-align: center;">
<img src = "https://dl.dropboxusercontent.com/s/fjp8p5i8rpnguveo45ucy/lunar_surface_network.png?rlkey=92h4gr7qtoji627pg8qccxqsd&dl=0"
style="height: 300px; width:503px;">
</div>
<br>
<div style="text-align: center;">
<i>Figure 1: Distributed Earth-to-LSCN time-transfer</i>
</div>

**Related Publications** <br>
[C9]  Bhamidipati,S., \***Iiyama, K**., \*Mina,T., and Gao,G., "Time-Transfer from Terrestrial GPS for Distributed Lunar Surface Communication Networks", *IEEE Aerospace Conference*, Big Sky, MT, March, 2022. (* Equal Contribution)  [[Paper](https://ieeexplore.ieee.org/document/9843716)] [[Slides](https://drive.google.com/file/d/1q2TtI9oUaNvA4X3iHQRx7EmVmS0OrKFX/view)]

## 2. Positioning, Navigation, and Timing in Lunar Orbit using Time-Differential Carrier Phase (TDCP)
We design an Extended Kalman filter framework with augmented states that harnesses the intermittently available terrestrial GPS time-differenced carrier phase (TDCP) values and the gravitational accelerations predicted by the orbital filter.
We implement an adaptive state noise compensation algorithm to estimate the process noise covariance that adapts to the challenging lunar environment with weak gravity and strong third-body perturbations.
Additionally, we perform measurement residual analysis to discard TDCP measurements corrupted by cycle slips and increased measurement noise. 
We showcase higher positioning and timing accuracy as compared to the pseudorange-only navigation solution via Monte-Carlo simulations of a lunar satellite in the elliptical lunar frozen orbit~(ELFO) and Quasi-Frozen Low Lunar Orbit (QFLLO). We also modified the developed framework to be applied for lunar surface rovers with faster rate IMU dynamics.

<div style="text-align: center;">
<img src = "https://dl.dropboxusercontent.com/s/2mukqys8v1atpmgfjan9q/v2_tdcp_concept_small.png?rlkey=hsy5e9doqlyzd0bzuhzae7e3m&dl=0"
style="height: 300px; width:503px;">
</div>
<br>
<div style="text-align: center;">
<i>Figure 2. Lunar PNT using Time Differential Carrier Phase</i>
</div>

<br>

**Related Publications** <br>
[J2]  **Iiyama, K**., Bhamidipati,S., and Gao,G., "Precise Positioning and Timekeeping in Lunar Orbit via Terrestrial GPS Time-Differenced Carrier-Phase Measurements", Navigation: Journal of the Institute of Navigation, March, 2024 [[Paper](https://navi.ion.org/content/71/1/navi.635)] <br>
[C12]  **Iiyama, K**., Bhamidipati,S., and Gao,G., "Terrestrial GPS Time-Differenced Carrier-Phase Positioning of Lunar Surface Users", *IEEE Aerospace Conference*, Big Sky, MT, March, 2023 [[Paper](https://drive.google.com/file/d/1KULYi3P5_tvvuyoWFqoC_dM_is_1V7Cz/view?usp=sharing)] [[Slides](https://drive.google.com/file/d/1v3gKyHCCTrFBDLstRb_Yw5Y619EQuwiw/view?usp=sharing)] <br>
[C11]  **Iiyama, K**., Bhamidipati,S., and Gao,G., "Precise Positioning and Timekeeping in Lunar Orbit via Terrestrial GPS Time-Differenced Carrier-Phase Measurements", *ION International Technical Meeting (ITM)*, Long Beach, CA, January, 2023 [[Paper](https://drive.google.com/file/d/1jgQMyomCPNhBYvDtb9MAKGabkehjIgL5/view?usp=sharing)][[Slides](https://drive.google.com/file/d/1Me1eJwT1VHI8-crE6kLqaEKAYND_dzS7/view?usp=sharing)]


## 3. Relative PNT in Lunar Orbit Using TDCP and Differential Carrier Phase
Relative positioning, navigation, and timing (PNT) are crucial to support proximity operations of multiple spacecraft in lunar orbit, which is expected to play a key role in upcoming lunar missions.
We propose a relative positioning and timekeeping technique in lunar orbit that leverages differential carrier phase measurements of the terrestrial GPS signals.
However, using GPS signals in the lunar orbit is challenging due to
1. the clustered GPS satellite direction leading to a low-observable system
2. the nonexistence of ionosphere delay models for lunar orbit, and
3. the possibility of cycle slips in the low $C/N_0$ signals. 

We designed a PNT framework that tackles the three challenges above, as follows
1. To robustly make the filter converge in a low-observable system, the proposed PNT framework estimates the absolute and relative states in two separate filters, where filter settings (e.g., process noise) can be tuned separately. 
2. To remove the signal-in-space errors, the proposed filter utilizes three different differential measurements. 
 - The absolute filter estimates time-differenced carrier phase (TDCP) measurements in combination with the pseudorange and pseudorange rate measurements, avoiding the need for estimating the integer ambiguity terms that are low observable.
 - The relative filter estimates the relative orbit and clock offsets by processing the single difference carrier phase (SDCP) measurements, where signal-in-space errors are removed thanks to the short inter-satellite distance compared to the Earth-Moon distance. 
 - Using the obtained single difference float ambiguity estimate, the relative filter also fixes the integer ambiguities in double difference carrier phase (DDCP) measurements to improve the relative orbit estimates.
3. Cycleslip corrupted carrier-phase measurements are removed by observing the residuals in the TDCP measurements.

We demonstrate the filter's performance through simulations of two closely operating lunar satellites with different clock grades in the elliptical lunar frozen orbit~(ELFO), wherein we showcase higher positioning and timing accuracy compared to code phase-only PNT methods.

<div style="text-align: center;">
<img src = "https://dl.dropboxusercontent.com/s/ssgjshazkvj3oz2b3kzqo/RelativePNTFramework.png?rlkey=wyd1u33rxqnqo921vbqtp73yi&dl=0">
</div>
<div style="text-align: center;">
<i>Figure 3.  The proposed filtering framework. The absolute filter estimates the absolute state by combining the GPS pseudorange, pseudorange
rate, and TDCP measurements. The estimated absolute orbit and clock biases are passed to the relative state filter to be used for relative orbit
propagation and relative clock bias correction. tion. The relative state filter estimates the relative state and the float solution of the single difference
(SD) float ambiguity. After the single difference float ambiguity estimate has converged, double difference (DD) measurements are formed
using the SD measurements, and integer ambiguity fixing is performed </i>
</div>

<br>

**Related Publications** <br>
[C15] **Iiyama, K**.,  and Gao,G., "Positioning and Timing of Distributed Lunar Satellites via Terrestrial GPS Differential Carrier Phase Measurements", *Proceedings of the Institute of Navigation GNSS+ conference (ION GNSS+ 2023)*, Denver, CO, September, 2023 [[Paper](https://drive.google.com/file/d/1cL5lgkM0RPiFzZyaT2CpQ2vhyATat6S7/view)] [[Slides](https://drive.google.com/file/d/1vNk6GMIdG3MgwIJZojvdi_QiUv46VeDr/view)]