#include<iostream>
using namespace std;


struct Array{
    
    int A[20];
    
    int length;
    
    
    
    
    
    
};

void display(struct Array arr){
    for(int i=0; i<arr.length; i++)
    {
        cout<<arr.A[i];
    }
    
    
}
int main(){
    
    
    
    
    
    struct Array arr{{1,2,3,4,5,63,3,43},19};
    
    display(arr);
    }
