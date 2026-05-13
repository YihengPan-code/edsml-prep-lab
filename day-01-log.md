# EDSML 预习 Day 01 学习笔记

**日期**: 2026-05-13 (周三)
**学习者**: Yiheng Pan
**位置**: v2 Taskbook · Week 0 · Day 1 — 项目冻结与入口重建周
**状态**: ✅ 工具链初始化完成 · ⏳ Project Cards 未开始

---

## 1. 今日定位

按 v2 任务书,今天是反向拆解学习计划的 Day 1。**Week 0 的目标不是"开始学 Python",而是停下来盘点**:把 AI-assisted 的 OpenHeat 和 Adaptive GVI/VVI 项目冻结,搞清楚自己理解的边界,建立 edsml-prep-lab 作为接下来 4 个月独立学习的根据地。

但 Day 1 实际进展超过预期 — 把 Mac 上的工具链跑通了,并把 shell/conda/git/Python 生态的基础概念全过了一遍。这是后面 21 周都要用的"压舱石"。

**今天的真正胜利**: 从"只会 `conda activate`"走到了"能解释为什么用 conda、能装好环境、能跑通第一段 Python"。

---

## 2. 今日完成 (Done)

### 2.1 工具链初始化

| 工具 | 状态 | 位置 |
|---|---|---|
| Git | ✅ 已有 (2.50.1) | 系统自带 + Apple CLT |
| VS Code | ✅ 已有 (1.119.1) | Apple Silicon 原生 |
| Python 3.12 (Homebrew) | ✅ 已有 | `/opt/homebrew/bin/python3.12` |
| **Miniforge3** | ✅ 新装 (conda 26.3.2) | `~/miniforge3/` |
| **edsml-prep conda 环境** | ✅ 新建 (Python 3.11) | `~/miniforge3/envs/edsml-prep/` |
| 基础包 | ✅ 已装 | numpy, pandas, matplotlib, jupyter, ipykernel |

### 2.2 第一段 Python 代码 (Mac 端)

```python
import numpy as np
print(np.array([1,2,3]) * 2)
# 输出: [2 4 6]
```

意义: 验证了 conda 环境 → numpy 安装 → Python 解释器全链路通畅。

### 2.3 概念扫盲 (今天的重头)

涵盖了 shell / OS / kernel 层级、PATH 机制、conda vs pip、多 Python 共存、Unix flag 语法、Python list vs numpy array、git 心智模型、Markdown 等多种文件格式的对比与适用场景。详见 §3。

---

## 3. 核心概念 (Mental Models)

### 3.1 系统层级 (从硬件到你)

```
[最底层] 硬件 — M 系列芯片 / 内存 / SSD
              ↓
         Darwin (kernel) — 直接和硬件对话的程序
              ↓
         macOS (操作系统) — kernel + 文件系统/网络/窗口
              ↓
         zsh (shell) — 接收文字命令,转译给 OS
              ↓
         终端 / VS Code — 你看到的界面
              ↓
[最上层] 你 — 输入命令
```

- **kernel** = 操作系统内核,负责管硬件 (内存分配、CPU 调度、权限、IO)。Mac 的 kernel 叫 Darwin,基于 BSD Unix
- **shell** = 包在 kernel 外面、让人能用文字和 OS 对话的程序。也是一种编程语言 (能写循环、条件、函数)
- **zsh** = 一种具体的 shell,macOS Catalina 之后的默认。bash 是它的"前辈",90% 命令通用

### 3.2 Shell 关键机制

**PATH**: shell 的"程序电话簿"。打 `conda --version` 时,shell 按 PATH 顺序去这些文件夹找 `conda` 可执行文件,找到第一个就跑。

**`~/.zshrc`**: zsh 的配置文件,"rc" = "run commands"。每次开新终端时 zsh 读它来设置环境。`~` 是 home 目录简写,`.` 开头表示隐藏文件。

**激活 conda 环境的本质**: `conda activate edsml-prep` = 把那个环境的 Python 路径塞到 PATH 最前面。这之后 `python`、`pip` 都指向那个环境的版本。

### 3.3 Python 生态: Python / conda / pip / 多 Python 共存

**Mac 上获取 Python 的 4 种主流方式**,可以共存,互不冲突:

