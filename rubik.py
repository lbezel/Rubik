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
        global archiv
        xrot = 0.0
        yrot = 0.0
        archiv = []
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
              

        glClearColor(0.5, 0.5, 0.5, 1.0)
        gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
        glRotatef(30, 1.0, 1.0, 0.0)
        glEnable(GL_CULL_FACE)
  
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

def keyboardkeys(key, x, y):     
        global colours
        global xrot
        global yrot
        global archiv
        coba = []
        for i in range(3):
            coba.append([])
            for j in range(3):
                coba[i].append([])
                for k in range(3):
                    coba[i][j].append([])
                    for l in range(6):
                        coba[i][j][k].append(BLACK)
        if key in b'zsexdrvgyZSEXDRVGY':
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        for l in range(6):
                            coba[i][j][k][l] = colours[i][j][k][l]
            archiv.append(coba) 
        def x_rotate(i):

            for j in range(3):
                der = colours[i][2][j][5]
                des = colours[i][2 - j][2][3]
                colours[i][2][j][5] = des
                colours[i][2 - j][2][3] = der
            for j in range(2):                
                den = colours[i][2 - j][2][4]
                dem = colours[i][2][j][4]
                colours[i][2 - j][2][4] = dem 
                colours[i][2][j][4] = den
            for j in range(2):                
                den = colours[i][2 - j][2][1]
                dem = colours[i][2][j][1]
                colours[i][2 - j][2][1] = dem 
                colours[i][2][j][1] = den                
                              
            for k in range(3):
                der = colours[i][2 - k][2][3]
                des = colours[i][0][2 - k][2]
                colours[i][2 - k][2][3] = des    
                colours[i][0][2 - k][2] = der
            for k in range(2):
                den = colours[i][0][2 - k][4]
                dem = colours[i][2 - k][2][4]
                colours[i][0][2 - k][4] = dem
                colours[i][2 - k][2][4] = den
            for j in range(2):                
                den = colours[i][0][2 - j][1]
                dem = colours[i][2 - j][2][1]
                colours[i][0][2 - j][1] = dem 
                colours[i][2 - j][2][1] = den                                    
                
            for l in range(3):
                der = colours[i][0][2 - l][2]
                des = colours[i][l][0][0]
                colours[i][0][2 - l][2] = des    
                colours[i][l][0][0] = der 
            for l in range(2):
                den = colours[i][l][0][4]
                dem = colours[i][0][2 - l][4] 
                colours[i][l][0][4] = dem
                colours[i][0][2 - l][4] = den 
            for j in range(2):                
                den = colours[i][j][0][1]
                dem = colours[i][0][2 - j][1]
                colours[i][j][0][1] = dem 
                colours[i][0][2 - j][1] = den                


           


        def y_rotate(i):

            for j in range(3):
                der = colours[2 - j][i][2][3]
                des = colours[2][i][j][4]
                colours[2 - j][i][2][3] = des
                colours[2][i][j][4] = der  
            for j in range(2):
                der = colours[2 - j][i][2][5]
                des = colours[2][i][j][5]
                colours[2 - j][i][2][5] = des
                colours[2][i][j][5] = der 
            for j in range(2):
                der = colours[2 - j][i][2][2]
                des = colours[2][i][j][2]
                colours[2 - j][i][2][2] = des
                colours[2][i][j][2] = der                


            for k in range(3):
                der = colours[2][i][k][4]
                des = colours[k][i][0][0]
                colours[2][i][k][4] = des
                colours[k][i][0][0] = der

            for k in range(2):
                der = colours[2][i][k][5]
                des = colours[k][i][0][5]
                colours[2][i][k][5] = des
                colours[k][i][0][5] = der
            for k in range(2):
                der = colours[2][i][k][2]
                des = colours[k][i][0][2]
                colours[2][i][k][2] = des
                colours[k][i][0][2] = der

            for l in range(3):
                der = colours[l][i][0][0]
                des = colours[0][i][2 - l][1]
                colours[l][i][0][0] = des
                colours[0][i][2 - l][1] = der 
            for l in range(2):
                der = colours[l][i][0][5]
                des = colours[0][i][2 - l][5]
                colours[l][i][0][5] = des
                colours[0][i][2 - l][5] = der 
            for l in range(2):
                der = colours[l][i][0][2]
                des = colours[0][i][2 - l][2]
                colours[l][i][0][2] = des
                colours[0][i][2 - l][2] = der 

           

        def z_rotate(i):

            for j in range(3):
                der = colours[0][2 - j][i][1]
                des = colours[2 - j][2][i][5]
                colours[0][2 - j][i][1] = des
                colours[2 - j][2][i][5] = der 
            for j in range(2):
                der = colours[0][2 - j][i][0]
                des = colours[2 - j][2][i][0]
                colours[0][2 - j][i][0] = des
                colours[2 - j][2][i][0] = der
            for j in range(2):
                der = colours[0][2 - j][i][3]
                des = colours[2 - j][2][i][3]
                colours[0][2 - j][i][3] = des
                colours[2 - j][2][i][3] = der

            for k in range(3):
                der = colours[2 - k][2][i][5]
                des = colours[2][k][i][4]
                colours[2 - k][2][i][5] = des
                colours[2][k][i][4] = der  
            for k in range(2):
                der = colours[2 - k][2][i][0]
                des = colours[2][k][i][0]
                colours[2 - k][2][i][0] = des
                colours[2][k][i][0] = der
            for k in range(2):
                der = colours[2 - k][2][i][3]
                des = colours[2][k][i][3]
                colours[2 - k][2][i][3] = des
                colours[2][k][i][3] = der                

            for l in range(3):
                der = colours[2][l][i][4]
                des = colours[l][0][i][2]
                colours[2][l][i][4] = des
                colours[l][0][i][2] = der               
            for l in range(2):
                der = colours[2][l][i][0]
                des = colours[l][0][i][0]
                colours[2][l][i][0] = des
                colours[l][0][i][0] = der
            for l in range(2):
                der = colours[2][l][i][3]
                des = colours[l][0][i][3]
                colours[2][l][i][3] = des
                colours[l][0][i][3] = der                  
           

        if key == b'd':
            x_rotate(1)         
        if key == b'x':
            x_rotate(0)
        if key == b'r':
            x_rotate(2)
        if key == b'y':
            y_rotate(2)  
        if key == b'v':
            y_rotate(0)
        if key == b'g':
            y_rotate(1) 
        if key == b'z':
            z_rotate(2) 
        if key == b's':
            z_rotate(1)
        if key == b'e':
            z_rotate(0) 

        def triple_f(func, param):
            func(param)
            func(param)
            func(param)
        if key == b'D':
            triple_f(x_rotate, 1)         
        if key == b'X':
            triple_f(x_rotate, 0)
        if key == b'R':
            triple_f(x_rotate, 2)
        if key == b'Y':
            triple_f(y_rotate, 2)  
        if key == b'V':
            triple_f(y_rotate, 0)
        if key == b'G':
            triple_f(y_rotate, 1) 
        if key == b'Z':
            triple_f(z_rotate, 2) 
        if key == b'S':
            triple_f(z_rotate, 1)
        if key == b'E':
            triple_f(z_rotate, 0) 


        if key == b'b':
            if not archiv:
                print("start position")
            else:
                coba = archiv.pop() 
                for i in range(3):
                    for j in range(3):
                        for k in range(3):
                            for l in range(6):
                                colours[i][j][k][l] = coba[i][j][k][l]
         
        glutPostRedisplay()

