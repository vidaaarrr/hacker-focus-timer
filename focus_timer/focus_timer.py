import time
import os
import random
from datetime import datetime
from collections import defaultdict

# 🎨 رنگ سبز هکری
os.system("color 0A")

# ⌨️ افکت تایپی
def slow_print(text, delay=0.02):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

# 🧠 تایمر تمرکز
def start_focus_timer(minutes=25):
    seconds = minutes * 60
    slow_print(f"\n>> FOCUS MODE ON: {minutes} minutes 🔒\n", 0.01)
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02}:{secs:02}"
        print(f"\r🕒 {timer}", end='', flush=True)
        time.sleep(1)
        seconds -= 1

    print("\n\n🔔 FOCUS COMPLETE! Great job 👏")
    save_session(minutes)
    show_motivation()
    show_progress_graph()

# 💾 ذخیره در فایل
def save_session(minutes):
    with open("focus_log.txt", "a", encoding="utf-8") as file:
        file.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] Focused {minutes} minutes\n")
    slow_print("✅ Logged to focus_log.txt")

# 💬 جمله انگیزشی تصادفی
def show_motivation():
    quotes = [
        "Stay focused. The grind is real. 🧠",
        "Discipline beats motivation. Every time.",
        "One session at a time. Keep going.",
        "Focus is your true superpower. ⚡",
        "Greatness is built in silence."
    ]
    quote = random.choice(quotes)
    slow_print(f"\n💬 Quote of the session:\n> {quote}", 0.02)

# 📈 گراف تمرکز روزانه
def show_progress_graph():
    if not os.path.exists("focus_log.txt"):
        return

    data = defaultdict(int)
    with open("focus_log.txt", "r", encoding="utf-8") as file:
        for line in file:
            if "Focused" in line:
                try:
                    date_part = line.split("]")[0].strip("[")
                    date = datetime.strptime(date_part, "%Y-%m-%d %H:%M").date()
                    minutes = int(line.split("Focused ")[1].split(" ")[0])
                    data[date] += minutes
                except:
                    continue

    if not data:
        return

    slow_print("\n📊 Today's Focus Summary:\n", 0.01)
    today = datetime.now().date()
    for date, minutes in sorted(data.items(), reverse=True):
        bar = "🟩" * (minutes // 5)
        tag = " ← today" if date == today else ""
        print(f"{date} | {minutes:3} min | {bar}{tag}")

# 🎯 اجرای اصلی
if __name__ == "__main__":
    slow_print("===== HACKER FOCUS TIMER v1.1 =====", 0.01)
    inp = input("⏱️ How many minutes? (default = 25): ").strip()

    try:
        mins = int(inp) if inp else 25
        start_focus_timer(mins)
    except:
        slow_print("⚠️ Invalid input. Try a number.")
