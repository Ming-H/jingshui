# 静水 (jingshui) 📈 — 投资理财指导 Skill

> A Claude Code Skill that distills the investment methodology of Zhihu professional investor **静水2008** into an actionable knowledge framework. / 体系化提炼职业投资人「静水2008」投资方法论的 Claude Code 技能。

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
  <img alt="Platform" src="https://img.shields.io/badge/platform-Claude%20Code-7c3aed.svg">
  <img alt="Language" src="https://img.shields.io/badge/content-中文-red.svg">
  <img alt="Status" src="https://img.shields.io/badge/status-learning--use--only-orange.svg">
</p>

---

## 📖 项目简介

这是一个 [Claude Code](https://claude.com/claude-code) 技能（Skill）。安装后，当你向 Claude 询问股票投资、选股、买卖时机、仓位、投资学习路径、普通人理财等问题时，Claude 会自动调用本技能，按一套结构化的投资框架作答。

框架提炼自知乎职业投资人 **静水2008**（主页 [zhihu.com/people/ban-ma-ban-ma-30-2](https://www.zhihu.com/people/ban-ma-ban-ma-30-2)，约 7.3 万粉丝、11.9 万赞同）的 192 条公开回答 + 4 篇专栏文章。

**它不是 196 篇原文的堆砌**，而是把散落的内容提炼为可执行的体系：核心理念、术语、选股方法论、识别清单、买卖纪律、周期仓位思维、雷区、学习书单。

---

## 🧠 核心框架速览

| 维度 | 要点 |
|------|------|
| **一句话理念** | 找到当下最景气行业里核心受益、市场认可的超级成长股（α），回调时分仓介入，对了死拿、错了砍掉 |
| **各时代主线** | 吃药喝酒(19-20)→新能源(21-23)→AI泛科技(24-26)→机器人(下一个)；核心 α＝创新高+持续超预期+板块效应；旧主线被新主线虹吸 |
| **投资模式五分法** | 短线题材 / 短线技术分析 / **中线成长价投(作者主做)** / 长线股权红利 / 长线股权垄断 |
| **三种选股法** | 成长选股（彼得·林奇路线）/ 财报选股（巴菲特·芒格路线）/ 周期选股 ＋ **产业对标法** |
| **核心因子 7 条** | 增速≥40% / 新品量价齐升 / 管理层认同 / 时代核心 α / 逻辑不可证伪 / 机构偏好 / 政策第一行业 |
| **5 不买清单** | 亏损股 / 主营增速<40% / 没创一年新高 / 无新产品新市场 / 无强供求矛盾——一票否决 |
| **趋势投资定位** | 本质=基本面投资(股价=EPS×PE，不需看图看量)；看见>分析；最适合散户；纯价投三难点；三弯路 |
| **买卖纪律** | 持盈止损——截断亏损、让利润奔跑；不做 T、不短炒；止损不止盈 |
| **风险红线** | 不加杠杆、不单吊单只（药明康德满融爆仓教训）；分仓分批 |
| **周期仓位** | 高切低是伪命题；关注被错杀优质蓝筹的戴维斯双击；万物皆周期 |
| **雷区** | 技术分析、缠论、短线做 T、高位炒概念、景气下行行业、捡便宜买垃圾股、加杠杆/单吊 |
| **普通人退路** | 存银行 + 红利股 + 指数 ETF |
| **真假大V标准** | 不收费/不写每日复盘/不炒短线/不看图/不做粉丝维护/参与过新能源+AI两波趋势 |

完整内容见 [`SKILL.md`](SKILL.md)。

---

## 📁 目录结构

```
jingshui/
├── SKILL.md        # 主文件：完整投资知识体系 + Claude 应用指南
├── 原文索引.md      # 196 条内容的元数据目录（摘要/赞数/时间/原文链接）
├── scripts/
│   └── build_collection.py  # 从 MediaCrawler JSON 重建「原文索引.md」+ 全文合集
├── README.md       # 本文件
└── LICENSE         # MIT
```

---

## 🚀 安装与使用

### 安装

将本目录复制到 Claude Code 的 skills 目录：

```bash
git clone https://github.com/Ming-H/jingshui.git
cp -r jingshui ~/.claude/skills/
```

### 使用

安装后直接对 Claude 提问即可，Claude 会自动识别并调用：

```
用静水的体系，普通人该怎么开始理财？
怎么找到超级成长股？
财报季该重点看什么？
什么时候该卖出？
```

---

## ⚠️ 重要声明 / Disclaimer

- **非投资建议**：本技能内容为静水2008 个人观点与方法论的整理，**不构成任何投资建议**。金融市场有风险，决策请自负。
- **内容归属**：投资方法论与观点的版权归原作者 静水2008 所有。本仓库为对公开内容的学习性总结（summary / study notes），并保留指向原文的链接（见 `原文索引.md`）。如有异议，请联系仓库所有者删除。
- **主观性提示**：原作内容带有较强主观色彩与自我推崇，部分表述（如天赋论、a9/a10 财富叙事）需批判性看待。
- **不荐股**：本技能不提供任何具体标的的买卖建议，涉及个股时只引导到方法论与财报验证。
- **仅供学习研究**，请遵守所在地法律法规与目标平台的使用条款。

---

## 📜 许可证

本仓库的技能结构与文档以 [MIT License](LICENSE) 开源。

> 其中所整理的投资知识内容归属原作者 静水2008，本仓库以「学习笔记 / 摘要」形式呈现并标注来源，仅用于个人学习与研究。

---

## 🙏 致谢

- 内容来源：[静水2008](https://www.zhihu.com/people/ban-ma-ban-ma-30-2) 于知乎发表的公开回答与专栏。
- 数据采集工具：[MediaCrawler](https://github.com/NanmiCoder/MediaCrawler)。
