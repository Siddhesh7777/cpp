#include<iostream>
using namespace std;


int main(){
    
    
    int a;
    int b;
    cout<<"enter the two nubers betmn which you want to do it"<<endl;
    cin>>a>>b;
    string s[]={"","one","two","three","four","five","six","seven","eight","nine"};
    
    for (int i=a; i<=b; i++) {
        cout<<s[i]<<endl;
        
       
    }
    for (int i=a; i<=b; i++) {
        
        
        if (i%2==0) {
            cout<<"even"<<endl;
        }
        if (i%2!=0) {
            cout<<"odd"<<endl;
        }
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
}
