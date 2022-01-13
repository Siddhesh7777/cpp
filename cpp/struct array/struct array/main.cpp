#include<iostream>
using namespace std;

struct array{
    int *a;
    int size;
    int length;
    
};

int main(){
    
    struct array arr;
    cout<<"enter the size of the array"<<endl;
    cin>>arr.size;
    arr.a=new int*arr.size;
    int n;
    arr.length=0;
    cout<<"enter number of numbers"<<endl;
    cin>>n;
    for (int i=0; i<n; i++) {
        cin>>arr.a[i];
    }
    
    
    
    
}
