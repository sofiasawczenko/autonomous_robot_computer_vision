#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv){
	int i;
	FILE *saida; // ponteiro que recebe o endereço de memória do arquivo
	char nome[100]; // recebe o nome do arquivo, pode ter no máximo 100 caracteres

	for(i= 0; i< 5; i++){
		sprintf(nome, "arquivo-%d.dat", i); // nome recebe o nome do arquivo
		saida= fopen(nome, "w"); // abre o arquivo para escrita
		fprintf(saida, "%d\n", i); // escreve um número inteiro dentro do arquivo
		fclose(saida); // fecha o arquivo
	}
	return 0;
}
