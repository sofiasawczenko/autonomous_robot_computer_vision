#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv){
	if(argc != 7){
		printf("Parra executar o programa digite:\n\n%s seis \
número entre 01 e 60\n\nPor exemplo: \
\n\n%s 07 34 45 51 55 59\n\n", argv[0], argv[0]);
		exit(1);
	}

	int i, j, k, counter;
	int *l, *m;
	FILE *file;

	l= (int *) calloc(6, sizeof(int));
	m= (int *) calloc(6, sizeof(int));

	for(i= 0; i< 6; i++){
		l[i]= atoi(argv[i+1]);
	}

	file= fopen("mega_sena.dat", "r");
	for(i= 0; i< 2194; i++){
		fscanf(file, "%d %d %d %d %d %d", &m[0], &m[1], &m[2], &m[3], &m[4], &m[5]);
		counter= 0;
		for(j= 0; j< 6; j++){
			for(k= 0; k< 6; k++){
				if(l[j] == m[k]){
					counter++;
				}
			}
		}
		if(counter >= 4){
			printf("%d %d\n", i+1, counter);
		}
	}
	fclose(file);

	free(l);
	free(m);
	return 0;
}
