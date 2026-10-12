| Comparison Item | Without Library (Pure Python) | With Library (Pandas) | Difference |
| :--- | :--- | :--- | :--- |
| **Line Count** (excluding blank lines and comments) | About 25 lines | About 5 lines | Pandas is much shorter and more concise |
| **Difficult Parts** | Had to manually implement loops, conditions, and exception handling (`try-except`) | Understanding how missing values (`NaN`) and error options (`errors="coerce"`) work | Pure Python code is longer and more complex |
| **Execution Result** | Korean 75.78, Math 82.83, English 82.0 | (When treating missing values as 0) Korean 75.78, Math 62.12, English 71.75 | Results can vary depending on how missing values are handled |