import keyboard as kb
import time

# remap pairs. left is to remap to right
REMAPS: dict = {
    "r": "w"
}

QUIT_HOT_KEY = "ctrl+shift+q"

def main():
    for source, target in REMAPS.items():
        kb.remap_key(source, target)
        print(f"Remmaped {source!r} key to {target!r} key")

    print("All inserted keys have been remaped.")
    time.sleep(0.5)
    print(f"Press {QUIT_HOT_KEY!r} to unbind remaps")
    kb.wait(QUIT_HOT_KEY)

    kb.unhook_all()
    print("remaps unbound.")

if __name__ == "__main__":
    main()