#include<iostream>
using namespace std;


struct Array{
    int A[10];
    int size;
    int length;
};

void append( struct Array *arr,int x){
    arr->A[arr.length++]=x;
    
    
}



int main(){
    
    struct Array arr{{1,2,3},10,8};
    
    
    
}
