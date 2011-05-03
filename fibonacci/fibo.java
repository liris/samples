import java.math.BigInteger;

public class fibo {
    static final BigInteger ZERO = new BigInteger("0");
    static final BigInteger ONE = new BigInteger("1");
    static final BigInteger TWO = new BigInteger("2");
    public static BigInteger fibonacci(BigInteger n) {
        if (n.equals(ZERO)) {
            return ZERO;
        } else if (n.equals(ONE)) {
            return ONE;
        }
        return fibonacci(n.subtract(ONE)).add(fibonacci(n.subtract(TWO)));
    }
    public static void main(String[] argv) {
        long start = System.currentTimeMillis();
        for (int i=0; i<30; i++) {
            System.out.println(fibonacci(new BigInteger(String.valueOf(i))));
        }
        long end = System.currentTimeMillis();
        System.out.println(1.0*(end - start)/1000);
    }
}
