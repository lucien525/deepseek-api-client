# DeepSeek 聊天客户端

一个用 Python 写的命令行聊天程序，调用 DeepSeek API 实现连续对话，支持多种对话模式。

## 效果

```
请选择对话模式：
  1. 写代码的高手
  2. 解决大学作业题的高手
  3. 强大的老师教学
  直接回车或输入其他任意键 → 通用模式
输入编号：2

已进入【解决大学作业题的高手】，输入 exit 退出。

你：求极限 lim(x→0) (sin x)/x
DeepSeek：解题步骤：
1. 这是基本极限公式，可直接使用。
2. 核心知识点：等价无穷小 sin x ~ x (x→0)。
3. 因此 lim(x→0) (sin x)/x = 1。
4. 常见错误：不要用洛必达法则绕远路，直接记结论。

你：exit
再见！
```

## 功能

- 启动时选择对话模式：
  - `1` 写代码的高手
  - `2` 解决大学作业题的高手
  - `3` 强大的老师教学
  - 直接回车或输入任意其他键 → 通用模式
- 命令行连续对话，输入 `exit` 退出
- 基于 DeepSeek API，兼容 OpenAI SDK
- API Key 通过 `.env` 文件管理，不硬编码在代码中

## 快速开始

### 1. 安装 Miniconda

下载地址：https://docs.conda.io/en/latest/miniconda.html

安装时勾选 **Add Miniconda3 to my PATH environment variable**。

安装完成后，Windows 用户从开始菜单打开 **Anaconda Prompt**，Mac 用户打开**终端**。后续所有命令都在这里执行。

### 2. 创建环境

```
conda create -n dp_api python=3.11 -y
conda activate dp_api
pip install openai python-dotenv
```

### 3. 下载本项目

```
git clone https://github.com/lucien525/deepseek-api-client.git
cd deepseek-api-client
```

### 4. 配置 API Key

访问 https://platform.deepseek.com，注册账号后进入 **API Keys** 页面，创建一个新密钥。

把项目里的 `.env.example` 复制一份，改名为 `.env`，用记事本打开，填入你的密钥：

```
DEEPSEEK_API_KEY=sk-你的真实密钥
```

### 5. 运行

```
python -m src.deepseek_client.main
```

看到模式选择菜单后，输入编号或直接回车，即可开始聊天。

## 项目结构

```
deepseek-api-client/
├── .env.example            # 配置模板，复制为 .env 后填写密钥
├── .gitignore              # Git 忽略规则
├── README.md               # 本文件
└── src/
    └── deepseek_client/
        ├── __init__.py
        ├── config.py       # 读取环境变量和配置
        ├── client.py       # 封装 DeepSeek API 调用
        └── main.py         # 程序入口，模式选择与命令行交互循环
```

## 搭建过程中踩过的坑

以下是实际搭建时遇到的问题和解决方法，按出现顺序整理。

### 坑 1：不知道用 Anaconda Prompt 还是普通 cmd

**现象**

在普通 cmd 里输入 `conda activate dp_api`，提示 `'conda' 不是内部或外部命令`。

**原因**

普通 cmd 没有加载 conda 的环境变量，找不到 `conda` 命令。

**解决**

始终使用 **Anaconda Prompt**，不要用普通 cmd。它打开时就已经配置好了 conda。

如果安装 Miniconda 时勾选了 “Add Miniconda3 to my PATH environment variable”，普通 cmd 也能用，但为了省事，统一用 Anaconda Prompt。

---

### 坑 2：`python -m src.deepseek_client.main` 看不懂

**现象**

完全不知道这条命令在干什么，为什么不能直接双击 `main.py`。

**解释**

拆开看：

```
python   -m   src.deepseek_client.main
  │      │            │
  │      │            └── 要运行的文件：main.py
  │      └── 以“模块”方式运行
  └── 调用 Python
```

- **模块** = 一个 `.py` 文件
- **包** = 一个装着 `.py` 文件的文件夹
- **点号 `.`** = 进入下一层文件夹

`src.deepseek_client.main` 对应 Windows 路径 `src\deepseek_client\main.py`，只是把反斜杠换成了点号，并去掉了 `.py`。

**为什么不能直接 `python src\deepseek_client\main.py`？**

