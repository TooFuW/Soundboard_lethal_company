import pygame

class Button:

    def __init__(self, rect : tuple, text : str, son : str = None):
        self.rect = pygame.Rect(rect)
        if son != None:
            self.son = pygame.mixer.Sound(son)
        else:
            self.son = son
        self.text = text
        gui_font = pygame.font.SysFont("Roboto", 25)
        self.text_surf = gui_font.render(text, True, (255, 255, 255))
        self.text_rect = self.text_surf.get_rect(center = self.rect.center)
        self.pressed = False
        self.is_pressing = False

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), self.rect, border_radius=10)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2, 10)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()
    
    def check_click(self):
        global son_actuel, play_sound
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
                self.is_pressing = True
            else:
                if self.pressed:
                    self.pressed = False
                    if self.son is not None:
                        try:
                            son_actuel.stop()
                        except:
                            pass
                        play_sound = True
                        son_actuel = self.son
                    else:
                        if self.text == "Back":
                            game_state.state = game_state.previous_state
                        elif self.text == "Stop sound":
                            try:
                                son_actuel.stop()
                            except:
                                pass
                        else:
                            game_state.previous_state = game_state.state
                            game_state.state = self.text
                self.is_pressing = False
        else:
            self.pressed = False
        if not pygame.mouse.get_pressed()[0]:
            self.is_pressing = False

class Hud_state:

    def __init__(self):
        self.previous_state = "Accueil"
        self.state = "Accueil"

    def accueil(self):
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), nav_bar)
        stop_sound_button.draw()

        jester.draw()
        ghostgirl.draw()
        bunkerspider.draw()
        coilhead.draw()
        thumper.draw()
        eyelessdog.draw()
        turret.draw()
        landmine.draw()
        bracken.draw()
        forestkeeper.draw()
        lootbug.draw()

        pygame.display.flip()

    def jester(self):
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), nav_bar)
        back_button.draw()
        stop_sound_button.draw()

        jester_music.draw()
        jester_stomp.draw()
        jester_turncranck.draw()
        jester_pop.draw()

        pygame.display.flip()

    def ghost_girl(self):
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), nav_bar)
        back_button.draw()
        stop_sound_button.draw()

        ghostgirl_breathe1.draw()
        ghostgirl_breathe2.draw()
        ghostgirl_laugh.draw()
        ghostgirl_longskipwalk.draw()
        ghostgirl_shortskipwalk.draw()
        ghostgirl_voicecry1.draw()
        ghostgirl_voicecry2.draw()
        ghostgirl_voicehey.draw()
        
        pygame.display.flip()

    def bunker_spider(self):
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), nav_bar)
        back_button.draw()
        stop_sound_button.draw()

        bunkerspider_breakweb.draw()
        bunkerspider_spiderattack.draw()
        bunkerspider_spiderdie.draw()
        bunkerspider_spiderhit.draw()
        
        pygame.display.flip()
        
    def coil_head(self):
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), nav_bar)
        back_button.draw()
        stop_sound_button.draw()

        coilhead_footstep.draw()
        coilhead_kill.draw()
        coilhead_spring1.draw()
        coilhead_spring2.draw()
        coilhead_spring3.draw()
        coilhead_springwobble1.draw()
        coilhead_springwobble2.draw()
        
        pygame.display.flip()
        
    def thumper(self):
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), nav_bar)
        back_button.draw()
        stop_sound_button.draw()

        thumper_biteplayer.draw()
        thumper_crawlerdie.draw()
        thumper_hitcrawler.draw()
        thumper_longroar.draw()
        thumper_shortroar.draw()
        thumper_stomp.draw()
        thumper_stun.draw()
        
        pygame.display.flip()
        
    def eyeless_dog(self):
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), nav_bar)
        back_button.draw()
        stop_sound_button.draw()

        eyelessdog_killplayer.draw()
        eyelessdog_roar.draw()
        eyelessdog_stomp.draw()
        eyelessdog_stun.draw()
        
        pygame.display.flip()
        
    def turret(self):
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), nav_bar)
        back_button.draw()
        stop_sound_button.draw()

        turret_activate.draw()
        turret_bersekmode.draw()
        turret_desactivate.draw()
        turret_fire.draw()
        turret_firedistance.draw()
        turret_seeplayer.draw()
        turret_wallhits.draw()
        
        pygame.display.flip()
        
    def landmine(self):
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), nav_bar)
        back_button.draw()
        stop_sound_button.draw()

        landime_beep.draw()
        landmine_detonate.draw()
        landmine_detonatedistance.draw()
        landmine_press.draw()
        landmine_trigger.draw()
        
        pygame.display.flip()
        
    def bracken(self):
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), nav_bar)
        back_button.draw()
        stop_sound_button.draw()

        bracken_angered.draw()
        bracken_crackneck.draw()
        bracken_stun.draw()
        
        pygame.display.flip()
        
    def forest_keeper(self):
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), nav_bar)
        back_button.draw()
        stop_sound_button.draw()

        forestkeeper_eatplayer.draw()
        forestkeeper_stomp.draw()
        forestkeeper_stun.draw()
        
        pygame.display.flip()
        
    def loot_bug(self):
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), nav_bar)
        back_button.draw()
        stop_sound_button.draw()

        lootbug_angryscreech1.draw()
        lootbug_angryscreech2.draw()
        lootbug_cry.draw()
        lootbug_die.draw()
        lootbug_fly.draw()
        lootbug_walk.draw()
        
        pygame.display.flip()

    def state_manager(self):
        """state_manager se charge d'afficher la bonne interface en fonction de l'état de self.state
        """
        match self.state:
            case "Accueil":
                self.accueil()
            case "Jester":
                self.jester()
            case "Ghost girl":
                self.ghost_girl()
            case "Bunker spider":
                self.bunker_spider()
            case "Coil head":
                self.coil_head()
            case "Thumper":
                self.thumper()
            case "Eyeless dog":
                self.eyeless_dog()
            case "Turret":
                self.turret()
            case "Landmine":
                self.landmine()
            case "Bracken":
                self.bracken()
            case "Forest keeper":
                self.forest_keeper()
            case "Loot bug":
                self.loot_bug()

