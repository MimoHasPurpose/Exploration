// include libraries


#include<GL/glut.h>

// callback function. what is to be drawn would be here
void renderScene(void){
glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);
glBegin(GL_TRIANGLES);
    glVertex3f(-0.5,-0.5,0.0);
    glVertex3f(0.5,0.0,0.0);
    glVertex3f(0.0,0.5,0.0);
glEnd();
glutSwapBuffers();


}

int main(int argc, char **argv){
    // init glut and create window

    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DEPTH|GLUT_DOUBLE|GLUT_RGBA);
    glutInitWindowPosition(300,300);
    glutInitWindowSize(320,320);
    glutCreateWindow("a triangle");
    // register callback
    glutDisplayFunc(renderScene);
    // enter GLUT event processing cycle

    glutMainLoop();
    return 1;


}

