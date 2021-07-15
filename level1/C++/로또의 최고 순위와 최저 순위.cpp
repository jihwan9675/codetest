#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    int min_n =0, max_n = 0;
    vector<int> answer;
    
    for (int i=0;i<6;i++){
        if(lottos[i]==0)
            max_n+=1;
        for (int j=0;j<6;j++){
            if(lottos[i]==win_nums[j]){
                min_n+=1;
                break;
            }
        }
    }
    if(min_n==0&&max_n==0){
        answer.push_back(6);
        answer.push_back(6);
        return answer;
    }
    answer.push_back(7-min_n-max_n);
    if(max_n==6){
        answer.push_back(6-min_n);
        return answer;
    }
    answer.push_back(7-min_n);
    
    return answer;
}
