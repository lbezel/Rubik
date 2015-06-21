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
        r = []

        edges = [[-0.2, -0.2, -0.2], [-0.2, -0.2, 0.2], [0.2, -0.2, 0.2], [0.2, -0.2, -0.2], [-0.2, 0.2, -0.2], [-0.2, 0.2, 0.2], [0.2, 0.2, 0.2], [0.2, 0.2, -0.2]]    
        colours = [  [  [100, 0, 0], [0, 100, 0], [0, 0, 100], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5]  ], 
                 [  [100, 0, 0], [5, 5, 5], [0, 0, 100], [5, 5, 5], [40, 0, 40], [5, 5, 5], [5, 5, 5]  ], 
                 [  [100, 0, 0], [0, 100, 0], [5, 5, 5], [5, 5, 5], [5, 5, 5], [0, 40, 40], [5, 5, 5]  ],
                 [  [5, 5, 5], [0, 100, 0], [0, 0, 100], [40, 40, 0], [5, 5, 5], [5, 5, 5], [5, 5, 5]  ], 
                 [  [100, 0, 0], [5, 5, 5], [5, 5, 5], [5, 5, 5], [40, 0, 40], [0, 40, 40], [5, 5, 5]  ], 
                 [  [5, 5, 5], [5, 5, 5], [0, 0, 100], [40, 40, 0], [40, 0, 40], [5, 5, 5], [5, 5, 5]  ],
                 [  [5, 5, 5], [0, 100, 0], [5, 5, 5], [40, 40, 0], [5, 5, 5], [0, 40, 40], [5, 5, 5]  ],
                 [  [5, 5, 5], [5, 5, 5], [5, 5, 5], [40, 40, 0], [40, 0, 40], [0, 40, 40], [5, 5, 5]  ]   ]
        def cube(edges, q, d):
            www = colours[d]
            glBegin(GL_POLYGON)
            glColor3b(  www[0][0], www[0][1], www[0][2] )
            glVertex3f(edges[0][0] + q[0], edges[0][1] + q[1], edges[0][2] + q[2])   
            glNormal3f(1,1,1)
            glVertex3f(edges[4][0] + q[0], edges[4][1] + q[1], edges[4][2] + q[2]) 
            glNormal3f(1,1,1)
            glVertex3f(edges[7][0] + q[0], edges[7][1] + q[1], edges[7][2] + q[2]) 
            glNormal3f(1,1,1)
            glVertex3f(edges[3][0] + q[0], edges[3][1] + q[1], edges[3][2] + q[2])    
            glNormal3f(1,1,1)       
            glEnd()

            glBegin(GL_POLYGON)
            glColor3b(  www[1][0], www[1][1], www[1][2]  )
            glVertex3f(edges[0][0]+ q[0], edges[0][1]+ q[1], edges[0][2] + q[2])   
            glNormal3f(1,1,1)
            glVertex3f(edges[1][0]+ q[0], edges[1][1]+ q[1], edges[1][2] + q[2]) 
            glNormal3f(1,1,1)
            glVertex3f(edges[5][0]+ q[0], edges[5][1]+ q[1], edges[5][2] + q[2]) 
            glNormal3f(1,1,1)
            glVertex3f(edges[4][0]+ q[0], edges[4][1]+ q[1], edges[4][2] + q[2])       
            glNormal3f(1,1,1)       
            glEnd()

            glBegin(GL_POLYGON)
            glColor3b(www[2][0], www[2][1], www[2][2])
            glVertex3f(edges[0][0]+ q[0], edges[0][1]+ q[1], edges[0][2]+ q[2] )   
            glNormal3f(1,1,1)
            glVertex3f(edges[3][0]+ q[0], edges[3][1]+ q[1], edges[3][2]+ q[2] ) 
            glNormal3f(1,1,1)
            glVertex3f(edges[2][0]+ q[0], edges[2][1]+ q[1], edges[2][2]+ q[2] ) 
            glNormal3f(1,1,1)
            glVertex3f(edges[1][0]+ q[0], edges[1][1]+ q[1], edges[1][2]+ q[2] )    
            glNormal3f(1,1,1)       
            glEnd()

            glBegin(GL_POLYGON)
            glColor3b(www[3][0], www[3][1], www[3][2])
            glVertex3f(edges[1][0]+ q[0], edges[1][1]+ q[1], edges[1][2]+ q[2] )   
            glNormal3f(1,1,1)
            glVertex3f(edges[2][0]+ q[0], edges[2][1]+ q[1], edges[2][2]+ q[2] ) 
            glNormal3f(1,1,1)
            glVertex3f(edges[6][0]+ q[0], edges[6][1]+ q[1], edges[6][2]+ q[2] ) 
            glNormal3f(1,1,1)
            glVertex3f(edges[5][0]+ q[0], edges[5][1]+ q[1], edges[5][2]+ q[2] )    
            glNormal3f(1,1,1)       
            glEnd()

            glBegin(GL_POLYGON)
            glColor3b(www[4][0], www[4][1], www[4][2])
            glVertex3f(edges[3][0]+ q[0], edges[3][1]+ q[1], edges[3][2]+ q[2] )   
            glNormal3f(1,1,1)
            glVertex3f(edges[7][0]+ q[0], edges[7][1]+ q[1], edges[7][2]+ q[2] ) 
            glNormal3f(1,1,1)
            glVertex3f(edges[6][0]+ q[0], edges[6][1]+ q[1], edges[6][2]+ q[2] ) 
            glNormal3f(1,1,1)
            glVertex3f(edges[2][0]+ q[0], edges[2][1]+ q[1], edges[2][2]+ q[2] )    
            glNormal3f(1,1,1)       
            glEnd()

            glBegin(GL_POLYGON)
            glColor3b(www[5][0], www[5][1], www[5][2])
            glVertex3f(edges[4][0]+ q[0], edges[4][1]+ q[1], edges[4][2]+ q[2] )   
            glNormal3f(1,1,1)
            glVertex3f(edges[5][0]+ q[0], edges[5][1]+ q[1], edges[5][2]+ q[2] ) 
            glNormal3f(1,1,1)
            glVertex3f(edges[6][0]+ q[0], edges[6][1]+ q[1], edges[6][2]+ q[2] ) 
            glNormal3f(1,1,1)
            glVertex3f(edges[7][0]+ q[0], edges[7][1]+ q[1], edges[7][2]+ q[2] )    
            glNormal3f(1,1,1)       
            glEnd()

        for i in range(18):
            r.append(1)    
        q = [0, 0, 0]
        l = [0.4, 0, 0]
        u = [0, 0.4, 0]     
        i = [0, 0, 0.4]        
        m = [0.4, 0.4, 0]        
        j = [0.4, 0, 0.4]
        n = [0, 0.4, 0.4]
        h = [0.4, 0.4, 0.4]
        wq = cube(edges, q, 0)
        wl = cube(edges, l, 1)
        wu = cube(edges, u, 2)      
        wi = cube(edges, i, 3)   
        wm = cube(edges, m, 4)
        wj = cube(edges, j, 5)     
        wn = cube(edges, n, 6)      
        wh = cube(edges, h, 7)
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
glutInitWindowSize(700, 700)
glutInitWindowPosition(300, 300)
glutInit(sys.argv)
glutCreateWindow(b"Happy New Year!")

#class cubik:
        #glutWireCube(0.5)
glEnable(GL_DEPTH_TEST)
glutDisplayFunc(draw)
glutSpecialFunc(specialkeys)
init()
glutMainLoop()
