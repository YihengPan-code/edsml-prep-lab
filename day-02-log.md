# EDSML 预习 Day 02 学习笔记

**日期**: 2026-05-14 (周四)
**学习者**: Yiheng Pan
**位置**: v2 Taskbook · Week 0 · Day 2 — 项目冻结与入口重建周
**状态**: ✅ EDSML Python §1 完成 · ✅ VS Code 配置优化 · ⏳ Project Cards 并行推进中

---

## 1. 今日定位

按 v2 任务书,Week 0 (05/13-05/17) 的官方任务是项目冻结 — 不学 Python。但 Day 1 实际跑通了 Week 1 的工具链(超前),所以今天把 **Python 副线** 加进来,主线仍然是 Project Cards(并行推进,不在这份日志里详述)。

**Python 副线节奏**: 跟 EDSML pre-induction 的 Python summary 一节一节读 → 我做笔记 → Claude 点评 → 我写 .py 跑通 → 贴代码+实际输出 → 进下一节。

**今天的真正胜利**:
1. 写出了第一个真正的 `.py` 文件(不是 `python -c`),跑通 6 道练习
2. 完整理解了 `\` 转义和 %-style 格式的**心智模型**(不是死记)
3. 学会 VS Code 设置,Enter 不再被建议偷走
4. 开始养成"**先跑再判断 + 逐字符对照原题**"的 debug 习惯

---

## 2. 今日完成 (Done)

### 2.1 概念学习

- EDSML Python summary §1 (print 与字符串格式化)
- `\` 转义的两种功能(语法 ↔ 数据 / 字母 → 特殊字符)
- 三种字符串格式化的历史脉络 (%-style / .format / f-string)
- %-style 格式代码全表 (s/d/f/e/g)
- 关键陷阱: `%d` 砍浮点不四舍五入 / `.f2` ≠ `.2f`

### 2.2 工作流

- 第一次用 `code 文件名.py` 创建文件并编辑
- 文件结构: `~/edsml-prep-lab/python-practice/s01_print.py`
- 终端运行 `.py` 流程: 写 → Cmd+S → `python file.py` → 看输出

### 2.3 VS Code 配置

- `Editor: Accept Suggestion On Enter` 从 `on` → `off` (Enter 不被偷)
- 确认无 Copilot / TabNine / Codeium / Cursor 等 AI 助手

### 2.4 学习计划

- 建立 EDSML Python summary 的**阅读地图**,把 25 节内容对齐到 v2 时间表(见 §4)

---

## 3. 核心概念 (Mental Models)

### 3.1 print() 函数: Python 的"显示文本"工具

**一句话心智模型**:

> `print(...)` 把括号里的东西**变成人能读的文字**(调用 `str()`),扔到 stdout,末尾默认加换行 `\n`。

任何东西都能扔进去 — print 不挑参数类型:

```python
print(23)                       # 23
print([1, 2, 3])                # [1, 2, 3]
print("hello")                  # hello
print(np.array([1,2,3]) * 2)    # [2 4 6]
```

**多参数用逗号**(不是字符串拼接):

```python
print("Alice", 23, "years old")
# Alice 23 years old   ← 默认空格分隔
```

**可选参数 `sep` 和 `end`**:

```python
print("a", "b", "c", sep="-")     # a-b-c
print("loading", end="")           # 不换行
print("...done")                   # 输出: loading...done
```

`end=""` 在长循环打进度时常用。

### 3.2 `\` 转义机制

**核心一句话**:

> **`\` 告诉 Python: 下一个字符不是语法, 是数据。**

为什么需要它?因为字符串用 `'` 或 `"` 包,内容里如果出现同样的引号,Python 不知道是结束符还是数据:

```
'I'm a programmer'
 ↑  ↑
 开始  ??? Python 以为字符串到这就结束了 → SyntaxError
```

`\` 来解二义性:

```
'I\'m a programmer'
   ↑↑
   \ 告诉 Python: 下一个 ' 是字符串内容, 不是结束符
