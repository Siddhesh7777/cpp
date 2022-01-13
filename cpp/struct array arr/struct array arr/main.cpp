#include<iostream>
using namespace std;
struct Array{
    int a[20];
    int length;
    
    
    
};
void display(struct Array arr){
    
    for (int i=0; i<=arr.length; i++) {
        cout<<arr.a[i];
    }
}
int main(){
    struct Array arr{{1,2,3,4,5,45,45,456,6},5};
    

}