def draw():
        global colours
        global xrot
        global yrot

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glRotatef(xrot, 1.0, 0.0, 0.0)
        glRotatef(yrot, 0.0, 1.0, 0.0)  #!!!!!!!

        vertexs = [[-0.15, -0.15, -0.15], [-0.15, -0.15, 0.15], 
        [0.15, -0.15, 0.15], [0.15, -0.15, -0.15], [-0.15, 0.15, -0.15], 
        [-0.15, 0.15, 0.15], [0.15, 0.15, 0.15], [0.15, 0.15, -0.15]]    
 
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
                    cube(vertexs, [(i - 1)*0.35, (j - 1)*0.35, (k - 1)*0.35], colours[i][j][k])

        glPopMatrix()

        glutSwapBuffers()
        
             


        
#mills = 30
#def Timer(a):
#    glutPostRedisplay()
#    glutTimerFunc(mills, a, 0)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInit(sys.argv)
glutCreateWindow(b"RUBIK'S CUBE!")


glEnable(GL_DEPTH_TEST)
glutInitWindowSize(900, 900)
glutInitWindowPosition(300, 300)
glutDisplayFunc(draw)
#glutTimerFunc(0, Timer, 0)
glutSpecialFunc(specialkeys)
glutKeyboardFunc(keyboardkeys)


init()
glutMainLoop()

