---
layout: single
title: "Publications"
permalink: /publications/
author_profile: true
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: https://dl.dropboxusercontent.com/s/7o74n4we213wtrp/ginzan_onsen.JPG?dl=0
  caption: "Photo by Keidai Iiyama / Ginzan Onsen, Japan"
excerpt: "List of journal papers and conference proceedings"
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
toc_sticky: true
years_journal: [2024, 2020]
years_conference: [2024, 2023, 2022, 2021, 2020, 2019]
---
<!--
How to use jekyll-scholar: https://open-research.gemmadanks.com/tutorials/how-to-use-jekyll-scholar-with-github-pages/
-->

You can also find my articles at my [ResearchGate](https://www.researchgate.net/profile/Keidai_Iiyama) and [Google Scholar](https://scholar.google.com/citations?user=84_oy1EAAAAJ&hl=ja).

\* Indicates equal contribution.

## Preprints (Under Review)
{% bibliography -f preprints %}

## Journal Publications
{% bibliography -f journals %}

## Conference Proceedings
{% for y in page.years_conference %}
  <h3  id="{{y}}" class="pubyear">{{y}}</h3>
  {% bibliography -f conferences -q @*[year={{y}}]* %}
{% endfor %}

<!--
## Peer-Reviewed Journal Publications
[J3] Cortinovis,M., **Iiyama,K.**, and Gao,G., "Satellite Ephemeris Approximation Methods to Support Lunar Positioning, Navigation, and Timing Services",  *Navigation: Journal of the Institute of Navigation*, (Submitted, Under revision) 

[J2]  **Iiyama, K**., Bhamidipati,S., and Gao,G., "Precise Positioning and Timekeeping in Lunar Orbit via Terrestrial GPS Time-Differenced Carrier-Phase Measurements", *Navigation: Journal of the Institute of Navigation*, Vol.71, No.1, 2024, [[Paper](https://navi.ion.org/content/71/1/navi.635)] 

[J1] Funase, R., Ikari, S., Miyoshi, K., et al., (**20th Author**), “ Mission to Earth-Moon Lagrange Point by a 6U CubeSat: EQUULEUS”, *IEEE Aerospace & Electro. Systems Magazine*, Vol.35, No.3, pp.30-44, 2020 [[Paper](https://ieeexplore.ieee.org/abstract/document/9076200)]
[<a href="javascript:void(0)" onclick="if(document.getElementById('collapse-bib').style.display=='none'){document.getElementById('collapse-bib').style.display=''}else{document.getElementById('collapse-bib').style.display='none'}">BibTex</a>] [<a href="javascript:void(0)" onclick="if(document.getElementById('collapse-abstract').style.display=='none'){document.getElementById('collapse-abstract').style.display=''}else{document.getElementById('collapse-abstract').style.display='none'}">Abstract</a>]
<div id="collapse-bib" style="display:none; font-family: Arial, sans-serif; font-size: 16px">
  <pre style="background-color: #f0f0f0; padding: 10px;">
      @ARTICLE{Funase_2020_Mission,
      author={Funase, Ryu and Ikari, Satoshi and Miyoshi, Kota and Kawabata, Yosuke and Nakajima, Shintaro and Nomura, Shunichiro and Funabiki, Nobuhiro and Ishikawa, Akihiro and Kakihara, Kota and Matsushita, Shuhei and Takahashi, Ryohei and Yanagida, Kanta and Mori, Daiko and Murata, Yusuke and Shibukawa, Toshihiro and Suzumoto, Ryo and Fujiwara, Masahiro and Tomita, Kento and Aohama, Hiroki and Iiyama, Keidai and Ishiwata, Sho and Kondo, Hirotaka and Mikuriya, Wataru and Seki, Hiroto and Koizumi, Hiroyuki and Asakawa, Jun and Nishii, Keita and Hattori, Akihiro and Saito, Yuji and Kikuchi, Kosei and Kobayashi, Yuta and Tomiki, Atsushi and Torii, Wataru and Ito, Taichi and Campagnola, Stefano and Ozaki, Naoya and Baresi, Nicola and Yoshikawa, Ichiro and Yoshioka, Kazuo and Kuwabara, Masaki and Hikida, Reina and Arao, Shogo and Abe, Shinsuke and Yanagisawa, Masahisa and Fuse, Ryota and Masuda, Yosuke and Yano, Hajime and Hirai, Takayuki and Arai, Kazuyoshi and Jitsukawa, Ritsuko and Ishioka, Eigo and Nakano, Haruki and Ikenaga, Toshinori and Hashimoto, Tatsuaki},
      journal={IEEE Aerospace and Electronic Systems Magazine}, 
      title={Mission to Earth–Moon Lagrange Point by a 6U CubeSat: EQUULEUS}, 
      year={2020},
      volume={35},
      number={3},
      pages={30-44},
      keywords={},
      doi={10.1109/MAES.2019.2955577}}
  </pre>
  <button onclick="copyToClipboard()">Copy</button>
  <script>
  function copyToClipboard() {
    var text = document.getElementById('codeBlock').innerText;
    navigator.clipboard.writeText(text).then(function() {
      document.getElementById('copyMessage').innerText = 'Copying to clipboard was successful!';
      setTimeout(function(){ document.getElementById('copyMessage').innerText = ''; }, 2000); // Clear message after 2 seconds
    }, function(err) {
      document.getElementById('copyMessage').innerText = 'Could not copy text: ' + err;
      setTimeout(function(){ document.getElementById('copyMessage').innerText = ''; }, 2000); // Clear message after 2 seconds
    });
  }
  </script>
</div>
<div id="collapse-abstract" style="display:none">
    <strong> Abstract: </strong> EQUULEUS (EQUilibriUm Lunar-Earth point 6U Spacecraft) will be the world's smallest spacecraft to explore the Earth–Moon Lagrange point. It is being jointly developed by JAXA (Japan Aerospace Exploration Agency) and the University of Tokyo, and will be launched by NASA's Space Launch System Exploration Mission-1. The spacecraft will fly to a libration orbit around the Earth–Moon L2 point (EML2) and will demonstrate low-energy trajectory-control techniques within the Sun—Earth—Moon region for the first time by a nano-class spacecraft. EQUULEUS also carries three scientific observation missions: imaging of Earth's plasmasphere by extreme ultraviolet wavelength, lunar impact flash observation on the far side of the moon, and micrometeoroid flux measurements in the cis-lunar region. While all these missions have their own scientific objectives, they will also contribute to future human activity and/or infrastructure development in the cis-lunar region. Most parts of the spacecraft system use commercial off-the-shelf components, or are designed based on the experiences of various past space missions, with the exception of the newly developed water resistojet propulsion system. EQUULEUS uses X-band frequency for deep space telecommunication. Japanese deep space antennas (64-m and 34-m) will be nominally used for spacecraft operation, and support from the deep space network of JPL (Jet Propulsion Laboratory) is also being planned, especially for the initial phase of operation. The spacecraft will fly to EML2 in less than one year, and will remain there for scientific observations until shortly before the depletion of the onboard propellant, when the spacecraft will leave the orbit for space-debris compliance.
</div>



## Conference Proceedings
*: Equal Contribution

### 2024
[C19] Mina, T., **Iiyama, K**, and Gao,G.,  "Passive Lunar Surface Network-Based Orbit Determination and Time Synchronization of the Lunar Satellite Navigation ", Proceedings of the Institute of Navigation GNSS+ conference (ION GNSS+ 2024), Baltimore, MD, September 2024 (Abstract Submitted) 
      
[C18] **Iiyama, K.**, and Gao,G.,  "Autonomous LunaNet Fault Monitoring with Inter-satellite Links: A Rigidity-Based Approach", Proceedings of the Institute of Navigation GNSS+ conference (ION GNSS+ 2024), Baltimore, MD, September 2024 (Abstract Submitted) 
  
[C17] **Iiyama, K.**, Vila, G.C., Cortinovis, M., Coimbra, K., and Gao,G.,  "System-Level Comparison of Lunar Orbit Determination and Time Synchronization Methods",  Proceedings of the Institute of Navigation GNSS+ conference (ION GNSS+ 2024), Baltimore, MD, September 2024 (Abstract Submitted) 

[C16] \***Iiyama, K**., \*Vila, G.C., and Gao,G.,  "Contact Plan Optimization and Distributed State Estimation for Delay Tolerant Satellite Networks", *IEEE Aerospace Conference*,  Big Sky, MT, March, 2024 [[Paper](https://drive.google.com/file/d/1ysgGIQmowmfzSefFNdOOIWnhi1dVh-9m/view?usp=sharing)] [[Slides](https://drive.google.com/file/d/1Q-1PTQZ3Gtd3rYOmMXX7g4UwT1eMOq-p/view?usp=sharing)]

### 2023

[C15] \***Iiyama, K**., \*Vila, G.C., and Gao,G.,  "LuPNT: Open-Source Simulator for Lunar Positioning, Navigation, and Timing", *Proceedings of the Institute of Navigation GNSS+ conference (ION GNSS+ 2023)*, Denver, CO, September, 2023 [[Paper](https://drive.google.com/file/d/1mdIEUHOrfckKYSbwEAUoubVuhX13GNV_/view)] [[Slides](https://drive.google.com/file/d/1skQkY_pcZwauKjDcvAk_734lyzUmuOUt/view)] [[Code](https://github.com/Stanford-NavLab/LuPNT)]

[C14]  **Iiyama, K**.,  and Gao,G., "Positioning and Timing of Distributed Lunar Satellites via Terrestrial GPS Differential Carrier Phase Measurements", *Proceedings of the Institute of Navigation GNSS+ conference (ION GNSS+ 2023)*, Denver, CO, September, 2023 [[Paper](https://drive.google.com/file/d/1cL5lgkM0RPiFzZyaT2CpQ2vhyATat6S7/view)] [[Slides](https://drive.google.com/file/d/1vNk6GMIdG3MgwIJZojvdi_QiUv46VeDr/view)]

[C13] Cortinovis,M., **Iiyama,K.**, and Gao,G., "Satellite Ephemeris Approximation Methods to Support Lunar Positioning, Navigation, and Timing Services", Proceedings of the Institute of Navigation GNSS+ conference (ION GNSS+ 2023), Denver, CO, September, 2023 **Best Presentation of the Session** [[Paper](https://drive.google.com/file/d/1z-j70jBJPtMAQ6cpA_ig5yjbLJkotSEX/view)]  [[Slides](https://drive.google.com/file/d/1HG9RaoZfY6DoCg29m-v_fsy_l1IcnqVM/view)] [[Video](https://www.youtube.com/watch?v=9dV94dEMBbA)]  

[C12] \*Shimane, Y., and \***Iiyama, K**., "Methods for Dual-Objective High Energy Tour Design", *AAS/AIAA Astrodynamics Specialist Conference*, Big Sky, MT, August, 2023 [[Paper](https://www.dropbox.com/scl/fi/n7kf8ohdq3q3a7ukw2u79/AAS_202308_gecco_spoc1.pdf?rlkey=1nvdlpd1sqvxq37554msyba6p&dl=0)]

[C11]  **Iiyama, K**., Bhamidipati,S., and Gao,G., "Terrestrial GPS Time-Differenced Carrier-Phase Positioning of Lunar Surface Users", *IEEE Aerospace Conference*, Big Sky, MT, March, 2023 [[Paper](https://drive.google.com/file/d/1KULYi3P5_tvvuyoWFqoC_dM_is_1V7Cz/view?usp=sharing)] [[Slides](https://drive.google.com/file/d/1v3gKyHCCTrFBDLstRb_Yw5Y619EQuwiw/view?usp=sharing)]

[C10]  **Iiyama, K**., Bhamidipati,S., and Gao,G., "Precise Positioning and Timekeeping in Lunar Orbit via Terrestrial GPS Time-Differenced Carrier-Phase Measurements", *ION International Technical Meeting (ITM)*, Long Beach, CA, January, 2023 [[Paper](https://drive.google.com/file/d/1jgQMyomCPNhBYvDtb9MAKGabkehjIgL5/view?usp=sharing)][[Slides](https://drive.google.com/file/d/1Me1eJwT1VHI8-crE6kLqaEKAYND_dzS7/view?usp=sharing)]

### 2022
[C9]  Bhamidipati,S., \***Iiyama, K**., \*Mina,T., and Gao,G., "Time-Transfer from Terrestrial GPS for Distributed Lunar Surface Communication Networks", *IEEE Aerospace Conference*, Big Sky, MT, March, 2022. (* Equal Contribution)  [[Paper](https://ieeexplore.ieee.org/document/9843716)] [[Slides](https://drive.google.com/file/d/1q2TtI9oUaNvA4X3iHQRx7EmVmS0OrKFX/view)]

[C8]  **Iiyama, K.**, Kruger, J., and D'Amico, S., "Autonomous Distributed Angles-Only Navigation and Timekeeping in Lunar Orbit", *ION International Technical Meeting (ITM)*, Long Beach, CA, January, 2022 [[Paper](https://www.dropbox.com/s/rmg7advab2m4j1c/ION_ITM_Lunar_Navigation_Paper_Rev3.pdf?dl=0)] [[Slides](https://www.dropbox.com/s/1ocz6mt59xswasl/Keidai_ION_ITM_2022_rev2_slideonly.pdf?dl=0)] [[Video](https://www.youtube.com/watch?v=KsUHGfXN5bM&t=241s)]

### 2021
[C7] **Iiyama, K**, Kawabata, Y., and Funase, R., “Autonomous and Decentralized Orbit Determination and Clock Offset Estimation of Lunar Navigation Satellites Using GPS Signals and Inter-Satellite Ranging”, *Proceedings of the Institute of Navigation GNSS+ conference (ION GNSS+ 2021)*, St.Louis, MO, September, 2021  [[Paper](https://www.dropbox.com/s/0t4kbo6w83hcmxv/ION_GNSS_2021_Iiyama.pdf?dl=0)] [[Slides](https://www.dropbox.com/s/h5wfe2z3tki8mrq/ION_GNSS_2021_iiyama_slideonly.pdf?dl=0)]

### 2020
[C6] Tomita, K., Skinner, K., **Iiyama, K.**, Jagatia, B.A., Nakagawa, T., and Ho, K., “Real-Time Terrain Mapping and Processing for Safe Landing via Deep Neural Networks”, *ASCEND*, Las Vegas, NV, November, 2020  [[Paper](https://arc.aiaa.org/doi/abs/10.2514/6.2020-4150)]

[C5] **Iiyama, K**, Tomita, K., Jagatia, B.A., Nakagawa, T., and Ho, K., “Deep Reinforcement Learning for Safe Landing Site Selection with Concurrent Consideration of Divert Maneuvers”, *AAS/AIAA Astrodynamics Specialist Conference*, Lake Tahoe, CA, August, 2020 [[Paper](https://arxiv.org/pdf/2102.12432.pdf)]

[C4] Shibukawa, T., Matsushita, S., **Iiyama, K.**, Ishikawa, A., Nishii, K., and Funase, R. “Flight Model Thermal Design and Validation for a 6U Deep Space Cubesat EQUULEUS”, *50th International Conference on Environmental Systems*, Lisbon, Portugal, July, 2020. (conference postponed) [[Paper](https://ttu-ir.tdl.org/bitstream/handle/2346/86455/ICES-2020-282.pdf?sequence=1&isAllowed=y)]


### 2019
[C3] Matsushita, S., Shibukawa, T., **Iiyama, K.**, and Funase, R. (2019), “Thermal Design and Validation for a 6U Cubesat EQUULEUS under Constraints Tightly Coupled with Orbital Design and Water Propulsion System”, *49th International Conference on Environmental Systems*, Bostion, MA, The United States, July, 2019, [[Paper](https://ttu-ir.tdl.org/bitstream/handle/2346/84425/ICES-2019-193.pdf?sequence=1&isAllowed=y)]

[C2] **Iiyama, K**., “Optimization of the Navigation satellite constellation and Lunar Monitoring Station for Lunar Global Navigation Satellite System”, *32nd International Symposium on Space Technology and Science*, Fukui, Japan, June, 2019 [[Paper](https://www.dropbox.com/s/ezpirkwlz9xzw6t/ISTS2019.pdf?dl=0)]

[C1] Shibukawa, T., Matsushita, S., **Iiyama, K.**, and Funase, R., “Reflection and Verification of Thermal Design under Tightly-Coupled Constraints to the 6U Deep Space CubeSat EQUULEUS”, *32nd International Symposium on Space Technology and Science*, Fukui, Japan, June, 2019.
 
 -->


<!--
## Domestic Conference Proceedings in Japan (国内学会)
1. **飯山敬大**, 尾崎直哉, 川端洋輔, 船瀬龍, 中須賀真一 "月衛星測位システムの段階的構築過程の最適化",第63回宇宙科学技術連合講演会, 徳島, 2019年11月
2. 秋⼭茉莉⼦, ⻄井啓太, 菊池航世, 室原昌弥, 王啓航, 安宅泰穂, 齋藤勇⼠, 服部旭⼤, 浅川純, ⼩泉宏之, 柿原浩太, 柳⽥幹太, 鈴本遼, **飯⼭敬⼤**, 船瀬⿓, ⼩紫公也，”6UCubeSat：EQUULEUS推進システムAQUARIUSフライトモデルのシステムインテグレーション”，日本航空宇宙学会第50期年会講演会，東京，2019年4月．
3. 菊池航世, 西井啓太, 服部旭大, 浅川純, 齋藤勇士, 菊池航世, 秋山茉莉子, 王啓航, 安宅泰穂, 室原昌弥, 小泉宏之, 柿原浩太, 柳田幹太, 鈴本遼, **飯山敬大**, 船瀬龍, 小紫公也, ”6U CubeSast: EQUULEUS推進システムAQUARIUSのフライトモデルの単体性能想定結果”，平成30年度宇宙輸送シンポジウム，相模原，2019年1月
-->
