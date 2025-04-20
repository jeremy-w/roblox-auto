# Game: Drill Digging Simulator
# URL: https://www.roblox.com/share?code=1e23a98a131ff24fa74775cf036cf1cb&type=ExperienceDetails&stamp=1745164194892
#
# Assumptions:
#
# * MBP screen for button positions
# * Keyboard movement: left is A, forward is W
# * Starting with drill armed
# * Camera is zoomed all the way out
import pyautogui as p
from time import sleep

# NOTE: You must be zoomed out all the way, and have the drill armed.

p.PAUSE = 1

# Button Positions
BTN_WORLDS = (227, 500)
BTN_MAGIC = (930, 414)  # if scrolled to bottom in Worlds menu
BTN_GREECE = (921, 556)  # if scrolled to bottom in Worlds menu
BTN_MAIN = (900, 541)  # when freshly opened
BTN_CLOSE = (1006, 296)  # drill shop close button

SAND_SEC = 4.8
BEST_DRILL_SEC = 20  # greek drill 3 on greek; better too long than too short
MID_DRILL_SEC = 50  # greek drill 2 on greek
WIN_W_SEC = 1


def hold_key(key, secs):
    p.keyDown(key)
    sleep(secs)
    p.keyUp(key)


def forward(secs):
    hold_key('w', secs)


def left(secs):
    hold_key('a', secs)


def teleport_main():
    p.click(*BTN_WORLDS)
    sleep(1)  # wait for UI
    p.moveTo(x=BTN_MAIN[0], y=BTN_MAIN[1])
    p.scroll(50)  # ensure at top
    p.click()


def teleport_magic():
    p.click(*BTN_WORLDS)
    sleep(1)
    w, h = p.size()
    p.moveTo(x=w/2, y=h/2)
    # - still seems to be "towards end of document", even with natural scrolling.
    p.scroll(-50)
    p.click(*BTN_MAGIC)


def teleport_greece():
    p.click(*BTN_WORLDS)
    sleep(1)
    w, h = p.size()
    p.moveTo(x=w/2, y=h/2)
    # - still seems to be "towards end of document", even with natural scrolling.
    p.scroll(-50)
    p.click(*BTN_GREECE)


def drill_to_bottom(hold_time):
    w, h = p.size()
    # Assume drill is armed

    # Reset to known location
    teleport_main()
    # teleport_magic()
    teleport_greece()

    # Run onto sand.
    forward(SAND_SEC)

    # Drill to bottom, hopefully
    center = (w/2, h/2)
    n, t = 3, 1
    for _ in range(n):
        print('click in center', center)
        p.mouseDown(*center)
        p.mouseUp(*center)
    print('holding down mouse button')
    p.mouseDown(*center)
    sleep(hold_time - n*t)
    p.mouseUp()

    # Need to pause after each motion else they blend into a diagonal movement.
    # But because distance traveled seems to depend on zoom, and you can't control zoom very well, this is hard to get right.
    # Oh. Duh. Max out zoom.
    left(WIN_W_SEC)
    sleep(1)


def t():
    print('quickly, cmd tab to roblox!')
    sleep(5)
    run_count = 0
    while True:
        run_count += 1
        print("starting run:", run_count)
        drill_to_bottom(BEST_DRILL_SEC)


def main():
    print('running main')
    t()


if __name__ == '__main__':
    main()
