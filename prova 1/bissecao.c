#include<stdio.h>
#include<math.h>

void bisection(double (*f)(double), double a, double b, int n){
    double fa = f(a);
    if(fa * f(b) >= 0){
        printf("Não sei dizer que f possui raiz no intervalo raiz no intervalo [%f, %f]", a, b);
        return;
    }else{
        double m =0;
        for(int i=0; i<n; i++){
            m = 0.5 * (a + b);
            printf("x_%d = %.16f\t", i + 1, 1.52 - m);
            double fm = f(m);
            printf("f(x_%d) = %.16f\n", i + 1, fm);
            if(fm == 0){
                printf("%f é uma raiz", m);
                return;
            }
            if(fa * fm < 0){
                b = m;
            }else{
                a = m;
                fa = fm;
            }
        }
    }

}

double f(double x){
        return 2*x - 1;
}

int main(int argc, char *argv[]){
    
    double a = -4.53;
    double b = -0.35;
    int n = 15;

    bisection(f, a, b, n);
}