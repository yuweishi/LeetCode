public class Solution {
    public int countPrimes(int n) {
        if (n < 3){
            return 0;
        }
        int real_n = n, bound = ((int) Math.sqrt(n) + 1)/ 2, count = n / 2;
        n /= 2;
        int [] primes = new int [n];
        for (int i = 1; i < bound; i++) {
            if (primes[i] == 0){
                int real_i = 2 * i + 1;
                for (int multi = real_i * real_i / 2; multi < n; multi += real_i){
                    if (primes[multi] == 0) {
                        primes[multi] = 1;
                        count --;
                    }
                }
            }
        }
        return count;
    }
}
