#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv){
	if(argc != 3){
		printf("%s nome_do_arquivo_de_dados.dat n_de_linhas\n", argv[0]);
		exit(1);
	}

	int i, n;
	double x;
	FILE *entrada; // ponteiro que recebe o endereço de memória do arquivo
	char nome[100]; // recebe o nome do arquivo, pode ter no máximo 100 caracteres

	sprintf(nome, "%s", argv[1]); // nome recebe o nome do arquivo
	entrada= fopen(nome, "r"); // abre o arquivo para escrita
	n= atoi(argv[2]); 
	for(i= 0; i< n; i++){
		fscanf(entrada, "%lf\n", &x); // lê um número do tipo double dentro do arquio
		printf("%g\n", x);
	}
	fclose(entrada); // fecha o arquivo
	return 0;
}
