---
title: "Ephemeris and Almanac Design for Lunar Navigation Satellites"
excerpt: "Ephemeris and Almanac Design for Lunar Navigation Satellites"
---
**With** Marta Cortinovis, Prof.Gao (Stanford University) <br>

<div style="text-align: center;">
<img src = "https://dl.dropboxusercontent.com/s/2cjk4br9ukk0u86uwq42d/EphemerisFramework.png?rlkey=91fyltmyib5wqth1sqt257bp7&st=ebks23x5&dl=0"
style="height: 248px; width:717px;">
</div>
<br>
<div style="text-align: center;">
</div>

LunaNet satellites need to inform users of their positions to perform trilateration.
To enable this, LunaNet satellites broadcast ephemeris data to lunar users as part of their navigation signal.
Ephemeris data contains parameters to compute satellite positions and clock biases at the time of interest.
The ephemeris must precisely represent satellite positions while minimizing message size to conserve bandwidth and reduce decoding time. 
Designing ephemerides for lunar navigation satellites is challenging because their orbits are elliptical, resulting in dynamically varying satellite velocities and perturbation forces acting on satellites, which require parameterizations adaptable to these changes.

In the earlier work with Marta Cortinovis, we proposed an ephemeris parameterization method that is capable of fitting lunar orbits at accuracies that meet the LunaNet specification.
The proposed method utilizes Chebyshev polynomials to represent the satellite orbit, and solves a constrained convex optimization problem to minimize orbital fitting errors within specified position and velocity tolerances. 
The key benefit of this approach is that it is capable of flexibly balancing the trade-off between message size and accuracy by adjusting the polynomial degree. 
This method, designed with my mentee Marta Cortinovis, was presented at the ION GNSS+ conference in 2023 and received the session's best presentation award.

Recently, I proposed a new representation that combines osculating elements, Chebyshev polynomials, and Fourier polynomials, which greatly reduces the message size and extending message validity.
I also proposed a representation for almanacs, which can fit the orbit for 15 days, within the accuracy of several degrees which is sufficient to warm start the receiver after lunar night.

**Related Publication:** 

[J7] Iiyama, K., Gao, G., “[Ephemeris and Almanac Design for Lunar Navigation Satellites](https://arxiv.org/abs/2510.25161)”, Submitted to IEEE Transactions on Aerospace and Electronic Systems, Under Review

[J3] Cortinovis, M., Iiyama, K., Gao, G., “[Satellite Ephemeris Parameterization Methods to Support Lunar Positioning, Navigation, and Timing Services](https://navi.ion.org/content/71/4/navi.664)”, NAVIGATION: Journal of the Institute of Navigation, Vol. 71, No. 4, 2024

[C14] Cortinovis, M., Iiyama, K., Gao, G., “[Satellite ephemeris approximation methods to support lunar positioning, navigation, and timing services](https://www.ion.org/publications/abstract.cfm?articleID=19282)”, Proceedings of the Institute of Navigation GNSS+ conference (ION GNSS+ 2023), 2023, Best Presentation of the Session [[Slides](https://drive.google.com/file/d/1HG9RaoZfY6DoCg29m-v_fsy_l1IcnqVM/view)]