| 来源 | 位置 | 谁维护 |
|---|---|---|
| macOS 系统 | `/usr/bin/python3` | Apple,**别碰** |
| python.org 安装包 | `/Library/Frameworks/Python.framework/...` | Python 软件基金会 |
| Homebrew | `/opt/homebrew/bin/python3.12` | Homebrew 社区 |
| conda (Miniforge) | `~/miniforge3/...` | conda-forge 社区 |

**我现在用的是 Miniforge** (注意不是 Miniconda 也不是 Anaconda):
- Miniforge 由 conda-forge 社区维护,不是 Anaconda 公司
- 默认 channel 是 conda-forge (~25000 包,完全开源)
- Apple Silicon 原生支持最完整
- 不踩 Anaconda 2024 后的商业 license 问题

**conda vs pip 的分工**:

| | conda | pip |
|---|---|---|
| 来源 | conda channels | PyPI |
| 能装 | Python + C/C++ 二进制 (GDAL, PROJ 等) | 只 Python |
| 包数量 | ~25000 (conda-forge) | ~500000 |
| 依赖处理 | 强,全局检查 | 弱,易冲突 |

**惯例**: 先 conda,后 pip。地理空间库 (geopandas, rasterio) 必须 conda。

**Homebrew (brew)**: macOS 的"包管理器",用于装命令行工具/app/底层库。对 EDSML 不是必需,nice-to-have。

### 3.4 Python 函数调用与 numpy 数组

`np.array([1,2,3])` 拆解:
- `np` = numpy 的别名 (因为 `import numpy as np`)
- `.array` = numpy 提供的函数
- `(...)` = 函数调用语法,把括号内的东西作为输入
- `[1,2,3]` = Python 原生 **list**,方括号语法

**list vs numpy array 的根本差别**:
```python
[1, 2, 3] * 2           # → [1, 2, 3, 1, 2, 3]  (列表被复制)
np.array([1,2,3]) * 2   # → [2 4 6]              (每元素乘 2)
```

numpy array 支持"逐元素数学运算",这是它存在的理由。EDSML 整个 ML 课程建立在 numpy 上。

`;` 在 Python: 等同换行符,允许一行写多句。**正常代码不用**,只在 `python -c "..."` 这种 shell 一行命令里见到。

### 3.5 Git 心智模型

```
[工作区]
working directory
     ↓ git add 文件             ← "装货"
[暂存区]
staging area
     ↓ git commit -m "说明"     ← "集中发货"
[本地仓库]
.git 文件夹 (历史快照库)
     ↓ git push                ← 同步到云
[远端]
GitHub
```

**关键概念**:
- 每次 commit 是一个**完整快照**,有唯一 hash (前 7 位常用)
- git 是本地工具,GitHub 是云服务,**两者独立**
- branch (分支): 平行的开发线,默认叫 `main`

**回退操作的三种方式**:

| 方式 | 命令 | 说明 |
|---|---|---|
| 安全: 看一看旧版本 | `git checkout <hash>` → `git checkout main` 回来 | 工作区临时变成旧版本 |
| 推荐: 正式撤销某次,留痕 | `git revert <hash>` | 新建一个 commit 抵消旧的,历史保留 |
| 危险: 抹掉某次,不留痕 | `git reset --hard <hash>` | **三个月内假装不存在** |

**取出/恢复的常见场景**:

| 想做的事 | 命令 |
|---|---|
| 看历史 | `git log --oneline` |
| 切到旧版本看看 | `git checkout <hash>` → `git checkout main` |
| 改坏一个文件想恢复 | `git restore 文件名` |
| 已 git add 但想拿回工作区 | `git restore --staged 文件名` |
| 从旧 commit 拿单个文件 | `git checkout <hash> -- 文件名` |
| 干净撤销某次 commit | `git revert <hash>` |

### 3.6 文件格式生态

| 格式 | 本质 | 纯文本 | 排版 | git 友好 | 用途 |
|---|---|---|---|---|---|
| TXT | 纯文本 | ✅ | 无 | ✅ | 简单笔记、配置 |
| **Markdown (.md)** | 纯文本 + 简单标记 | ✅ | 中 | ✅ | **学习笔记、README、技术文档** |
| HTML | 纯文本 + 标签 | 半 | 极强 | ✅(diff啰嗦) | 网页、富文档 |
| PDF | 二进制 | ❌ | 极强 | ❌ | 论文、最终交付 |
| Word (.docx) | 二进制 | ❌ | 极强 | ❌ | 办公文档 |

