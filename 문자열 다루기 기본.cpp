#include <string>
#include <vector>
#include <iostream>
using namespace std;

bool solution(string s) {
    if(s.size() == 4 || s.size() == 6){
        for(int i=0;i<s.size();i++){
            if (!(s[i]<=57 && s[i]>=48)){
                return false;
            }
        }
    }
    else{
        return false;
    }
    
    return true;
}
