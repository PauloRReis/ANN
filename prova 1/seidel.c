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
    int rows = 4;
    //estimativa inicial para solução do sistema
    double chute[4] = {2.66, 4.35, 4.14, -0.87};
    //matriz estendida do sistema linear
    double matrix[4][5] = {{-16.34, -4.84, 4.82, -4.93, -2.07 }, {3.84, 11.14,-1.49, 4.06, 3.23}, {1.38, -3.2, -9.09, -2.76, 0.43}, {-0.67, -3.48, 3.44, -9.34, -0.54}};
    //numero máximo de iterações
    int max_iter = 16;

    seidel(chute, rows, matrix, max_iter);
}