#include <vector>
#include <algorithm>
#include <set>
using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    set<int> set;
    for(int i=0;i<nums.size();i++)
    {
        set.insert(nums[i]);
    }
    return set.size()>=nums.size()/2?nums.size()/2:set.size();
}
