
import os
from game_optimizer import apply_game_optimizations

def run_test():
    test_ini_path = "test_configs/sample_game.ini"
    test_cfg_path = "test_configs/sample_game.cfg"

    print("Applying optimizations to sample_game.ini...")
    apply_game_optimizations("sample_game", test_ini_path)

    print("\nApplying optimizations to sample_game.cfg...")
    apply_game_optimizations("sample_game", test_cfg_path)

if __name__ == "__main__":
    run_test()
