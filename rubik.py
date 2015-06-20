from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
global xrot
global yrot
global ambient
global greencolor
global treecolor
global lightpos
def init():
        global xrot
        global yrot
        global ambient
        global greencolor
        global treecolor
        global lightpos
        xrot = 0.0
        yrot = 0.0
        ambient = (0.0, 0.0, 0.0, 0.0)
        greencolor = (0.2, 0.8, 0.0, 0.8)
        treecolor = (1.0, 1.0, 1.0, 1.0)
        lightpos = (2000.0, 2000.0, 1.0)
        glClearColor(0.5, 0.5, 0.5, 1.0)
        gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
        glRotatef(30, 1.0, 1.0, 0.0)
        #glLightModelfv(GL_LIGHT_MODEL_DIFFUSE, diffuse)
        #glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE);
        #glEnable(GL_LIGHTING)
        #glEnable(GL_LIGHT0)
        #glLightfv(GL_LIGHT0, GL_POSITION, lightpos)

def specialkeys(key, x, y):
        global xrot
        global yrot
        if key == GLUT_KEY_LEFT:
                yrot -=3.0
        if key == GLUT_KEY_RIGHT:
                yrot += 3.0
        if key == GLUT_KEY_UP:
                xrot -=3.0
        if key == GLUT_KEY_DOWN:
                xrot += 3.0
        
        glutPostRedisplay()
#Cuubes =[]
#for i in range(18):
       # p = p
     #   coordinates = []
    #    Cuubes.append(Cube(p, coordinates))        
def draw():
        global xrot
        global yrot
        global lightpos
        global greencolor
        global treecolor
        glClear(GL_COLOR_BUFFER_BIT)
        glPushMatrix()
        glRotatef(xrot, 1.0, 0.0, 0.0)
        glRotatef(yrot, 0.0, 1.0, 0.0)  #!!!!!!!
        #glLightfv(GL_LIGHT0, GL_POSITION, lightpos)

        glMaterialfv(GL_FRONT, GL_DIFFUSE, treecolor)
        #glTranslatef(0.0, 0.0, -0.7)
        #glutSolidCylinder(0.1, 0.2, 20, 20)
        #glMaterialfv(GL_FRONT, GL_DIFFUSE, greencolor)
        #glTranslatef(0.0, 0.0, 0.2)
        #glutSolidCone(0.5, 0.5, 20, 20)
        #glutSolidCube(0.5)
        #glTranslatef(0.0, 0.0, 0.3)
        #glutSolidCone(0.4, 0.4, 20, 20)
        #glTranslatef(0.0, 0.0, 0.3)
        #glutSolidCone(0.3, 0.3, 20, 20)

  #      glBegin(GL_TRIANGLE_STRIP)
    #    a = [50, 400, 5]
  #      glColor3b(a[0], a[1], a[2]);
     #   glNormal3f(1,1,1) 
   #     glVertex3f(1.0, 0.0, 0.0);
    #    glColor3b(100,2,30)
    #    glNormal3f(1,1,1)
     #   glVertex3f(0.0, 1.0, 0.0);
  #      glColor3b(1,200,30)
 #       glNormal3f(1,1,1)
 #       glVertex3f(0.0, 0.0, 1.0);
   #     glEnd()
        #glColor3f(100,200,30)
        #glVertex3f(0.0, 10.0, 10.0)
        #glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, greencolor)
        #glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);

        #glutWireCube(1.0)
        glBegin(GL_POLYGON)
        glColor3b(20, 10, 30)
        glVertex3f(0.0, 0.0, 0.0)   
        glNormal3f(1,1,1)
     #   glColor3b(20, 40, 80)
        glVertex3f(0.0, 0.5, 0.0) 
        glNormal3f(1,1,1)
     #   glColor3b(5, 40, 70)
        glVertex3f(0.5, 0.5, 0.0) 
        glNormal3f(1,1,1)
      #  glColor3b(20, 40, 0)
        glVertex3f(0.5, 0.0, 0.0)    
        glNormal3f(1,1,1)       
        glEnd()                 
        R = Cuube()

        glPopMatrix()
        glutSwapBuffers()
        
        
a = [50, 400, 5]
b = [50, 5, 400]
c = [400, 50, 5]
d = [400, 5, 50]
e = [5, 400, 50]
f = [5, 50, 400]       
g = [5, 5, 5] 
def elemental(a, b):
        glBegin(GL_POLYGON)
        glColor3b(a[0], a[1], a[2])
        glVertex3f(b, b, b)   
        glNormal3f(1,1,1)
        glVertex3f(b, b + 0.5, b) 
        glNormal3f(1,1,1)
        glVertex3f(b + 0.5, b + 0.5, b) 
        glNormal3f(1,1,1)
        glVertex3f(b + 0.5, b, b)    
        glNormal3f(1,1,1)       
        glEnd()                 


