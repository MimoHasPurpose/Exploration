#include <GL/glu.h>
#include <GL/glut.h>

void Draw()
{
}

int main(int c, char *v[])
{
    glutInit(&c, v);

    glutInitWindowPosition(400, 150);
    glutInitWindowSize(500, 500);
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);
    glutCreateWindow("points");
    glutDisplayFunc(Draw);
    glutMainLoop();
    return 0;
}