import socket
import pygame

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
main_socket.connect(("localhost", 8080))
pygame.init()
WIDTH = 100
HIGHT = 100
display = pygame.display.set_mode()