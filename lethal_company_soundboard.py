import pygame
from icecream import ic

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

        jester.draw()
        ghostgirl.draw()
        bunkerspider.draw()
        coilhead.draw()
        thumper.draw()

        pygame.display.flip()

    def jester(self):
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), nav_bar)
        back_button.draw()

        jester_music.draw()
        jester_stomp1.draw()
        jester_stomp2.draw()
        jester_stomp3.draw()
        jester_turncranck1.draw()
        jester_turncranck2.draw()
        jester_turncranck3.draw()
        jester_pop.draw()

        pygame.display.flip()

    def ghost_girl(self):
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), nav_bar)
        back_button.draw()

        ghostgirl_breathe1.draw()
        ghostgirl_breathe2.draw()
        ghostgirl_laugh.draw()
        ghostgirl_skipwalk1.draw()
        ghostgirl_skipwalk2.draw()
        ghostgirl_skipwalk3.draw()
        ghostgirl_voicecry1.draw()
        ghostgirl_voicecry2.draw()
        ghostgirl_voicehey.draw()
        
        pygame.display.flip()

    def bunker_spider(self):
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), nav_bar)
        back_button.draw()

        bunkerspider_breakweb.draw()
        bunkerspider_spiderattack.draw()
        bunkerspider_spiderdie.draw()
        bunkerspider_spiderhit.draw()
        
        pygame.display.flip()
        
    def coil_head(self):
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), nav_bar)
        back_button.draw()

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

        thumper_biteplayer.draw()
        thumper_crawlerdie.draw()
        thumper_hitcrawler.draw()
        thumper_longroar1.draw()
        thumper_longroar2.draw()
        thumper_longroar3.draw()
        thumper_shortroar.draw()
        thumper_stomp1.draw()
        thumper_stomp2.draw()
        thumper_stuncrawler.draw()
        
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
background = pygame.image.load(f"{current_folder}lethal-company_35w1.jpg")
background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))

