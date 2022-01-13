#include <iostream>
using namespace std;
void find_greatest(int a, int b, int c, int d)
{
    if (a > b) {
        if (a > c) {
            if (a > d) {
                cout << a;
            }
            else {
                cout << d;
            }
        }
    }
    else if (b > c) {
        if (b > d) {
            cout << b;
        }
        else {
            cout << d;
        }
    }
    else if (c > d) {
        cout << c;
    }
    else {
        cout << d;
    }
}
int main(){
    
    int x,y,z,c;
    cin>>x;
    cin>>y;
    cin>>z;
    cin>>c;
    find_greatest(x, y, z, c);
}
