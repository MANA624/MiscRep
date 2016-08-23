import pygame
from random import randint, seed, random
from datetime import datetime
import operator
import re

pygame.init()
pygame.display.set_caption("Long-Legged Man")

seed(datetime.now())
pygame.mixer.init()
mute = False

display_width = 1000
display_height = 600

dark_red = (180, 0, 0)
sand = (220, 170, 100)
blue = (0, 0, 240)
gold = (0, 255, 0)
white = (255, 255, 255)

game_display = pygame.display.set_mode((display_width, display_height))
game_display.fill(dark_red)

clock = pygame.time.Clock()
FPS = 25
cumulative_time = [0, 0, 0]

scroll_start = 350

guy_height = 250
guy_width = 150
floor_height = 50
jump_height = 155
arms = 20
can_jump = True
on_platform = False

num_of_platforms = 30
platform_width = 100
platform_height = 17

s_font = pygame.font.SysFont(None, 30)
m_font = pygame.font.SysFont(None, 50)
l_font = pygame.font.SysFont(None, 70)
xl_font = pygame.font.SysFont(None, 150)

speed = 10
gravity = 1.2
jump_factor = -2

cloud = pygame.image.load("cloud.png")
cloud_size = [[round(cloud.get_rect()[2]*(random() + 0.9)), round(cloud.get_rect()[3]*(random() + 0.5))]
              for _ in range(3)]
cloud1 = pygame.transform.scale(cloud, cloud_size[0])
cloud2 = pygame.transform.scale(cloud, cloud_size[1])
cloud3 = pygame.transform.scale(cloud, cloud_size[2])
cloud_pos = [[5, randint(5, 150)], [400, randint(5, 150)], [800, randint(5, 150)]]
cloud_speed = [random()*2+1 for __ in range(3)]

still_guy = pygame.image.load("still_guy.png")
walking_guy_1 = pygame.image.load("moving1.png")
walking_guy_2 = pygame.image.load("moving2.png")
lefty1 = pygame.transform.flip(walking_guy_1, True, False)
lefty2 = pygame.transform.flip(walking_guy_2, True, False)

game_exit = False

num_of_leaders = 10

can_sink = True
stage = 1
clever_sayings = ["Round 1: Life is good!",
                  "Round 2: Time is running, er, has run out!",
                  "Round 3: Don't look down. It won't help",
                  "Round 4: Can you keep up with the pace?",
                  "Round 5: You jump like white boy"]


