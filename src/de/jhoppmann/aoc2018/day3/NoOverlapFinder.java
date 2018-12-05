package de.jhoppmann.aoc2018.day3;

import java.util.ArrayList;
import java.util.List;


public class NoOverlapFinder {

   private static List<Rectangle> rectangles = new ArrayList<>();


   public static void main( String[] args ) {
      for ( String definition : Input.input ) {
         rectangles.add(new Rectangle(definition));
      }

      for ( Rectangle r1 : rectangles ) {
         boolean intersects = false;
         for ( Rectangle r2 : rectangles ) {
            if ( r1.intersects(r2) ) {
               intersects = true;
               break;
            }
         }
         if ( !intersects ) {
            System.out.println(r1.id);
         }

      }

   }
}
