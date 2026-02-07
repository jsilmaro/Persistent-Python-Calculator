| Method            | Execution Order                                       | GWA Output | Execution Time (seconds) |
|-------------------|-------------------------------------------------------|------------|--------------------------|
| Multithreading    | Non-deterministic (thread execution order varies)     | 1.94       | 0.001767                 |
| Multiprocessing   | Non-deterministic (process execution order varies)    | 1.94       | 0.001842                 |


1. Which approach demonstrates true parallelism in Python? Explain.
   - Multiprocessing demonstrates true parallelism in Python because it creates separate processes that can run at the same time using multiple CPU cores. Each process works independently, which allows tasks to be completed faster, especially for heavy computations.

2. Compare execution times between multithreading and multiprocessing.
   - For 8 subjects, both approaches have very similar execution times. Multithreading is slightly faster due to lower overhead, while multiprocessing has additional cost from creating separate processes.

3. Can Python handle true parallelism using threads? Why or why not?
   - Python threads cannot achieve true parallelism for CPU-bound tasks because of the Global Interpreter Lock (GIL), which allows only one thread to execute Python bytecode at a time.

4. What happens if you input a large number of grades (e.g., 1000)? Which
method is faster and why?
   - With a large number of grades, multiprocessing becomes faster because it can distribute computation across multiple CPU cores. Multithreading does not scale as well due to the GIL.

5. Which method is better for CPU-bound tasks and which for I/O-bound
tasks?
   - Multiprocessing is better for CPU-bound tasks because it allows multiple cores to process heavy calculations at the same time. Multithreading is better for I/O-bound tasks such as reading files, network communication, or user input because threads can run while waiting for data.

6. How did your group apply creative coding or algorithmic solutions in this
lab?
   - The group applied input validation, modularized the code for threading and multiprocessing, measured execution time, and structured the program to clearly compare concurrent and parallel execution.


