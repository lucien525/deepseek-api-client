from .client import chat

if __name__ == "__main__":
    print("DeepSeek 聊天程序已启动，输入 exit 退出。\n")
    while True:
        user_input = input("你：")
        if user_input.strip().lower() in ("exit", "quit"):
            print("再见！")
            break
        if not user_input.strip():
            continue
        answer = chat(user_input)
        print(f"DeepSeek：{answer}\n")