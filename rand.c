#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char **argv){
	int i;
	srand(time(NULL));
	for(i= 0; i< 5; i++){
		printf("%e\n", (double)rand()/RAND_MAX);
	}
	return 0;
}
