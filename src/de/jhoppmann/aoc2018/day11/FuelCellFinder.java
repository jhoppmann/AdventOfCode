package de.jhoppmann.aoc2018.day11;

import java.util.Arrays;


public class FuelCellFinder {

   static private int gridSerialNumber = 5034;

   public static void main( String[] args ) {

      int[][] powerLevels = new int[300][300];
      for (int x = 1; x <= 300; x++) {
         for (int y = 1; y <= 300; y++) {
            powerLevels[x-1][y-1] = calculatePowerLevel(x, y);
         }
      }
      int[] coordinates = findLargestPowerSquare(powerLevels);
      System.out.println(Arrays.toString(coordinates));

      int[] coordinatesLargest = findLargestSquareAnySize(powerLevels);
      System.out.println(Arrays.toString(coordinatesLargest));
   }

   private static int[] findLargestSquareAnySize( int[][] values ) {
      int largest = Integer.MIN_VALUE;
      int[] largestCoordinates = new int[3];
      for (int size = 1; size <= 300; size++) {
         int upperLimit = (300 - size) + 1;

         for (int x = 1; x<=upperLimit;x++) {
            for (int y = 1; y<=upperLimit;y++) {
               int areaLevel = findAreaLevel(x, y, values, size);
               if (areaLevel > largest ) {
                  largest = areaLevel;
                  largestCoordinates[0] = x;
                  largestCoordinates[1] = y;
                  largestCoordinates[2] = size;
               }

            }
         }
      }
      return largestCoordinates;
   }

   private static int[] findLargestPowerSquare(int[][] values) {
      int largest = Integer.MIN_VALUE;
      int[] largestCoordinates = new int[2];
      for (int x = 1; x<=298;x++) {
         for (int y = 1; y<=298;y++) {
            int areaLevel =findAreaLevel(x, y, values, 3);
            if (areaLevel > largest ) {
               largest = areaLevel;
               largestCoordinates[0] = x;
               largestCoordinates[1] = y;
            }

         }
      }
      return largestCoordinates;
   }

   private static int calculatePowerLevel(int x, int y) {
      int rackId = x+10;

      int powerLevel = rackId*y;
      powerLevel += gridSerialNumber;
      powerLevel *= rackId;
      powerLevel /= 100;
      powerLevel %= 10;

      powerLevel -= 5;

      return powerLevel;
   }

   private static int findAreaLevel(int x, int y, int[][] values, int size) {
      int sum = 0;

      for (int i = x-1; i < x-1+size;i++) {
         for (int k = y-1; k < y-1+size;k++) {
            sum += values[i][k];
         }
      }
      return sum;
   }

}
