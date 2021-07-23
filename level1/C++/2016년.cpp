#include <string>
#include <vector>

using namespace std;

string solution(int a, int b) {
    int month[] = {0,31,29,31,30,31,30,31,31,30,31,30,31};
    string day[] = {"THU","FRI","SAT","SUN","MON","TUE","WED"};
    string answer = "";
    int sumday= b;
    
    for (int i=1;i<a;i++){
        sumday += month[i];
    }
    
    
    return day[sumday%7];
}
