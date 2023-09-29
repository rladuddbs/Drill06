from pico2d import *
import math

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
hand_arrow = load_image('hand_arrow.png')
character = load_image('run_animation.png')

def handle_events():
    global running
    global mx, my
    global coor_list

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            coor_list.append((mx, my))


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
cursor_x, cursor_y = x, y
coor_list = []
frame = 0

while running:
    clear_canvas()
    hide_cursor()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    handle_events()

    hand_arrow.draw(mx, my)
    # 마우스 클릭한 위치에 화살표 그리기
    for coor in coor_list:
        hand_arrow.draw(coor[0], coor[1])

    if len(coor_list) > 0:
        target_x, target_y = coor_list[0]
        length = math.sqrt((target_x - x) ** 2 + (target_y - y) ** 2)

        if length > 0:
            x_dist = (target_x - x) / length
            y_dist = (target_y - y) / length
            x += x_dist * 20
            y += y_dist * 20

        if target_x >= x:
            character.clip_draw(frame * 100, 0, 100, 102, x, y, 100, 102)
        elif target_x < x:
            character.clip_composite_draw(frame * 100, 0, 100, 102, 0, 'h', x, y, 100, 102)

        if (x - 50 < target_x < x + 50) and (y - 50 < target_y < y + 50):
            del coor_list[0]
    else:
        character.clip_draw(frame * 100, 0, 100, 102, x, y, 100, 102)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.1)

close_canvas()