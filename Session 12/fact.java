    class FactorialExample2{  
     static int factorial(int n, int k){    
      if (n == 0 || n == 1)    
        return k;    
        // return 1;
      else
        // return n * factorial(n-1);
        return factorial(n-1, k*n);    
     }    
     public static void main(String args[]){  
      long i,fact=1;  
      int number=10;//It is the number to calculate factorial    
      long start = System.nanoTime();
      fact = factorial(number, 1);
      long end = System.nanoTime();
    long elapsedTime = end - start;
      
    System.out.println("Total Time taken "+elapsedTime);
     }  
    }  