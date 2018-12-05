package de.jhoppmann.aoc2018.day4;

import static de.jhoppmann.aoc2018.day4.SleepyGuardFinder.extractGuard;
import static de.jhoppmann.aoc2018.day4.SleepyGuardFinder.extractMinute;
import static de.jhoppmann.aoc2018.day4.SleepyGuardFinder.isBeginLine;
import static de.jhoppmann.aoc2018.day4.SleepyGuardFinder.isFallAsleep;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


public class SleepyMinuteFinder {

   private static List<String>                        sortedGuardTimes  = new ArrayList<>();
   private static Map<Integer, Map<Integer, Integer>> sleepTimesByGuard = new HashMap<>();


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
            Map<Integer, Integer> times = sleepTimesByGuard.getOrDefault(currentGuard, new HashMap<>());
            int wakeUpMinute = extractMinute(logLine);
            for ( int i = fallAsleepMinute; i < wakeUpMinute; i++ ) {
               times.put(i, times.getOrDefault(i, 0) + 1);
            }
            sleepTimesByGuard.put(currentGuard, times);
         }
      }

      int max = 0;
      int minute = 0;
      int guard = 0;

      for ( Integer guardId : sleepTimesByGuard.keySet() ) {
         for ( int i = 0; i < 60; i++ ) {
            if ( sleepTimesByGuard.get(guardId).getOrDefault(i, 0) > max ) {
               max = sleepTimesByGuard.get(guardId).getOrDefault(i, 0);
               minute = i;
               guard = guardId;
            }
         }
      }

      System.out.println(minute + " * " + guard + " = " + guard * minute);
   }

}
