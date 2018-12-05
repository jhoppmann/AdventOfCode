package de.jhoppmann.aoc2018.day4;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


public class SleepyGuardFinder {

   private static List<String>          sortedGuardTimes  = new ArrayList<>();
   private static Map<Integer, Integer> sleepTimesByGuard = new HashMap<>();


   public static void main( String[] args ) {
      sortedGuardTimes.addAll(Arrays.asList(Input.input));
      sortedGuardTimes.sort(String::compareTo);

      int currentGuard = 0;
      int fallAsleepMinute = 0;

      for ( String logLine : sortedGuardTimes ) {
         if ( isBeginLine(logLine) ) {
            currentGuard = extractGuard(logLine);
         } else if ( isFallAsleep(logLine) ) {
            fallAsleepMinute = extractMinute(logLine);
         } else {
            int wakeUpMinute = extractMinute(logLine);
            int sleepTime = wakeUpMinute - fallAsleepMinute;
            sleepTimesByGuard.put(currentGuard, (sleepTimesByGuard.getOrDefault(currentGuard, 0) + sleepTime));
         }
      }

      int[] minutes = new int[60];
      int guard = findGuardWithMostMinutes();
      for ( String logLine : sortedGuardTimes ) {
         if ( isBeginLine(logLine) ) {
            currentGuard = extractGuard(logLine);
         }
         if ( currentGuard == guard ) {
            if ( isFallAsleep(logLine) ) {
               fallAsleepMinute = extractMinute(logLine);
            } else {
               int wakeUpMinute = extractMinute(logLine);

               for ( int i = fallAsleepMinute; i < wakeUpMinute; i++ ) {
                  minutes[i]++;
               }
            }
         }
      }

      int max = 0;
      int minute = 0;
      for ( int i = 0; i < minutes.length; i++ ) {
         if ( minutes[i] > max ) {
            max = minutes[i];
            minute = i;
         }
      }

      System.out.println(minute * guard);
   }

   static int extractGuard( String logLine ) {
      String[] split = logLine.split("#");
      String numberString = split[1].substring(0, split[1].indexOf(" "));
      return Integer.valueOf(numberString);
   }

   static int extractMinute( String logLine ) {
      String[] split = logLine.split(":");
      return Integer.valueOf(split[1].substring(0, 2));
   }

   private static int findGuardWithMostMinutes() {
      int longest = 0;
      int guard = 0;
      for ( Integer guardId : sleepTimesByGuard.keySet() ) {
         if ( sleepTimesByGuard.getOrDefault(guardId, 0) > longest ) {
            guard = guardId;
            longest = sleepTimesByGuard.get(guardId);
         }
      }
      return guard;
   }

   static boolean isBeginLine( String logLine ) {
      return logLine.contains("begins");
   }

   static boolean isFallAsleep( String logLine ) {
      return logLine.contains("asleep");
   }
}
