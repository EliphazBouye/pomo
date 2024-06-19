import time
import os


class Pomo:
    def __init__(self):
        self.minutes = 0
        self.secondes = 10
        self.running = True
        self.history = []

        # Start a session during initialization
        self._session()

    def _session(self):
        while self.running:
            if (self._get_secondes == 0):
                self.__decrement_minutes()
                if (self._get_minutes == 0):
                    self.__decrement_secondes()

            if (self._get_secondes != 0):
                self.__decrement_secondes()

    def __decrement_minutes(self, minutes_number_to_dec = 1)-> int:
        minutes_updated = self.minutes - minutes_number_to_dec 
        self.minutes = minutes_updated

    def __decrement_secondes(self, secondes_number_to_dec = 1)-> int:
        if (self.secondes == 0):
            self.__secondes_new_cycle()
        secondes_updated = self.secondes - secondes_number_to_dec
        self.secondes = secondes_updated
        self.display_time()

        if (self.minutes == 0 and self.secondes == 0):
            self._clear_screen()
            print("\x1b[6;30;42m🚨 It's done congratulations! :) now do a short break!\x1b[0m")
            time.sleep(3)
            self._short_break_session()
            #self.running = False

    def __secondes_new_cycle(self)-> int:
        self.secondes = 60

    def _clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_time(self):
        time.sleep(1)
        self._clear_screen()
        print(f"🍅 {self.minutes:02d}:{self.secondes:02d}")

    def _restart_session(self):
        pass

    def _set_minutes(self, minutes: int):
        self.minutes = minutes

    def _set_secondes(self, secondes: int):
        self.secondes = secondes

    def _get_minutes(self)-> int:
        return self.minutes

    def _get_secondes(self)-> int:
        return self.secondes

    # TODO: implement save sessions
    def save_sessions(self):
        pass

    def _short_break_session(self):
        self._set_minutes(0)
        self._set_secondes(4)
        self._session()

    def set_long_break(self):
        pass

def main():
    Pomo()

if __name__ == '__main__':
    main()

