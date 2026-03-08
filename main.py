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


async def main(): # main fonksiyonu async yapıldı
    pygame.init()
    pygame.display.set_caption("Ali ile Ela El Ele")
    controller = GeneralController()
    game = Game()
    # DÜZELTME: async fonksiyon çağrılırken await eklenmeli
    await show_intro_screen(game, controller)


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
        game.refresh_window()
        if controller.press_key(pygame.event.get(), K_RETURN):
            # DÜZELTME: await eklendi
            await show_level_screen(game, controller)
        await asyncio.sleep(0)

async def show_level_screen(game, controller):
    level_select = LevelSelect()
    level = game.user_select_level(level_select, controller)
    # DÜZELTME: await eklendi
    await run_game(game, controller, level)


async def show_gucci_warning(game, controller):
    game.display.fill((0, 0, 0))
    font_big = pygame.font.Font(None, 55)
    font_small = pygame.font.Font(None, 35)
    text1 = font_big.render("GUCCI KACIRILDI!", True, (255, 50, 50))
    text2 = font_small.render("Onu kurtarmak icin son engeli asmalisiniz.", True, (255, 255, 255))
    text3 = font_small.render("[ Baslamak Icin ENTER'a Basin ]", True, (100, 255, 100))
    game.display.blit(text1, (110, 150))
    game.display.blit(text2, (40, 210))
    game.display.blit(text3, (90, 300))
    while True:
        game.refresh_window()
        if controller.press_key(pygame.event.get(), K_RETURN):
            break
        await asyncio.sleep(0)

async def show_win_screen(game, controller):
    win_screen = pygame.image.load('data/screens/win_screen.png')
    win_screen.set_colorkey((255, 0, 255))
    game.display.blit(win_screen, (0, 0))
    while True:
        game.refresh_window()
        if controller.press_key(pygame.event.get(), K_RETURN):
            await show_level_screen(game, controller)
        await asyncio.sleep(0)

async def show_gucci_win_screen(game, controller):
    gucci_screen = pygame.image.load('data/gucci_rescue.png').convert_alpha()
    gucci_screen = pygame.transform.smoothscale(gucci_screen, (600, 400))
    screen_width = game.display.get_width()
    screen_height = game.display.get_height()
    x = (screen_width - 600) // 2
    y = (screen_height - 400) // 2
    game.display.blit(gucci_screen, (x, y))
    while True:
        game.refresh_window()
        if controller.press_key(pygame.event.get(), K_RETURN):
            await show_level_screen(game, controller)
        await asyncio.sleep(0)

