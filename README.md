# FISF Thesis Supervisors — Faculty Directory & Supervision Statistics

Interactive data reports on thesis supervision at **Fudan University's International School of Finance (FISF)**.

## Reports

| Report | Description |
|--------|-------------|
| `output/fisf-thesis-supervisors.html` | Main faculty directory with 26 supervisor profiles, thesis statistics, and interactive ECharts visualizations. 308 theses mapped across MFin, MBA, and EMBA programs. |
| `output/fisf-ai-fintech-theses.html` | Curated collection of 67 AI/ML/FinTech-focused theses with tag-based filtering and topic analytics. |

## Research Gap Analysis

`FISF_Thesis_Gap_Analysis.md` identifies critical research gaps for prospective MFin students, including:

- **Agentic AI for investment & portfolio management** (0 existing theses)
- **LLM-based financial analysis** (0 existing theses)
- **Modern deep learning for portfolio optimization** (1 existing thesis)
- 10 concrete thesis topic suggestions with recommended FISF supervisors

## Data

| File | Contents |
|------|----------|
| `thesis_data_314.json` | Raw scraped data from thesis.fudan.edu.cn |
| `thesis_by_supervisor.json` | Theses grouped by supervisor |
| `fintech_ai_theses.json` | 67 AI/ML/FinTech theses with topic tags |
| `thesis_translations.json` | Chinese-to-English title translations |
| `faculty_urls.json` | Faculty profile URLs |
| `thesis_inject.js` | Standalone JS for injecting profile links and thesis dropdowns |

## Tech Stack

Single-file HTML reports built with:
- **ECharts 5** (SVG renderer) — bar, donut, and horizontal bar charts
- **TailwindCSS** — responsive layout and utility styling
- **GSAP + ScrollTrigger** — scroll-triggered animations
- **Google Fonts** — DM Serif Display, Inter, JetBrains Mono

## Source

Data scraped from the [Fudan University Thesis Repository](https://thesis.fudan.edu.cn) (International School of Finance department).

---

Built with [MuleRun](https://mulerun.com)
