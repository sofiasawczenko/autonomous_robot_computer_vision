#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

int main(int argc, char **argv){
	int i, n;
	srand(time(NULL));
	double x= (double)rand()/RAND_MAX;
	double y= (double)rand()/RAND_MAX;
	for(i= 0; i< 1e6; i++){
		n= 3*(double)rand()/RAND_MAX;
		switch(n){
			case 0:
				x= 0.5*(0.0 + x);
				y= 0.5*(0.0 + y); 
				printf("%e %e\n", x, y);
			break;
			case 1:
				x= 0.5*(1.0 + x);
				y= 0.5*(0.0 + y); 
				printf("%e %e\n", x, y);
			break;
			default:
				x= 0.5*(0.5 + x);
				y= 0.5*(0.5*sqrt(3) + y); 
				printf("%e %e\n", x, y);
		}
	}
	return 0;
}