```

#### `\` 的两种功能(同一思路)

**功能 1: 把"语法字符"变回"数据字符"**

| 写法 | 实际表示 |
|---|---|
| `\'` | 一个单引号 |
| `\"` | 一个双引号 |
| `\\` | 一个反斜杠(因为 `\` 本身现在是特殊字符,打它本人也要转义) |

**功能 2: 把"普通字母"变成"特殊字符"**

| 写法 | 实际表示 |
|---|---|
| `\n` | 换行(**一个**字符,不是 `\` 和 `n` 两个) |
| `\t` | tab |
| `\r` | 回车(老 Windows 文件里见) |

这种是 Python 借自 C 的传统约定: 反斜杠 + 字母 = "键盘上没法直接打的特殊字符"。

#### 实战规则

- 字符串里有 `'` → 外层用 `"`
- 字符串里有 `"` → 外层用 `'`
- **只有两种都有**才需要 `\` 转义

日常 90% 靠"换引号"就解决,`\` 是后备方案。

### 3.3 三种字符串格式化 — Python 的三代答案

"格式化"本质是: **把变量的值嵌进文字模板**。Python 历史上给了三代答案,写新代码默认 f-string,但**读老代码要认得另两种** — GitHub 上扒别人脚本随时撞见。

#### 方式 1: %-style (1990s, 借自 C)

```python
print("%s is %d years old" % (name, age))
```

`%s` = 占位符(任何东西自动 str-化),`%d` = 整数,`%.2f` = 2 位小数浮点。模板和值用 `%` 连接,值放元组里。

#### 方式 2: .format() (Python 2.6+, 2008)

```python
print("{} is {} years old".format(name, age))
print("{name} is {age} years old".format(name=name, age=age))
```

`{}` 是占位符,位置或命名都行。

#### 方式 3: f-string (Python 3.6+, 2016, 现代默认)

```python
print(f"{name} is {age} years old")
print(f"Pi is {3.14159:.2f}")     # Pi is 3.14
```

字符串前加 `f`,大括号里**直接写变量名或表达式**。可读性最好。

### 3.4 格式说明 (format spec)

**关键规则**: 格式说明必须**在 `{}` 里面**,用 `:` 隔开。

公式:
```
{变量 : 格式说明}
```

常用三个:

| 写法 | 作用 | 示例 |
|---|---|---|
| `:.2f` | 浮点数保留 2 位小数 | `f"{3.14159:.2f}"` → `3.14` |
| `:,` | 千位分隔符 | `f"{1234567:,}"` → `1,234,567` |
| `:>10` / `:<10` | 右/左对齐到 10 宽 | `f"{'a':>10}"` → 9 个空格 + `a` |

可以组合: `{x:>10.2f}` = 右对齐 10 宽 + 2 位小数。

**格式记法**: `.` `数字` `f` — 顺序固定。**`.f2` 不对,必须是 `.2f`**(今天踩坑点)。

### 3.5 %-style 格式代码全表

| 代码 | 类型 | 例子 | 输出 |
|---|---|---|---|
| `%s` | string(自动 str-化) | `"%s" % 123` | `"123"` |
| `%d` | **整数**(浮点会被截断) | `"%d" % 1.7` | `"1"` |
| `%f` | 浮点数(默认 6 位小数) | `"%f" % 1.7` | `"1.700000"` |
| `%.2f` | 浮点数 2 位小数 | `"%.2f" % 1.755` | `"1.76"` |
| `%e` | 科学计数法 | `"%e" % 1234` | `"1.234000e+03"` |
| `%g` | 通用,自动选最短 | `"%g" % 1234.5` | `"1234.5"` |

**记忆方法**:
```
s = string
d = digit (整数)
f = float
e = exponential
g = general
```

**关键陷阱**: `%d` 拿到浮点会**直接砍小数**(不四舍五入)。`1.755 → 1`。

#### 跨格式化通用

`s` / `d` / `f` / `e` 这套字母在 `%-style` 和 `f-string` 里都通用:

```python
"%.2f" % 1.755          # "1.76"          ← %-style
f"{1.755:.2f}"          # "1.76"          ← f-string

"%d" % 1.755            # "1"             ← %-style 砍小数, 不报错
f"{1.755:d}"            # ValueError!     ← f-string 比较严格
```

**学一次用两套**。

---

## 4. EDSML Python summary 阅读地图

那 25 节**不是 Week 1-2 全吃掉**。按 v2 时间表分配:

| EDSML 节 | 什么时候啃 | 为什么 |
|---|---|---|
| **§1** print/格式化 | ✅ Day 2 (今天) 完成 | 最低门槛 |
| §2 变量/基础类型 | 这周末 / Week 1 | 看任何代码必备 |
| §3-6 if/while/list/for | Week 1 (05/18-05/24) | OpenHeat CSV 处理最小集 |
| §7 列表推导 + §10-11 import/函数 | Week 2 (05/25-05/31) | 重写一个数据处理函数 |
| §9 异常 + §13 文件 + §14 字典 | Week 3 (06/01-06/07) | OpenHeat archive 读取 |
| §17 matplotlib | Week 4 (06/08-06/14) | observed vs predicted 图 |
| §16 set / §19 class / §20 lambda | Week 7+ | 现在不缺 |
| §21-23 MATLAB/R/C++ 对比 | **跳过** | 我不是从这些语言来的 |
| §24-25 装饰器/高级 | Week 15 工程化时回看 | 现阶段没用钉子学钉枪 |

**数学 summary**: 暂时只看**线代第一节** (Vectors / 几何解释) 一页,其他 Week 5 (06/15) 再开。现在啃微积分/PDE 就是消化不良。

---

## 5. 工作流: 从终端创建/编辑/运行 .py 文件

### 5.1 三件事是分开的

| 动作 | 干什么 | 工具 |
|---|---|---|
| 创建 | 造个空文件 | `touch` / 编辑器保存 / `code 新文件名` |
| 编辑 | 写代码 | VS Code / nano / 任何文本编辑器 |
| 运行 | Python 读并执行 | `python 文件名.py` |

Jupyter Notebook 把这三件事揉到一起,所以平时感觉不到分别。但 **95% 的 Python 工作流是分开的**: 编辑器写文件 → 终端跑文件。

### 5.2 推荐主流程: VS Code 写 + 终端跑

```bash
# 1. 建文件夹 (一次性)
mkdir -p ~/edsml-prep-lab/python-practice
cd ~/edsml-prep-lab/python-practice

# 2. 打开/创建文件
code s01_print.py

# 3. (VS Code 里) 写代码, Cmd+S 保存

# 4. 回终端跑
python s01_print.py
```

`code 文件名` 关键点: 文件没真存在,要等 `Cmd+S` 保存才落盘。

### 5.3 备用: 纯终端用 nano

适合一两行的快速改:

```bash
nano s01_print.py
# Ctrl+O 回车 = 保存
# Ctrl+X = 退出
```

**别用 vim**,容易卡住(救命: `:q!` 退出不保存)。

### 5.4 .py 文件 vs Jupyter Notebook

| | `.py` 文件 | `.ipynb` Notebook |
|---|---|---|
| 长什么样 | 纯文本, git 友好 | JSON, git diff 像天书 |
| 怎么跑 | `python file.py` 一次性 | 单元格逐个跑 |
| 适合 | 脚本/函数/工具/可复用代码 | 数据探索/混代码+图+文字 |
| 现在阶段 | **§1-§11 全用这个** | Week 3 起 Pandas 探索再用 |

---

## 6. VS Code 配置 (减少打扰)

### 6.1 关键 3 个键

| 键 | 作用 |
|---|---|
| **Esc** | 关掉所有弹窗,回到"没人打扰我"状态 |
| **Tab** | 接受当前高亮的建议(主动想用时按) |
| **↑ / ↓** | 在建议列表里挑 |

### 6.2 最值得改的设置: 让 Enter 只换行

**操作**:
1. `Cmd + ,` 打开 Settings
2. 搜 `accept suggestion on enter`
3. 改成 `off`

改完 Enter 不再被建议偷走。**这一条解决 90% 的"VS Code 打断我"**。

### 6.3 进一步推迟自动补全

搜 `quick suggestions delay`,默认 10ms 改成 `500` 或 `1000`(毫秒)— 停手半秒到一秒才弹。

代码区的自动补全建议**保留**,它帮你认识 numpy/pandas 那些函数名,学习阶段算助教。

### 6.4 AI 助手 — 必须关

**装了的话立刻卸载**:
- GitHub Copilot
- TabNine
- Codeium
- Cursor / Cody

**理由**: v2 任务书的核心是不让 AI 帮我写代码。Copilot 整段猜你想写啥,Tab 一下就接受,**永远学不到底层**。违背我自己定的"避免对 AI 依赖加深"原则。

VS Code 自带的 **IntelliSense / Pylance** 不是 AI 生成代码,只是列出已存在的函数名,**留着没事**。

---

## 7. 今日代码 (s01_print.py)

文件: `~/edsml-prep-lab/python-practice/s01_print.py`

```python
#question 1
print("Hello world!")

#question 2 
print("I'm a programmer.")
print('I\'m a programmer.')

#question 3
print("""
Good morning,
it's sunny and spring.
Time for some hiking.
""")

#question 4 (using %)
name = "Bob"
height = 1.755
print("%s is %.2f m tall" % (name, height))

#question 4 (using f)
print(f"{name} is {height:.2f} m tall")

#question 5 (new — 等号对齐)
mae = 0.8734
rmse = 1.2456
print(f"{'MAE':<4} = {mae:.2f}")
print(f"{'RMSE':<4} = {rmse:.2f}")

#question 6 (new — 千位分隔符)
n_samples = 1234567
print(f"Loaded {n_samples:,} rows")
```

**期望输出**:
```
Hello world!
I'm a programmer.
I'm a programmer.

Good morning,
it's sunny and spring.
Time for some hiking.

Bob is 1.76 m tall
Bob is 1.76 m tall
MAE  = 0.87
RMSE = 1.25
Loaded 1,234,567 rows
```

---

## 8. 今天养成的两个 debug 习惯

### 8.1 "改 → 保存 → 跑 → 看 → 再改"

```
改代码 → 保存 → python file.py → 看实际输出
   ↑                                    ↓
   └──────── 不对就回来再改 ←────────────┘
```

**不要看着代码猜对不对,跑一次就知道**。

Python 报错信息比任何 AI 点评更有效 — 它**逼你去想"那应该写什么"**。这是后面 debug AI 写的代码的核心技能。

### 8.2 "逐字符对照原题"

今天 Q2 漏了句号 `.` 两次。Claude 提醒: **EDSML 后面跑测试时,预期输出和实际输出差 1 个字符就算 fail**。养成逐字符对照原题的习惯。

---

## 9. 易踩的坑 (今天踩的)

1. **`:.f2` ≠ `:.2f`** — 格式说明顺序是 `点 → 数字 → f`,反了 `ValueError`
2. **`%d` 拿浮点会砍小数** — 不四舍五入,直接截。`1.755 → 1`
3. **`{height}` 不加格式说明就原样打** — `1.755` 不会变 `1.76`,要 `{height:.2f}`
4. **`f-string` 比 `%-style` 严格** — `f"{1.755:d}"` 直接报错,`"%d" % 1.755` 不报错但结果不对
5. **格式说明挂在 `{}` 外面飘** — 必须在 `{}` 里面,前面用 `:` 隔开
6. **VS Code 的 Enter 会偷走建议** — 改 `editor.acceptSuggestionOnEnter` 为 off
7. **没跑就贴代码 = 浪费 Claude 的轮次** — 跑一遍至少能消化 50% 的明显问题
8. **写死了值就用不到练习目的** — `mae = 0.87` 跳过了 `:.2f`,要写原始 `0.8734` 让格式说明真的工作

---

## 10. 待解决 / 明天 (Day 03) 入口

### Week 0 主线(并行推进中,优先级高)

- [ ] OpenHeat Project Card
- [ ] Adaptive GVI/VVI Project Card
- [ ] What_I_need_to_understand.md
- [ ] edsml-prep-lab 文件夹结构正式建好:
  ```bash
  mkdir -p ~/edsml-prep-lab/{project-cards,weekly-notes,no-ai-rewrites,cheatsheets,ai-use-log,python-practice}
  ```
- [ ] `git init` + 第一次 commit
- [ ] GitHub 远端连接(SSH key 或 PAT)

### Python 副线

- [ ] EDSML §2 (变量与基础数据类型)
  - 数字: `int` / `float`,`//` 整除,`%` 取余,`**` 幂
  - 字符串: 索引 `s[0]`、切片 `s[0:5]`、方法 `lower()`/`upper()`/`replace()`/`split()`/`join()`、`len()`
  - 布尔: `True` / `False`,`and` / `or` / `not`,比较运算符 `==` `!=` `<` `>` `<=` `>=`

### 建议明天的开局

| 状态 | 做什么 |
|---|---|
| 状态好 | §2 + 一个 Project Card |
| 状态一般 | 先建 edsml-prep-lab 文件夹 + git init(15 分钟),再做 §2 或 Card |
| 状态差 | 只更新这个 log 就够 |

---

## 11. 给未来 Claude 的上下文 (AI Onboarding)

### 11.1 我是谁

- 普利茅斯大学 Y3 环境科学本科生,即将入读 Imperial EDSML,2026 年 9 月开学
- 研究兴趣: 城市气候 / 暴露于水热 nexus
- 已有技能: R 中等(有 AI 依赖),QGIS 熟练,空间分析 (DBSCAN/GWR/NDVI/GVI)
- 弱项: Python 几乎从零(**现在过了 §1**),C++ 完全无,数学(2019 大一后没碰)
- 性格: INTP — 需要先理解模型再执行,执行力是已知挑战

### 11.2 我现在的位置

- 在执行 **v2 Taskbook** (AI-assisted prototype → 独立可解释能力)
- OpenHeat-ToaPayoh 和 Adaptive GVI/VVI 是 AI-assisted prototypes,**不是我独立写的**
- 4 个月 (2026-05-13 ~ 09-27) 目标: 把这两个项目变成"我自己能解释、能复现、能 defend"
- v2 计划详情见项目根目录的 `YihengPan_EDSML_Taskbook_v2_AI_Assisted_2026.docx`
- Adaptive GVI/VVI 项目: v0.7,详见 `Adaptive_GVI_VVI_Project_Handoff_v0_7_CN.md`

### 11.3 v2 Taskbook 原则

1. 不再加新功能,先冻结、拆解、重写、解释
2. 每周只设一个主主题
3. 每周必须做一次 no-AI reconstruction
4. 对外表达必须诚实: AI-assisted implementation,我贡献的是 problem framing, testing, validation
5. 目标不是提前学完 EDSML,而是开学前拥有可解释、可复现的基础工具箱

### 11.4 v2 时间表(主要里程碑)

- Week 0 (05/13-05/17): 项目冻结 ← **我现在在 Day 2**
- Week 1-2 (05/18-05/31): Python/conda/Git/terminal
- Week 3-4 (06/01-06/14): NumPy/Pandas
- Week 5-6 (06/15-06/28): 线性代数与最小二乘
- Week 7-8 (06/29-07/12): 优化与反演
- Week 9-10 (07/13-07/26): ML workflow
- Week 11-12 (07/27-08/09): Geospatial Python
- Week 13 (08/10-08/16): CV / GVI
- Week 14 (08/17-08/23): PyTorch / SegFormer
- Week 15 (08/24-08/30): FastAPI / 工程化
- Week 16 (08/31-09/06): C++ 预接触
- Week 17 (09/07-09/13): Big Data / SQL
- Week 18-19 (09/14-09/27): 收口 + Mock coursework

### 11.5 给 Claude 的指导原则

- **先给模型,后给操作**: 直接给步骤我不行,要先理解 why
- **每次只面对下一个 10-30 分钟能闭环的事**: 一次塞太多我会过载放弃
- **诚实评估状态**: 状态比进度重要,该停就停。降载规则是 v2 设计的一部分
- **避免对 AI 的依赖加深**: 鼓励我 no-AI reconstruction,告诉我什么时候该自己硬试
- **承认 AI-assisted 工作**: 不要让我把 AI 写的代码说成自己写的
- **代码要解释每个细节**: 我现在不能跳过任何符号,所有 `()` `[]` `:` `\` `.` 都要解释
- **不要假装我会**: 我是真的零基础,不要从"你应该已经知道..."开始

### 11.6 Python 学习模式 (Day 2 确定的工作流)

跟 EDSML pre-induction 的 Python summary **一节一节读**:

1. Claude 把这一节里 EDSML 省略的"为什么"补出来,给心智模型 + 示例
2. 我做我自己的笔记(不照抄)
3. Claude 出练习题(EDSML 原题 + 项目相关的补充题)
4. 我写 .py 文件,**必须先跑通**再贴
5. 贴的时候: 代码 + 终端实际输出
6. Claude 一次点评完,进下一节

**不跑通就贴是禁止动作**。Claude 看到时直接打回,让我先去跑。

### 11.7 当前进度快照 (Day 2 结束)

✅ Day 1 全部内容(工具链,conda,基础概念)
✅ EDSML Python §1 完成(print + 格式化)
✅ 第一个 `.py` 文件跑通(s01_print.py,6 题全对)
✅ VS Code 配置优化(Enter 不被偷,无 Copilot)
✅ EDSML summary 阅读地图(匹配 v2 节奏)
✅ 心智模型: `\` 转义机制 / 三代格式化 / 格式说明 / %-style 代码全表

⏳ Project Cards(并行推进中,不在日志里详述)
⏳ edsml-prep-lab 文件夹结构未正式建
⏳ `git init` 和 GitHub 远端未连
⏳ EDSML §2-§25 待办

---

## 12. 心理状态记录

(给未来的我看)

今天的节奏比 Day 1 更稳。Day 1 是"高强度新概念扫盲",Day 2 是"少一点新概念,多一点实际操作(写 .py 文件 / 跑 / 修 bug)"。**这种"动手"的疲劳和"读概念"的疲劳不一样,是更踏实的累**。

INTP 的一个小观察: 我两次都在 Q2 漏句号,两次都在 Q5 把 mae 写死 — 都是"看清原题"的纪律问题,不是知识问题。Claude 让我"逐字符对照"是对的,这点要意识到。

明天不用追进度。**Project Card 是真的更重要** — Python 副线可以慢一拍,Week 0 三件事 (Project Cards + lab 文件夹 + understand list) 是后面 17 周的"地图"。

**今天结束。明天继续。**

---

*文档生成: 2026-05-14 by Claude*
*更新约定: 每天结束时手动加 §N+1 "Day N 更新",或者在新对话里让 Claude 据当日内容生成 day-NN-log.md*
