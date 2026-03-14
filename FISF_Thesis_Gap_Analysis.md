# FISF Thesis Research Gap Analysis: Agentic AI, ML Prediction Models & FinTech for Investment/Portfolio Management

**Date:** March 2026
**Scope:** 67 tech-related FISF theses (2020--2025) analyzed against frontier research in Agentic AI, LLM-based finance, and ML-driven portfolio management

---

## 1. Categorization of Existing 67 Theses by Relevance

### Category A: AI Agents / Autonomous Systems for Investment

| Thesis | Author | Degree/Year | Relevance Level |
|--------|--------|-------------|-----------------|
| Application of Deep Reinforcement Learning with Attention Mechanism to Stock Portfolio Weight Allocation: China A-Share Market | 钱泽葭 | MFin/2022 | **HIGH** -- directly addresses autonomous portfolio allocation using DRL |
| Research on Index Futures Price Volatility Prediction and Trading Strategy Based on Machine Learning | 许蔚 | EMBA/2021 | **MEDIUM** -- ML-driven trading strategy, but not agent-based |
| Impact of Tightened HFT Regulation on Quantitative Private Fund Competitiveness | 胡晓慧 | MBA/2023 | **LOW** -- regulatory perspective on quantitative trading, not AI agents |
| Research on AI Empowering Enterprise Compliance Management | 高梓瑜 | MBA/2023 | **LOW** -- AI automation for compliance, not investment agents |

**Verdict: Only 1 thesis (钱泽葭, 2022) directly touches autonomous AI systems for investment. ZERO theses address LLM-based agents, multi-agent orchestration, ReAct-pattern financial agents, or agentic workflows for portfolio construction.**

### Category B: ML Prediction Models for Finance

| Thesis | Author | Degree/Year | Relevance Level |
|--------|--------|-------------|-----------------|
| Research on Credit Risk Early Warning Model for Listed Companies Based on SSA-XGBoost | 马逸杰 | MFin/2023 | **HIGH** -- ML model for credit risk |
| Prediction of Personal Non-performing Loan Repayment Based on Machine Learning | 夏怡卿 | MFin/2023 | **HIGH** -- ML for loan default prediction |
| Research on Index Futures Price Volatility Prediction and Trading Strategy Based on ML | 许蔚 | EMBA/2021 | **HIGH** -- ML for price/volatility prediction |
| Integration of Sentiment Index and Market Return Prediction: PLS Analysis | 狄泽宇 | MFin/2023 | **HIGH** -- sentiment-based return prediction |
| Market Sentiment and Price Prediction in Chinese Real Estate Market | 龚沛承 | MFin/2022 | **MEDIUM** -- prediction model, real estate domain |
| Impact of Investor Sentiment on Stock Returns and Volatility | 林泽伟 | MFin/2023 | **MEDIUM** -- analytical, not a prediction model per se |
| Mechanism of Market Stabilization Role of the "National Team" from a Sentiment Perspective | 吕彦泽 | MFin/2023 | **LOW** -- analytical framework, not predictive ML |
| Impact of IPO Market Performance on Secondary Market Stock Returns and Investor Sentiment | 陈冠安 | MFin/2022 | **LOW** -- empirical analysis, not ML-based |

**Verdict: 4--5 theses use ML for prediction (credit risk, loan default, volatility, sentiment-return). However, all use classical ML (XGBoost, PLS). ZERO theses employ Transformers, LLMs for financial text, Graph Neural Networks, or modern deep learning architectures beyond the single DRL paper.**

### Category C: FinTech for Portfolio/Wealth Management

| Thesis | Author | Degree/Year | Relevance Level |
|--------|--------|-------------|-----------------|
| Application of Deep Reinforcement Learning... to Stock Portfolio Weight Allocation | 钱泽葭 | MFin/2022 | **HIGH** -- directly about portfolio allocation |
| Management Optimization of Fintech Services for Commercial Banks | 戚大伟 | EMBA/2024 | **MEDIUM** -- FinTech services, but bank operations, not portfolio/wealth |
| Impact of Fintech Innovation Regulatory Pilot Programs on Enterprise Productivity | 费沸 | MFin/2023 | **LOW** -- regulatory impact study |
| New Framework for Corporate Cross-border Payments | 朱晓梅 | EMBA/2024 | **LOW** -- payments, not portfolio management |
| Research on Third-party Payment Innovation Under Online Payment Agent Services | 刘爱娜 | MBA/2023 | **LOW** -- payment infrastructure |

