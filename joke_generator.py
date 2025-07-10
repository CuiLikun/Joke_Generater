import random
from datetime import datetime

class JokeGenerator:
    def __init__(self):
        self.joke_count = 0
        self.total_word_count = 0
        self.saved_jokes = []

    def generate_joke(self, style="1234", word_limit=50):
        styles = {
            "1234": [
                "为什么程序员喜欢用暗模式？因为亮模式会让他们的代码看起来像是被太阳晒过。",
                "程序员的梦想是什么？代码一次通过，永不改动！",
                "为什么程序员总是很冷？因为他们总是待在低温的服务器房间里。",
                "程序员的座右铭是什么？'没有 bug 的代码是不存在的！'"
            ],
            "custom": ["这是一个自定义笑话示例。"],
            "funny": [
                "为什么计算机喜欢吃饼干？因为它们有很多字节！",
                "程序员的宠物是什么？Bug。",
                "为什么程序员总是很累？因为他们一直在跑循环！"
            ],
        "tech": [
            "为什么程序员喜欢用 Linux？因为他们喜欢自由。",
            "为什么云计算很受欢迎？因为它让人感觉轻松自在。",
            "为什么硬盘总是很忙？因为它们一直在转圈圈。"
        ],
        "office": [
            "为什么老板喜欢 Excel？因为它能让他们看起来很专业。",
            "为什么会议总是很长？因为没人愿意结束。",
            "为什么打印机总是坏？因为它们讨厌工作。"
            "你好"
        ],
        "random": [
            "为什么鸡过马路？为了去另一边。",
            "为什么鱼不喜欢说话？因为它们总是沉默。",
            "为什么树喜欢站着？因为它们不喜欢坐下。"
        ]
        }

        # 如果用户输入 custom，则进一步选择具体风格
        if style == "custom":
            sub_style = input("请输入自定义笑话风格 (例如: funny, tech, office, random): ")
            selected_style = styles.get(sub_style, ["该自定义风格不存在，请检查输入！"])
        else:
            selected_style = styles.get(style, styles["custom"])

        joke = random.choice(selected_style)
        if len(joke) > word_limit:
            joke = joke[:word_limit] + "..."
        self.joke_count += 1
        self.total_word_count += len(joke)
        return joke

    def save_joke(self, joke):
        self.saved_jokes.append(joke)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("saved_jokes.txt", "a", encoding="utf-8") as file:
            file.write(f"{timestamp} - {joke}\n")

    def get_statistics(self):
        average_word_count = self.total_word_count / self.joke_count if self.joke_count > 0 else 0
        return {
            "joke_count": self.joke_count,
            "total_word_count": self.total_word_count,
            "average_word_count": average_word_count
        }

    def display_saved_jokes(self):
        return self.saved_jokes

def show_saved_jokes_from_file():
    try:
        with open("saved_jokes.txt", "r", encoding="utf-8") as file:
            jokes = file.readlines()
            if not jokes:
                print("暂无已保存的笑话。")
            else:
                print("历史保存的笑话：")
                for joke in jokes:
                    print(joke.strip())
    except FileNotFoundError:
        print("还没有保存过笑话。")

# 主程序
if __name__ == "__main__":
    generator = JokeGenerator()
    while True:
        print("\n1. 生成笑话")
        print("2. 查看已保存的笑话")
        print("3. 退出")
        choice = input("请选择操作（1/2/3）：")
        if choice == "1":
            print("请选择笑话风格：1234 或者输入 custom 自定义风格")
            style = input("风格: ")
            try:
                word_limit = int(input("请输入笑话字数限制: "))
            except ValueError:
                print("字数限制必须是数字，请重新输入!")
                continue

            joke = generator.generate_joke(style, word_limit)
            print(f"生成的笑话: {joke}")

            save_option = input("是否收藏并保存笑话? (y/n): ")
            if save_option.lower() == "y":
                generator.save_joke(joke)
                print("笑话已保存!")

            stats = generator.get_statistics()
            print(f"目前已创作笑话数量: {stats['joke_count']}, 总字数: {stats['total_word_count']}, 平均字数: {stats['average_word_count']:.2f}")
        elif choice == "2":
            show_saved_jokes_from_file()
        elif choice == "3":
            break
        else:
            print("无效选择，请重新输入。")

    print("已保存的笑话:")
    for saved_joke in generator.display_saved_jokes():
        print(saved_joke)