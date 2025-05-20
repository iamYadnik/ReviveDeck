
import os
from game_optimizer import apply_game_optimizations

def batch_optimize(profile_dir="game_profiles", config_dir="test_configs"):
    optimized = []
    skipped = []

    for filename in os.listdir(config_dir):
        if filename.endswith(".ini") or filename.endswith(".cfg"):
            game_name = filename.split(".")[0]  # base name without extension
            config_path = os.path.join(config_dir, filename)
            result = apply_game_optimizations(game_name, config_path, profile_dir)
            if result is None:
                skipped.append(filename)
            else:
                optimized.append(filename)

    print(f"✅ Optimized {len(optimized)} files.")
    if skipped:
        print(f"⚠️ Skipped {len(skipped)} files (no matching profile):")
        for f in skipped:
            print(f"  - {f}")

if __name__ == "__main__":
    batch_optimize()
