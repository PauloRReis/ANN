#include <stdio.h>

void seidel(double *chute, int rows, double matrix[rows][rows+1], int n){
    for(int i=0; i<n; i++){
        for(int r =0; r<rows; r++){
            double temp = 0;
            temp += matrix[r][rows];
            for(int c = 0; c<rows; c++){
                if(r!=c){
                    temp -= (matrix[r][c] * chute[c]);
                }
            }
            temp /= matrix[r][r];
            printf("X_%d,%d = %.16f\n", r + 1, i + 1, temp);
            chute[r] = temp;
        }
        printf("\n");
    }
}

int main(){
    /*
    //ordem do sistema
    int rows = 3;
    //estimativa inicial para solução do sistema
    double chute[3] = {-1.73763, 0.57524, 0.71905};
    //matriz estendida do sistema linear
    double matrix[3][4] = {{3.65843, 1.64339, 0.5043, 2.03862}, {1.97877, -8.46215, -4.97264, -4.06993}, {4.79323, 3.72841, 10.03238, -1.48057}};
    //numero máximo de iterações
    int max_iter = 18;
    */

   //ordem do sistema
    int rows = 3;
    //estimativa inicial para solução do sistema
    double chute[3] = {4.23793, 3.35832, 4.9764};
    //matriz estendida do sistema linear
    double matrix[3][4] = {{3.62382, 1.04167, 1.55212, 0.98612}, {-3.08151, -8.37228, -4.26073, 0.32161}, {-2.31705, 0.69484, -4.04192, -1.66764}};
    //numero máximo de iterações
    int max_iter = 20;

    seidel(chute, rows, matrix, max_iter);
}