**Verdict: Only 1 thesis (钱泽葭, again) directly addresses portfolio management technology. ZERO theses on robo-advisory, automated wealth management platforms, algorithmic rebalancing, or FinTech-driven asset allocation for retail/HNW clients.**

---

## 2. What Has Been Covered Well (Strengths)

### 2.1 Breadth of Digital Transformation Coverage
The 17 digital transformation theses provide extensive coverage of how various industries (banking, insurance, manufacturing) are adopting digital tools. This gives FISF a strong foundation in understanding enterprise-level technology adoption.

### 2.2 Sentiment Analysis as a Financial Factor
With 5 theses addressing investor sentiment and market returns (狄泽宇, 吕彦泽, 林泽伟, 陈冠安, 龚沛承), FISF has built a meaningful cluster of work exploring behavioral finance through quantitative lenses. The PLS-based multi-source sentiment proxy work (狄泽宇) is particularly methodologically rigorous.

### 2.3 Classical ML for Credit/Default Risk
The SSA-XGBoost credit risk model (马逸杰) and the ML-based NPL repayment prediction (夏怡卿) demonstrate competence in applying established ML frameworks to supervised classification problems in banking/credit.

### 2.4 Early DRL for Portfolio Allocation
The 钱泽葭 thesis (2022) on deep reinforcement learning with attention mechanisms for A-share portfolio allocation was forward-looking at the time and remains the only thesis that bridges AI and direct investment decision-making.

### 2.5 ESG and Green Finance Integration
With 8 ESG-related theses, FISF shows strong awareness of sustainable finance, though these remain largely empirical/analytical rather than technology-driven.

### 2.6 Regulatory and Platform Perspectives
Theses on FinTech regulation (费沸), HFT regulation impact (胡晓慧), and blockchain for carbon databases (林力) show awareness of the institutional and infrastructure dimensions of financial technology.

---

## 3. Clear Research Gaps

### GAP 1: LLM-Based Financial Analysis and Reasoning Agents -- CRITICAL GAP

**What is missing:** There is not a single thesis exploring Large Language Models (GPT-4, DeepSeek, Qwen, etc.) for financial analysis tasks such as:
- Earnings call transcript analysis and alpha signal extraction
- Automated equity research report generation
- LLM-based sentiment analysis (far more nuanced than dictionary/PLS methods)
- Financial document understanding (10-K/annual report parsing)
- Chain-of-thought financial reasoning

**Why it matters:** The CFA Institute (2025) reports that 73% of investment-related Y Combinator startups funded between Jan 2024 and June 2025 were agentic AI related. The survey by Yu et al. (2024, arXiv:2408.06361) on "LLM Agents in Financial Trading" documents an explosion of research using LLMs as autonomous trading agents. FISF has zero representation in this space.

**China-specific angle:** DeepSeek-V3, Qwen-2.5, and other Chinese LLMs offer direct research opportunities with domestic models on Chinese financial texts (annual reports in Mandarin, CSRC filings, analyst reports on Wind/Choice).

### GAP 2: Agentic AI Workflows for Investment Decision-Making -- CRITICAL GAP

**What is missing:** No thesis explores:
- Multi-agent systems for investment research (e.g., analyst agent + risk agent + compliance agent)
- ReAct-pattern agents that autonomously retrieve data, reason, and make recommendations
- Orchestrator-worker architectures for portfolio construction (as demonstrated in CFA Institute Case Study 3)
- Human-in-the-loop agentic systems for wealth management
- Tool-augmented LLM agents that call financial APIs (Wind, Bloomberg, Tushare)

**Why it matters:** The CFA Institute's "Automation Ahead" series (Pisaneschi, 2025) provides detailed blueprints for agentic AI in fundamental screening, sustainability research, and portfolio construction. This is now industry-standard frontier knowledge, yet FISF has produced no thesis work in this area.

### GAP 3: Modern Deep Learning for Portfolio Optimization -- SIGNIFICANT GAP

**What is missing:** Beyond the single 2022 DRL paper, there is no thesis exploring:
- Transformer-based models for return prediction and portfolio optimization
- Graph Neural Networks (GNN) for modeling stock relationships and sector dynamics
- Temporal Fusion Transformers for multi-horizon forecasting
- Diffusion models for financial scenario generation
- Foundation models pre-trained on financial data for downstream portfolio tasks
- Attention-based asset allocation with explainability

