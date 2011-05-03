import java.math.BigInteger;

public class fibo2 {
    public static BigInteger fibonacci(int n) {
        BigInteger value = new BigInteger("0");
        BigInteger f1 = new BigInteger("1");
        BigInteger f2 = new BigInteger("-1");
        for (int i=0; i< n+1; i++) {
            value = f1.add(f2);
            f2 = f1;
            f1 = value;
        }

        return value;
    }
    public static void main(String[] argv) {
        long start = System.currentTimeMillis();
        for (int i=0; i<5000; i++) {
            fibonacci(i);
        }
        long end = System.currentTimeMillis();
        System.out.println(1.0*(end - start)/1000);
    }
}
