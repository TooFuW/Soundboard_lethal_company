import pygame

def action_click(button):
    global son_actuel, play_sound
    match button.text:
        case "Back":
            game_state.state = game_state.previous_state
        case "Jester":
            game_state.previous_state = game_state.state
            game_state.state = "jester"
        case "Ghost girl":
            game_state.previous_state = game_state.state
            game_state.state = "ghostgirl"
        case "Jester music":
            try:
                son_actuel.stop()
            except:
                pass
            play_sound = True
            son_actuel = jester_music_sound
        case "Jester stomp 1":
            try:
                son_actuel.stop()
            except:
                pass
            play_sound = True
            son_actuel = jester_stomp1_sound
        case "Jester stomp 2":
            try:
                son_actuel.stop()
            except:
                pass
            play_sound = True
            son_actuel = jester_stomp2_sound
        case "Jester stomp 3":
            try:
                son_actuel.stop()
            except:
                pass
            play_sound = True
            son_actuel = jester_stomp3_sound
        case "Jester turncranck 1":
            try:
                son_actuel.stop()
            except:
                pass
            play_sound = True
            son_actuel = jester_turncranck1_sound
        case "Jester turncranck 2":
            try:
                son_actuel.stop()
            except:
                pass
            play_sound = True
            son_actuel = jester_turncranck2_sound
        case "Jester turncranck 3":
            try:
                son_actuel.stop()
            except:
                pass
            play_sound = True
            son_actuel = jester_turncranck3_sound
        case "Jester pop":
            try:
                son_actuel.stop()
            except:
                pass
            play_sound = True
            son_actuel = jester_pop_sound
        case "Ghost girl breathe 1":
            try:
                son_actuel.stop()
            except:
                pass
            play_sound = True
            son_actuel = ghostgirl_breathe1_sound
        case "Ghost girl breathe 2":
            try:
                son_actuel.stop()
            except:
                pass
            play_sound = True
            son_actuel = ghostgirl_breathe2_sound
        case "Ghost girl laugh":
            try:
                son_actuel.stop()
            except:
                pass
            play_sound = True
            son_actuel = ghostgirl_laugh_sound
        case "Ghost girl laugh":
            try:
                son_actuel.stop()
            except:
                pass
            play_sound = True
            son_actuel = ghostgirl_laugh_sound
        case "Ghost girl skipwalk 1":
            try:
                son_actuel.stop()
            except:
                pass
            play_sound = True
            son_actuel = ghostgirl_skipwalk1_sound
        case "Ghost girl skipwalk 2":
            try:
                son_actuel.stop()
            except:
                pass
            play_sound = True
            son_actuel = ghostgirl_skipwalk2_sound
        case "Ghost girl skipwalk 3":
            try:
                son_actuel.stop()
            except:
                pass
            play_sound = True
            son_actuel = ghostgirl_skipwalk3_sound
        case "Ghost girl voicecry 1":
            try:
                son_actuel.stop()
            except:
                pass
            play_sound = True
            son_actuel = ghostgirl_voicecry1_sound
        case "Ghost girl voicecry 2":
            try:
                son_actuel.stop()
            except:
                pass
            play_sound = True
            son_actuel = ghostgirl_voicecry2_sound
        case "Ghost girl voicehey":
            try:
                son_actuel.stop()
            except:
                pass
            play_sound = True
            son_actuel = ghostgirl_voicehey_sound

class Button:

    def __init__(self, rect : pygame.Rect, text : str):
        self.rect = rect
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
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
                self.is_pressing = True
            else:
                if self.pressed:
                    self.pressed = False
                    action_click(self)
                self.is_pressing = False
        else:
            self.pressed = False
        if not pygame.mouse.get_pressed()[0]:
            self.is_pressing = False

class Hud_state:

    def __init__(self):
        self.previous_state = "accueil"
        self.state = "accueil"

    def accueil(self):
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), nav_bar)

        jester.draw()
        ghostgirl.draw()

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

    def state_manager(self):
        """state_manager se charge d'afficher la bonne interface en fonction de l'état de self.state
        """
        match self.state:
            case "accueil":
                self.accueil()
            case "jester":
                self.jester()
            case "ghostgirl":
                self.ghost_girl()

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

