import threading
import time
import os

def gwa_thread(grade, i):
    print(f"[Thread {threading.current_thread().name}] Subject {i}: grade = {grade}")


while True:
    n = int(input("How many subjects (max 10)? "))
    if 1 <= n <= 10:
        break
    print("Please enter a number between 1 and 10 only.")

grades_list = []

for i in range(1, n + 1):
    while True:
        try:
            grade = float(input(f"Enter grade for subject {i}: "))
            if 0 <= grade <= 100:
                grades_list.append(grade)
                break
            else:
                print("Invalid grade. Please enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

os.system("clear")

start_time = time.perf_counter()

threads = []
for i, grade in enumerate(grades_list, start=1):
    t = threading.Thread(
        target=gwa_thread,
        args=(grade, i),
        name=f"T{i}"
    )
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = time.perf_counter()

gwa = sum(grades_list) / len(grades_list)
print(f"\nGWA: {gwa:.2f}")
print(f"Execution Time (Multithreading): {end_time - start_time:.6f} seconds")