**重要新闻 (2026-05 ~ )**: Anthropic Claude Code 团队成员 Thariq Shihipar 写文章主张 AI 输出应改用 HTML 而非 Markdown,引发争论。结论尚不统一:**Markdown 在文本主导/git 协作/快速写作场景仍占优**,HTML 在可视化展示/交互场景占优。**对我学习日志、README 等用途,Markdown 依然是首选**。

---

## 4. 命令速查表

### 4.1 Shell 常用 (zsh / bash 通用)

```bash
# 导航
pwd                 # 我在哪
ls                  # 列出当前文件
ls -la              # 详细列表 + 显示隐藏文件
cd 路径             # 切换目录
cd ~                # 回 home
cd ..               # 上一层 (父目录)
cd -                # 回到上一次的目录

# 文件夹/文件
mkdir name          # 建文件夹
mkdir -p a/b/c      # 顺便建上层 (递归)
touch name          # 建空文件 (或更新时间戳)
rm file             # 删文件
rm -r folder        # 删文件夹 (递归)
rm -rf folder       # 危险! 强制无确认 — 慎用
cp file dest        # 复制
cp -r folder dest   # 复制文件夹
mv src dest         # 移动/改名

# 看文件
cat file            # 全部打印
head file           # 前 10 行
tail file           # 后 10 行
less file           # 分页浏览,q 退出
grep "词" file      # 搜关键词

# 通用
which 命令          # 这条命令在哪
man 命令            # 看命令手册,q 退出
echo "文字"         # 打印
clear               # 清屏 (= Ctrl+L)
history             # 命令历史
open 文件           # (Mac) 用默认 app 打开
open -a "App名" 文件 # (Mac) 指定 app 打开
```

**键盘快捷键** (高频):
- **Tab**: 自动补全 — 必须养成的肌肉记忆
- **↑/↓**: 翻历史命令
- **Ctrl+C**: 中断当前程序
- **Ctrl+D**: 退出 shell
- **Ctrl+L**: 清屏

### 4.2 Git 常用

```bash
# 基础流程
git init                    # 把当前文件夹变成 git 仓库
git status                  # 看现在什么改了
git add 文件                # 文件进暂存区
git add .                   # 所有改动进暂存区
git commit -m "说明"        # 集中发货
git log --oneline           # 看历史

# 远端
git push                    # 推到 GitHub
git pull                    # 从 GitHub 拉
git clone URL               # 克隆远端仓库

# 看变化
git diff                    # 看具体改了哪几行

# 恢复/回退
git restore 文件            # 恢复文件到最近 commit 的样子
git checkout <hash>         # 切到某个旧 commit (看)
git checkout main           # 回到最新
git revert <hash>           # 正式撤销某次 commit
```

### 4.3 conda 常用

```bash
# 环境
conda create -n 环境名 python=3.11 -y    # 创建环境
conda activate 环境名                    # 激活
conda deactivate                         # 退出当前环境
conda env list                           # 列出所有环境
conda env remove -n 环境名               # 删除环境

# 包
conda install 包名                       # 装包 (用 conda-forge)
conda install -y 包名                    # 自动 yes
conda list                               # 列出当前环境装的包
conda update 包名                        # 更新

# 信息
conda --version                          # 版本
conda info                               # 当前配置
```

### 4.4 Markdown 5 分钟速学

```markdown
# 一级标题
## 二级标题
### 三级标题

正文段落直接写,空一行表示新段落。

**加粗** *斜体* `行内代码` ~~删除线~~

- 无序列表项
- 无序列表项

1. 有序列表项
2. 有序列表项

> 引用块

[链接文字](https://example.com)
![图片描述](path/to/image.png)

| 表头 1 | 表头 2 |
|---|---|
| 单元格 | 单元格 |
```

代码块 (用三个反引号包起来,后面写语言名):

    ```python
    print("hello")
    ```

---

## 5. Unix Flag 家族 (短横线常见用法)

| Flag | 全名 | 作用 |
|---|---|---|
| `-h` | `--help` | 显示帮助 |
| `-V` / `-v` | `--version` | 显示版本 (大小写视工具而定) |
| `-y` | `--yes` | 自动同意所有 y/n |
| `-n` | `--name` | 起名字 (如 `conda create -n`) |
| `-c` | `--command` | 后接代码字符串 (如 `python -c`) |
| `-o` | `--output` | 输出到指定文件名 |
| `-O` | (大写) | curl 用原文件名保存 |
| `-L` | `--location` | curl 跟随重定向 |
| `-r` / `-R` | `--recursive` | 递归 (文件夹) |
| `-f` | `--force` | 强制不询问 |
| `-i` | `--interactive` | 询问式 |
| `-l` | `--long` | 详细列表 |
| `-a` | `--all` | 包含隐藏 |
| `-p` | `--parents` | 顺便建上层 |
| `-q` | `--quiet` | 安静模式 |
| `-m` | `--message` | 后接说明文字 (如 `git commit -m`) |