# Chargement des sons
# Jester
jester_music_sound = pygame.mixer.Sound(f"{current_folder}jester_sounds\music.mp3")
jester_stomp1_sound = pygame.mixer.Sound(f"{current_folder}jester_sounds\stomp1.mp3")
jester_stomp2_sound = pygame.mixer.Sound(f"{current_folder}jester_sounds\stomp2.mp3")
jester_stomp3_sound = pygame.mixer.Sound(f"{current_folder}jester_sounds\stomp3.mp3")
jester_turncranck1_sound = pygame.mixer.Sound(f"{current_folder}jester_sounds\\turncranck1.mp3")
jester_turncranck2_sound = pygame.mixer.Sound(f"{current_folder}jester_sounds\\turncranck2.mp3")
jester_turncranck3_sound = pygame.mixer.Sound(f"{current_folder}jester_sounds\\turncranck3.mp3")
jester_pop_sound = pygame.mixer.Sound(f"{current_folder}jester_sounds\pop.mp3")
# Ghost girl
ghostgirl_breathe1_sound = pygame.mixer.Sound(f"{current_folder}ghostgirl_sounds\\breathe1.mp3")
ghostgirl_breathe2_sound = pygame.mixer.Sound(f"{current_folder}ghostgirl_sounds\\breathe2.mp3")
ghostgirl_laugh_sound = pygame.mixer.Sound(f"{current_folder}ghostgirl_sounds\laugh.mp3")
ghostgirl_skipwalk1_sound = pygame.mixer.Sound(f"{current_folder}ghostgirl_sounds\skipwalk1.mp3")
ghostgirl_skipwalk2_sound = pygame.mixer.Sound(f"{current_folder}ghostgirl_sounds\skipwalk2.mp3")
ghostgirl_skipwalk3_sound = pygame.mixer.Sound(f"{current_folder}ghostgirl_sounds\skipwalk3.mp3")
ghostgirl_voicecry1_sound = pygame.mixer.Sound(f"{current_folder}ghostgirl_sounds\\voicecry1.mp3")
ghostgirl_voicecry2_sound = pygame.mixer.Sound(f"{current_folder}ghostgirl_sounds\\voicecry2.mp3")
ghostgirl_voicehey_sound = pygame.mixer.Sound(f"{current_folder}ghostgirl_sounds\\voicehey.mp3")

# Boutons catégories
back_button = Button(pygame.Rect(10, 5, 185, 40), "Back")
jester = Button(pygame.Rect(10, 55, 185, 50), "Jester")
ghostgirl = Button(pygame.Rect(205, 55, 185, 50), "Ghost girl")
# Boutons sons
# Jester
jester_music = Button(pygame.Rect(10, 55, 185, 50), "Jester music")
jester_stomp1 = Button(pygame.Rect(205, 55, 185, 50), "Jester stomp 1")
jester_stomp2 = Button(pygame.Rect(10, 115, 185, 50), "Jester stomp 2")
jester_stomp3 = Button(pygame.Rect(205, 115, 185, 50), "Jester stomp 3")
jester_turncranck1 = Button(pygame.Rect(10, 175, 185, 50), "Jester turncranck 1")
jester_turncranck2 = Button(pygame.Rect(205, 175, 185, 50), "Jester turncranck 2")
jester_turncranck3 = Button(pygame.Rect(10, 235, 185, 50), "Jester turncranck 3")
jester_pop = Button(pygame.Rect(205, 235, 185, 50), "Jester pop")
# Ghost girl
ghostgirl_breathe1 = Button(pygame.Rect(10, 55, 185, 50), "Ghost girl breathe 1")
ghostgirl_breathe2 = Button(pygame.Rect(205, 55, 185, 50), "Ghost girl breathe 2")
ghostgirl_laugh = Button(pygame.Rect(10, 115, 185, 50), "Ghost girl laugh")
ghostgirl_skipwalk1 = Button(pygame.Rect(205, 115, 185, 50), "Ghost girl skipwalk 1")
ghostgirl_skipwalk2 = Button(pygame.Rect(10, 175, 185, 50), "Ghost girl skipwalk 2")
ghostgirl_skipwalk3 = Button(pygame.Rect(205, 175, 185, 50), "Ghost girl skipwalk 3")
ghostgirl_voicecry1 = Button(pygame.Rect(10, 235, 185, 50), "Ghost girl voicecry 1")
ghostgirl_voicecry2 = Button(pygame.Rect(205, 235, 185, 50), "Ghost girl voicecry 2")
ghostgirl_voicehey = Button(pygame.Rect(10, 295, 185, 50), "Ghost girl voicehey")

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