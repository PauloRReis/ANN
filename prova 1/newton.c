#include<stdio.h>
#include<math.h>

void newton(double (*f)(double), double (*df)(double), double x0, double n)
{
    for (int i = 0; i < n; i++)
    {
        double xn;
        xn = x0 - f(x0) / df(x0);
        x0 = xn;
        printf("x_%d = %.16f\n", i + 1, xn);
    }
}

double f(double x){
    double pi = 3.14159265358979323846;
    return (pi*pow(x, 2))*((3*7.28-x)/3) - 645.67;
}
double df(double x){
    double pi = 3.14159265358979323846;
    return (364*pi*x)/25 - pi * pow(x,2);
}

int main(int argc, char *argv[]){
    
    double x0 = 1.26 ;
    int n = 5;

    newton(f, df, x0, n);
}