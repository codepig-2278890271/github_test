"""
猜数字游戏 - 增强版
一个有趣的数字猜测游戏，支持多个难度级别
"""

import random


def get_difficulty_level():
    """获取用户选择的难度等级"""
    print("\n" + "=" * 40)
    print("欢迎来到猜数字游戏！")
    print("=" * 40)
    print("\n选择难度等级：")
    print("1 - 简单 (1-10)")
    print("2 - 中等 (1-50)")
    print("3 - 困难 (1-100)")
    
    while True:
        try:
            choice = input("\n请输入难度等级 (1-3)：").strip()
            if choice in ['1', '2', '3']:
                levels = {
                    '1': (1, 10, "简单"),
                    '2': (1, 50, "中等"),
                    '3': (1, 100, "困难")
                }
                return levels[choice]
            else:
                print("❌ 请输入 1、2 或 3！")
        except KeyboardInterrupt:
            print("\n再见！")
            exit()


def play_game(min_num, max_num, difficulty_name):
    """主游戏循环"""
    number = random.randint(min_num, max_num)
    attempts = 0
    guesses = []
    
    print(f"\n🎮 已选择【{difficulty_name}】难度")
    print(f"我想了一个 {min_num} 到 {max_num} 之间的数字，来猜猜看！\n")
    
    while True:
        try:
            guess_input = input("请输入你的猜测：").strip()
            
            # 检查输入是否为有效的整数
            if not guess_input:
                print("⚠️  请输入一个数字！")
                continue
            
            guess = int(guess_input)
            
            # 检查输入范围
            if guess < min_num or guess > max_num:
                print(f"⚠️  请输入 {min_num} 到 {max_num} 之间的数字！")
                continue
            
            attempts += 1
            guesses.append(guess)
            
            # 比较和反馈
            if guess < number:
                diff = number - guess
                print(f"📍 太小啦！还差 {diff} 点")
            elif guess > number:
                diff = guess - number
                print(f"📍 太大啦！超了 {diff} 点")
            else:
                print_win_message(attempts, difficulty_name, guesses)
                return attempts
        
        except ValueError:
            print("❌ 请输入一个有效的整数！")
        except KeyboardInterrupt:
            print("\n\n游戏已退出，再见！")
            exit()


def print_win_message(attempts, difficulty_name, guesses):
    """打印获胜消息和统计信息"""
    print("\n" + "🎉" * 20)
    print("恭喜你，猜对了！")
    print("🎉" * 20)
    
    # 评价表现
    if difficulty_name == "简单":
        threshold = 3
    elif difficulty_name == "中等":
        threshold = 5
    else:
        threshold = 8
    
    if attempts <= threshold:
        rating = "⭐⭐⭐ 厉害！你太聪明了！"
    elif attempts <= threshold * 1.5:
        rating = "⭐⭐ 不错，再来一盘？"
    else:
        rating = "⭐ 加油，多练习就会更快！"
    
    print(f"\n📊 游戏统计：")
    print(f"  难度等级：{difficulty_name}")
    print(f"  尝试次数：{attempts}")
    print(f"  表现评价：{rating}")
    print(f"  你的猜测序列：{guesses}")
    print()


def main():
    """主函数"""
    play_again = True
    total_games = 0
    total_attempts = 0
    
    while play_again:
        min_num, max_num, difficulty_name = get_difficulty_level()
        attempts = play_game(min_num, max_num, difficulty_name)
        
        total_games += 1
        total_attempts += attempts
        
        # 询问是否继续游戏
        while True:
            choice = input("要再来一盘吗？(y/n)：").strip().lower()
            if choice in ['y', 'yes', '是']:
                break
            elif choice in ['n', 'no', '否']:
                play_again = False
                break
            else:
                print("请输入 'y' 或 'n'！")
    
    # 游戏结束统计
    print("\n" + "=" * 40)
    print("感谢游玩！最终统计：")
    print("=" * 40)
    print(f"总游戏局数：{total_games}")
    print(f"总尝试次数：{total_attempts}")
    if total_games > 0:
        avg_attempts = total_attempts / total_games
        print(f"平均每局尝试次数：{avg_attempts:.1f}")
    print("=" * 40)
    print("下次再见！👋\n")


if __name__ == "__main__":
    main()