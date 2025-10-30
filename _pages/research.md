---
layout: splash
title: "Research"
permalink: /research/
author_profile: true
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: https://dl.dropboxusercontent.com/s/y426s802k93sote/volcano.jpg?dl=0
  caption: "Photo by Keidai Iiyama / Volcano, Hawaii"
excerpt: "Selected research projects"
intro: 
  - excerpt: ''
feature_row_lunar_pnt:
  - image_path: https://dl.dropboxusercontent.com/s/3983cccoobov71ttnilqu/sidelobe.png?rlkey=mujdzj9f1ggnxeigpbubh5499&st=vnba9f4o&dl=0
    alt: "Sidelobe"
    title: "Lunar PNT using GNSS Sidelobe Signals"
    excerpt: "Utilizing GNSS side lobe signals for autonomous orbit determination and time synchronization of lunar navigation satellites" 
    url: /research/sidelobe/
  - image_path: https://dl.dropboxusercontent.com/s/xzu000hbl4qczibaimxu1/Constellation.png?rlkey=pin5jx167g64psj68m78gl77x&st=kscnohyv&dl=0
    alt: "constellation"
    title: "LunaNet Constellation Design with Staged Development"
    excerpt: "Jointly optimize lunar navigation satellite constellation and staged development sequence to expand coverage from South pole to global"
    url: /research/constellation/
  - image_path: https://dl.dropboxusercontent.com/s/q9hu65kl7q2gss832t0ao/EDMDF_Concept.png?rlkey=cy9pzhrt6mzxfna65xcueykjg&dl=0
    alt: "rigidity"
    title: "Cooperative Satellite Clock Fault Detection Using ISRs"
    excerpt: "Detecting satellite onboard clock jumps without ground monitoring using inter-satellite ranging (ISR) and rigid-graph theory"
    url: /research/rigid_fault/
  - image_path: https://dl.dropboxusercontent.com/s/u7v6y9lbkr7kl4t0uj03c/EphemerisConcept.png?rlkey=sv7aqyjje77gh60e73q4jhilx&st=40rx0pfu&dl=0
    alt: "ephemeris"
    title: "Almanac and Ephemeris Design for Lunar Satellites"
    excerpt: "We design compact and precise ephemeris and almanac representations for lunar navigation satellites" 
    url: /research/ephemeris/
  - image_path: https://dl.dropboxusercontent.com/s/4n17sjahbnzl37s7gaika/dtn_link.gif?rlkey=4b98ld2ogiz7sql4wa3qxitxm&st=o7qsh9io&dl=0
    alt: "contactplan"
    title: "Contact Plan and Distributed State Estimation for DTNs"
    excerpt: "Scheduling links in delay torelant networks (DTNs) to minimize communication delay while improving orbit determination"
    url: /research/contact_plan/
  - image_path: https://dl.dropboxusercontent.com/s/f6vkb0gsvypb88e4cybft/simulator_landscape.png?rlkey=0c65f7rtfwt0jqr62isc8asy5&dl=0
    alt: "simulator"
    title: "LuPNT: Open Source Simulator for Lunar PNT"
    excerpt: "Open-source simulator development in C++ and Python that suports wide range of lunar PNT simulations"
    url: /research/lupnt/
feature_row_others:
  - image_path: https://dl.dropboxusercontent.com/s/4j8zsl5ykc0lcxigvs37u/ARTMS_32.png?rlkey=750qz3qu2yp7w2yiqfolgknrl&dl=0
    alt: "ARTMS"
    title: "Vision Based Distributed Angles-only Navigation in Satellite Swarms (ARTMS)" 
    excerpt: "Angles-only swarm navigation in lunar orbit using startracker images. With Space Rendezvous Lab (SLAB) at Stanford University. "
    url: /research/angles_only/
  - image_path: https://dl.dropboxusercontent.com/s/k9jx2f61223hlmc6r1mke/landing_trajectory_32.png?rlkey=4zomxszw1hlrta4rhjna3ihfj&dl=0
    alt: "Landing Trajectory"
    title: "Landing Site Selection and Divert Maneuver Planning with Reinforcement Learning"
    excerpt: "Optimize landing trajectory that diverts to a safe landing site using RL. With Space Systems Optimization Group (SSOG) at Georgia Tech."
    url: /research/landing/
  - image_path: https://dl.dropboxusercontent.com/s/fb6wopjg888orna8czlgp/Constellation_GS3d-ezgif.com-crop.gif?rlkey=4g577t2eka50houx5hpgvahl4&st=kfymw0c7&dl=0
    alt: "mars_pnt"
    title: "Design and Orbit Determination of Future Mars PNT + Relay Constellation"
    excerpt: "Designing a Mars PNT + relay constellation and autonomous orbit determination framework using inter-satellite links. With Group 332H at JPL."
    url: /research/mars_pnt/
  - image_path: https://dl.dropboxusercontent.com/s/zkj0ej1hf8g1mqjk4i5fh/equuleus_32.jpg?rlkey=40ywuodkeehptvjamdeypyct0&dl=0
    alt: "equuleus"
    title: "EQUULEUS"
    excerpt: 'A 6U lunar small satellite that achieved succesfull lunar flyby with water based propulsion.'
    url: /research/equuleus/
  - image_path: https://dl.dropboxusercontent.com/s/c3ygi209m7yy088qmxsy2/lac_simulator.png?rlkey=02zcy1malsm016zcd61jipcxt&st=p075coh1&dl=0
    alt: "lac"
    title: "Lunar Autonomy Challenge"
    excerpt: 'Won top prize as NAV LAB team on the Lunar Autonomy Challenge, hosted by NASA and APL.'
    url: /research/lac/
---

{% include feature_row id="intro" type="center" %}

# Research Projects
My research interest lies at the intersection of lunar positioning, navigation, and timing (PNT), astrodynamics, spacecraft guidance, navigation, and control (GNC), and multi-agent systems. Below are the lists of research projects that I have worked on at Stanford University, Jet Propulsion Laboratory, and The University of Tokyo.

## Lunar Positioning, Navigation, and Timing (PNT)
My Ph.D. dissertation is on designing a "Lunar GPS" (is called Lunar Augmented Navigation Service, LANS). My reasearch tackles the unique challenges of designing such systems.
{% include feature_row id="feature_row_lunar_pnt" %}

## Other Research Projects
Before and during my Ph.D., I worked with several leading space research groups on projects related to lunar and Martian exploration:
{% include feature_row id="feature_row_others" %}
