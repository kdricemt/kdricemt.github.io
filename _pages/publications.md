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
years_conf: [2025, 2024, 2023, 2022, 2021, 2020, 2019]
---
  
You can also find my articles at my [ResearchGate](https://www.researchgate.net/profile/Keidai_Iiyama) and [Google Scholar](https://scholar.google.com/citations?user=84_oy1EAAAAJ&hl=ja).

## Peer-Reviewed Journal Publications
<ul class="publications-list" style="list-style: none; padding: 0; margin: 0;">
  {% for pub in site.data.pubs_journal %}
    <li class="publication-item" style="padding: 0px; margin-bottom: 0px">
      <p>
        {{ pub.id }} 
        {{ pub.author | strip }}, 
        “{{ pub.title }}”, 
        <em>{{ pub.journal }}</em>, 
        Vol. {{ pub.volume }}, 
        No. {{ pub.number }}, 
        {% if pub.pages %}
          pp. {{ pub.pages }}, 
        {% endif %}
        {{ pub.year }},
        <!-- Paper -->
        [<a href="{{ pub.url }}">Paper</a>]
        <!-- BibTeX -->
        [<a href="javascript:void(0)" onclick="toggleVisibility('bibtex-{{ forloop.index }}')">BibTeX</a>] 
        <!-- Abstract -->
        [<a href="javascript:void(0)" onclick="toggleVisibility('abstract-{{ forloop.index }}')">Abstract</a>]
        <!-- BibTeX Section -->
        <div id="bibtex-{{ forloop.index }}" style="display:none; font-family: Arial, sans-serif; font-size: 16px">
          <pre style="background-color: #f0f0f0;">{{ pub.bibtex }}</pre>
          <button onclick="copyToClipboard('bibtex-{{ forloop.index }}')">Copy</button>
        </div>
        <!-- Abstract Section -->
        <div id="abstract-{{ forloop.index }}" style="display:none">
          <strong>Abstract:</strong>
          {{ pub.abstract }}
        </div>
      </p>
    </li>
  {% endfor %}
</ul>

## Conference Proceedings
{% for year in page.years_conf %}

**{{ year }}**
<ul class="publications-list-conf" style="list-style: none; padding: 0; margin: 0;">
    {% for pub in site.data.pubs_conference %}
      {% if pub.year_num == year %}
        <li class="publication-item-conf" style="padding: 0px; margin-bottom: -3px">
          <p>
            {{ pub.id }} 
            {{ pub.author | strip }}, 
            “{{ pub.title }}”, 
            <em>{{ pub.journal }}</em>, 
            {{ pub.year }},
            {% if pub.award != '' %}
            <strong> {{ pub.award }} </strong>
            {% endif %}
            {% if pub.pdf != '' %}
            [<a href="{{ pub.pdf }}">Paper</a>]
            {% endif %}
            {% if pub.slides != '' %}
              [<a href="{{ pub.slides }}">Slides</a>]
            {% endif %}
            {% if pub.code != '' %}
              [<a href="{{ pub.code }}">Code</a>]
            {% endif %}
            {% if pub.video != '' %}
              [<a href="{{ pub.video }}">Video</a>]
            {% endif %}
            <!-- BibTeX -->
            [<a href="javascript:void(0)" onclick="toggleVisibility('bibtex-conf-{{ forloop.index }}')">BibTeX</a>] 
            <!-- Abstract -->
            [<a href="javascript:void(0)" onclick="toggleVisibility('abstract-conf-{{ forloop.index }}')">Abstract</a>]
            <!-- BibTeX Section -->
            <div id="bibtex-conf-{{ forloop.index }}" style="display:none; font-family: Arial, sans-serif; font-size: 16px">
              <pre style="background-color: #f0f0f0;">{{ pub.bibtex }}</pre>
              <button onclick="copyToClipboard('bibtex-conf-{{ forloop.index }}')">Copy</button>
            </div>
            <!-- Abstract Section -->
            <div id="abstract-conf-{{ forloop.index }}" style="display:none">
              <strong>Abstract:</strong>
              {{ pub.abstract }}
            </div>
          </p>
        </li>
        {% endif %}
    {% endfor %}
</ul>
{% endfor %}

<!--- Javascript --->
<script>
  function toggleVisibility(id) {
    const element = document.getElementById(id);
    element.style.display = element.style.display === 'none' ? '' : 'none';
  }

  function copyToClipboard(id) {
    const elementText = document.getElementById(id).innerText;
    navigator.clipboard.writeText(elementText).then(function () {
      alert('Copied to clipboard!');
    }, function (err) {
      alert('Error copying to clipboard: ' + err);
    });
  }
</script>


<!--
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