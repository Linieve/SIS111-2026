/*-g++ a.cpp -o a
.\a.exe-*/

#include <bits/stdc++.h>
using namespace std;

int hace(vector<int> vec,int op){
    int s=0, r=vec[0]*2, m=1, di=vec[0]*vec[0];
    for(int i=0; i<vec.size(); i++){
        s+=vec[i]; r-=vec[i]; m*=vec[i]; di/=vec[i];
    }
    if(op==1){
        return s;
    }else if(op==2){
        return r;
    }else if(op==3){
        return m;
    }else if(op==4){
        return di;
    }
    return 0;
}

int main(){
    int op, n,a;
    while(true){
        vector<int> vec;
        cin>>op>>n;
        while(n--){
            cin>>a;
            vec.push_back(a);
        }
        cout<<hace(vec,op);
    }
}