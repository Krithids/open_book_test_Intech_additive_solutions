#include<GL/glut.h>  //it  provides the functions to create windows  , to  handle input,to draw 3D shapes
                                    
float  earthAngle=0.0f, moonAngle=0.0f; //created 2 variables to track the rotation angles of earth and moon
                                                             
void init(){
	glEnable(GL_DEPTH_TEST);   //used for depth testing
glEnable(GL_LIGHTING);
glEnable(GL_LIGHT0);
GLfloat lightPos[]={0,0,0,1};      //at the origin to place the sun
glLightfv(GL_LIGHT0,GL_POSITION,lightPos);
glClearColor(0,0,0,1);                   // setting the background color to black
}

//Used for displaying
void display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();

     //To draw the sun
               glPushMatrix();
               glColor3f(1, 1, 0);     //gives the yellow color              
               glutSolidSphere(1.5, 30, 30);       //it draws the solid 3D sphere 
               glPopMatrix();
               
               //To draw the earth
	glPushMatrix();
        glRotatef(earthAngle, 0, 1, 0);   //it rotates the earth around the sun    
        glTranslatef(6, 0, 0);    //keeping earth away from the sun            
        glColor3f(0, 0, 1);       //setting earth color to blue            
        glutSolidSphere(0.5, 20, 20);     //it draws the solid 3D sphere   

   //to draw the moon
           glPushMatrix();
            glRotatef(moonAngle, 0, 1, 0);    //to move moon around the earth
            glTranslatef(1.2, 0, 0);     //distance of the moon from the earth      
            glColor3f(0.5, 0.5, 0.5);   //color of moon to gray      
            glutSolidSphere(0.2, 15, 15);    //it draws the solid 3D sphere   
            glPopMatrix();
            glPopMatrix();
             
            glutSwapBuffers();
            }

//Timer Function
void update(int) {
    earthAngle += 0.3f;    //controlling the earth orbit around the  sun
    moonAngle += 1.0f;      //controlling the moon orbit around the earth
    glutPostRedisplay();       //calling the display function
    glutTimerFunc(16, update, 0);   // to call the function after specifies time
          }

//Handling the window resize function
void reshape(int w, int h) {
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(60.0, (float)w / h, 1.0, 100.0);
    glMatrixMode(GL_MODELVIEW);
             }
  int main(int argc, char** argv) {
    glutInit(&argc, argv); 
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(800, 600); 
    glutCreateWindow("3D Solar System");
    init();                          // Setting up lighting, depth
    glutDisplayFunc(display);       // Calling to draw each frame
    glutReshapeFunc(reshape);       // Calling when window resizes
    glutTimerFunc(0, update, 0);    // Start animation loop
    glutMainLoop();                 // Start the main event loop
    return 0;
         }
