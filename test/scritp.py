from pathlib import Path

current_dir = Path.cwd()
print(f"Files in {current_dir}: {list(current_dir.iterdir())}")