#include<stdio.h>

#define ROWS 3
#define COLS 3

void jacobi(double a[ROWS][COLS], double b[COLS], double chute[COLS], int n){
    
    for(int it = 0; it < n; it++){
        double temp[COLS];
        for(int i =0; i < ROWS; i++){
            double xi = b[i];
            for(int j=0; j<COLS; j++){
                if(i != j){
                    xi -= a[i][j] * chute[j];
                }
            }
            xi /= a[i][i];
            temp[i] = xi;
        }
        printf("X^(%d) -> ", it + 1);
        for(int k=0; k < COLS; k++){
            chute[k] = temp[k];
            printf("%.10f\t", chute[k]);
        }
        printf("\n");
    }
}
int main(){
    
    double a[ROWS][COLS] = {{5.55349, -3.40242, -0.8525}, {-0.81535, -3.89477, 1.78084}, {2.91846, 2.74225, -6.95928}};
    double b[ROWS] = {-4.0115, 0.58744, 0.41145};

    double chute[COLS] = {-0.03204, 2.80044, 2.97158};

    int n = 20;

    jacobi(a, b, chute, n);
}