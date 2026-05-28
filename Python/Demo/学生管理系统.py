students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 58},
    {"name": "王五", "score": 92},]

def show_all():
    print("\n====== 当前学生成绩表 ======")
    if not students:
        print("（暂无学生数据）")
        return
    for idx, s in enumerate(students, 1):
        print(f"序号: {idx} | 姓名: {s['name']:<4} | 成绩: {s['score']}分")


def add_student():
    print("\n====== 添加学生成绩 ======")
    name = input("请输入学生姓名: ").strip()
    if name == "":
        print("❌ 姓名不能为空！")
        return
    score_str = input("请输入学生成绩: ")
    if not score_str.isdigit():
        print("❌ 成绩必须是纯数字！")
        return
    score = int(score_str)
    new_student = {"name": name, "score": score}
    students.append(new_student)
    print(f"✅ 成功添加：{name} ({score}分)")


def delete_student():
    print("\n====== ❌删除学生成绩 ======")
    name = input("请输入要删除的学生姓名: ").strip()
    for s in students:
        if s["name"] == name:
            students.remove(s)
            print(f"✅ 成功删除学生: {name}")
            return
    print("⚠️ 未找到该名字的学生！")
def update_student():
    print("\n======  修改学生成绩 ======")
    name = input("请输入要修改成绩的学生姓名: ").strip()
    for s in students:
        if s["name"] == name:
            new_score_str = input(f"找到学生 {name}，当前成绩为 {s['score']}。请输入新成绩: ")
            if not new_score_str.isdigit():
                print("❌ 成绩必须是纯数字！")
                return
            s["score"] = int(new_score_str)
            print(f"✅ 成绩修改成功！{name} 的新成绩为 {s['score']}分")
            return

    print("⚠️ 未找到该名字的学生！")
def show_report():
    print("\n====== 📊 班级成绩分析报告 ======")
    if not students:
        print("📁 暂无数据，无法统计。")
        return
    scores = [s["score"] for s in students]
    total_students = len(students)
    avg_score = sum(scores) / total_students
    max_score = max(scores)
    min_score = min(scores)
    passing_count = sum(1 for s in students if s["score"] >= 60)
    passing_rate = (passing_count / total_students) * 100
    print(f"📈 班级总人数: {total_students} 人")
    print(f"📘 班级平均分: {avg_score:.1f} 分")
    print(f"🔥 班级最高分: {max_score} 分")
    print(f"❄️ 班级最低分: {min_score} 分")
    print(f"🎓 考试及格率: {passing_rate:.1f}%")
def show_leaderboard():
    print("\n======  学生成绩排行榜 ======")
    if not students:
        print("（暂无学生数据）")
        return
    sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)
    
    for idx, s in enumerate(sorted_students, 1):
        print(f"姓名: {s['name']:<4} | 成绩: {s['score']}分")

def export_to_file():
    print("\n====== 导出成绩数据 ======")
    if not students:
        print("❌ 没有数据可以导出！")
        return
    
    try:
        with open("成绩单.txt", "w", encoding="utf-8") as f:
            f.write("=== 学生成绩备份 ===\n")
            for s in students:
                f.write(f"姓名: {s['name']}, 成绩: {s['score']}分\n")
        print("✅ 成功导出！请查看当前文件夹下的 成绩单.txt文件")
    except Exception as e:
        print(f"❌ 导出失败，原因: {e}")
def main():
    while True:
        print("\n==============================")
        print("   🎓 学生成绩管理系统    ")
        print("==============================")
        print(" 1. 查看所有成绩 ")
        print(" 2. 添加学生成绩 ")
        print(" 3. 删除学生成绩 ")
        print(" 4. 修改学生成绩 ")
        print(" 5. 查看成绩分析报告 ")
        print(" 6. 查看成绩排行榜 ")
        print(" 7. 导出成绩到本地 ")
        print(" 8. 退出系统")
        print("==============================")

        choice = input("请选择操作编号 (1-8): ").strip()

        if choice == "1":
            show_all()
        elif choice == "2":
            add_student()
            show_all() 
        elif choice == "3":
            delete_student()
            show_all()
        elif choice == "4":
            update_student()
            show_all()
        elif choice == "5":
            show_report()
        elif choice == "6":
            show_leaderboard()
        elif choice == "7":
            export_to_file()
        elif choice == "8":
            print("\n感谢使用，系统已退出！")
            break 
        else:
            print("❌ 输入错误，请输入 1 到 8 之间的数字！")


if __name__ == "__main__":
    main()
