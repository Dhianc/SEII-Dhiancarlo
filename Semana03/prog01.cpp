#include <iostream>
#include <compl.h>
using namespace std;


int main() {

  comp N1, N2, N3;

  // N1 = 15 + j30
  N1.R = 15.0;
  N1.I = 30.0;

  // N2 = 10 + j20
  N2.R = 10.0;
  N2.I = 20.0;

  // N3 = 5 <45 graus
  N3.raio = 5.0;
  N3.ang = 45.0;

  soma(N1.R, N2.R, N1.I, N2.I);
  subtracao(N1.R, N2.R, N1.I, N2.I);
  multiplicacao(N1.R, N2.R, N1.I, N2.I);
  divisao(N1.R, N2.R, N1.I, N2.I);
  ret2pol(N1.R, N1.I);
  pol2ret(N3.raio, N3.ang);
  return 0;
} 