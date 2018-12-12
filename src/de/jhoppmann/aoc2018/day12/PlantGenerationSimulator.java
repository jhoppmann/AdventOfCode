package de.jhoppmann.aoc2018.day12;

import java.util.Arrays;


public class PlantGenerationSimulator {

   private static RuleFinder rf;
   private static int        offset = 30;

   public static void main( String[] args ) {
      System.out.println(calculateFor(20));

      long result = (50000000000L - 2000) * 102 + 205377;
      System.out.println(result);
   }

   private static long calculateFor(long generations) {
      int offsetSize = 4;
      int offset = offsetSize;
      rf = new RuleFinder(Input.rules);

      boolean[] plants = new boolean[2*offset + Input.getInitial().length];

      for (int i = 0; i < Input.getInitial().length; i++) {
         plants[i+offset] = Input.getInitial()[i];
      }

      for (long generation = 0; generation < generations; generation++){
         boolean[] newGen = new boolean[plants.length];

         for (int i = 2; i<plants.length-2;i++) {
            newGen[i] = rf.getStatusInNextGen(Arrays.copyOfRange(plants, i-2,i+3));
         }

         offset += offsetSize;
         plants = new boolean[2*offset + Input.getInitial().length];
         for (int i = 0; i < newGen.length; i++) {
            plants[i+offsetSize] = newGen[i];
         }
      }
      return calcSum(offset, plants);


   }

   private static int calcSum( int offset, boolean[] plants ) {
      int sum = 0;
      for (int i = 0; i<plants.length;i++) {
         if (plants[i]) {
            sum += i-offset;
         }
      }
      return sum;
   }

   private static String arrayToString(boolean[] values) {
      StringBuilder builder = new StringBuilder();
      for ( boolean value : values ) {
         if ( value ) {
            builder.append("#");
         } else {
            builder.append(".");
         }
      }
      return builder.toString();
   }

}
