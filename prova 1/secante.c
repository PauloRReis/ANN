#include<stdio.h>
#include<math.h>

void secant(double (*f)(double), double x0, double x1, int n){
    for (int i = 0; i < n; i++)
    {
        double fx0 = f(x0);
        double fx1 = f(x1);
        if (fx0 == fx1)
        {
            printf("Divisao por zero");
            return;
        }
        double x2;
        x2 = (x0 * fx1 - x1 * fx0) / (fx1 - fx0);
        x0 = x1;
        x1 = x2;
        printf("x_%d = %.16f\n", i + 1, x2);
    }
}

double f(double x){
        double pi = 3.14159265358979323846;
        return (pi*pow(x, 2))*((3*7.28-x)/3) - 645.67;
    }

int main(int argc, char *argv[]){

    double x0 = 2.31;
    double x1 = 12.48;
    int n = 5;

    secant(f , x0, x1, n);
}