#include <vector>
#include <iostream>
using namespace std;

int solution(vector<int> nums) {
    int answer = -1;

    for(int i=0;i<nums.size();i++)
    {
        for(int j=i+1;j<nums.size();j++)
        {
            for(int k=j+1;k<nums.size();k++)
            {
                int sub = nums[i] + nums[j]+ nums[k];
                bool check = true;
                for (int z = 2;z<sub;z++){
                    if(sub%z==0){
                        check = false;
                        break;
                    }
                }
                if(check){
                    answer +=1;
                }
            }
        }
    }
    

    return answer+1;
}
