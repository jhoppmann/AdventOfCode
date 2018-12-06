package de.jhoppmann.aoc2018.day6;

import java.awt.*;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;


public class ManhattanDistanceField {

   private static Map<Point, Integer> fieldsNearest = new HashMap<>();
   private static int                 maxX;
   private static int                 maxY;
   private static List<Point>         points;


   public static void main( String[] args ) {
      points = Input.getPoints();
      maxX = (int)points.stream().mapToDouble(Point::getX).max().orElse(0.0);
      maxY = (int)points.stream().mapToDouble(Point::getY).max().orElse(0.0);

      double minX = points.stream().mapToDouble(Point::getX).min().orElse(0);
      double minY = points.stream().mapToDouble(Point::getY).min().orElse(0);

      // Brute-forcing it...
      // I need to fix this
      for ( int x = -2*maxX; x <= 4*maxX; x++) {
         for ( int y = -2*maxY; y <= 4* maxY; y++) {
            findNearestPoint(x, y);
         }
      }

      List<Map.Entry<Point, Integer>> entries = fieldsNearest.entrySet().stream().sorted(Comparator.comparing(Map.Entry::getValue)).collect(Collectors.toList());
      for ( Map.Entry<Point, Integer> entry : entries) {
         System.out.println(entry.getValue());
      }
      System.out.println("-------------------------------------------------");
      System.out.println(fieldsNearest.entrySet().stream().mapToInt(Map.Entry::getValue).max());
      System.out.println(fieldsNearest.entrySet().stream().mapToInt(Map.Entry::getValue).sum());
      System.out.println(maxX * maxY);

   }

   private static void findNearestPoint( int x, int y ) {
      Map<Integer, List<Point>> manhattanDistance = new HashMap<>();

      for (Point p : points) {
         int distance = calculateManhattanDistance(p, x, y);
         List<Point> points = manhattanDistance.computeIfAbsent(distance, s -> new ArrayList<>());
         points.add(p);
      }

      int closestDistance = manhattanDistance.keySet().stream().mapToInt(Integer::intValue).min().orElse(-1);
      if (closestDistance >= 0) {
         List<Point> points = manhattanDistance.get(closestDistance);
         if (points.size() == 1) {
            fieldsNearest.put(points.get(0), fieldsNearest.getOrDefault(points.get(0), 0) + 1);
         }
      } else
         System.out.println("ERROR!");
   }

   static int calculateManhattanDistance( Point p, int x, int y) {
      return (int)(Math.abs(p.getX() - x) + Math.abs(p.getY() - y));
   }

}
