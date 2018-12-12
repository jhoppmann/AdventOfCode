package de.jhoppmann.aoc2018.day12;

import java.util.Arrays;


public class PlantGenerationSimulator {

   private static RuleFinder rf;
   private static int        offset = 3;

   public static void main( String[] args ) {
      rf = new RuleFinder(Input.rules);

      boolean[] plants = new boolean[2*offset + Input.getInitial().length];

      for (int i = 0; i < Input.getInitial().length; i++) {
         plants[i+offset] = Input.getInitial()[i];
      }

      System.out.println(arrayToString(plants));

      for (int generation = 0; generation <= 20; generation++){
         // do things here

      }
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
