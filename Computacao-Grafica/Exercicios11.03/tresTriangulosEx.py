import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

x = -1.5
y = 0
r = 0

ex = 1
ey = 1
ez = 1

def init():
    glClearColor(0, 0, 1, 1)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 640/480, 0.1, 100)
    glMatrixMode(GL_MODELVIEW)

def draw():
    glLoadIdentity()

    glTranslatef(x, y, -6)
    glRotatef(r, 0, 1, 0)
    glScalef(ex, ey, ez)

    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)
    glVertex3f(0, 1, 0)
    glVertex3f(-1, -1, 0)
    glVertex3f(1, -1, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)
    glVertex3f(0 + 2, 1, 0)
    glVertex3f(-1 + 2, -1, 0)
    glVertex3f(1 + 2, -1, 0)
    glEnd()

def main():
    pygame.init()
    pygame.display.set_mode((640, 480), DOUBLEBUF | OPENGL)
    init()

    global x, y, r, ex, ey, ez

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_a:
                    x += -0.2
                if event.key == K_d:
                    x += 0.2
                if event.key == K_w:
                    y += 0.2
                if event.key == K_s:
                    y += -0.2

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 4:
                    ex += 0.2
                    ey += 0.2
                    ez += 0.2
                if event.button == 5:
                    ex -= 0.2
                    ey -= 0.2
                    ez -= 0.2

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw()
        pygame.display.flip()
        pygame.time.wait(10)
        r += 3

    pygame.quit()

if __name__ == "__main__":
    main()
