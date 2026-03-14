import json

# All translations from 7 batches - build cn->en mapping
translations = {}

# Batch 1
b1 = [
  {"cn": "银行资本充足率的影响因素与优化策略 ——以G银行为例", "en": "Impact Factors and Optimization Strategies of Bank Capital Adequacy Ratio: A Case Study of Bank G"},
  {"cn": "A银行个人养老金客户画像与数字化策略研究", "en": "Research on Customer Profiling and Digital Strategies for Personal Pension Business at Bank A"},
  {"cn": "上市公司市值管理现状及策略-宝钢股份为例", "en": "Current Status and Strategies of Market Value Management in Listed Companies: A Case Study of Baosteel Group"},
  {"cn": "互联网金融平台并购转型绩效分析：以东方财富并购同信证券为例", "en": "Performance Analysis of M&A Transformation in Internet Finance Platforms: A Case Study of East Money's Acquisition of Tongxin Securities"},
  {"cn": "商业银行供应链融资新模式研究——基于J银行案例的策略优化探讨", "en": "Research on New Models of Supply Chain Finance in Commercial Banks: Strategic Optimization Based on Bank J Case Study"},
  {"cn": "A证券公司培训体系优化研究", "en": "Research on Optimization of Training System at Securities Company A"},
  {"cn": "郑煤机集团智能制造数字化转型研究", "en": "Research on Digital Transformation of Intelligent Manufacturing in Zhengzhou Coal Mining Machinery Group"},
  {"cn": "证券公司自营投资策略研究-以G证券公司为例", "en": "Research on Proprietary Investment Strategies of Securities Companies: A Case Study of Securities Company G"},
  {"cn": "减持新规下企业分红行为的差异化路径 对经营绩效的影响 ——基于剑桥科技与恒铭达的案例比较分析", "en": "Differentiated Paths of Corporate Dividend Behavior Under New Reduction Rules and Impact on Operating Performance: A Comparative Case Analysis of Cambridge Technology and Hengmingda"},
  {"cn": "关于中小型券商投行业务差异化竞争战略的研究 —以A证券为例", "en": "Research on Differentiated Competitive Strategies for Investment Banking Services in Small and Medium-sized Securities Companies: A Case Study of Securities Company A"},
  {"cn": "锂电企业实践ESG对企业价值的影响——以天齐锂业为例", "en": "Impact of ESG Practice Implementation on Enterprise Value in Lithium Battery Companies: A Case Study of Tianqi Lithium"},
  {"cn": "A光伏企业股权激励对企业绩效的影响研究", "en": "Research on the Impact of Equity Incentives on Enterprise Performance in Photovoltaic Company A"},
  {"cn": "公司跨境支付新框架：地缘政治、金融监管与前沿技术的协同演进", "en": "New Framework for Corporate Cross-border Payments: Synergistic Evolution of Geopolitics, Financial Regulation, and Frontier Technology"},
  {"cn": "广发证券公司发展战略研究", "en": "Research on Development Strategy of Guangfa Securities Company"},
  {"cn": "科技园区对科技企业融资服务路径优化研究——以中关村科技园为例", "en": "Research on Optimization of Financing Service Paths for Technology Enterprises in Science Parks: A Case Study of Zhongguancun Science Park"},
  {"cn": "报行合一政策下保险中介业务转型分析 ——以 DT 公司为例", "en": "Analysis of Insurance Intermediary Business Transformation Under the Integration Policy of Reporting and Practice: A Case Study of Company DT"},
  {"cn": "碳中和债券发行动因及效应分析——以上市公司紫 金矿业集团\u201c21 紫金矿业 GN001\u201d为例", "en": "Analysis of Motivations and Effects of Carbon-Neutral Bond Issuance: A Case Study of Zijin Mining Group's '21 Zijin Mining GN001'"},
  {"cn": "绿色金融发展对非绿色企业的绩效影响", "en": "Impact of Green Finance Development on Performance of Non-Green Enterprises"},
  {"cn": "中小城商行制造业贷款管理问题与优化策略研究-以A银行为例", "en": "Research on Manufacturing Loan Management Issues and Optimization Strategies in Small and Medium-sized City Commercial Banks: A Case Study of Bank A"},
  {"cn": "L体育公司体育赛事营销策略研究", "en": "Research on Sports Event Marketing Strategies of Sports Company L"},
  {"cn": "实体清单政策对企业研发活动的影响：以中芯国际为例", "en": "Impact of Entity List Policy on Corporate R&D Activities: A Case Study of SMIC"},
  {"cn": "Q公司财务共享服务中心绩效评价指标体系优化研究", "en": "Research on Optimization of Performance Evaluation Index System for Shared Financial Services Center at Company Q"},
  {"cn": "情绪视角下\u201c国家队\u201d的股市维稳作用机制", "en": "Mechanism of Market Stabilization Role of 'National Team' from the Perspective of Sentiment"},
  {"cn": "银行普惠业务考核占比加重背景下银行内部风险管理效益分析——以工商银行X支行为例", "en": "Analysis of Internal Risk Management Effectiveness Under Increased Assessment Weight of Inclusive Finance Business: A Case Study of ICBC Branch X"},
  {"cn": "短期国际资本流动与资产价格", "en": "Short-term International Capital Flows and Asset Prices"},
  {"cn": "逆全球化下中国跨境电商公司的战略研究 ——基于TikTok的成功启示视角", "en": "Strategic Research on Chinese Cross-border E-commerce Companies Under Deglobalization: Insights from TikTok's Success"},
  {"cn": "基于沪深300ETF期权的随机波动率模型定价分析", "en": "Pricing Analysis of Stochastic Volatility Models Based on CSI 300 ETF Options"},
  {"cn": "环境规制对重污染企业绿色转型影响——基于新《环保法》的准自然实验", "en": "Impact of Environmental Regulation on Green Transformation of Heavy Polluting Enterprises: A Quasi-natural Experiment Based on the New Environmental Protection Law"},
  {"cn": "管理层讨论与分析信息效率对股价同步性的影响——以2019~2023 A股上市公司样本为例", "en": "Impact of MD&A Information Efficiency on Stock Price Synchronicity: Evidence from A-share Listed Companies (2019-2023)"},
  {"cn": "中国传统仿制药企业转型创新药企业发展战略研究——以A公司为例", "en": "Research on Development Strategy for Transformation of Traditional Generic Drug Enterprises to Innovative Drug Enterprises in China: A Case Study of Company A"},
  {"cn": "企业战略研究——以照明企业 OP 公司为例", "en": "Research on Corporate Strategy: A Case Study of Lighting Company OP"},
  {"cn": "汇川技术发展战略研究", "en": "Research on Development Strategy of Inovance Technology"},
  {"cn": "F银行在华零售业务的发展战略研究", "en": "Research on Development Strategy of Retail Business in China for Bank F"},
  {"cn": "中国医疗器械流通行业并购整合研究：基于J公司案例", "en": "Research on M&A Integration in China's Medical Device Distribution Industry: A Case Study of Company J"},
  {"cn": "新时期民营企业内部腐败特征及治理举措研究 ------ 以 XX 集团为例", "en": "Research on Characteristics of Internal Corruption and Governance Measures in Private Enterprises in the New Era: A Case Study of Group XX"},
  {"cn": "基于品牌社区关系视角下顾客忠诚度对医疗美容行业影响的浅析", "en": "Brief Analysis of Customer Loyalty Impact on the Medical Aesthetics Industry from the Perspective of Brand Community Relationships"},
  {"cn": "外资银行对中国商业银行风险承担的影响研究", "en": "Research on the Impact of Foreign Banks on Risk-Taking of Chinese Commercial Banks"},
  {"cn": "保障性租赁住房REITs融资动因与风险研究 ——以华润有巢REIT为例", "en": "Research on Financing Motivations and Risks of Public Rental Housing REITs: A Case Study of China Resources Home Nest REIT"},
  {"cn": "数字经济时代财富管理数字化机遇与挑战研究：以Z商业银行为例", "en": "Research on Opportunities and Challenges of Wealth Management Digitalization in the Digital Economy Era: A Case Study of Commercial Bank Z"},
  {"cn": "上市公司面值退市的原因分析 ——以广汇汽车为例", "en": "Analysis of Reasons for Delisting at Par Value in Listed Companies: A Case Study of Guanghui Automotive"},
  {"cn": "融资租赁在楼宇节能设备产业发展的创新模式研究", "en": "Research on Innovative Financing Leasing Models in the Development of Building Energy-Saving Equipment Industry"},
  {"cn": "折扣化超市供应链效率现状及提升策略研究 —以HMNB为例", "en": "Research on Current Status and Enhancement Strategies of Supply Chain Efficiency in Discount Supermarkets: A Case Study of HMNB"},
  {"cn": "数字化改造机加工工厂的绩效评估方案优化", "en": "Optimization of Performance Evaluation Schemes for Digital Transformation in Mechanical Processing Factories"},
  {"cn": "SQ轻钢结构屋面光伏集成公司商业模式创新研究", "en": "Research on Business Model Innovation of Light Steel Structure Roof Photovoltaic Integration Company SQ"},
  {"cn": "商业银行助力银发经济推动中国式养老高质量发展的路径研究", "en": "Research on Pathways for Commercial Banks to Support the Silver Economy and Promote High-Quality Development of Chinese-style Elderly Care"},
]

for t in b1:
    translations[t["cn"]] = t["en"]

print(f"Batch 1: {len(b1)} translations")
with open("/workspace/translations_b1.json", "w") as f:
    json.dump(translations, f, ensure_ascii=False)
print(f"Total so far: {len(translations)}")
