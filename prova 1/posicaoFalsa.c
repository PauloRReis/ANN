#include <stdio.h>
#include <math.h>

void false_position(double (*f)(double), double a, double b, int n, double tol){
    if (f(a) * f(b) < 0)
    {

        for (int i = 0; i < n; i++)
        {
            double fa = f(a);
            double fb = f(b);
            double c;
            c = (a * fb - b * fa) / (fb - fa);
            if (f(c) == 0)
            {
                printf("Voce encontrou uma raiz para f. Ela é: %.16f\n", c);
                return;
            }

            printf("x_%d = %.15f \n", i + 1, c);
            if (fa * f(c) < 0)
            {
                b = c;
            }
            else
            {
                a = c;
            }
        }
    }
    else
    {
        printf("O intervalo [ %.16f, %.16f] nao serve\n", a, b);
    }
}

double f(double x){
        return 2*(x+1)*(x-0.5)*(x-1);
}

int main(){

    double a = 0.7036;
    double b = 1.2688;
    int max_iter = 5;
    double tol = 0.00001;

    false_position(f, a, b, max_iter, tol);
}