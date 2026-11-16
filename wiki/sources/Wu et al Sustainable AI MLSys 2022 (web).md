---
title: Wu et al Sustainable AI MLSys 2022 (web)
type: source
created: 2026-11-11
updated: 2026-11-11
source_count: 1
tags: [A, B, energy, carbon, ai-infrastructure]
elements: [A, B]
origin: web
tier: peer-reviewed
citable: yes
url: https://proceedings.mlsys.org/paper_files/paper/2022/file/462211f67c7d858f663355eff93b745e-Paper.pdf
rehost: no
---

# Wu et al Sustainable AI MLSys 2022 (web)

## Citation

Carole-Jean Wu, Ramya Raghavendra, Udit Gupta, Bilge Acun, Newsha Ardalani, Kiwan Maeng, Gloria Chang, Fiona Aga Behram, James Huang, Charles Bai, Michael Gschwind, Anurag Gupta, Myle Ott, Anastasia Melnikov, Salvatore Candido, David Brooks, Geeta Chauhan, Benjamin Lee, Hsien-Hsin S. Lee, Bugra Akyildiz, Max Balandat, Joe Spisak, Ravi Jain, Mike Rabbat and Kim Hazelwood. "Sustainable AI: Environmental Implications, Challenges and Opportunities." In *Proceedings of Machine Learning and Systems 4 (MLSys 2022)*, Santa Clara, California, 2022. https://proceedings.mlsys.org/paper_files/paper/2022/file/462211f67c7d858f663355eff93b745e-Paper.pdf. Read 2026-11-11.

## Bottom line

- The paper measures the carbon footprint of AI computing at Meta, across data, experimentation, training and inference, and across the life cycle of the hardware.
- For large machine learning (ML) tasks at Meta, it estimates the split between embodied (manufacturing) and operational carbon at roughly 30% to 70%.
- Optimization cut operational power by 20% every six months, but growth in AI use left a net reduction of 28.5% over two years.

## Background

Most authors were at Meta AI; some were also at Harvard University or the University of Pennsylvania. The paper appeared at the fifth MLSys Conference. It uses Meta's production data and Meta's greenhouse gas statistics. The acknowledgements thank "the anonymous reviewers".

## Key claims

- Growth: "The explosive growth in AI use cases at Meta has driven 2.9× increase in AI training infrastructure capacity over the 1.5 years." (Section 1)
- Inference: "we observe trillions of inference per day across Meta’s data centers—more than doubling in the past 3 years." (Section 1)
- Clean energy limits: "Shifting model training and inference to data centers with carbon-free energy can reduce emissions; however, this approach may not scale to a broad set of use cases." (Section 1)
- Clean energy limits: "Infrastructure for carbon-free energy is limited by factors such as geography and available materials (e.g. rare metals), and takes significant economic resources and time to build." (Section 1)
- Embodied share: "the split between the embodied and (location-based) operational carbon footprint is roughly 30% / 70% for the large scale ML tasks." (Section 3)
- Value chain: "More than 50% of Meta’s emissions owe to its value chain — Scope 3 of Meta’s GHG emission." (Section 2.2)
- Net effect: "we reduce the power footprint across the machine learning hardware-software stack by 20% every 6 months. But at the same time, AI infrastructure continued to scale out. The net effect, with Jevon’s Paradox, is a 28.5% operational power footprint reduction over two years" (Section 3)
- Model optimization: "Optimization across the axes of algorithms, platforms, infrastructures, hardware can significantly reduce the operational carbon footprint for the universal translation model by 810×." (Section 5, Key Takeaways)

## Evidence and method

This is a peer-reviewed systems paper. It measures energy use of Meta's ML workloads and estimates embodied carbon with a life cycle assessment (LCA). It assumes a Power Usage Effectiveness (PUE) of 1.1 and server use of 30 to 60% over a 3- to 5-year life.

## Limits

- All measured data are from Meta's fleet. The paper says that open-source model results "may not be reflective of production use cases" (Figure 4 caption).
- Its embodied carbon estimate uses the production footprint of an Apple workstation as a stand-in for a GPU training system.
- It gives no cost in dollars.
- The paper gives "more than 800×" in Section 1 and "810×" in Section 5 for the same translation model.
