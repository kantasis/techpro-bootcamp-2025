public class Sorting {

   public static void main(String[] args){
   
      float[] array = {40,80,50,70,90,20,10,30,100,60};
      float current_min = array[0];
      float previous_min;
      int min_j=-1;


      for (int i=0; i<array.length;i++){
         current_min = array[i];
         min_j = i;
         for (int j=i;j<array.length;j++){
            
            if (array[j] < current_min){
               current_min = array[j];
               min_j = j;
            }
         }
         float temp  = array[min_j];
         array[min_j] = array[i];
         array[i] = temp;
      }

      for (int i=0;i<array.length;i++)
         System.out.println(array[i]);

   }

}
