#include <GL/glu.h>
#include <GL/glut.h>

void MyInit()
{
    glClearColor(0, 0, 0, 1);
    glColor3f(1, 0, 0);
}
void DrawPoints()
{
    glPointSize(5);
    glBegin(GL_POINTS);
    glVertex2d(-0.5, 0.5);
    glVertex2d(0.5, 0.5);
    glVertex2d(0.5, -0.5);
    glVertex2d(-0.5, -0.5);
    glEnd();
}
void DrawLines()
{
    glBegin(GL_LINES);
    glVertex2d(-0.5, 0.5);
    glVertex2d(0.5, 0.5);
    glVertex2d(0.5, -0.5);
    glVertex2d(-0.5, -0.5);
    glEnd();
}
void DrawRect()
{
    glBegin(GL_POLYGON);
    glVertex2d(-0.5, 0.5);
    glVertex2d(0.5, 0.5);
    glVertex2d(0.5, -0.5);
    glVertex2d(-0.5, -0.5);
    glEnd();
}
void Draw()
{
    glClear(GL_COLOR_BUFFER_BIT);
    DrawPoints();
    DrawRect();
    glFlush();
}

int main(int c, char *v[])
{
    glutInit(&c, v);

    glutInitWindowPosition(400, 150);
    glutInitWindowSize(500, 500);
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);
    glutCreateWindow("points");
    MyInit();
    glutDisplayFunc(Draw);
    glutMainLoop();
    return 0;
}