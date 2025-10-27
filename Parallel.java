public class Parallel {
   public static void main(String[] args){
      int[] scores = {10,15,20,15,13,19,12,11,16};
      String[] names = {"George", "John", "Michael", "Anna", "Evridiki", "Theologia", "Anastasia", "Meropi", "Theodoros"};


      int max_grade = scores[0];
      int max_index = 0;
      
      for (int i=0; i<scores.length; i++){
         // System.out.println(i+" " +names[i]+": "+scores[i]);
         if (scores[i] > max_grade){
            max_grade = scores[i];
            max_index=i;
         }
      }

      System.out.println("Student with best grade: "+names[max_index]+ " with grade " + max_grade);
   }
}
