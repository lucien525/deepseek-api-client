import os
from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = "https://api.deepseek.com"
DEFAULT_MODEL = "deepseek-flash"

if not DEEPSEEK_API_KEY:
    raise RuntimeError(
        "未找到 DEEPSEEK_API_KEY。请检查项目根目录下的 .env 文件，"
        "确认其中设置了 DEEPSEEK_API_KEY=sk-..."
    )