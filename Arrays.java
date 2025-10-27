public class Arrays {
   public static void main(String[] args){
      int[] list = {1,2,31,14,25,31,52,621,14,13,521,62};
      
      //for (int element : list){
      for (int i=list.length-1; i>=0; i=i-1){
         System.out.println(list[i]);
      }  
/*
      for (int i=0; i<list.length; i++){
         System.out.println(list[list.length - i - 1]);
      }
*/

   }
}
