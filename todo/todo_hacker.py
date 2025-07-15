import os
import time

FILE_NAME = "data.txt"
not_done = []
done = []

def slow_print(text, delay=0.02):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

def save():
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for task in not_done:
            file.write(f"❌ {task}\n")
        for task in done:
            file.write(f"✅ {task}\n")

# 🌱 بارگذاری داده‌ها
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("✅ "):
                done.append(line[2:].strip())
            elif line.startswith("❌ "):
                not_done.append(line[2:].strip())

# 🧪 وایب هکری موقع شروع
os.system("color 0A")  # مشکی-سبز
slow_print(".: ACCESSING TODO SYSTEM :.")
slow_print(">> INITIATING TERMINAL MODE ...")
time.sleep(1)

slow_print("\n1. add task → add title")
slow_print("2. mark done → tick title")
slow_print("3. unmark done → untick title")
slow_print("4. remove task → remove title")
slow_print("5. exit → exit\n")

while True:
    slow_print("========== Not Done ==========", 0.005)
    for task in not_done:
        slow_print(f"❌ {task}", 0.001)
    slow_print("=========== Done =============", 0.005)
    for task in done:
        slow_print(f"✅ {task}", 0.001)
    
    command = input(">> ").strip()

    if command == "exit":
        save()
        slow_print("Saving progress...")
        time.sleep(0.5)
        slow_print("Session terminated. ☠")
        break

    elif command.startswith("add "):
        title = command[4:]
        if title not in not_done and title not in done:
            not_done.append(title)
        else:
            slow_print("⚠️ Already exists or invalid.")

    elif command.startswith("tick "):
        title = command[5:]
        if title in not_done:
            not_done.remove(title)
            done.append(title)
        else:
            slow_print("⚠️ Task not found in not_done.")

    elif command.startswith("untick "):
        title = command[7:]
        if title in done:
            done.remove(title)
            not_done.append(title)
        else:
            slow_print("⚠️ Task not found in done.")

    elif command.startswith("remove "):
        title = command[7:]
        if title in not_done:
            not_done.remove(title)
        elif title in done:
            done.remove(title)
        else:
            slow_print("⚠️ Task not found.")

    else:
        slow_print("⚠️ Invalid command.")

    print()
