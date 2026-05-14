# OpenHeat-ToaPayoh Project Card

## 1. 问题定义

OpenHeat-ToaPayoh 是我的长期个人技术项目，目标是为新加坡 Toa Payoh 建立一个 100m 网格级城市热暴露 / WBGT 预测、空间审计、校准与风险制图系统。它要解决的不是“画一张热图”，而是：在开放数据不完整、城市形态复杂、官方 WBGT station 稀疏的条件下，如何生成可信、可解释、可复现的街区级热风险判断。项目目前核心方法是 audit → correct → validate → calibrate：先发现数据缺口，再修正空间输入，再用 UMEP/SOLWEIG 和 NEA archive 做验证与校准。

## 2. 输入与输出

系统输入包括 NEA WBGT station archive、Open-Meteo per-station weather forcing、HDB3D / URA / OSM building footprints、OSM overhead infrastructure、vegetation DSM、GEE / Dynamic World / NDVI / land-cover features、SingStat vulnerability proxy、QGIS/UMEP/SOLWEIG outputs。系统输出包括 reviewed augmented DSM、v10-gamma base hazard map、v10-delta overhead sensitivity map、confident/caveated hotspot interpretation map、selected-cell SOLWEIG Tmrt validation、v11 station-weather paired archive、M0–M7 calibration ladder、threshold scan、bootstrap CI、future ML residual dataset。重型 raster、raw archive、SOLWEIG 原始输出不进 Git，只保留轻量报告、脚本、配置和图件。

## 3. 我做了什么

我独立确定项目问题、AOI、版本路线和证据标准；搭建并运行 Python/QGIS/UMEP/SOLWEIG pipeline；手动检查 QGIS 卫星底图、补 missing buildings、修正异常 building height / geometry；发现 v0.9 building DSM gap 后冻结旧结果；在 v10 中完成 augmented DSM、morphology rerun、overhead sensitivity、selected-cell SOLWEIG validation；在 v11 中启动长期 archive collector，建立 NEA–Open-Meteo station pairing、M0–M7 calibration ladder、hourly aggregation、S142 sensitivity、M7 compact baseline、bootstrap CI 与 fixed-threshold scan。关键判断均区分 smoke test 与 formal pass。

## 4. AI 做了什么

AI 主要作为 pair programmer、debug assistant、report drafter 和方法论 reviewer：帮助生成脚本草案、配置模板、bat pipeline、README、handoff、findings report、figure package、Git upload checklist 和迁移文档；协助解释报错、设计 ablation、整理版本叙事，并在多轮 audit 后帮助修正 framing。代码和结论没有直接无审查采用：我负责本地运行、QGIS/卫星图人工验证、manual QA、archive loop 管理、Git 操作、文件筛选、结果取舍和最终判断。AI 的贡献是加速和结构化，不替代我的项目方向、数据验证和方法论责任。

## 5. 我能解释什么

我能解释为什么 v0.9 必须 freeze：旧 HDB3D+URA DSM completeness 不足导致 false hotspot；为什么 v10 要先做 reviewed DSM 而不是直接 ML；为什么 overhead infrastructure 不能简单当 building 或 open space；为什么 TP_0565 / TP_0986 是 confident hot anchors，而 TP_0088 / TP_0916 是 overhead-confounded；为什么 v11 calibration 要拆分 retrospective 与 operational pairing；为什么 hourly_max 比 15-min WBGT 更适合 operational warning；为什么 M5/M6/M7 bit-identical 说明当前 NEA station network 下 morphology calibration 不可识别，而不是 morphology 物理上没用。

## 6. 我不能解释什么 / 下一步要学什么

我目前不能完全 defend 全 AOI SOLWEIG 物理细节、wind / longwave / anisotropic sky 的完整参数化，也不能把 v11-beta.1 的 4–5 天 smoke result 当正式 calibration science。morphology 对 station-level WBGT 的贡献现在受 NEA network 稀疏限制，不能靠现有数据强行证明。未来需要等 14-day formal beta snapshot，再判断 M4 / M7 / H1–H11 是否稳定；30 天 archive 后才考虑 ML residual。下一步学习重点是 headless SOLWEIG batch、formal snapshot discipline、uncertainty / conformal prediction、water-heat nexus、risk integration，以及如何设计更合理的 sensor network 或 mobile validation。 
