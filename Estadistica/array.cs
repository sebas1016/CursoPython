using System;

namespace MyCompiler {
    class Program {
        public static void Main(string[] args) {
            Console.WriteLine("Hello world!");
            //Se declaran las variables
            int m=3;
            int n=3;
            int[] nums1 = new int[6] {1,2,3,0,0,0};
            int[] nums2 = new int[3] {2,5,6};
            
               
              //Se guarda el array nums2 en el Array nums1
              for(int i = 0; i<m;i++){
                for(int j = 0; j<n;i++){
                  if(nums1[i] == 0){
                    nums1[i] = nums2[j];
                  }
                }
              }
              //Se ordenan los Array de forma creciente
              int [] aux = new int [m+n];
              for(int i = 0; i<m;i++){
                for(int j = 0; j<6;j++){
                  if(nums1[i] > nums1[j]){
                    aux[i]=nums1[i];
                    nums1[i]=nums1[j];
                    nums1[j]=aux[i];
        
                    
                  }
                }
              }
            for(int i =0;i<6;i++){
                Console.WriteLine(nums1[i]);
            }
        }
    }
}