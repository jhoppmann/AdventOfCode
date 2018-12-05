package de.jhoppmann.aoc2018.day5;

import java.util.HashSet;
import java.util.Set;


public class PolymerReactor {

   public static void main( String[] args ) {
      String polymer = Input.input;
      boolean reacted = true;
      Set<Integer> indicesToRemove = new HashSet<>();
      while ( reacted ) {
         System.out.println(polymer);
         indicesToRemove.clear();

         int i = 0;
         int j = 1;

         if ( polymer.length() <= 1 ) {
            break;
         }

         while ( j < polymer.length() ) {
            if ( Math.abs(polymer.charAt(i) - polymer.charAt(j)) == 32 ) {
               indicesToRemove.add(i);
               indicesToRemove.add(j);
               i++;
               j++;
            }
            i++;
            j++;
         }

         StringBuilder rest = new StringBuilder();
         for ( int k = 0; k < polymer.length(); k++ ) {
            if ( !indicesToRemove.contains(k) ) {
               rest.append(polymer.charAt(k));
            }
         }

         reacted = !indicesToRemove.isEmpty();
         polymer = rest.toString();
      }
      System.out.println("Final: " + polymer.length());
   }

}
