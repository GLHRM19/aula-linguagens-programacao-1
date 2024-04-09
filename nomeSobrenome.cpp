#include <iostream>
#include <string>
#include <cstring>
using namespace std;
int main() {
    char nome[2000];
    string sobrenome;
    cin >>nome;
    cin >>sobrenome;
    cout<<sobrenome<<","<<nome[0]<< nome[strlen(nome)-1]<<endl;
    
    return 0;

}









