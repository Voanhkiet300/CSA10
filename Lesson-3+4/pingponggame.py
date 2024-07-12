import pygame
from classes.ball import Ball
from classes.paddle import Paddle
from classes.player import Player


class Main:
    def __init__(
        self,
        title,
        size,
        bg,
        win_bg,
        lose_bg,
        ball_img_link,
        paddle_img_link,
        ball_speed,
        ball_location,
        paddle_1_location,
        paddle_2_location,
        time,
        end
    ) -> None:
        # setup canvas
        pygame.init()
        pygame.display.set_caption(title)
        self.canvas = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.bg = bg
        self.win_bg = win_bg
        self.lose_bg = lose_bg
        self.ball_img_link = ball_img_link
        self.paddle_img_link = paddle_img_link
        # create objects (player, ball, paddles)
        self.ball = Ball(
            img_url=ball_img_link, speed_x=ball_speed[0], speed_y=ball_speed[1], lose=False
        )
        self.paddle_1 = Paddle(img_url=paddle_img_link)
        self.paddle_2 = Paddle(img_url=paddle_img_link)
        self.player = Player()
        # setup location for objects
        self.ball.setX(x=ball_location[0])
        self.ball.setY(y=ball_location[1])
        self.paddle_1.setX(x=paddle_1_location[0])
        self.paddle_1.setY(y=paddle_1_location[1])
        self.paddle_2.setX(x=paddle_2_location[0])
        self.paddle_2.setY(y=paddle_2_location[1])
        self.time = time
        self.end = end

    def run(self):
        while True:  # play game
            events = pygame.event.get()  # bat su kien
            for e in events:
                # quit
                if e.type == pygame.QUIT:
                    return
                # keyboard check
                elif e.type == pygame.KEYDOWN:  # nhan phim
                    if e.key == pygame.K_w:
                        self.player.setKeyUp1(True)
                    elif e.key == pygame.K_s:
                        self.player.setKeyDown1(True)
                    elif e.key == pygame.K_UP:
                        self.player.setKeyUp2(True)
                    elif e.key == pygame.K_DOWN:
                        self.player.setKeyDown2(True)

                elif e.type == pygame.KEYUP:  # khong nhan phim
                    if e.key == pygame.K_w:
                        self.player.setKeyUp1(False)
                    elif e.key == pygame.K_s:
                        self.player.setKeyDown1(False)
                    elif e.key == pygame.K_UP:
                        self.player.setKeyUp2(False)
                    elif e.key == pygame.K_DOWN:
                        self.player.setKeyDown2(False)

            self.ball.move(
                paddle_1_x=self.paddle_1.getX(),
                paddle_1_y=self.paddle_1.getY(),
                paddle_1_distance= 25,
                paddle_2_x=self.paddle_2.getX(),
                paddle_2_y=self.paddle_2.getY(),
                paddle_2_distance= -18,
            )
        

            # kiem tra nut bam de di chuyen paddles
            if self.player.getKeyUp1():
                self.paddle_1.move(direction=-1, bound_top=0, bound_down=480)
            if self.player.getKeyDown1():
                self.paddle_1.move(1, 0, 480)
            if self.player.getKeyUp2():
                self.paddle_2.move(-1, 0, 480)
            if self.player.getKeyDown2():
                self.paddle_2.move(1, 0, 480)
            
            
            
            if self.end == False:
                # show canvas
                self.canvas.fill(self.bg)
                self.canvas.blit(self.ball.img_url, (self.ball.getX(), self.ball.getY()))
                self.canvas.blit(
                    self.paddle_1.img, (self.paddle_1.getX(), self.paddle_1.getY())
                )
                self.canvas.blit(
                    self.paddle_2.img, (self.paddle_2.getX(), self.paddle_2.getY())
                )
                self.check_lose()
                self.show_time()
                self.time_counter()
                self.clock.tick(60)
            else:
                self.clock.tick(0)


            # update
            pygame.display.flip()

    def time_counter(self):
        self.time -= 1/60
        if self.time < 25:
            self.end = True
            self.win()

    
    def show_time(self):
        if self.time >= 0 and self.ball.lose == False:
            if pygame.font:
                font = pygame.font.Font(None, 36)
                time = font.render(f"time left: {self.time:.0f}", 1, (255, 255, 255))
                self.canvas.blit(time, (2, 2))

    def check_lose(self):
        if self.ball.lose == True:
            self.end = True
            self.lose()

    def win(self):
        self.canvas.fill(self.win_bg)
        if pygame.font:
            font = pygame.font.Font(None, 36)
            text = font.render("You win!", 1, (255, 255, 255))
            self.canvas.blit(text, (260, 280))

    def lose(self):
        self.canvas.fill(self.lose_bg)
        if pygame.font:
            font = pygame.font.Font(None, 36)
            text = font.render("HAHAHAAHA", 1, (255, 255, 255))
            self.canvas.blit(text, (230, 250))
            text = font.render("You lose!", 1, (255, 255, 255))
            self.canvas.blit(text, (260, 280))

        


# Driver code
main = Main(
    title="Ping Pong",
    size=(600, 600),
    bg=(252, 16, 140),
    win_bg = (223, 245, 22),
    lose_bg = (59, 34, 97),
    ball_img_link="Lesson-3+4\\assets\\ball.png",
    paddle_img_link="Lesson-3+4\\assets\\paddle.png",
    ball_location=(285, 300),
    ball_speed=(3, 2.5),
    paddle_1_location=(0, 250),
    paddle_2_location=(570, 250),
    time = 30,
    end = False
)
main.run()