因为 `main.py` 里写了 `from .client import chat`，这个 `.` 表示“当前包”。直接运行文件时，Python 不知道它在哪个包里，会报错：

```
ImportError: attempted relative import with no known parent package
```

用 `-m` 方式运行，Python 才知道包结构，相对导入才能正常工作。

**记住一件事**

必须在**项目根目录**（有 `.env` 和 `src` 的那一层）运行这条命令。

---

### 坑 3：`git push` 连不上 GitHub

**现象**

```
fatal: unable to access 'https://github.com/...': Failed to connect to github.com port 443 after 21141 ms: Could not connect to server
```

**原因**

网络连接不上 GitHub 的 443 端口，通常是代理没配置或网络环境限制。

**解决方法一：配置 Git 代理**

如果本机开了代理软件（VPN），需要让 Git 也走代理。常见端口是 `7890` 或 `7897`，在代理软件设置里可以查到。

```
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890
```

把 `7890` 换成你自己的端口号。设置完再 `git push`。

如果还是不行，或者根本没开代理，先清除代理设置：

```
git config --global --unset http.proxy
git config --global --unset https.proxy
```

**解决方法二：强制使用 HTTP/1.1**

有些网络对 HTTP/2 支持不好：

```
git config --global http.version HTTP/1.1
```

**解决方法三：改用 SSH**

如果 HTTPS 始终连不上，可以改用 SSH 方式：

1. 生成密钥：
   ```
   ssh-keygen -t ed25519 -C "你的GitHub邮箱"
   ```
   一路按回车。

2. 查看公钥：
   ```
   type %USERPROFILE%\.ssh\id_ed25519.pub
   ```
   复制输出的全部内容。

3. 添加到 GitHub：Settings → SSH and GPG keys → New SSH key，粘贴公钥。

4. 修改远程地址并推送：
   ```
   git remote set-url origin git@github.com:你的用户名/仓库名.git
   git push -u origin main
   ```

---

### 坑 4：担心 `.env` 里的密钥被传到 GitHub

**现象**

`git add .` 之后，不确定 `.env` 会不会被提交。

**解决**

在 `git add` **之前**，先确保 `.gitignore` 文件里写了：

```
.env
```

执行 `git add .` 后，立刻执行：

```
git status
```

看列表里有没有 `.env`：

- **没有** → 正常，继续 `git commit`
- **有** → 停下来，检查 `.gitignore` 文件名是不是写成了 `.gitignore.txt`

如果不小心把 `.env` 传上去了：

1. 立即去 https://platform.deepseek.com 删除旧密钥，重新生成一个
2. 去 GitHub 仓库删除 `.env` 文件
3. 本地补好 `.gitignore`，重新提交

---

### 坑 5：conda 环境每次都要手动激活

**现象**

每次重新打开 Anaconda Prompt，都要重新输入 `conda activate dp_api` 和 `cd /d D:\file\dp`，很麻烦。

**解决**

做一个 `.bat` 批处理文件，双击就能进入。

1. 先找到 Miniconda 安装路径，在 Anaconda Prompt 里执行：
   ```
   where conda
   ```
   输出的路径里，去掉 `\Scripts\conda.exe`，剩下的就是 Miniconda 根目录。比如：
   ```
   D:\app\miniconda\conda
   ```

2. 桌面新建一个文本文档，改名为 `进入dp.bat`（注意去掉 `.txt` 后缀）。

3. 右键编辑，写入：
   ```bat
   @echo off
   call "D:\app\miniconda\conda\Scripts\activate.bat" dp_api
   cd /d D:\file\dp
   cmd /k
   ```
   把路径换成你自己的。

4. 双击运行，就会自动激活环境并进入项目目录。

---

### 坑 6：README 写太长，别人看不懂

**现象**

把整个搭建过程写成一份超长文档，小白看完还是不知道从哪下手。

**解决**

README 只写三部分：

1. 这是什么（一句话 + 效果截图）
2. 怎么用（别人拿到后要执行的步骤）
3. 踩过的坑（遇到问题怎么解决）

不要把“自己搭建的全过程”写进去，那是开发记录，不是使用说明。别人只需要知道**怎么用**，不需要知道你当时怎么建的。

---

## 许可

MIT