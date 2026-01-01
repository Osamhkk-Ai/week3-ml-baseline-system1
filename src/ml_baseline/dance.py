import os
import time

FRAMES = [
    r"""
      (•_•)
     <)   )╯  ML
      /   \
    """,
    r"""
      (•_•)
    <(   ( ╯  ML
      /   \
    """,
    r"""
      (•_•)
     <)   )╯  ML
      /   \
    """,
    r"""
      (•_•)
       \(   (>  ML
        /   \
    """,
    r"""
      (•_•)
      <)   )>  ML
       /   \
    """,
    r"""
      (•_•)
       \(   (>  ML
        /   \
    """,
]

def _clear():
    os.system("cls" if os.name == "nt" else "clear")

def dance(repeat: int = 4, delay: float = 0.35):
    for _ in range(repeat):
        for frame in FRAMES:
            _clear()
            print(frame)
            time.sleep(delay)
