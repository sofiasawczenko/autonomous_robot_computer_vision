#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

int main(int argc, char **argv){
	int i, n;
	double x, y;
	srand(time(NULL));
	n= 0;
	for(i= 0; i< 1e6; i++){
		x= (double)rand()/RAND_MAX;
		y= (double)rand()/RAND_MAX;
		if(sqrt(x*x+y*y) < 1.0){
			n++;
		}
	}
	printf("%g\n", 4.0*n/1e6);
	return 0;
}
