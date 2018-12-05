package de.jhoppmann.aoc2018.day3;

import java.util.ArrayList;
import java.util.List;


public class OverlapFinder {

   private static List<Rectangle> rectangles = new ArrayList<>();
   private static boolean[][]     marked     = new boolean[1000][1000];

   private static String[] test = { "#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2" };


   public static void main( String[] args ) {
      for ( String definition : Input.input ) {
         rectangles.add(new Rectangle(definition));
      }

      int counter = 0;
      for ( Rectangle r1 : rectangles ) {
         for ( Rectangle r2 : rectangles ) {
            if ( r1.intersects(r2) ) {
               findOverlapArea(r1, r2);
            }
         }
         counter++;
         System.out.println("Checked " + counter + " of " + Input.input.length + " rectangles.");
      }

      System.out.println(countTrues());
   }

   private static int countTrues() {
      int counter = 0;

      for ( boolean[] aMarked : marked ) {
         for ( boolean innerMarked : aMarked ) {
            if ( innerMarked ) {
               counter++;
            }
         }
      }

      return counter;
   }

   private static void findOverlapArea( Rectangle r1, Rectangle r2 ) {
      java.awt.Rectangle r = r1.rect.intersection(r2.rect);

      for ( double i = r.getX(); i < r.getX() + r.getWidth(); i++ ) {
         for ( double j = r.getY(); j < r.getY() + r.getHeight(); j++ ) {
            marked[(int)i][+(int)j] = true;
         }
      }
   }

}
