package de.jhoppmann.aoc2018.day6;

import java.awt.*;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


public class RegionDistanceFinder {

   static         Map<Point, Integer> fieldsNearest = new HashMap<>();
   private static int                 maxX;
   private static int                 maxY;
   private static List<Point>         points;
   private static int                 size          = 0;

   public static void main( String[] args ) {

      points = Input.getPoints();
      maxX = (int)points.stream().mapToDouble( Point::getX).max().orElse(0.0);
      maxY = (int)points.stream().mapToDouble(Point::getY).max().orElse(0.0);

      double minX = points.stream().mapToDouble(Point::getX).min().orElse(0);
      double minY = points.stream().mapToDouble(Point::getY).min().orElse(0);

      for (int x = -maxX; x <= 2*maxX; x++) {
         for (int y = -maxY; y <= 2*maxY; y++) {
            if (sumToAll(x, y) < 10000) {
               size++;
            }
         }
      }

      System.out.println(size);
   }

   private static int sumToAll( int x, int y ) {
      int sum = 0;
      for (Point p : points) {
         sum += ManhattanDistanceField.calculateManhattanDistance(p, x, y);
      }
      return sum;
   }
}
