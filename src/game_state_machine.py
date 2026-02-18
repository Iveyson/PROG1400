from enum import Enum, auto

class GameState(Enum):
    LEVEL_INIT = auto()
    PLAYING = auto()
    PAUSED = auto()
    POWER_MODE = auto()
    LIFE_LOST = auto()
    LEVEL_COMPLETE = auto()
    GAME_OVER = auto()

class GameStateMachine:
    def __init__(self):
        self.state = GameState.LEVEL_INIT
        self.lives=1

    def set_state(self, new_state):
        print(f"[STATE] {self.state.name}-> {new_state.name}")
        self.state = new_state

    def pause_pressed(self):
        if self.state == GameState.PLAYING:
            self.set_state(GameState.PAUSED)
        elif self.state == GameState.PAUSED:
            self.set_state(GameState.PLAYING)

    def collision_normal(self):
        if self.state == GameState.PLAYING:
            self.lives -= 1
            self.set_state(GameState.LIFE_LOST)
    
    def update(self):
        if self.state == GameState.LEVEL_INIT:
            print("Initializing level...")
            self.init_complete()

        elif self.state == GameState.PLAYING:
            print("Playing...")

        elif self.state == GameState.PAUSED:
            print("Paused...")

        elif self.state == GameState.LIFE_LOST:
            print("Life lost...")
            self.set_state(GameState.LEVEL_INIT)

        elif self.state == GameState.GAME_OVER:
            print("Game over.")

if __name__ == "__main__":
    gsm = GameStateMachine()

    gsm.update()
    gsm.pause_pressed()
    gsm.update()
    gsm.collision_normal()
    gsm.update()