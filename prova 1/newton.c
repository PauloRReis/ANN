#include<stdio.h>
#include<math.h>

void newton(double (*f)(double), double (*df)(double), double x0, int n){
    for(int i; i< n; i++){
        double dfx0 = df(x0);
        if(dfx0 == 0){
            printf("Divisão por zero, Não foi possivel a interação %d do método de Newton.", i+1);
            return;
        }else{
            x0 = x0 - f(x0)/dfx0;
            printf("x_%d = %.16f\n", i + 1, x0);
        }
    }
}

double f(double x){
    return 4*pow(x, 2);
}
double df(double x){
    return 2*x;
}

int main(int argc, char *argv[]){
    
    double x0 = -2.4257 ;
    int n = 5;

    newton(f, df, x0, n);
}