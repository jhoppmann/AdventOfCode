package de.jhoppmann.aoc2018.day6;

import java.awt.*;
import java.util.ArrayList;
import java.util.List;


public class Input {

   private static String[] input = { "268, 273", "211, 325", "320, 225", "320, 207", "109, 222", "267, 283", "119, 70", "138, 277", "202, 177", "251, 233", "305, 107", "230, 279", "243, 137", "74, 109", "56, 106", "258, 97", "248, 346", "71, 199", "332, 215", "208, 292", "154, 80", "74, 256", "325, 305", "174, 133", "148, 51", "112, 71", "243, 202", "136, 237", "227, 90", "191, 145", "345, 133", "340, 299", "322, 256", "86, 323", "341, 310", "342, 221", "50, 172", "284, 160", "267, 142", "244, 153", "131, 147", "245, 323", "42, 241", "90, 207", "245, 167", "335, 106", "299, 158", "181, 186", "349, 286", "327, 108"};

   static List<Point> getPoints() {
      List<Point> points = new ArrayList<>();

      for (String point : input) {
         String[] coordinates = point.split(",");
         int x = Integer.valueOf(coordinates[0].trim());
         int y = Integer.valueOf(coordinates[1].trim());

         Point p = new Point(x,y);
         points.add(p);
      }

      return points;
   }

}
