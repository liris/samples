
import java.util.concurrent.Semaphore;

public class SemaTest {
    public static void main(String[] argv) {
        final int loopMax = argv.length >= 1 ? Integer.valueOf(argv[0]) : 100;
        final boolean useSemaphore = argv.length >= 2 ? Boolean.valueOf(argv[1]) : true;
        final boolean useFair = argv.length >= 3 ? Boolean.valueOf(argv[2]) : true;
        final Semaphore sema = new Semaphore(10, useFair);
        for (int i=0; i<100; i++) {
            new Thread(new Runnable() {
                    public void run() {
                        int total = 0;
                        for (int i=0; i<loopMax; i++) {
                            try {
                                if (useSemaphore) {
                                    sema.acquire();
                                }
                                total++;
                            } catch (Exception e) {
                            } finally {
                                if (useSemaphore) {
                                    sema.release();
                                }
                            }
                        }
                    }
                }).start();
        }
    }
}
