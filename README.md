# DeepSeek 聊天客户端

一个用 Python 写的命令行聊天程序，调用 DeepSeek API 实现连续对话。

## 效果

```
DeepSeek 聊天程序已启动，输入 exit 退出。

你：你好
DeepSeek：你好！有什么我可以帮你的吗？

你：介绍一下 REST API
DeepSeek：REST API 是一种基于 HTTP 协议、用 URL 定位资源并用标准方法操作资源的应用程序接口设计风格。

你：exit
再见！
```

## 功能

- 命令行连续对话，输入 `exit` 退出
- 基于 DeepSeek API，兼容 OpenAI SDK
- API Key 通过 `.env` 文件管理，不硬编码在代码中

## 快速开始

### 1. 安装 Miniconda

下载地址：https://docs.conda.io/en/latest/miniconda.html

安装时勾选 **Add Miniconda3 to my PATH environment variable**。

### 2. 创建环境

打开 Anaconda Prompt，执行：

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

看到 `你：` 提示符就可以开始聊天了。

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
        └── main.py         # 程序入口，命令行交互循环
```

## 常见问题

**`'conda' 不是内部或外部命令`**

请使用 Anaconda Prompt，不要用普通 cmd。

**`ModuleNotFoundError: No module named 'src'`**

必须在项目根目录（包含 `src` 文件夹的那一层）运行。

**`401 Unauthorized`**

API Key 错误。检查 `.env` 文件里的密钥是否完整、是否过期。

**`余额不足`**

前往 https://platform.deepseek.com 充值。

**`git push` 连不上 GitHub**

如果本机开了代理，为 Git 配置代理：

```
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890
```

端口号 `7890` 换成你自己代理软件的端口。

## 许可

MIT