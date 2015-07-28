from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
LEFT = 1 #!
RED = [127, -128, -128]
PINK = [123, 18, 54]
BLACK = [5, 5, 5]
ORANGE = [0, 127, 0]
PURPLE = [40, 0, 40]
GREEN = [0, 0, 127]
BLUE = [0, 0, 34]
NEW = [40, 40, 0]
global xrot
global yrot
global ambient
global greencolor
global treecolor
global lightpos
global colours
def init():
        global colours
        global xrot   
        global yrot
        global ambient
        global greencolor
        global treecolor
        global lightpos
        xrot = 0.0
        yrot = 0.0
        colours = [ ]        
        for i in range(3):
            colours.append([])
            for j in range(3):
                colours[i].append([])
                for k in range(3):
                    colours[i][j].append([])
                    for l in range(6):
                        colours[i][j][k].append(BLACK)

        for i in colours[0]:
            for j in i:
                j[1] = RED
        for i in range(3):
            for j in colours[i][0]:
                j[2] = GREEN
        for i in range(3):
            for j in colours[i][2]:
                j[5] = BLUE
        for i in colours[2]:
            for j in i:
                j[4] = ORANGE             
        for i in colours:
            for j in i:
                j[0][0] = PURPLE
        for i in colours:
            for j in i:
                j[2][3] = PINK      
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
        glEnable(GL_CULL_FACE)
  
def specialkeys(key, x, y):
        global xrot
        global yrot

        if key == GLUT_KEY_LEFT:
                xrot -=3.0
                
        if key == GLUT_KEY_RIGHT:
                yrot += 3.0
        if key == GLUT_KEY_UP:
                xrot -=3.0
        if key == GLUT_KEY_DOWN:
                xrot += 3.0
        glutPostRedisplay()
def keyboardkeys(key, x, y):     
        global colours
        global xrot
        global yrot
       # colours[0][0][0][0] = colours[2][2][2], colours[2][2][2] = colours[0][0][0]
        colours[0][2][0][5] = NEW
        if key == 70:
                
                print("ihear")
      #  glutPostRedisplay()

def draw():
        global colours
        global xrot
        global yrot
        global lightpos
        global greencolor
        global treecolor
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glRotatef(xrot, 1.0, 0.0, 0.0)
        glRotatef(yrot, 0.0, 1.0, 0.0)  #!!!!!!!
        #glLightfv(GL_LIGHT0, GL_POSITION, lightpos)

        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, treecolor)
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
          
        R = Cuube()
        r = []

        vertexs = [[-0.2, -0.2, -0.2], [-0.2, -0.2, 0.2], [0.2, -0.2, 0.2], [0.2, -0.2, -0.2], [-0.2, 0.2, -0.2], [-0.2, 0.2, 0.2], [0.2, 0.2, 0.2], [0.2, 0.2, -0.2]]    

          
       

        def cube(vertexs, q, www):
            
            def edge(v1, v2, v3, v4, q, colour):
                glBegin(GL_POLYGON)
                glColor3b(  colour[0], colour[1], colour[2] )
                glVertex3f(v1[0] + q[0], v1[1] + q[1], v1[2] + q[2])   
                glNormal3f(1,1,1)
                glVertex3f(v2[0] + q[0], v2[1] + q[1], v2[2] + q[2]) 
                glNormal3f(1,1,1)
                glVertex3f(v3[0] + q[0], v3[1] + q[1], v3[2] + q[2]) 
                glNormal3f(1,1,1)
                glVertex3f(v4[0] + q[0], v4[1] + q[1], v4[2] + q[2])    
                glNormal3f(1,1,1)       
                glEnd()
            edge(vertexs[0], vertexs[4], vertexs[7], vertexs[3], q, www[0])
            edge(vertexs[0], vertexs[1], vertexs[5], vertexs[4], q, www[1])
            edge(vertexs[0], vertexs[3], vertexs[2], vertexs[1], q, www[2])
            edge(vertexs[1], vertexs[2], vertexs[6], vertexs[5], q, www[3])
            edge(vertexs[3], vertexs[7], vertexs[6], vertexs[2], q, www[4])
            edge(vertexs[4], vertexs[5], vertexs[6], vertexs[7], q, www[5])


        for i in range(3):
            for j in range(3):
                for k in range(3):
                    cube(vertexs, [(i - 1)*0.45, (j - 1)*0.45, (k - 1)*0.45], colours[i][j][k])



        glPopMatrix()

        glutSwapBuffers()
        
        

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
        pass
        
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







glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInit(sys.argv)
glutCreateWindow(b"Happy New Year!")

#class cubik:
        #glutWireCube(0.5)
glEnable(GL_DEPTH_TEST)
glutInitWindowSize(700, 700)
glutInitWindowPosition(300, 300)
glutDisplayFunc(draw)
glutSpecialFunc(specialkeys)
glutKeyboardFunc(keyboardkeys)


init()
glutMainLoop()