**Why it matters:** Transformer architectures have become the dominant paradigm in ML research since 2023. Papers on CSI 300 portfolio optimization using Transformers (e.g., dual-variable forecasting frameworks) are now common in top venues. FISF's ML thesis work stops at XGBoost-era methods.

### GAP 4: Robo-Advisory and Automated Wealth Management -- SIGNIFICANT GAP

**What is missing:** Zero theses on:
- Robo-advisor platform design and performance evaluation in the Chinese market
- Automated asset allocation algorithms for retail investors
- Behavioral profiling and personalized portfolio construction using AI
- Comparison of robo-advisory versus human advisor performance in China
- Regulatory framework analysis for robo-advisory services under CSRC/CBIRC rules

**Why it matters:** Statista projects China's robo-advisor AUM to grow substantially through 2028. Ant Group (蚂蚁集团), Lufax (陆金所), and major banks all offer intelligent investment advisory. Despite FISF's fintech focus, no thesis examines this rapidly growing market.

### GAP 5: NLP for Chinese Financial Text Mining -- MODERATE GAP

**What is missing:**
- Named Entity Recognition (NER) for Chinese financial documents
- Event-driven trading strategies using Chinese news/social media NLP
- Structured extraction from CSRC regulatory filings
- Knowledge graph construction from Chinese corporate disclosures (only 1 tangential thesis by 张心远 on knowledge graphs for movable property)
- Fine-tuning Chinese LLMs (Qwen, ChatGLM, DeepSeek) on domain-specific financial corpora

### GAP 6: Explainable AI (XAI) in Financial Decision-Making -- MODERATE GAP

**What is missing:**
- Interpretability methods (SHAP, LIME, attention visualization) applied to financial ML models
- Regulatory-compliant model explanation for credit scoring and investment decisions
- Trust and adoption studies of AI-driven financial recommendations in the Chinese context

### GAP 7: AI for Alternative Data and Alpha Generation -- MODERATE GAP

**What is missing:**
- Satellite imagery, supply chain data, or web scraping for investment signals
- Social media (Weibo, Xueqiu/雪球) data for real-time sentiment and trading signals
- Integration of alternative data sources with traditional factor models

### GAP 8: Real-Time ML Systems for Trading Execution -- MODERATE GAP

**What is missing:**
- Optimal execution algorithms using reinforcement learning
- Market microstructure analysis with deep learning
- High-frequency feature engineering with neural networks
- Latency-aware ML model deployment for live trading

---

## 4. Recommended Thesis Topics to Fill These Gaps

### TOPIC 1: "Multi-Agent LLM System for A-Share Equity Research: Autonomous Analyst, Risk Assessor, and Compliance Checker"

**Research question:** Can a multi-agent LLM architecture (using DeepSeek or Qwen as the backbone) that decomposes equity research into specialized agent roles (fundamental analysis, risk assessment, compliance checking) produce research outputs comparable to junior analyst quality for CSI 300 stocks?

**Methodology:** Design an orchestrator-worker multi-agent system following the ReAct paradigm. The analyst agent retrieves data from Tushare/AKShare APIs, the risk agent evaluates VaR and drawdown scenarios, and the compliance agent checks against CSRC disclosure requirements. Evaluate output quality via expert scoring and back-tested signal performance.

**Fills gap(s):** GAP 1, GAP 2

**Feasibility:** High for MFin -- open-source LLMs (DeepSeek-V3) and free financial data APIs (Tushare, AKShare) make this achievable without Bloomberg access. Code frameworks (LangChain, CrewAI, AutoGen) are well-documented.

**Suggested supervisor:** **童国士 (Tong Guoshi)** -- supervised both ML-finance theses (马逸杰's XGBoost and 钱泽葭's DRL); demonstrated interest in computational methods for finance. Alternatively, **张纯信 (Zhang Chunxin)** -- supervised digital technology thesis and leads the FinTech Research Center with interest in technology applications.

---

### TOPIC 2: "LLM-Based Sentiment Analysis of Chinese Earnings Call Transcripts: Alpha Signal Extraction Using DeepSeek for A-Share Markets"

**Research question:** Does fine-tuned LLM-based sentiment analysis of Chinese-language earnings call transcripts generate statistically significant alpha signals beyond traditional dictionary-based or PLS sentiment measures for A-share stock returns?

