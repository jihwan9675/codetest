class Solution {
 public String solution(int[] numbers, String hand) {
        int left = 9;
        int right = 11;
        String answer = "";

        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = numbers[i]-1;
            if(numbers[i]==-1){
                numbers[i]=10;
            }
            if (numbers[i] == 0 || numbers[i] == 3 || numbers[i] == 6) {
                answer += "L";
                left = numbers[i];
            }
            else if (numbers[i] == 2 || numbers[i] == 5 || numbers[i] == 8) {
                answer += "R";
                right = numbers[i];
            }
            else {
                int n_idx_1 = numbers[i]/3;
                int n_idx_2 = numbers[i]%3;
                int left_a = left/3;
                int left_b = left%3;
                int right_a = right/3;
                int right_b = right%3;

                int sum_l = Math.abs(n_idx_1 - left_a) + Math.abs(n_idx_2 - left_b);
                int sum_r = Math.abs(n_idx_1 - right_a) + Math.abs(n_idx_2 - right_b);

                if (sum_l == sum_r) {
                    if (hand.equals("right")) {
                        answer += "R";
                        right = numbers[i];
                    } else {

                        answer += "L";
                        left = numbers[i];
                    }

                } else if (sum_l > sum_r) {

                    answer += "R";
                    right = numbers[i];

                } else {
                    answer += "L";
                    left = numbers[i];
                }
            } 

        }
        return answer;
 }
}