class Cuube:
    def __init__(self):
        glBegin(GL_POLYGON)
        glColor3b(20, 10, 30)
        glVertex3f(-0.5, -0.5, -0.5)   
        glNormal3f(1,1,1)
      #  glColor3b(20, 40, 80)
        glVertex3f(-0.5, 0.5, -0.5) 
        glNormal3f(1,1,1)
      #  glColor3b(5, 40, 70)
        glVertex3f(0.5, 0.5, -0.5) 
        glNormal3f(1,1,1)
      #  glColor3b(20, 40, 900)
        glVertex3f(0.5, -0.5, -0.5)    
        glNormal3f(1,1,1)       
        glEnd()

        glBegin(GL_POLYGON)
        glColor3b(20, 5, 40)
        glVertex3f(-0.5, -0.5, -0.5)   
        glNormal3f(1,1,1)
      #  glColor3b(20, 40, 80)
        glVertex3f(-0.5, 0.5, -0.5) 
        glNormal3f(1,1,1)
     #   glColor3b(5, 40, 70)
        glVertex3f(0.5, 0.5, -0.5) 
        glNormal3f(1,1,1)
     #   glColor3b(20, 40, 90)
        glVertex3f(0.5, -0.5, -0.5)    
        glNormal3f(1,1,1)       
        glEnd()

        glBegin(GL_POLYGON)
        glColor3b(50, 10, 20)
        glVertex3f(-0.5, -0.5, -0.5)   
        glNormal3f(1,1,1)
     #   glColor3b(20, 40, 80)
        glVertex3f(-0.5, 0.5, -0.5) 
        glNormal3f(1,1,1)
    #    glColor3b(5, 40, 70)
        glVertex3f(-0.5, 0.5, 0.5) 
        glNormal3f(1,1,1)
     #   glColor3b(20, 40, 90)
        glVertex3f(-0.5, -0.5, 0.5)    
        glNormal3f(1,1,1)       
        glEnd()

        glBegin(GL_POLYGON)
        glColor3b(20, 50, 10)
        glVertex3f(-0.5, -0.5, 0.5)   
        glNormal3f(1,1,1)
     #   glColor3b(20, 40, 80)
        glVertex3f(-0.5, 0.5, 0.5) 
        glNormal3f(1,1,1)
    #    glColor3b(5, 40, 70)
        glVertex3f(0.5, 0.5, 0.5) 
        glNormal3f(1,1,1)
     #   glColor3b(20, 40, 90)
        glVertex3f(0.5, -0.5, 0.5)    
        glNormal3f(1,1,1)       
        glEnd()

        glBegin(GL_POLYGON)
        glColor3b(10, 10, 20)
        glVertex3f(0.5, -0.5, -0.5)   
        glNormal3f(1,1,1)
     #   glColor3b(20, 40, 80)
        glVertex3f(0.5, 0.5, -0.5) 
        glNormal3f(1,1,1)
     #   glColor3b(5, 40, 70)
        glVertex3f(0.5, 0.5, 0.5) 
        glNormal3f(1,1,1)
     #   glColor3b(20, 40, 90)
        glVertex3f(0.5, -0.5, 0.5)    
        glNormal3f(1,1,1)       
        glEnd()

        glBegin(GL_POLYGON)
        glColor3b(5, 30, 30)
        glVertex3f(-0.5, 0.5, -0.5)   
        glNormal3f(1,1,1)
     #   glColor3b(20, 40, 80)
        glVertex3f(-0.5, 0.5, 0.5) 
        glNormal3f(1,1,1)
     #   glColor3b(5, 40, 70)
        glVertex3f(0.5, 0.5, 0.5) 
        glNormal3f(1,1,1)
     #   glColor3b(20, 40, 90)
        glVertex3f(0.5, 0.5, -0.5)    
        glNormal3f(1,1,1)       
        glEnd()
        
    def rotateRight(self, mode):
        pass
    def rotateLeft(self, mode):
        pass
    def rotateFront(self, mode):
        pass
    def rotateTop(self, mode):
        pass
    def rotateBottom(self, mode):
        pass
    def rotateBack(self, mode):
        pass







glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(300, 300)
glutInitWindowPosition(300, 300)
glutInit(sys.argv)
glutCreateWindow(b"Happy New Year!")

#class cubik:
        #glutWireCube(0.5)

glutDisplayFunc(draw)
glutSpecialFunc(specialkeys)
init()
glutMainLoop()
