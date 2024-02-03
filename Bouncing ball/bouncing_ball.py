# import socket
#
# server_addr = input("What server do you want to connect to? ")
# server_port = int(input("What port is the server on? "))
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect((server_addr, server_port))
# # print all Get requests
#
# print("Connected to server!")
#
#
# import turtle
# import math
#
# # Set key parameters
# gravity = -0.005  # pixels/(time of iteration)^2
# y_velocity = 0.5  # pixels/(time of iteration) - reduced for slower speed
# x_velocity = 0.1  # pixels/(time of iteration) - reduced for slower speed
# energy_loss = 0.95
#
# width = 600
# height = 600
# radius = 150  # radius of the circular boundary
#
# # Set window and ball
# window = turtle.Screen()
# window.setup(width, height)
# window.tracer(0)
#
# # Draw circular boundary
# boundary = turtle.Turtle()
# boundary.penup()
# boundary.color("red")
# boundary.pensize(5)
# boundary.goto(0, -radius)
# boundary.pendown()
# boundary.circle(radius)
#
# ball = turtle.Turtle()
#
# ball.penup()
# ball.color("green")
# ball.shape("circle")
#
# # Main loop
# while True:
#     # Move ball
#     ball.sety(ball.ycor() + y_velocity)
#     ball.setx(ball.xcor() + x_velocity)
#
#     # Acceleration due to gravity
#     y_velocity += gravity
#
#     # Bounce off the ground
#     if ball.ycor() < -height / 2:
#         y_velocity = -y_velocity * energy_loss
#         # Set ball to ground level to avoid it getting "stuck"
#         ball.sety(-height / 2)
#
#     # Bounce off the walls (left and right)
#     if ball.xcor() > width / 2 or ball.xcor() < -width / 2:
#         x_velocity = -x_velocity
#
#     # Bounce off the circular boundary
#     distance_to_center = math.sqrt(ball.xcor()**2 + ball.ycor()**2)
#     if distance_to_center > radius:
#         # Calculate angle of reflection
#         angle = math.atan2(ball.ycor(), ball.xcor())
#         new_angle = math.pi + angle
#         # Set new velocity components
#         speed = math.sqrt(x_velocity**2 + y_velocity**2)
#         x_velocity = math.cos(new_angle) * speed
#         y_velocity = math.sin(new_angle) * speed
#
#     window.update()
import pygame
import sys
import math
import random

# Initialize Pygame and mixer
pygame.init()
pygame.mixer.init()

# Set key parameters
gravity = 0.1
ball_velocity = [2, 2]  # Random initial velocity
ball_position = [300, 300]
ball_radius = 20
max_radius = 200
radius = 200
energy_loss = 0.95
bounce_speed_increase = 0.1  # Set the speed increase factor

width, height = 600, 600

# Set up Pygame window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball")
clock = pygame.time.Clock()

# Set the snippet duration in seconds
snippet_duration = 0.5

# # Load the full song
# pygame.mixer.music.load("zain.mp3")  # Replace with your actual song file

# Track the start time for the song snippet
snippet_start_time = 0
ball_color = (0, 255, 0)
# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move ball
    ball_position[0] += ball_velocity[0]
    ball_position[1] += ball_velocity[1]

    # Acceleration due to gravity
    ball_velocity[1] += gravity

    # Draw background
    screen.fill((0, 0, 0))

    # Draw circular boundary
    pygame.draw.circle(screen, (255, 0, 0), (width // 2, height // 2), radius, 10)

    pygame.draw.circle(screen, ball_color, (int(ball_position[0]), int(ball_position[1])), int(ball_radius))

    # Bounce off the circular boundary
    distance_to_center = math.sqrt((ball_position[0] - width // 2) ** 2 + (ball_position[1] - height // 2) ** 2)
    if distance_to_center > radius - ball_radius:
        angle = math.atan2(ball_position[1] - height // 2, ball_position[0] - width // 2)
        new_angle = math.pi + angle + random.uniform(-0.1, 0.1)  # Add random angle deviation
        speed = math.sqrt(ball_velocity[0] ** 2 + ball_velocity[1] ** 2)
        ball_velocity[0] = math.cos(new_angle) * (speed + bounce_speed_increase)  # Increase speed
        ball_velocity[1] = math.sin(new_angle) * (speed + bounce_speed_increase)  # Increase speed
        print("Bounce!")
        # Draw ball with a random color
        ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if ball_radius < max_radius:
            ball_radius += 1

        # Play the song snippet
        # pygame.mixer.music.play(start=snippet_start_time, fade_ms=0,)
        #
        #
        # # Update the start time for the next snippet
        # snippet_start_time += snippet_duration

    pygame.display.flip()
    clock.tick(60)









