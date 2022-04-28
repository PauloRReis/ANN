#include<stdio.h>

/* #define ROWS 3
#define COLS 3 */

#define ROWS 4
#define COLS 4

void jacobi(double A[ROWS][ROWS], double B[ROWS], double chute[ROWS], int n){

    double next[ROWS];
    for(int k = 0 ; k < n ; k++){
        for(int i = 0 ; i < ROWS ; i++){
            double bi = B[i];
            for(int j = 0 ; j < ROWS ; j++){
                if(j != i){
                    bi -= A[i][j] * chute[j];
                }
            }
            bi /= A[i][i];
            printf("x_%d^(%d) = %.16f\t", i+1, k+1, bi);
            next[i] = bi;
        }
        printf("\n");
        //atualizar o chute
        for(int i = 0 ; i < ROWS ; i++){
            chute[i] = next[i];
        }
    }

}

int main(){
    
/* M[3][3]
    double a[ROWS][COLS] = {{5.05, 3.02, 0.98, }, {-1.03, 5.42, 3.34}, {-4.78, 3.43, 9.26}};
    double b[ROWS] = {-0.75, -2.14, 3.36};
    double chute[COLS] = {-4.09, -0.7, -1.09}; */

    double a[ROWS][COLS] = {{5.41, -0.3, -3.07, -0.14}, {1.75, -11.91, -4.21, 4.06}, {-2.49, -1.86, 11.14, 4.89}, {-2.83, 0.77, -2.96, -8.45}};
    double b[ROWS] = {1.26, 1.83, -1.64, 1.98};
    double chute[COLS] = {1.12, 4.3 ,-4.58,-2.09}; 

    int n = 18;

    jacobi(a, b, chute, n);
}
/*     for(int it = 0; it < n; it++){
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
    } */