# Boutons catégories
back_button = Button(pygame.Rect(10, 5, 185, 40), "Back")
jester = Button(pygame.Rect(10, 55, 185, 50), "Jester")
ghostgirl = Button(pygame.Rect(205, 55, 185, 50), "Ghost girl")
bunkerspider = Button(pygame.Rect(10, 115, 185, 50), "Bunker spider")
coilhead = Button(pygame.Rect(205, 115, 185, 50), "Coil head")
thumper = Button(pygame.Rect(10, 175, 185, 50), "Thumper")
# Boutons sons
# Jester
jester_music = Button(pygame.Rect(10, 55, 185, 50), "Jester music", f"{current_folder}jester_sounds\music.mp3")
jester_stomp1 = Button(pygame.Rect(205, 55, 185, 50), "Jester stomp 1", f"{current_folder}jester_sounds\stomp1.mp3")
jester_stomp2 = Button(pygame.Rect(10, 115, 185, 50), "Jester stomp 2", f"{current_folder}jester_sounds\stomp2.mp3")
jester_stomp3 = Button(pygame.Rect(205, 115, 185, 50), "Jester stomp 3", f"{current_folder}jester_sounds\stomp3.mp3")
jester_turncranck1 = Button(pygame.Rect(10, 175, 185, 50), "Jester turncranck 1", f"{current_folder}jester_sounds\\turncranck1.mp3")
jester_turncranck2 = Button(pygame.Rect(205, 175, 185, 50), "Jester turncranck 2", f"{current_folder}jester_sounds\\turncranck2.mp3")
jester_turncranck3 = Button(pygame.Rect(10, 235, 185, 50), "Jester turncranck 3", f"{current_folder}jester_sounds\\turncranck3.mp3")
jester_pop = Button(pygame.Rect(205, 235, 185, 50), "Jester pop", f"{current_folder}jester_sounds\pop.mp3")
# Ghost girl
ghostgirl_breathe1 = Button(pygame.Rect(10, 55, 185, 50), "Ghost girl breathe 1", f"{current_folder}ghostgirl_sounds\\breathe1.mp3")
ghostgirl_breathe2 = Button(pygame.Rect(205, 55, 185, 50), "Ghost girl breathe 2", f"{current_folder}ghostgirl_sounds\\breathe2.mp3")
ghostgirl_laugh = Button(pygame.Rect(10, 115, 185, 50), "Ghost girl laugh", f"{current_folder}ghostgirl_sounds\laugh.mp3")
ghostgirl_skipwalk1 = Button(pygame.Rect(205, 115, 185, 50), "Ghost girl skipwalk 1", f"{current_folder}ghostgirl_sounds\skipwalk1.mp3")
ghostgirl_skipwalk2 = Button(pygame.Rect(10, 175, 185, 50), "Ghost girl skipwalk 2", f"{current_folder}ghostgirl_sounds\skipwalk2.mp3")
ghostgirl_skipwalk3 = Button(pygame.Rect(205, 175, 185, 50), "Ghost girl skipwalk 3", f"{current_folder}ghostgirl_sounds\skipwalk3.mp3")
ghostgirl_voicecry1 = Button(pygame.Rect(10, 235, 185, 50), "Ghost girl voicecry 1", f"{current_folder}ghostgirl_sounds\\voicecry1.mp3")
ghostgirl_voicecry2 = Button(pygame.Rect(205, 235, 185, 50), "Ghost girl voicecry 2", f"{current_folder}ghostgirl_sounds\\voicecry2.mp3")
ghostgirl_voicehey = Button(pygame.Rect(10, 295, 185, 50), "Ghost girl voicehey", f"{current_folder}ghostgirl_sounds\\voicehey.mp3")
# Bunker spider
bunkerspider_breakweb = Button(pygame.Rect(10, 55, 185, 50), "Spider breakweb", f"{current_folder}bunkerspider_sounds\\breakweb.mp3")
bunkerspider_spiderattack = Button(pygame.Rect(205, 55, 185, 50), "Spider attack", f"{current_folder}bunkerspider_sounds\spiderattack.mp3")
bunkerspider_spiderdie = Button(pygame.Rect(10, 115, 185, 50), "Spider die", f"{current_folder}bunkerspider_sounds\spiderdie.mp3")
bunkerspider_spiderhit = Button(pygame.Rect(205, 115, 185, 50), "Spider hit", f"{current_folder}bunkerspider_sounds\spiderhit.mp3")
# Coil head
coilhead_footstep = Button(pygame.Rect(10, 55, 185, 50), "Coil head footstep", f"{current_folder}coilhead_sounds\\footstep.mp3")
coilhead_kill = Button(pygame.Rect(205, 55, 185, 50), "Coil head kill", f"{current_folder}coilhead_sounds\kill.mp3")
coilhead_spring1 = Button(pygame.Rect(10, 115, 185, 50), "Coil head spring 1", f"{current_folder}coilhead_sounds\spring1.mp3")
coilhead_spring2 = Button(pygame.Rect(205, 115, 185, 50), "Coil head spring 2", f"{current_folder}coilhead_sounds\spring2.mp3")
coilhead_spring3 = Button(pygame.Rect(10, 175, 185, 50), "Coil head spring 3", f"{current_folder}coilhead_sounds\spring3.mp3")
coilhead_springwobble1 = Button(pygame.Rect(205, 175, 185, 50), "Coil head wobble 1", f"{current_folder}coilhead_sounds\springwobble1.mp3")
coilhead_springwobble2 = Button(pygame.Rect(10, 235, 185, 50), "Coil head wobble 2", f"{current_folder}coilhead_sounds\springwobble2.mp3")
#Thumper
thumper_biteplayer = Button(pygame.Rect(10, 55, 185, 50), "Thumper bite player", f"{current_folder}thumper_sounds\\biteplayer.mp3")
thumper_crawlerdie = Button(pygame.Rect(205, 55, 185, 50), "Thumper crawler die", f"{current_folder}thumper_sounds\crawlerdie.mp3")
thumper_hitcrawler = Button(pygame.Rect(10, 115, 185, 50), "Thumper hit crawler", f"{current_folder}thumper_sounds\hitcrawler.mp3")
thumper_longroar1 = Button(pygame.Rect(205, 115, 185, 50), "Thumper long roar 1", f"{current_folder}thumper_sounds\longroar1.mp3")
thumper_longroar2 = Button(pygame.Rect(10, 175, 185, 50), "Thumper long roar 2", f"{current_folder}thumper_sounds\longroar2.mp3")
thumper_longroar3 = Button(pygame.Rect(205, 175, 185, 50), "Thumper long roar 3", f"{current_folder}thumper_sounds\longroar3.mp3")
thumper_shortroar = Button(pygame.Rect(10, 235, 185, 50), "Thumper short roar", f"{current_folder}thumper_sounds\shortroar.mp3")
thumper_stomp1 = Button(pygame.Rect(205, 235, 185, 50), "Thumper stomp 1", f"{current_folder}thumper_sounds\stomp1.mp3")
thumper_stomp2 = Button(pygame.Rect(10, 295, 185, 50), "Thumper stomp 2", f"{current_folder}thumper_sounds\stomp2.mp3")
thumper_stuncrawler = Button(pygame.Rect(205, 295, 185, 50), "Thumper stun crawler", f"{current_folder}thumper_sounds\stuncrawler.mp3")

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