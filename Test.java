public class Test {


   public static boolean isPrime(int n){
      boolean result = true;
      for (int i=2;i<n;i++){
         if (n % i==0) {
            result=false;
            break;
         }
      }
      return result;
   }
   public static void main(String[] args) {
      int input = 55;

      int output = input;
      while ( ! isPrime(output))
         output = output + 1;

      System.err.println("Next prime to "+input+" is " + output);
      System.err.println("Prime? "+isPrime(output));
   }



}