async def show_womens_day_screen(game, controller):
    game.display.fill((20, 0, 10))
    font_main = pygame.font.Font(None, 50)
    font_sub = pygame.font.Font(None, 25)
    color_pink = (255, 105, 180)
    color_white = (255, 255, 255)
    text1_surf = font_main.render("KADINLAR GUNUN", True, color_pink)
    text2_surf = font_main.render("KUTLU OLSUN ASKIM <3", True, color_pink)
    text3_surf = font_sub.render("[ Baslamak Icin ENTER'a Basin ]", True, color_white)
    screen_width = game.display.get_width()
    t1_rect = text1_surf.get_rect(center=(screen_width // 2, 180))
    t2_rect = text2_surf.get_rect(center=(screen_width // 2, 230))
    t3_rect = text3_surf.get_rect(center=(screen_width // 2, 320))
    game.display.blit(text1_surf, t1_rect)
    game.display.blit(text2_surf, t2_rect)
    game.display.blit(text3_surf, t3_rect)
    while True:
        game.refresh_window()
        if controller.press_key(pygame.event.get(), K_RETURN):
            break
        await asyncio.sleep(0)

async def ily_screen(game, controller):
    game.display.fill((20, 0, 10))
    font_main = pygame.font.Font(None, 50)
    font_sub = pygame.font.Font(None, 25)
    color_pink = (255, 105, 180)
    color_white = (255, 255, 255)
    text1_surf = font_main.render("SENI COK SEVIYORUM", True, color_pink)
    text2_surf = font_main.render("ASKIM <3", True, color_pink)
    text3_surf = font_sub.render("[ Baslamak Icin ENTER'a Basin ]", True, color_white)
    screen_width = game.display.get_width()
    t1_rect = text1_surf.get_rect(center=(screen_width // 2, 180))
    t2_rect = text2_surf.get_rect(center=(screen_width // 2, 230))
    t3_rect = text3_surf.get_rect(center=(screen_width // 2, 320))
    game.display.blit(text1_surf, t1_rect)
    game.display.blit(text2_surf, t2_rect)
    game.display.blit(text3_surf, t3_rect)
    while True:
        game.refresh_window()
        if controller.press_key(pygame.event.get(), K_RETURN):
            break
        await asyncio.sleep(0)

async def lps_screen(game, controller):
    game.display.fill((20, 0, 10))
    font_main = pygame.font.Font(None, 50)
    font_sub = pygame.font.Font(None, 25)
    color_pink = (255, 105, 180)
    color_white = (255, 255, 255)
    text1_surf = font_main.render("SEVGILIMLE LPS", True, color_pink)
    text2_surf = font_main.render("ALMAYA GIDIYORUZZ <3", True, color_pink)
    text3_surf = font_sub.render("[ Baslamak Icin ENTER'a Basin ]", True, color_white)
    screen_width = game.display.get_width()
    t1_rect = text1_surf.get_rect(center=(screen_width // 2, 180))
    t2_rect = text2_surf.get_rect(center=(screen_width // 2, 230))
    t3_rect = text3_surf.get_rect(center=(screen_width // 2, 320))
    game.display.blit(text1_surf, t1_rect)
    game.display.blit(text2_surf, t2_rect)
    game.display.blit(text3_surf, t3_rect)
    while True:
        game.refresh_window()
        if controller.press_key(pygame.event.get(), K_RETURN):
            break
        await asyncio.sleep(0)

async def show_death_screen(game, controller, level):
    death_screen = pygame.image.load('data/screens/death_screen.png')
    death_screen.set_colorkey((255, 0, 255))
    game.display.blit(death_screen, (0, 0))
    while True:
        game.refresh_window()
        events = pygame.event.get()
        if controller.press_key(events, K_RETURN):
            await run_game(game, controller, level)
        if controller.press_key(events, K_ESCAPE):
            await show_level_screen(game, controller)
        await asyncio.sleep(0)

async def run_game(game, controller, level="level1"):
    if level == "level1":
        await show_womens_day_screen(game, controller)
        board = Board('data/level1.txt')
        gate_location = (285, 128)
        plate_locations = [(190, 168), (390, 168)]
        gate = Gates(gate_location, plate_locations)
        gates = [gate]
        fire_door = FireDoor((64, 48))
        water_door = WaterDoor((128, 48))
        doors = [fire_door, water_door]
        magma_boy = MagmaBoy((16, 336))
        hydro_girl = HydroGirl((35, 336))

    elif level == "level2":
        await lps_screen(game, controller)
        board = Board('data/level2.txt')
        gates = []
        fire_door = FireDoor((390, 48))
        water_door = WaterDoor((330, 48))
        doors = [fire_door, water_door]
        magma_boy = MagmaBoy((16, 336))
        hydro_girl = HydroGirl((35, 336))

    elif level == "level4":
        await ily_screen(game, controller)
        board = Board('data/level4.txt')
        gates = []
        fire_door = FireDoor((192, 240))
        water_door = WaterDoor((228, 240))
        doors = [fire_door, water_door]
        magma_boy = MagmaBoy((16, 336))
        hydro_girl = HydroGirl((35, 336))

    elif level == "level5":
        await show_gucci_warning(game, controller)
        board = Board('data/level5.txt')
        gates = []
        fire_door = FireDoor((96, 48))
        water_door = WaterDoor((432, 48))
        doors = [fire_door, water_door]
        magma_boy = MagmaBoy((16, 336))
        hydro_girl = HydroGirl((35, 336))

    else: # level3 varsayılan
        board = Board('data/level3.txt')
        gates = []
        fire_door = FireDoor((5 * 16, 4 * 16))
        water_door = WaterDoor((28 * 16, 4 * 16))
        doors = [fire_door, water_door]
        magma_boy = MagmaBoy((28 * 16, 4 * 16))
        hydro_girl = HydroGirl((5 * 16, 4 * 16))

    arrows_controller = ArrowsController()
    wasd_controller = WASDController()
    clock = pygame.time.Clock()
    show_touch_controls = False

    while True:
        clock.tick(60)
        events = pygame.event.get()
        game.draw_level_background(board)
        game.draw_board(board)
        if gates:
            game.draw_gates(gates)
        game.draw_doors(doors)
        game.draw_player([magma_boy, hydro_girl])

        arrows_controller.control_player(events, magma_boy)
        wasd_controller.control_player(events, hydro_girl)
        game.move_player(board, gates, [magma_boy, hydro_girl])
        game.check_for_death(board, [magma_boy, hydro_girl])
        game.check_for_gate_press(gates, [magma_boy, hydro_girl])
        game.check_for_door_open(fire_door, magma_boy)
        game.check_for_door_open(water_door, hydro_girl)

        game.refresh_window()

        if hydro_girl.is_dead() or magma_boy.is_dead():
            await show_death_screen(game, controller, level)

        if game.level_is_done(doors):
            if level == "level5":
                await show_gucci_win_screen(game, controller)
            else:
                await show_win_screen(game, controller)

        if controller.press_key(events, K_ESCAPE):
            await show_level_screen(game, controller)

        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        await asyncio.sleep(0)

if __name__ == '__main__':
    asyncio.run(main())