**Methodology:** Collect 3+ years of Chinese listed company earnings call transcripts (available via Wind or Eastmoney). Fine-tune DeepSeek/Qwen on financial sentiment classification. Compare long-short portfolio performance of LLM sentiment signals versus traditional sentiment proxies (as used in 狄泽宇's PLS thesis). Control for Fama-French-Carhart factors adapted for the Chinese market.

**Fills gap(s):** GAP 1, GAP 5, GAP 7

**Feasibility:** High for MFin -- transcript data is commercially available, fine-tuning can be done with LoRA/QLoRA on consumer GPUs, and the comparison framework builds directly on existing FISF sentiment research.

**Suggested supervisor:** **张纯信 (Zhang Chunxin)** -- supervised 狄泽宇's sentiment-PLS thesis; direct intellectual lineage. Alternatively, **蒋亮 (Jiang Liang)** -- supervised ML prediction thesis and the real estate sentiment prediction thesis.

---

### TOPIC 3: "Transformer-Based Multi-Factor Portfolio Optimization for CSI 500: Attention Mechanisms for Dynamic Factor Weight Allocation"

**Research question:** Can a Temporal Fusion Transformer (TFT) that dynamically adjusts factor exposures (value, momentum, quality, size, volatility) based on macroeconomic regime signals outperform static factor allocation and classical DRL approaches in the Chinese mid-cap equity market (CSI 500)?

**Methodology:** Train a TFT model on CSI 500 constituent stocks with inputs including traditional factor scores, macroeconomic indicators (PMI, CPI, Shibor), and market microstructure features. Compare Sharpe ratios, maximum drawdowns, and turnover against: (1) equal-weighted factor portfolio, (2) DRL-based allocation (extending 钱泽葭's approach), (3) Black-Litterman baseline. Conduct ablation studies on the attention mechanism to provide interpretability.

**Fills gap(s):** GAP 3, GAP 6

**Feasibility:** Moderate-high for MFin -- requires computational resources but public data and open-source TFT implementations (PyTorch Forecasting) are available. Directly extends 钱泽葭's earlier work with modern architecture.

**Suggested supervisor:** **童国士 (Tong Guoshi)** -- natural extension of his supervised DRL portfolio thesis. Alternatively, **施东辉 (Shi Donghui)** -- supervised the ML-based futures trading strategy thesis and has market microstructure expertise.

---

### TOPIC 4: "Evaluating Robo-Advisory Performance in China: A Comparative Study of AI-Driven vs. Human-Advised Portfolios at Commercial Banks"

**Research question:** How do robo-advisory portfolio outcomes (risk-adjusted returns, drawdown management, client retention, behavioral bias mitigation) compare with human-advised portfolios at major Chinese commercial banks, and what drives adoption/resistance among Chinese retail investors?

**Methodology:** Mixed-methods approach: (1) Quantitative -- collect portfolio performance data from 2-3 robo-advisory platforms (e.g., Ant Fortune's AI advisory, ICBC's AI investment, China Merchants Bank's "摩羯智投") and compare against matched human-advised portfolios over 3 years. (2) Qualitative -- survey 300+ retail investors on adoption barriers, trust factors, and behavioral patterns. Apply the UTAUT2 framework adapted for the Chinese financial services context.

**Fills gap(s):** GAP 4

**Feasibility:** Moderate for MFin -- platform performance data may be available through industry partnerships or public disclosures; survey design is standard MFin methodology. FISF's industry connections should facilitate data access.

**Suggested supervisor:** **马畅 (Ma Chang)** -- supervised the FinTech services for commercial banks thesis (戚大伟); understands bank-FinTech intersection. Alternatively, **王遐昕 (Wang Xiaxin)** -- supervised multiple internet finance and payment theses; familiar with platform economics.

---

### TOPIC 5: "Knowledge Graph-Augmented Credit Risk Assessment: Integrating Corporate Relationship Networks with ML Models for Chinese SME Lending"

**Research question:** Does augmenting traditional ML credit risk models (XGBoost, LightGBM) with knowledge graph-derived features from corporate ownership networks, supply chain relationships, and executive connections improve default prediction accuracy for Chinese SME loans?

**Methodology:** Construct a corporate knowledge graph using Tianyancha/Qichacha data (ownership, legal, supply chain links) for 10,000+ Chinese SMEs. Extract graph-based features (centrality, community detection, path-based risk propagation). Compare prediction performance of: (1) traditional ML with financial features only, (2) ML + knowledge graph features, (3) Graph Neural Network (GNN) end-to-end model. Use Chinese banking NPL data for evaluation.

**Fills gap(s):** GAP 3, GAP 5

**Feasibility:** High for MFin -- extends the methodology of both 马逸杰's credit risk thesis and 张心远's knowledge graph thesis. Public corporate data from Tianyancha is accessible. GNN frameworks (DGL, PyG) are mature.

**Suggested supervisor:** **童国士 (Tong Guoshi)** or **施东辉 (Shi Donghui)** -- both have supervised ML-based risk modeling. **蒋亮 (Jiang Liang)** is also a fit given supervision of the NPL prediction thesis.

---

### TOPIC 6: "Agentic AI for ESG Portfolio Construction: An LLM-Driven Sustainability Screening Workflow for Chinese Equities"

**Research question:** Can an LLM-based agentic workflow that autonomously collects, analyzes, and scores Chinese corporate sustainability disclosures (CSR reports, ESG filings, news) produce ESG scores that are more timely and predictive of future ESG controversies than commercial ESG ratings (MSCI, Wind ESG)?

**Methodology:** Implement the evaluator-optimizer agentic pattern (following CFA Institute Case Study 2 methodology) using a Chinese LLM (DeepSeek/Qwen) to: (1) generate search queries across 5 sustainability dimensions, (2) retrieve and analyze Chinese corporate sustainability reports, (3) iteratively refine until coverage is sufficient, (4) generate scored assessments. Compare LLM-generated ESG scores against MSCI and Wind ESG ratings for predictive power on ESG controversies and stock returns for CSI 300 firms.

**Fills gap(s):** GAP 1, GAP 2, GAP 6 (also bridges the existing ESG thesis cluster with AI/ML methods)

**Feasibility:** Moderate-high for MFin -- combines FISF's existing ESG strength with the agentic AI frontier. FISF has 8 ESG theses providing domain context; this thesis adds the technological dimension.

**Suggested supervisor:** **张纯信 (Zhang Chunxin)** -- FinTech Research Center director with blockchain/technology focus; or supervisors of existing ESG theses for domain guidance. **唐敦哲 (Tang Dunzhe)** -- supervised the AI-agency costs thesis and the FinTech regulation thesis; could provide the AI + corporate governance lens.

---

### TOPIC 7: "Reinforcement Learning for Optimal Trade Execution in China's A-Share Market: Navigating T+1 Settlement and Price Limits"

**Research question:** Can a reinforcement learning agent learn optimal execution strategies (minimizing market impact and slippage) for large institutional orders in the Chinese A-share market, accounting for China-specific microstructure constraints including T+1 settlement, +/-10% price limits, and intraday auction mechanisms?

**Methodology:** Train a Deep Q-Network (DQN) or Proximal Policy Optimization (PPO) agent on Level-2 order book data from the Shanghai/Shenzhen exchanges. The agent's action space includes order splitting, timing, and aggressive/passive order choice. Compare against TWAP, VWAP, and implementation shortfall benchmarks. Evaluate on execution cost (basis points saved), information leakage, and robustness across market volatility regimes.

**Fills gap(s):** GAP 8, GAP 3

**Feasibility:** Moderate for MFin -- requires Level-2 market data (available from CSMAR or commercial providers). Computationally intensive but achievable. The China-specific microstructure constraints make this a genuinely novel contribution versus Western-focused execution research.

**Suggested supervisor:** **施东辉 (Shi Donghui)** -- directly relevant given his supervision of the ML-based futures trading strategy thesis and established expertise in market microstructure and quantitative trading.

---

### TOPIC 8: "Can LLMs Read Chinese Annual Reports? Evaluating Financial Information Extraction and Investment Signal Quality from A-Share Corporate Filings"

**Research question:** How accurately can Chinese-language LLMs (DeepSeek-V3, Qwen-2.5, ChatGLM) extract structured financial information (revenue guidance, risk factors, related-party transactions, contingent liabilities) from Chinese listed company annual reports, and do extracted signals predict future stock returns and earnings surprises?

**Methodology:** (1) Construct a benchmark dataset of 500+ Chinese annual reports with manually labeled key financial items. (2) Evaluate extraction accuracy (precision, recall, F1) of 3+ Chinese LLMs in zero-shot and few-shot settings. (3) Construct long-short portfolios based on LLM-extracted signals (e.g., management tone, risk factor changes, revenue guidance language). (4) Test return predictability controlling for standard factors.

**Fills gap(s):** GAP 1, GAP 5, GAP 7

**Feasibility:** High for MFin -- annual reports are freely available from CNINFO (巨潮资讯). LLM APIs (DeepSeek) are low-cost. The benchmark construction provides a lasting contribution to the Chinese financial NLP community.

**Suggested supervisor:** **张纯信 (Zhang Chunxin)** -- FinTech Research Center expertise in technology applications. **蒋亮 (Jiang Liang)** -- experience with prediction models. **唐敦哲 (Tang Dunzhe)** -- interest in AI's impact on corporate information environments.

---

### TOPIC 9: "Explainable AI for Quantitative Investment: SHAP-Based Factor Attribution in Deep Learning Portfolio Models Applied to Chinese Markets"

**Research question:** Can post-hoc explainability methods (SHAP, integrated gradients, attention visualization) provide financially meaningful and stable factor attribution for deep learning-based quantitative investment models in the Chinese equity market, and does explainability improve institutional investor trust and adoption?

**Methodology:** (1) Train multiple deep learning models (LSTM, Transformer, DRL) for A-share stock selection/portfolio allocation. (2) Apply SHAP and attention-based attribution to decompose model predictions into factor contributions. (3) Evaluate attribution stability (do explanations remain consistent across time periods?), faithfulness (do attributions reflect true model behavior?), and financial meaningfulness (do top-attributed factors align with known Chinese market factor premia?). (4) Conduct structured interviews with 15-20 quantitative fund managers on whether XAI outputs influence their model adoption decisions.

**Fills gap(s):** GAP 6, GAP 3

**Feasibility:** Moderate for MFin -- technically demanding but all components use open-source tools. The qualitative component (interviews with quant managers) leverages FISF's strong industry network.

**Suggested supervisor:** **童国士 (Tong Guoshi)** -- natural fit for the ML/DL model component. **孙林 (Sun Lin)** -- supervised the HFT regulation thesis; understands quantitative fund operations and could advise on the institutional adoption angle.

---

### TOPIC 10: "Automated Financial Advisory Chatbot Using RAG and Chinese LLMs: Design, Evaluation, and Regulatory Compliance for Retail Investor Services"

**Research question:** Can a Retrieval-Augmented Generation (RAG) system built on Chinese LLMs, grounded in CSRC-approved financial advisory content and real-time market data, provide personalized investment advice to Chinese retail investors that meets regulatory standards for suitability and disclosure?

**Methodology:** (1) Build a RAG pipeline using DeepSeek/Qwen with a vector database of: CSRC regulations on investor suitability, fund prospectuses, market commentary, and educational materials. (2) Implement guardrails for compliance: no specific stock recommendations for low-risk-tolerance clients, mandatory risk disclosures, suitability matching. (3) Evaluate on: factual accuracy (versus ground truth), regulatory compliance rate (expert-judged), user satisfaction (survey of 200+ retail investors), and comparison against existing bank chatbot advisory services.

**Fills gap(s):** GAP 2, GAP 4, GAP 5

**Feasibility:** High for MFin -- all technology components are open source. The regulatory analysis provides practical value for the Chinese wealth management industry. Could be developed in partnership with a bank or FinTech company through FISF industry connections.

**Suggested supervisor:** **马畅 (Ma Chang)** -- FinTech banking expertise. **王遐昕 (Wang Xiaxin)** -- internet finance and digital payment platform expertise. **张纯信 (Zhang Chunxin)** -- FinTech Research Center leadership.

---

## 5. Summary: Gap Severity Matrix

| Research Domain | Existing FISF Coverage (2020-2025) | Industry/Academic Frontier (2024-2026) | Gap Severity |
|----------------|-----------------------------------|---------------------------------------|-------------|
| LLM-based financial analysis | **0 theses** | Explosive growth (84+ papers 2022-2025 per PMC review) | **CRITICAL** |
| Agentic AI for investment | **0 theses** | 73% of YC investment startups are agentic AI (CFA Institute 2025) | **CRITICAL** |
| Modern DL for portfolio optimization (Transformer, GNN) | **0 theses** (1 DRL from 2022) | Transformer portfolio models now standard in top venues | **HIGH** |
| Robo-advisory / automated wealth management | **0 theses** | China's robo-advisor market growing rapidly | **HIGH** |
| Chinese financial NLP / text mining | **0 theses** | Rich opportunity with DeepSeek, Qwen, ChatGLM | **HIGH** |
| Explainable AI in finance | **0 theses** | Growing regulatory demand for model interpretability | **MODERATE** |
| Alternative data for alpha | **0 theses** | Mainstream in industry; academic work accelerating | **MODERATE** |
| RL for trade execution | **0 theses** | Active area with China-specific microstructure opportunities | **MODERATE** |
| Classical ML for credit/risk | **2 theses** (XGBoost, NPL prediction) | Mature area; adequate coverage | **LOW** |
| Sentiment and market prediction | **5 theses** | Well-covered at FISF | **LOW** |
| Digital transformation (general) | **17 theses** | Saturated at FISF | **NONE** |
| ESG analysis (non-tech) | **8 theses** | Well-covered at FISF | **NONE** |

---

## 6. Supervisor Mapping for AI/ML Finance Research

Based on thesis supervision patterns observed in the dataset:

| Supervisor | Supervised Theses (Relevant) | Research Alignment | Best Fit Topics |
|-----------|------------------------------|-------------------|----------------|
| **童国士 (Tong Guoshi)** | SSA-XGBoost credit risk, DRL portfolio allocation, AIGC marketing | Computational finance, ML methods | Topics 1, 3, 5, 9 |
| **张纯信 (Zhang Chunxin)** | Sentiment-PLS, virtual digital humans, GenAI; directs FinTech Research Center | FinTech, blockchain, digital innovation | Topics 1, 2, 6, 8, 10 |
| **施东辉 (Shi Donghui)** | ML futures trading, knowledge graph risk, smart elderly care | Market microstructure, quantitative finance | Topics 3, 5, 7 |
| **蒋亮 (Jiang Liang)** | NPL prediction (ML), real estate sentiment prediction | Prediction models, applied ML | Topics 2, 5, 8 |
| **马畅 (Ma Chang)** | FinTech for commercial banks | Banking + technology intersection | Topics 4, 10 |
| **王遐昕 (Wang Xiaxin)** | Third-party payment innovation, IPO sentiment | Internet finance, platform economics | Topics 4, 10 |
| **唐敦哲 (Tang Dunzhe)** | AI impact on agency costs, FinTech regulation | AI + corporate governance/regulation | Topics 6, 8 |
| **孙林 (Sun Lin)** | HFT regulation impact on quant funds | Quantitative fund industry, regulation | Topic 9 |

---

## 7. Strategic Recommendations for FISF

1. **Urgently fill the LLM/Agentic AI gap.** This is the single most conspicuous absence in the thesis portfolio. The industry has moved decisively toward LLM-based financial analysis (CFA Institute series, arXiv survey with 84+ papers), and FISF has zero representation. Topics 1, 2, 6, 8, and 10 all address this.

2. **Leverage Chinese-language LLM advantage.** FISF has a natural competitive advantage that Western business schools lack: direct access to Chinese financial corpora, Chinese-native LLMs (DeepSeek, Qwen), and the China A-share market's unique microstructure. Topics should explicitly target Chinese-language and Chinese-market specificities.

3. **Bridge existing strengths to new frontiers.** The 8 ESG theses + 5 sentiment theses provide domain expertise that can be combined with AI/ML innovation (Topic 6 bridges ESG + agentic AI; Topic 2 bridges sentiment + LLMs). This is more impactful than isolated "AI for X" theses.

4. **Move beyond XGBoost-era methods.** The ML theses cluster around 2021--2023 vintage methods. New theses should employ Transformer architectures, GNNs, and foundation model approaches (Topics 3, 5, 7, 9).

5. **Add robo-advisory coverage.** Given FISF's FinTech positioning and China's growing robo-advisory market, this is a notable blind spot easily addressed through Topics 4 and 10.

---

*Analysis prepared based on complete review of 67 FISF tech-related theses (2020--2025), CFA Institute "Automation Ahead" Agentic AI research (Pisaneschi, 2025), LLM trading agent survey (Yu et al., arXiv:2408.06361), and current academic/industry trends in AI-driven investment management.*
