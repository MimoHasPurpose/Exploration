#include <GL/glut.h>
void display()
{
  glClear(GL_COLOR_BUFFER_BIT);
  glBegin(GL_POINTS);
  glVertex3f(0.0f, 0.0f, 0.0f);
  glVertex3f(50.0f, 40.0f, 0.0f);
  glVertex3f(50.0f, 50.0f, 50.0f);
  glEnd();
  glFlush();
}

int main(int argc, char **argv)
{
  glutInit(&argc, argv);
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
  glutInitWindowPosition(80, 80);
  glutInitWindowSize(400, 300);
  glutCreateWindow("A dot!!");
  glutDisplayFunc(display);

  glutMainLoop();
}

