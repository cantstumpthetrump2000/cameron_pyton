#include <stdio.h>
void printing_matrix(float vaule1[],float vauel2[]);
int main()
{
    int size_x_1;
    int size_y_1;
    int size_x_2;
    int size_y_2;
    
    
    printf("enther the size of the first matirx\n");
    printf("number of rows\n");
    scanf("%d",&size_x_1);
    printf("number of rows %d\n",size_x_1);
    


    printf("number of clomuns\n");
    scanf("%d",&size_y_1);
    printf("number of clomuns %d\n",size_y_1);
    
    float matrix_1[size_x_1][size_y_1];
    
    
    printf("matric 1  %f \n",size_y_1);
    
 
    
    printf("enther the size of the second  matirx\n");
    printf("number of rows\n");
    scanf("%d",&size_x_2);
    printf("number of rows %d\n",size_x_2);
    


    printf("number of clomuns\n");
    scanf("%d",&size_y_2);
    printf("number of clomuns %d\n",size_y_2);
    
    
    float matrix_2[size_x_2][size_y_2];
    
    
    if (size_x_1 != size_y_2) && (size_x_2 != size_y_1){
         printf(" can mutilple the matrix \n");
         return 0;
    }
    
    
    for(int x=0; x>size_y_1; x++) {
        for(int x=0; x>size_x_2; x++) {
            
        
    }
    }

    
    
    
    printing_matrix(matrix_1,matrix_2);
    
    return 0;
}




void printing_matrix(float vaule1[],float vauel2[]){
    printf("mutipleing the matrix \n");
    
    float reult=5.0;
    printf("%f",&reult);
}