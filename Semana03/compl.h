#include <iostream>
#include <cmath>
using namespace std;

struct comp
{
  float R, I, raio, ang;
};

float soma (float r1, float r2, float i1, float i2)
{
    float real = r1 + r2;
    float imag = i1 + i2;
    cout << "Resultado: " << real << " + j" << imag;
    return 0.0;
}

float subtracao (float r1, float r2, float i1, float i2)
{
    float real = r1 - r2;
    float imag = i1 - i2;
    cout << "Resultado: " << real << " + j" << imag;
    return 0.0;
}

float multiplicacao (float r1, float r2, float i1, float i2)
{
    float real = r1*r2 - i1*i2;
    float imag = r1*i2 + i1*r2;
    cout << "Resultado: " << real << " + j" << imag;
    return 0.0;
}

float divisao (float r1, float r2, float i1, float i2)
{
    float real = (r1*r2 + i1*i2)/(r2*r2 + i2*i2);
    float imag = (r2*i1 - r1*i2)/(r2*r2 + i2*i2);
    cout << "Resultado: " << real << " + j" << imag;
    return 0.0;
}

float ret2pol (float real, float imag)
{
    float raio = sqrt(real*real + imag*imag);
    float ang = atan(imag/real);
    cout << "Resultado: " << raio << " <" << ang;
    return 0.0;
}

float pol2ret (float raio, float ang)
{
    float rad = ang*3.14159/180;
    float real = raio * cos(rad);
    float imag = raio * sin(rad);
    cout << "Resultado: " << real << " + j" << imag;
    return 0.0;
}