def start_screen():
    global game_exit
    file = "Sound/Greeting.ogg"
    pygame.mixer.music.load(file)
    if not mute:
        pygame.mixer.music.play()
    starting = True
    spacer = 0
    shift = 110
    height = 60
    game_display.fill(dark_red)
    text = ["Welcome to The Long-Legged Man",
            "Press the left and right arrow keys to move",
            "Press up to jump",
            "Press space bar to boost",
            "Press 'p' to pause and 'm' to mute",
            "You CAN jump from platforms",
            "PRESS ANY BUTTON TO CONTINUE"]

    for line in text:
        if spacer == 0:
            text_surf = l_font.render(line, True, gold)
        elif spacer == 1:
            text_surf = s_font.render(line, True, gold)
            spacer += 1
        else:
            text_surf = s_font.render(line, True, gold)
        text_rect = text_surf.get_rect()
        text_rect.center = (display_width // 2, shift + spacer*height)
        game_display.blit(text_surf, text_rect)
        spacer += 1

    pygame.display.update()

    while starting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                starting = False
                game_exit = True
            elif event.type == pygame.KEYDOWN:
                starting = False


def set_variables():
    global wall_location, platform_x, platform_y, platform_touched, touch_count, current_x, current_y, current_x_speed
    global current_y_speed, should_flip, time, num_of_boosts
    wall_location = 50
    platform_x = [randint(wall_location, 8*display_width) for _ in range(num_of_platforms)]
    platform_y = [randint(display_height - floor_height - jump_height - platform_height, display_height - floor_height -
                          platform_height) for _ in range(num_of_platforms)]
    platform_y.sort()
    platform_touched = [False for _ in range(num_of_platforms)]

    touch_count = 0

    current_x = scroll_start + 1
    current_y = display_height - guy_height - floor_height
    current_x_speed = 0
    current_y_speed = 0

    should_flip = 0

    time = [1, 15, 00]

    if stage < 5:
        num_of_boosts = 5 - stage + 1
    else:
        num_of_boosts = 0


def check_scores():
    try:
        read = open("Leaderboard.txt", 'r')
        scores = read.read()
        read.close()
    except FileNotFoundError:
        write = open("Leaderboard.txt", 'w')
        write.close()
        scores = ""
    if len(scores.split('\n')) < 10:
        write = open("Leaderboard.txt", 'a')
        write.write("0:00:00:00\n" * 10)
        write.close()


def title_screen():
    global stage, game_exit, time, can_sink, FPS, num_of_boosts

    pygame.mixer.music.stop()

    game_display.fill(dark_red)

    if stage == 2:
        time = [1, 00, 00]
    elif stage == 3:
        can_sink = False
        time = [0, 50, 00]
    elif stage == 4:
        FPS += 5
        time = [0, 45, 00]
    elif stage == 5:
        FPS += 3
        time = [0, 40, 00]
    elif stage > 5:
        FPS += 3
        secs = 40 - 5*(stage - 5)
        time = [00, secs, 00]

    if stage < 6:
        welcome = clever_sayings[stage-1]
        text_surf = l_font.render(welcome, True, gold)
    else:
        text_surf = l_font.render("Stage " + str(stage), True, gold)
    stage += 1
    text_rect = text_surf.get_rect()
    text_rect.center = (display_width // 2, display_height // 2)

    game_display.blit(text_surf, text_rect)
    pygame.display.update()
    for _ in range(30):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
        clock.tick(9)


def pausing():
    global game_exit, current_x_speed

    pygame.mixer.music.pause()

    paused = True

    game_display.fill(dark_red)
    pause_surf = m_font.render("Game paused. Press 'p' to continue or 'q' to quit", True, gold)
    pause_rect = pause_surf.get_rect()
    pause_rect.center = (display_width // 2, display_height // 2)
    game_display.blit(pause_surf, pause_rect)

    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
                game_exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
                elif event.key == pygame.K_q:
                    paused = False
                    game_exit = True
    pygame.mixer.music.unpause()
    current_x_speed = 0


def sort_time(scores, keeping):
    scores = scores.split('\n')
    scores = scores[:-1]
    tups = []
    for score in scores:
        score = score.split(':')
        tups.append((int(score[0]), int(score[1]), int(score[2]), int(score[3])))

    tups = sorted(tups, key=operator.itemgetter(0, 1, 2, 3), reverse=True)
    if keeping:
        tups = tups[:keeping]
    scores = ""
    for i in range(len(tups)):
        scores += str(tups[i][0]) + ':'
        if len(str(tups[i][1])) == 1:
            scores += '0'
        scores += str(tups[i][1]) + ':'
        if len(str(tups[i][2])) == 1:
            scores += '0'
        scores += str(tups[i][2]) + ':'
        if len(str(tups[i][3])) == 1:
            scores += '0'
        scores += str(tups[i][3]) + '\n'

    return scores


def leaderboard():
    global game_exit
    shift = 70
    leading = True
    reader = open('Leaderboard.txt', 'r')
    all_times = reader.read()
    reader.close()
    all_times = sort_time(all_times, False)
    all_times = all_times.split('\n')
    all_times = all_times[:-1]
    new_times = [re.sub(':', '  ', score, 1) for score in all_times]

    game_display.fill(dark_red)
    leader_surf = l_font.render("High Scores", True, gold)
    leader_rect = leader_surf.get_rect()
    leader_rect.center = (display_width // 2, shift)  # The start to the scores
    game_display.blit(leader_surf, leader_rect)
    for i in range(2, 12):
        on_screen = str(i-1) + ". " + new_times[i-2]
        leader_surf = s_font.render(on_screen, True, gold)
        leader_rect = leader_surf.get_rect()
        leader_rect.center = (display_width // 2, i*(display_height // num_of_leaders - 15) + shift)
        game_display.blit(leader_surf, leader_rect)
    pygame.display.update()
    while leading:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    leading = False
                elif event.key == pygame.K_q:
                    game_exit = True
                    return False

    if not game_exit:
        main()


def clocking(increment):
    global time, game_exit, t1, t2, t3, cum_t1, cum_t2, cum_t3

    if increment:
        if time[1] == 0 and time[0] != 0:
            time[0] -= 1
            time[1] = 59
            time[2] = 96
        elif time[2] == 0:
            time[1] -= 1
            time[2] = 96
        else:
            time[2] -= 4

    t1 = str(time[0])
    t2 = str(time[1])
    t3 = str(time[2])
    if len(t1) == 1:
        t1 = '0' + t1
    if len(t2) == 1:
        t2 = '0' + t2
    if len(t3) == 1:
        t3 = '0' + t3

    cum_t1 = str(cumulative_time[0])
    cum_t2 = str(cumulative_time[1])
    cum_t3 = str(cumulative_time[2])
    if len(cum_t1) == 1:
        cum_t1 = '0' + cum_t1
    if len(cum_t2) == 1:
        cum_t2 = '0' + cum_t2
    if len(cum_t3) == 1:
        cum_t3 = '0' + cum_t3


def get_input():
    global game_exit, current_y_speed, jump, on_platform, current_x_speed, num_of_boosts, mute
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                current_x_speed = speed
            elif event.key == pygame.K_LEFT:
                current_x_speed = -speed
            elif event.key == pygame.K_UP:
                if can_jump:
                    current_y_speed = jump_factor*speed
                    jump = False
                    on_platform = False
            elif event.key == pygame.K_DOWN:
                if on_platform and can_sink:
                    current_y_speed += 3
            elif event.key == pygame.K_p:
                pausing()
            elif event.key == pygame.K_SPACE:
                if num_of_boosts > 0:
                    num_of_boosts -= 1
                    current_y_speed -= 15
            elif event.key == pygame.K_m:
                mute = not mute
                if mute:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                if current_x_speed == speed:
                    current_x_speed = 0
            if event.key == pygame.K_LEFT:
                if current_x_speed == -speed:
                    current_x_speed = 0


def make_gravity():
    global current_x, current_y, current_y_speed
    if not on_platform:
        current_y_speed += gravity
    current_x += current_x_speed
    current_y += current_y_speed


def play_music():
    if not pygame.mixer.music.get_busy() and not mute:
        sound_int = randint(1, 785)
        sfile = 'Sound/Zelda/zelda' + str(sound_int) + '.mp3'
        pygame.mixer.music.load(sfile)
        pygame.mixer.music.play()


def collision_detection():
    global current_x, current_y, current_x_speed, current_y_speed, on_platform, touch_count, can_jump
    if current_y > display_height - guy_height - floor_height:
        current_y_speed = 0
        current_y = display_height - guy_height - floor_height
    elif current_y <= 0:
        if current_y_speed < 0:
            current_y_speed *= -1

    if current_x < 0:
        current_x = 0
        current_x_speed = 0
    elif current_x + guy_width > display_width:
        current_x = display_width - guy_width
        current_x_speed = 0

    on_platform = False
    for i in range(num_of_platforms):
        if current_x + guy_width - arms > platform_x[i] and current_x + arms < platform_x[i] + platform_width:
            if platform_y[i] + current_y_speed/2+1 >= current_y + guy_height >= platform_y[i] - current_y_speed/2-1:
                if current_y_speed >= 0:
                    current_y = platform_y[i] - guy_height
                    current_y_speed = 0
                    on_platform = True
                    if not platform_touched[i]:
                        platform_touched[i] = True
                        touch_count += 1
    if current_x <= wall_location:
        current_x = wall_location + 1
        current_x_speed = 0

    if current_y_speed == 0:
        can_jump = True
    else:
        can_jump = False


def scrolling():
    global wall_location, current_x
    if current_x >= display_width - scroll_start:
        for i in range(num_of_platforms):
            platform_x[i] -= current_x_speed
        current_x -= current_x_speed
        wall_location -= current_x_speed
    elif current_x + guy_width <= scroll_start:
        for i in range(num_of_platforms):
            platform_x[i] -= current_x_speed
        current_x -= current_x_speed
        wall_location -= current_x_speed


def draw():
    global should_flip
    game_display.fill(dark_red)

    draw_clouds()

    text_surface = s_font.render("Platforms touched: " + str(touch_count) + " / " + str(num_of_platforms), True, gold)
    text_rect = text_surface.get_rect()
    text_rect.center = (150, 50)

    boost_surf = s_font.render("Boosts: " + str(num_of_boosts), True, gold)
    boost_rect = boost_surf.get_rect()
    boost_rect.center = (display_width - 150, 50)

    pygame.draw.rect(game_display, sand, [0, display_height-floor_height, display_width, floor_height])
    for i in range(num_of_platforms):
        if not platform_touched[i]:
            pygame.draw.rect(game_display, blue, [platform_x[i], platform_y[i], platform_width, platform_height])
        else:
            pygame.draw.rect(game_display, gold, [platform_x[i], platform_y[i], platform_width, platform_height])
    pygame.draw.rect(game_display, white, [0, 0, wall_location, display_height])

    should_flip += 1
    if current_x_speed == 0:
        game_display.blit(still_guy, [current_x, current_y])
    elif current_x_speed > 0:
        if should_flip % 16 > 8:
            game_display.blit(walking_guy_1, [current_x, current_y])
        else:
            game_display.blit(walking_guy_2, [current_x, current_y])
    else:
        if should_flip % 16 > 8:
            game_display.blit(lefty1, [current_x, current_y])
        else:
            game_display.blit(lefty2, [current_x, current_y])

    game_display.blit(text_surface, text_rect)
    game_display.blit(boost_surf, boost_rect)

    clock_surf = m_font.render(t1 + ':' + t2 + ':' + t3, True, gold)
    clock_rect = clock_surf.get_rect()
    clock_rect.center = (display_width//2, 60)
    game_display.blit(clock_surf, clock_rect)

    if not game_exit:
        pygame.display.update()

    clock.tick(FPS)


def draw_clouds():
    global cloud_pos, cloud_speed, cloud1, cloud2, cloud3, cloud_size
    game_display.blit(cloud1, cloud_pos[0])
    cloud_pos[0][0] += cloud_speed[0]
    if cloud_pos[0][0] > display_width:
        cloud_size = [[round(cloud.get_rect()[2]*(random() + 0.9)), round(cloud.get_rect()[3]*(random() + 0.5))]
                      for _ in range(3)]
        cloud1 = pygame.transform.scale(cloud, cloud_size[0])
        cloud_pos[0][0] = -cloud_size[0][0] - randint(40, 60)
        cloud_speed[0] = random()*2+1
        cloud_pos[0][1] = randint(5, 150)

    game_display.blit(cloud2, cloud_pos[1])
    cloud_pos[1][0] += cloud_speed[1]
    if cloud_pos[1][0] > display_width:
        cloud_size = [[round(cloud.get_rect()[2]*(random() + 0.9)), round(cloud.get_rect()[3]*(random() + 0.5))]
                      for _ in range(3)]
        cloud2 = pygame.transform.scale(cloud, cloud_size[1])
        cloud_pos[1][0] = -cloud_size[1][0] - randint(20, 40)
        cloud_speed[1] = random()*2+1
        cloud_pos[1][1] = randint(5, 150)

    game_display.blit(cloud3, cloud_pos[2])
    cloud_pos[2][0] += cloud_speed[2]
    if cloud_pos[2][0] > display_width:
        cloud_size = [[round(cloud.get_rect()[2]*(random() + 0.9)), round(cloud.get_rect()[3]*(random() + 0.5))]
                      for _ in range(3)]
        cloud3 = pygame.transform.scale(cloud, cloud_size[2])
        cloud_pos[2][0] = -cloud_size[2][0] - randint(0, 20)
        cloud_speed[2] = random()*2+1
        cloud_pos[2][1] = randint(5, 150)


def has_won():
    global game_exit, stage, FPS, can_sink, cumulative_time
    if touch_count == num_of_platforms or time[0] == time[1] == time[2] == 0:
        cumulative_time[0] += time[0]
        cumulative_time[1] += time[1]
        cumulative_time[2] += time[2]
        if cumulative_time[2] >= 100:
            cumulative_time[2] -= 100
            cumulative_time[1] += 1
        if cumulative_time[1] >= 60:
            cumulative_time[1] -= 60
            cumulative_time[0] += 1
        pygame.mixer.music.stop()
        game_display.fill(dark_red)

        if time[0] == time[1] == time[2] == 0:
            save_score()
            stage = 1
            clocking(False)
            cumulative_time = [0, 0, 0]
            can_sink = True
            FPS = 25
            win_surface = xl_font.render("You suck!", True, gold)
        else:
            clocking(False)
            win_surface = xl_font.render("YOU WIN!!!", True, gold)
        win_rect = win_surface.get_rect()
        win_rect.center = (display_width // 2, display_height // 2 - 50)

        win_score = xl_font.render(cum_t1 + ':' + cum_t2 + ':' + cum_t3, True, gold)
        win_score_rect = win_score.get_rect()
        win_score_rect.center = (display_width // 2, display_height // 2 + 50)

        plus_surf = m_font.render('+' + t1 + ':' + t2 + ':' + t3, True, gold)
        plus_rect = plus_surf.get_rect()
        plus_rect.center = (display_width // 2, display_height // 2 + 120)

        info = s_font.render("Press 'C' to continue or 'Q' to Quit or 'L' to see the leaderboard", True, gold)
        info_rect = info.get_rect()
        info_rect.center = (display_width // 2, display_height - 70)

        game_display.blit(win_score, win_score_rect)
        game_display.blit(win_surface, win_rect)
        game_display.blit(plus_surf, plus_rect)
        game_display.blit(info, info_rect)
        pygame.display.update()

        getting_input = True
        while getting_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    getting_input = False
                    game_exit = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        getting_input = False
                    elif event.key == pygame.K_q:
                        game_exit = True
                        getting_input = False
                    elif event.key == pygame.K_l:
                        getting_input = leaderboard()

        if not game_exit:
            main()


def save_score():
    saving = open("Leaderboard.txt", 'a')
    saving.write(str(stage-1) + ':' + cum_t1 + ':' + cum_t2 + ':' + cum_t3 + '\n')
    saving.close()


def clean_high_scores():
    read = open('Leaderboard.txt', 'r')
    scores = read.read()
    read.close()

    scores = sort_time(scores, num_of_leaders)

    write = open("Leaderboard.txt", 'w')
    write.write(scores)
    write.close()


def main():
    if stage == 1:
        start_screen()
    set_variables()
    check_scores()
    if not game_exit:
        title_screen()
    while not game_exit:
        play_music()
        clocking(True)
        get_input()
        make_gravity()
        collision_detection()
        scrolling()
        draw()
        has_won()
    clean_high_scores()


if __name__ in '__main__':
    main()
