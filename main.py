"""
Main file for Magma Boy and Hydro Girl game.
"""

# import pygame and other needed libraries
import sys
import pygame
import asyncio
from pygame.locals import *

# import classes
from game import Game
from board import Board
from character import MagmaBoy, HydroGirl
from controller import ArrowsController, WASDController, GeneralController
from gates import Gates
from doors import FireDoor, WaterDoor
from level_select import LevelSelect


def main():
    pygame.init()
    pygame.display.set_caption("Ali ile Ela El Ele")
    controller = GeneralController()
    game = Game()
    show_intro_screen(game, controller)


async def show_intro_screen(game, controller):
    game.display.fill((200, 200, 200))

    font_title = pygame.font.Font(None, 55)
    font_love_small = pygame.font.Font(None, 22)
    font_text = pygame.font.Font(None, 24)

    color_ali = (255, 50, 50)
    color_ela = (50, 50, 255)
    color_love = (255, 20, 147)
    color_black = (0, 0, 0)

    screen_width = game.display.get_width()

    t_main = font_title.render("ALI ILE ELA EL ELE", True, color_black)

    t1 = font_text.render("CONTROL ALI WITH THE ARROW KEYS", True, color_black)
    t2 = font_text.render("CONTROL ELA WITH THE WASD KEYS", True, color_black)

    t3_1 = font_text.render("ALI", True, color_ali)
    t3_2 = font_text.render(" CAN TOUCH LAVA, BUT NOT WATER", True, color_black)

    t4_1 = font_text.render("ELA", True, color_ela)
    t4_2 = font_text.render(" CAN TOUCH WATER, BUT NOT LAVA", True, color_black)

    t5 = font_text.render("NEITHER CAN TOUCH GOO", True, (0, 100, 0))

    t_love1 = font_love_small.render("ALI IS IN LOVE WITH ELA", True, color_love)
    t_love2 = font_love_small.render("ELA IS IN LOVE WITH ALI", True, color_love)

    t6 = font_text.render("SOLVE THE PUZZLES AND GET TO THE EXIT!", True, color_black)
    t7 = font_text.render("PRESS <ENTER> TO BEGIN", True, color_black)

    game.display.blit(t_main, t_main.get_rect(center=(screen_width // 2, 50)))

    game.display.blit(t1, t1.get_rect(center=(screen_width // 2, 110)))
    game.display.blit(t2, t2.get_rect(center=(screen_width // 2, 135)))

    res_t3 = pygame.Surface((t3_1.get_width() + t3_2.get_width(), t3_1.get_height()), pygame.SRCALPHA)
    res_t3.blit(t3_1, (0, 0))
    res_t3.blit(t3_2, (t3_1.get_width(), 0))
    game.display.blit(res_t3, res_t3.get_rect(center=(screen_width // 2, 180)))

    res_t4 = pygame.Surface((t4_1.get_width() + t4_2.get_width(), t4_1.get_height()), pygame.SRCALPHA)
    res_t4.blit(t4_1, (0, 0))
    res_t4.blit(t4_2, (t4_1.get_width(), 0))
    game.display.blit(res_t4, res_t4.get_rect(center=(screen_width // 2, 205)))

    game.display.blit(t5, t5.get_rect(center=(screen_width // 2, 235)))

    game.display.blit(t_love1, t_love1.get_rect(center=(screen_width // 2, 270)))
    game.display.blit(t_love2, t_love2.get_rect(center=(screen_width // 2, 295)))

    game.display.blit(t6, t6.get_rect(center=(screen_width // 2, 340)))
    game.display.blit(t7, t7.get_rect(center=(screen_width // 2, 380)))

    while True:
        await asyncio.sleep(0)
        game.refresh_window()
        if controller.press_key(pygame.event.get(), K_RETURN):
            show_level_screen(game, controller)
def show_level_screen(game, controller):
    level_select = LevelSelect()
    level = game.user_select_level(level_select, controller)
    run_game(game, controller, level)


async def show_gucci_warning(game, controller):
    """Gucci Kurtarma Operasyonu - Gizli Uyarı Ekranı"""
    game.display.fill((0, 0, 0))  # Siyah arka plan

    # Yazı tiplerini ve boyutlarını ayarlıyoruz
    font_big = pygame.font.Font(None, 55)
    font_small = pygame.font.Font(None, 35)

    # Yazıları ve renklerini (RGB) oluşturuyoruz
    text1 = font_big.render("GUCCI KACIRILDI!", True, (255, 50, 50))  # Kırmızı
    text2 = font_small.render("Onu kurtarmak icin son engeli asmalisiniz.", True, (255, 255, 255))  # Beyaz
    text3 = font_small.render("[ Baslamak Icin ENTER'a Basin ]", True, (100, 255, 100))  # Yeşil

    # Yazıları ekranın ortasına hizalayarak yerleştiriyoruz
    game.display.blit(text1, (110, 150))
    game.display.blit(text2, (40, 210))
    game.display.blit(text3, (90, 300))

    while True:
        await asyncio.sleep(0)
        game.refresh_window()
        # Oyuncu ENTER'a basana kadar bu siyah ekranda kalır
        if controller.press_key(pygame.event.get(), K_RETURN):
            break
async def show_win_screen(game, controller):
    win_screen = pygame.image.load('data/screens/win_screen.png')
    win_screen.set_colorkey((255, 0, 255))
    game.display.blit(win_screen, (0, 0))


    while True:
        await asyncio.sleep(0)
        game.refresh_window()
        if controller.press_key(pygame.event.get(), K_RETURN):
            show_level_screen(game, controller)


async def show_gucci_win_screen(game, controller):
    gucci_screen = pygame.image.load('data/gucci_rescue.png').convert_alpha()
    gucci_screen = pygame.transform.smoothscale(gucci_screen, (600, 400))

    screen_width = game.display.get_width()
    screen_height = game.display.get_height()
    x = (screen_width - 600) // 2
    y = (screen_height - 400) // 2

    game.display.blit(gucci_screen, (x, y))


    while True:
        await asyncio.sleep(0)
        game.refresh_window()
        if controller.press_key(pygame.event.get(), K_RETURN):
            show_level_screen(game, controller)


async def show_womens_day_screen(game, controller):
    game.display.fill((20, 0, 10))

    # Yazı tiplerini ve boyutlarını daha sığacak şekilde ayarladık (50, 25)
    font_main = pygame.font.Font(None, 50)
    font_sub = pygame.font.Font(None, 25)

    # Hot Pink renk ve Beyaz renk tanımı
    color_pink = (255, 105, 180)
    color_white = (255, 255, 255)

    # Metinleri oluşturuyoruz
    text1_surf = font_main.render("KADINLAR GUNUN", True, color_pink)
    text2_surf = font_main.render("KUTLU OLSUN ASKIM <3", True, color_pink)
    text3_surf = font_sub.render("[ Baslamak Icin ENTER'a Basin ]", True, color_white)

    # Ekran boyutlarını alıp ortalamak için matematik kullanıyoruz
    screen_width = game.display.get_width()
    screen_height = game.display.get_height()

    # Metinlerin merkez koordinatlarını (x, y) otomatik hesaplıyoruz
    t1_rect = text1_surf.get_rect(center=(screen_width // 2, 180))
    t2_rect = text2_surf.get_rect(center=(screen_width // 2, 230))
    t3_rect = text3_surf.get_rect(center=(screen_width // 2, 320))

    # Metinleri hesaplanan tam orta koordinatlara çiziyoruz
    game.display.blit(text1_surf, t1_rect)
    game.display.blit(text2_surf, t2_rect)
    game.display.blit(text3_surf, t3_rect)

    while True:
        await asyncio.sleep(0)
        game.refresh_window()
        if controller.press_key(pygame.event.get(), K_RETURN):
            break


async def ily_screen(game, controller):
    game.display.fill((20, 0, 10))

    # Yazı tiplerini ve boyutlarını daha sığacak şekilde ayarladık (50, 25)
    font_main = pygame.font.Font(None, 50)
    font_sub = pygame.font.Font(None, 25)

    # Hot Pink renk ve Beyaz renk tanımı
    color_pink = (255, 105, 180)
    color_white = (255, 255, 255)

    # Metinleri oluşturuyoruz
    text1_surf = font_main.render("SENI COK SEVIYORUM", True, color_pink)
    text2_surf = font_main.render("ASKIM <3", True, color_pink)
    text3_surf = font_sub.render("[ Baslamak Icin ENTER'a Basin ]", True, color_white)

    # Ekran boyutlarını alıp ortalamak için matematik kullanıyoruz
    screen_width = game.display.get_width()
    screen_height = game.display.get_height()

    # Metinlerin merkez koordinatlarını (x, y) otomatik hesaplıyoruz
    t1_rect = text1_surf.get_rect(center=(screen_width // 2, 180))
    t2_rect = text2_surf.get_rect(center=(screen_width // 2, 230))
    t3_rect = text3_surf.get_rect(center=(screen_width // 2, 320))

    # Metinleri hesaplanan tam orta koordinatlara çiziyoruz
    game.display.blit(text1_surf, t1_rect)
    game.display.blit(text2_surf, t2_rect)
    game.display.blit(text3_surf, t3_rect)

    while True:
        await asyncio.sleep(0)
        game.refresh_window()
        if controller.press_key(pygame.event.get(), K_RETURN):
            break


async def lps_screen(game, controller):
    game.display.fill((20, 0, 10))

    # Yazı tiplerini ve boyutlarını daha sığacak şekilde ayarladık (50, 25)
    font_main = pygame.font.Font(None, 50)
    font_sub = pygame.font.Font(None, 25)

    # Hot Pink renk ve Beyaz renk tanımı
    color_pink = (255, 105, 180)
    color_white = (255, 255, 255)

    # Metinleri oluşturuyoruz
    text1_surf = font_main.render("SEVGILIMLE LPS", True, color_pink)
    text2_surf = font_main.render("ALMAYA GIDIYORUZZ <3", True, color_pink)
    text3_surf = font_sub.render("[ Baslamak Icin ENTER'a Basin ]", True, color_white)

    # Ekran boyutlarını alıp ortalamak için matematik kullanıyoruz
    screen_width = game.display.get_width()
    screen_height = game.display.get_height()

    # Metinlerin merkez koordinatlarını (x, y) otomatik hesaplıyoruz
    t1_rect = text1_surf.get_rect(center=(screen_width // 2, 180))
    t2_rect = text2_surf.get_rect(center=(screen_width // 2, 230))
    t3_rect = text3_surf.get_rect(center=(screen_width // 2, 320))

    # Metinleri hesaplanan tam orta koordinatlara çiziyoruz
    game.display.blit(text1_surf, t1_rect)
    game.display.blit(text2_surf, t2_rect)
    game.display.blit(text3_surf, t3_rect)

    while True:
        await asyncio.sleep(0)
        game.refresh_window()
        if controller.press_key(pygame.event.get(), K_RETURN):
            break
async def show_death_screen(game, controller, level):
    death_screen = pygame.image.load('data/screens/death_screen.png')
    death_screen.set_colorkey((255, 0, 255))
    game.display.blit(death_screen, (0, 0))
    while True:
        await asyncio.sleep(0)
        game.refresh_window()
        events = pygame.event.get()
        if controller.press_key(events, K_RETURN):
            run_game(game, controller, level)
        if controller.press_key(events, K_ESCAPE):
            show_level_screen(game, controller)


async def run_game(game, controller, level="level1"):
    # load level data
    if level == "level1":
        show_womens_day_screen(game, controller)
        board = Board('data/level1.txt')
        gate_location = (285, 128)
        plate_locations = [(190, 168), (390, 168)]
        gate = Gates(gate_location, plate_locations)
        gates = []

        fire_door_location = (64, 48)
        fire_door = FireDoor(fire_door_location)
        water_door_location = (128, 48)
        water_door = WaterDoor(water_door_location)
        doors = [fire_door, water_door]

        magma_boy_location = (16, 336)
        magma_boy = MagmaBoy(magma_boy_location)
        hydro_girl_location = (35, 336)
        hydro_girl = HydroGirl(hydro_girl_location)

    if level == "level2":
        lps_screen(game, controller)
        board = Board('data/level2.txt')
        gates = []

        fire_door_location = (390, 48)
        fire_door = FireDoor(fire_door_location)
        water_door_location = (330, 48)
        water_door = WaterDoor(water_door_location)
        doors = [fire_door, water_door]

        magma_boy_location = (16, 336)
        magma_boy = MagmaBoy(magma_boy_location)
        hydro_girl_location = (35, 336)
        hydro_girl = HydroGirl(hydro_girl_location)

    if level == "level3":

        board = Board('data/level3.txt')
        gates = []

        fire_door_location = (5 * 16, 4 * 16)
        fire_door = FireDoor(fire_door_location)
        water_door_location = (28 * 16, 4 * 16)
        water_door = WaterDoor(water_door_location)
        doors = [fire_door, water_door]

        magma_boy_location = (28 * 16, 4 * 16)
        magma_boy = MagmaBoy(magma_boy_location)
        hydro_girl_location = (5 * 16, 4 * 16)
        hydro_girl = HydroGirl(hydro_girl_location)
    if level == "level4":
        ily_screen(game,controller)
        board = Board('data/level4.txt')
        gates = []  # Bu romantik bölümde açılacak kapı/buton yok, sadece siz varsınız!

        # Çıkış Kapıları (Haritanın sol üst tarafına koydum)
        fire_door_location = (192, 240)
        fire_door = FireDoor(fire_door_location)
        water_door_location = (228, 240)
        water_door = WaterDoor(water_door_location)
        doors = [fire_door, water_door]

        # Karakterlerin Doğma Noktaları (Haritanın sol alt köşesinde başlarlar)
        magma_boy_location = (16, 336)
        magma_boy = MagmaBoy(magma_boy_location)
        hydro_girl_location = (35, 336)
        hydro_girl = HydroGirl(hydro_girl_location)

    if level == "level5":
        show_gucci_warning(game, controller)
        board = Board('data/level5.txt')
        gates = []

        # Çıkış Kapıları (Miniş Kulaklarının Tam Üstünde!)
        fire_door_location = (96, 48)
        fire_door = FireDoor(fire_door_location)
        water_door_location = (432, 48)
        water_door = WaterDoor(water_door_location)
        doors = [fire_door, water_door]

        # Karakterlerin Doğma Noktaları (Haritanın zemininde)
        magma_boy_location = (16, 336)
        magma_boy = MagmaBoy(magma_boy_location)
        hydro_girl_location = (35, 336)
        hydro_girl = HydroGirl(hydro_girl_location)
    # initialize needed classes

    arrows_controller = ArrowsController()
    wasd_controller = WASDController()

    clock = pygame.time.Clock()

    show_touch_controls = False

    screen_w = game.display.get_width()
    screen_h = game.display.get_height()
    btn_size = 50
    ela_left_btn = pygame.Rect(20, screen_h - 80, btn_size, btn_size)
    ela_right_btn = pygame.Rect(90, screen_h - 80, btn_size, btn_size)
    ela_up_btn = pygame.Rect(55, screen_h - 140, btn_size, btn_size)
    ali_left_btn = pygame.Rect(screen_w - 140, screen_h - 80, btn_size, btn_size)
    ali_right_btn = pygame.Rect(screen_w - 70, screen_h - 80, btn_size, btn_size)
    ali_up_btn = pygame.Rect(screen_w - 105, screen_h - 140, btn_size, btn_size)

    # main game loop
    while True:
        await asyncio.sleep(0)
        # pygame management
        clock.tick(60)
        events = pygame.event.get()

        # draw features of level
        game.draw_level_background(board)
        game.draw_board(board)
        if gates:
            game.draw_gates(gates)
        game.draw_doors(doors)

        # draw player
        game.draw_player([magma_boy, hydro_girl])

        # move player
        arrows_controller.control_player(events, magma_boy)
        wasd_controller.control_player(events, hydro_girl)

        game.move_player(board, gates, [magma_boy, hydro_girl])

        # check for player at special location
        game.check_for_death(board, [magma_boy, hydro_girl])

        game.check_for_gate_press(gates, [magma_boy, hydro_girl])

        game.check_for_door_open(fire_door, magma_boy)
        game.check_for_door_open(water_door, hydro_girl)

        if show_touch_controls:
            pygame.draw.rect(game.display, (200, 200, 200), ela_left_btn, border_radius=10)
            pygame.draw.polygon(game.display, (50, 50, 50),
                                [(ela_left_btn.x + 35, ela_left_btn.y + 15), (ela_left_btn.x + 35, ela_left_btn.y + 35),
                                 (ela_left_btn.x + 15, ela_left_btn.y + 25)])

            pygame.draw.rect(game.display, (200, 200, 200), ela_right_btn, border_radius=10)
            pygame.draw.polygon(game.display, (50, 50, 50), [(ela_right_btn.x + 15, ela_right_btn.y + 15),
                                                             (ela_right_btn.x + 15, ela_right_btn.y + 35),
                                                             (ela_right_btn.x + 35, ela_right_btn.y + 25)])

            pygame.draw.rect(game.display, (200, 200, 200), ela_up_btn, border_radius=10)
            pygame.draw.polygon(game.display, (50, 50, 50),
                                [(ela_up_btn.x + 15, ela_up_btn.y + 35), (ela_up_btn.x + 35, ela_up_btn.y + 35),
                                 (ela_up_btn.x + 25, ela_up_btn.y + 15)])

            pygame.draw.rect(game.display, (200, 200, 200), ali_left_btn, border_radius=10)
            pygame.draw.polygon(game.display, (50, 50, 50),
                                [(ali_left_btn.x + 35, ali_left_btn.y + 15), (ali_left_btn.x + 35, ali_left_btn.y + 35),
                                 (ali_left_btn.x + 15, ali_left_btn.y + 25)])

            pygame.draw.rect(game.display, (200, 200, 200), ali_right_btn, border_radius=10)
            pygame.draw.polygon(game.display, (50, 50, 50), [(ali_right_btn.x + 15, ali_right_btn.y + 15),
                                                             (ali_right_btn.x + 15, ali_right_btn.y + 35),
                                                             (ali_right_btn.x + 35, ali_right_btn.y + 25)])

            pygame.draw.rect(game.display, (200, 200, 200), ali_up_btn, border_radius=10)
            pygame.draw.polygon(game.display, (50, 50, 50),
                                [(ali_up_btn.x + 15, ali_up_btn.y + 35), (ali_up_btn.x + 35, ali_up_btn.y + 35),
                                 (ali_up_btn.x + 25, ali_up_btn.y + 15)])

            mouse_pressed = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()

            if mouse_pressed[0]:
                if ela_left_btn.collidepoint(mouse_pos):
                    hydro_girl.moving_left = True
                if ela_right_btn.collidepoint(mouse_pos):
                    hydro_girl.moving_right = True
                if ela_up_btn.collidepoint(mouse_pos):
                    hydro_girl.jumping = True
                if ali_left_btn.collidepoint(mouse_pos):
                    magma_boy.moving_left = True
                if ali_right_btn.collidepoint(mouse_pos):
                    magma_boy.moving_right = True
                if ali_up_btn.collidepoint(mouse_pos):
                    magma_boy.jumping = True
        # refresh window
        game.refresh_window()

        # special events
        if hydro_girl.is_dead() or magma_boy.is_dead():
            show_death_screen(game, controller, level)

        if game.level_is_done(doors):
            if level == "level5":
                show_gucci_win_screen(game, controller)
            else:
                show_win_screen(game, controller)
        if controller.press_key(events, K_ESCAPE):
            show_level_screen(game, controller)

        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                show_touch_controls = False
            if event.type == MOUSEBUTTONDOWN or getattr(pygame, 'FINGERDOWN', None) == event.type:
                show_touch_controls = True


if __name__ == '__main__':
    asyncio.run(main())