**通用规则**:
- 短 flag 可连写: `ls -la` = `ls -l -a`
- 长 flag 可用等号: `--name=edsml-prep`
- 大小写区分: `-o` ≠ `-O`
- 同字母不同工具含义不同,看不懂 `命令 --help`

---

## 6. Windows ↔ Mac 命令对照

| Windows cmd | Mac/Linux |
|---|---|
| `type file` | `cat file` |
| `dir` | `ls` |
| `cls` | `clear` |
| `copy` | `cp` |
| `move` | `mv` |
| `del` | `rm` |
| `md` | `mkdir` |
| 双击 Anaconda Prompt | 任何终端窗口 (conda 自动在 PATH) |
| `C:\Users\gg` | `/Users/gg` 或 `~` |
| `\` 路径分隔 | `/` 路径分隔 |
| 文件属性藏 | 文件名 `.` 开头藏 |

---

## 7. 易踩的坑 / 救命知识

1. **`rm -rf` 是新手最大的坑**。误跑 `rm -rf ~` 或 `rm -rf /` 能毁掉系统。任何带 `-rf` 的命令按回车前多看一眼
2. **`git reset --hard` 不可恢复**。三个月内只用 `git revert`
3. **如果 `git commit` 不小心打开 vim 卡死**: 按 ESC,输 `:q!` 回车 (不保存退出);或 `:wq` 保存退出
4. **`zsh: no matches found`**: 通配符 `*` 没匹配到东西。检查拼写或路径
5. **pip install 装了但 python import 不到**: 多半是 pip 和 python 不在同一个环境。用 `which pip` 和 `which python` 检查
6. **不要混用系统 Python 和 conda Python**: 系统 Python 留给 Apple,EDSML 工作只用 conda 环境

---

## 8. 待解决 / 明天 (Day 02) 入口

### 还没做的 Week 0 任务

- [ ] 创建 `~/edsml-prep-lab` 文件夹
- [ ] `git init` 这个文件夹
- [ ] 写 **OpenHeat Project Card** (问题定义/输入输出/我做了什么/AI 做了什么/我能解释什么/不能解释什么)
- [ ] 写 **Adaptive GVI/VVI Project Card** (同上结构)
- [ ] 写 **What_I_need_to_understand.md** (列出看 AI 代码看不懂的地方)
- [ ] 建立 GitHub 远端连接 (SSH key 或 PAT)
- [ ] 在 VS Code 装 `code` 命令到 PATH (`Cmd+Shift+P` → "Shell Command: Install 'code'...")

### 建议明天的开局

1. 先建文件夹结构 (15 分钟):
   ```bash
   mkdir -p ~/edsml-prep-lab/{project-cards,weekly-notes,no-ai-rewrites,cheatsheets,ai-use-log}
   cd ~/edsml-prep-lab
   git init
   ```
2. 把今天这份 `day-01-log.md` 放进 `weekly-notes/`
3. 第一个 `git commit -m "day 01: setup + first log"`
4. 然后写 OpenHeat Project Card

### 长期 (本周内) 目标

- 完成 Week 0 三份文档 (两份 Project Card + 一份 understand list)
- GitHub 远端连接好,有第一次 `git push`

---

## 9. 给未来 Claude 的上下文 (AI Onboarding)

如果在新对话窗口让 Claude 接续我的进度,把以下内容贴给它,它就能跟上:

### 9.1 我是谁

- 普利茅斯大学 Y3 环境科学本科生,即将入读 Imperial EDSML (MSc Environmental Data Science and Machine Learning),2026 年 9 月开学
- 研究兴趣: 城市气候 / 暴露于水热 nexus
- 已有技能: R 中等 (受 AI 影响有依赖),QGIS 熟练,空间分析 (DBSCAN/GWR/NDVI/GVI)
- 弱项: Python 几乎从零,C++ 完全无,数学 (2019 大一线代/高数后没碰过)
- 性格: INTP — 需要先理解模型再执行,执行力是已知挑战

### 9.2 我现在的位置

- 在执行 **v2 Taskbook (AI-assisted prototype 到独立可解释能力)**
- 已经诚实承认: OpenHeat-ToaPayoh 和 Adaptive GVI/VVI 是 AI-assisted prototypes,不是我独立写出来的
- 接下来 4 个月 (2026-05-13 ~ 09-27) 的目标: 把这两个项目变成"我自己能解释、能复现、能 defend 的项目"
- v2 计划详情见项目根目录的 `YihengPan_EDSML_Taskbook_v2_AI_Assisted_2026.docx`
- Adaptive GVI/VVI 项目当前状态: v0.7,详见 `Adaptive_GVI_VVI_Project_Handoff_v0_7_CN.md`

### 9.3 v2 Taskbook 的几条原则

1. **不再加新功能**,先冻结一个可运行版本,然后拆解、重写、解释
2. **每周只设一个主主题**,避免每天切换不同任务
3. **每周必须做一次 no-AI reconstruction**: 从 AI 项目里抽一个小模块,不看原代码重写简化版
4. **对外表达必须诚实**: AI-assisted implementation,我贡献的是 problem framing, testing, validation, research interpretation
5. **目标不是提前学完整个 EDSML**,而是开学前拥有可运行、可解释、可复现的基础工具箱

### 9.4 v2 时间表 (主要里程碑)

- Week 0 (05/13-05/17): 项目冻结与入口重建 ← **我现在在这里**
- Week 1-2 (05/18-05/31): Python/conda/Git/terminal
- Week 3-4 (06/01-06/14): NumPy/Pandas
- Week 5-6 (06/15-06/28): 线性代数与最小二乘
- Week 7-8 (06/29-07/12): 优化与反演
- Week 9-10 (07/13-07/26): ML workflow
- Week 11-12 (07/27-08/09): Geospatial Python
- Week 13 (08/10-08/16): Computer Vision / GVI
- Week 14 (08/17-08/23): PyTorch / SegFormer
- Week 15 (08/24-08/30): FastAPI / 工具工程化
- Week 16 (08/31-09/06): C++ 预接触
- Week 17 (09/07-09/13): Big Data / SQL / 数据格式
- Week 18-19 (09/14-09/27): Imperial pre-induction + Mock coursework

### 9.5 我的指导原则给 Claude

- **先给模型,后给操作**: 直接给步骤我不行,要先理解 why
- **每次只面对下一个 10-30 分钟能闭环的事**: 一次塞太多我会过载放弃
- **诚实评估状态**: 状态比进度重要,该停就停。降载规则是 v2 设计的一部分
- **避免对 AI 的依赖加深**: 鼓励我 no-AI reconstruction,告诉我什么时候该自己硬试
- **承认 AI-assisted 工作**: 不要让我把 AI 写的代码说成自己写的,这对面试和老师对话是危险信号
- **代码要解释每个细节**: 我现在还不能跳过任何符号,所有 `()` `[]` `-x` `~` `.` 都要解释
- **不要假装我会**: 我是真的零基础,不要从"你应该已经知道..."开始

### 9.6 当前进度快照

✅ Miniforge3 装好,conda 26.3.2
✅ edsml-prep 环境建好 (Python 3.11)
✅ numpy / pandas / matplotlib / jupyter / ipykernel 已装
✅ 跑通第一段 Python (`np.array([1,2,3]) * 2`)
✅ Shell / Python / conda / git / 文件格式基础概念已过一遍

⏳ edsml-prep-lab 文件夹未创建
⏳ Project Cards 未写
⏳ GitHub 远端未连接
⏳ 真正的 .py 脚本文件未写过 (只用过 `python -c`)

---

## 10. 心理状态记录

(给未来的我看)

今天扛过了一个很密集的学习日。从早上"动摇要不要去 IC"的状态,走到晚上能解释 PATH、解释 conda channel、解释 git revert 的状态。**这是 INTP 在状态线上的样子**。

要记住的:
- 不需要逼自己每天 4 小时。今天 1.5-2 小时的有效学习已经超额完成 Day 1 的最低要求
- 焦虑数学/Python/C++ 是正常的,但时间表给了余地: 数学 Week 5 才开始,C++ Week 16 才碰
- 执行力的解法不是逼自己,是知道什么时候该停

**今天结束。明天继续。**

---

*文档生成: 2026-05-13 by Claude*
*更新: 每天结束时手动加 §N+1 "Day N 更新"*