# pygame setup
pygame.init()
screen_info = pygame.display.Info()
screen = pygame.display.set_mode((400, 800), pygame.SCALED|pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
game_state = Hud_state()
nav_bar = pygame.Rect(0, 0, screen.get_width(), 50)
son_actuel = None
play_sound = False

# Chargement des images
current_folder = __file__[:-28]
background = pygame.image.load(f"{current_folder}lethal_company.jpg")
background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))

# Boutons catégories
stop_sound_button = Button(pygame.Rect(10, 5, 185, 40), "Stop sound")
back_button = Button(pygame.Rect(205, 5, 185, 40), "Back")
jester = Button(pygame.Rect(10, 55, 185, 50), "Jester")
ghostgirl = Button(pygame.Rect(205, 55, 185, 50), "Ghost girl")
bunkerspider = Button(pygame.Rect(10, 115, 185, 50), "Bunker spider")
coilhead = Button(pygame.Rect(205, 115, 185, 50), "Coil head")
thumper = Button(pygame.Rect(10, 175, 185, 50), "Thumper")
eyelessdog = Button(pygame.Rect(205, 175, 185, 50), "Eyeless dog")
turret= Button(pygame.Rect(10, 235, 185, 50), "Turret")
landmine = Button(pygame.Rect(205, 235, 185, 50), "Landmine")
bracken = Button(pygame.Rect(10, 295, 185, 50), "Bracken")
forestkeeper = Button(pygame.Rect(205, 295, 185, 50), "Forest keeper")
lootbug = Button(pygame.Rect(10, 355, 185, 50), "Loot bug")
# Boutons sons
# Jester
jester_music = Button(pygame.Rect(10, 55, 380, 50), "Jester music", f"{current_folder}jester_sounds\music.mp3")
jester_stomp = Button(pygame.Rect(10, 115, 380, 50), "Jester stomp", f"{current_folder}jester_sounds\stomp.mp3")
jester_turncranck = Button(pygame.Rect(10, 175, 380, 50), "Jester turncranck", f"{current_folder}jester_sounds\\turncranck.mp3")
jester_pop = Button(pygame.Rect(10, 235, 380, 50), "Jester pop", f"{current_folder}jester_sounds\pop.mp3")
# Ghost girl
ghostgirl_breathe1 = Button(pygame.Rect(10, 55, 380, 50), "Ghost girl breathe 1", f"{current_folder}ghostgirl_sounds\\breathe1.mp3")
ghostgirl_breathe2 = Button(pygame.Rect(10, 115, 380, 50), "Ghost girl breathe 2", f"{current_folder}ghostgirl_sounds\\breathe2.mp3")
ghostgirl_laugh = Button(pygame.Rect(10, 175, 380, 50), "Ghost girl laugh", f"{current_folder}ghostgirl_sounds\laugh.mp3")
ghostgirl_longskipwalk = Button(pygame.Rect(10, 235, 380, 50), "Ghost girl long skipwalk", f"{current_folder}ghostgirl_sounds\longskipwalk.mp3")
ghostgirl_shortskipwalk = Button(pygame.Rect(10, 295, 380, 50), "Ghost girl short skipwalk", f"{current_folder}ghostgirl_sounds\shortskipwalk.mp3")
ghostgirl_voicecry1 = Button(pygame.Rect(10, 355, 380, 50), "Ghost girl voicecry 1", f"{current_folder}ghostgirl_sounds\\voicecry1.mp3")
ghostgirl_voicecry2 = Button(pygame.Rect(10, 415, 380, 50), "Ghost girl voicecry 2", f"{current_folder}ghostgirl_sounds\\voicecry2.mp3")
ghostgirl_voicehey = Button(pygame.Rect(10, 475, 380, 50), "Ghost girl voicehey", f"{current_folder}ghostgirl_sounds\\voicehey.mp3")
# Bunker spider
bunkerspider_breakweb = Button(pygame.Rect(10, 55, 380, 50), "Spider breakweb", f"{current_folder}bunkerspider_sounds\\breakweb.mp3")
bunkerspider_spiderattack = Button(pygame.Rect(10, 115, 380, 50), "Spider attack", f"{current_folder}bunkerspider_sounds\spiderattack.mp3")
bunkerspider_spiderdie = Button(pygame.Rect(10, 175, 380, 50), "Spider die", f"{current_folder}bunkerspider_sounds\spiderdie.mp3")
bunkerspider_spiderhit = Button(pygame.Rect(10, 235, 380, 50), "Spider hit", f"{current_folder}bunkerspider_sounds\spiderhit.mp3")
# Coil head
coilhead_footstep = Button(pygame.Rect(10, 55, 380, 50), "Coil head footstep", f"{current_folder}coilhead_sounds\\footstep.mp3")
coilhead_kill = Button(pygame.Rect(10, 115, 380, 50), "Coil head kill", f"{current_folder}coilhead_sounds\kill.mp3")
coilhead_spring1 = Button(pygame.Rect(10, 175, 380, 50), "Coil head spring 1", f"{current_folder}coilhead_sounds\spring1.mp3")
coilhead_spring2 = Button(pygame.Rect(10, 235, 380, 50), "Coil head spring 2", f"{current_folder}coilhead_sounds\spring2.mp3")
coilhead_spring3 = Button(pygame.Rect(10, 295, 380, 50), "Coil head spring 3", f"{current_folder}coilhead_sounds\spring3.mp3")
coilhead_springwobble1 = Button(pygame.Rect(10, 355, 380, 50), "Coil head wobble 1", f"{current_folder}coilhead_sounds\springwobble1.mp3")
coilhead_springwobble2 = Button(pygame.Rect(10, 415, 380, 50), "Coil head wobble 2", f"{current_folder}coilhead_sounds\springwobble2.mp3")
# Thumper
thumper_biteplayer = Button(pygame.Rect(10, 55, 380, 50), "Thumper bite player", f"{current_folder}thumper_sounds\\biteplayer.mp3")
thumper_crawlerdie = Button(pygame.Rect(10, 115, 380, 50), "Thumper crawler die", f"{current_folder}thumper_sounds\crawlerdie.mp3")
thumper_hitcrawler = Button(pygame.Rect(10, 175, 380, 50), "Thumper hit crawler", f"{current_folder}thumper_sounds\hitcrawler.mp3")
thumper_longroar = Button(pygame.Rect(10, 235, 380, 50), "Thumper long roar", f"{current_folder}thumper_sounds\longroar.mp3")
thumper_shortroar = Button(pygame.Rect(10, 295, 380, 50), "Thumper short roar", f"{current_folder}thumper_sounds\shortroar.mp3")
thumper_stomp = Button(pygame.Rect(10, 355, 380, 50), "Thumper stomp", f"{current_folder}thumper_sounds\stomp.mp3")
thumper_stun = Button(pygame.Rect(10, 415, 380, 50), "Thumper stuned", f"{current_folder}thumper_sounds\stun.mp3")
# Eyeless dog
eyelessdog_killplayer = Button(pygame.Rect(10, 55, 380, 50), "Eyeless dog kill player", f"{current_folder}eyelessdog_sounds\killplayer.mp3")
eyelessdog_roar = Button(pygame.Rect(10, 115, 380, 50), "Eyeless dog roar", f"{current_folder}eyelessdog_sounds\\roar.mp3")
eyelessdog_stomp = Button(pygame.Rect(10, 175, 380, 50), "Eyeless dog stomp", f"{current_folder}eyelessdog_sounds\stomp.mp3")
eyelessdog_stun = Button(pygame.Rect(10, 235, 380, 50), "Eyeless dog stuned", f"{current_folder}eyelessdog_sounds\stun.mp3")
# Turret
turret_activate = Button(pygame.Rect(10, 55, 380, 50), "Turret activate", f"{current_folder}turret_sounds\\activate.mp3")
turret_bersekmode = Button(pygame.Rect(10, 115, 380, 50), "Turret bersek Mode", f"{current_folder}turret_sounds\\bersekmode.mp3")
turret_desactivate = Button(pygame.Rect(10, 175, 380, 50), "Turret desactivate", f"{current_folder}turret_sounds\desactivate.mp3")
turret_fire = Button(pygame.Rect(10, 235, 380, 50), "Turret fire", f"{current_folder}turret_sounds\\fire.mp3")
turret_firedistance = Button(pygame.Rect(10, 295, 380, 50), "Turret fire distance", f"{current_folder}turret_sounds\\firedistance.mp3")
turret_seeplayer = Button(pygame.Rect(10, 355, 380, 50), "Turret see player", f"{current_folder}turret_sounds\seeplayer.mp3")
turret_wallhits = Button(pygame.Rect(10, 415, 380, 50), "Turret wall hits", f"{current_folder}turret_sounds\wallhits.mp3")
# Landmine
landime_beep = Button(pygame.Rect(10, 55, 380, 50), "Landmine beep", f"{current_folder}landmine_sounds\\beep.mp3")
landmine_detonate = Button(pygame.Rect(10, 55, 380, 50), "Landmine detonate", f"{current_folder}landmine_sounds\detonate.mp3")
landmine_detonatedistance = Button(pygame.Rect(10, 115, 380, 50), "Landmine detonate distance", f"{current_folder}landmine_sounds\detonatedistance.mp3")
landmine_press = Button(pygame.Rect(10, 115, 380, 50), "Landmine press", f"{current_folder}landmine_sounds\press.mp3")
landmine_trigger = Button(pygame.Rect(10, 175, 380, 50), "Landmine trigger", f"{current_folder}landmine_sounds\\trigger.mp3")
# Bracken
bracken_angered = Button(pygame.Rect(10, 55, 380, 50), "Bracken angered", f"{current_folder}bracken_sounds\\angered.mp3")
bracken_crackneck = Button(pygame.Rect(10, 55, 380, 50), "Bracken crackneck", f"{current_folder}bracken_sounds\crackneck.mp3")
bracken_stun = Button(pygame.Rect(10, 115, 380, 50), "Bracken stun", f"{current_folder}bracken_sounds\stun.mp3")
# Forest keeper
forestkeeper_eatplayer = Button(pygame.Rect(10, 55, 380, 50), "Forest keeper eat player", f"{current_folder}forestkeeper_sounds\eatplayer.mp3")
forestkeeper_stomp = Button(pygame.Rect(10, 55, 380, 50), "Forest keeper stomp", f"{current_folder}forestkeeper_sounds\stomp.mp3")
forestkeeper_stun = Button(pygame.Rect(10, 235, 380, 50), "Forest keeper stun", f"{current_folder}forestkeeper_sounds\stun.mp3")
# Loot bug
lootbug_angryscreech1 = Button(pygame.Rect(10, 55, 380, 50), "Loot bug angry screech 1", f"{current_folder}lootbug_sounds\\angryscreech1.mp3")
lootbug_angryscreech2 = Button(pygame.Rect(10, 55, 380, 50), "Loot bug angry screech 2", f"{current_folder}lootbug_sounds\\angryscreech2.mp3")
lootbug_cry = Button(pygame.Rect(10, 115, 380, 50), "Loot bug cry", f"{current_folder}lootbug_sounds\cry.mp3")
lootbug_die = Button(pygame.Rect(10, 115, 380, 50), "Loot bug die", f"{current_folder}lootbug_sounds\die.mp3")
lootbug_fly = Button(pygame.Rect(10, 175, 380, 50), "Loot bug fly", f"{current_folder}lootbug_sounds\\fly.mp3")
lootbug_walk = Button(pygame.Rect(10, 175, 380, 50), "Loot bug walk", f"{current_folder}lootbug_sounds\walk.mp3")

if __name__ == "__main__":
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if play_sound:
            play_sound = False
            son_actuel.play()
        game_state.state_manager()
        clock.tick(120)
    pygame.quit()