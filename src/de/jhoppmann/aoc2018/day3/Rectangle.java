package de.jhoppmann.aoc2018.day3;

class Rectangle {

   java.awt.Rectangle rect;

   int id;


   Rectangle( String info ) {
      readString(info);
   }

   boolean intersects( Rectangle rectangle ) {
      if ( id == rectangle.id ) {
         return false;
      }
      return rect.intersects(rectangle.rect);
   }

   private void readString( String info ) {
      String[] splitId = info.split("@");
      id = Integer.valueOf(splitId[0].substring(1).trim());

      String[] splitCoordinates = splitId[1].trim().split(":");
      String[] splitCorners = splitCoordinates[0].split(",");

      String[] sizes = splitCoordinates[1].trim().split("x");
      int width = Integer.valueOf(sizes[0]);
      int height = Integer.valueOf(sizes[1]);
      rect = new java.awt.Rectangle(Integer.valueOf(splitCorners[0]), Integer.valueOf(splitCorners[1]), width, height);

   }
}
