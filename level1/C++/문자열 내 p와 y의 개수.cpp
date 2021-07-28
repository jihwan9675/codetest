#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    int P=0 , Y=0;
    
    for(int i=0;i<s.size();i++){
        if (s[i] == 'p' || s[i]=='P'){
            P+=1;
        }
        else if (s[i] == 'y' || s[i]=='Y'){
            Y+=1;
        }
    }
    if(P==Y){
        return true;
    }
    return false;
}
