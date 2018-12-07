package de.jhoppmann.aoc2018.day7;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


public class ElfWorkers {

   private static int                        availableWorkers = 5;
   private static Map<Integer, List<String>> seconds          = new HashMap<>();
   private static int                        currentSecond    = 0;

   public static void main( String[] args ) {
      List<Input.InstructionStep> steps = Input.getInstructions();

      System.out.println(steps);

      Map<String, List<String>> prerequisitesForSteps = new HashMap<>();


      for ( Input.InstructionStep step : steps) {
         List<String> prerequisites = prerequisitesForSteps.computeIfAbsent(step.opens, s-> new ArrayList<>());
         prerequisites.add(step.first);
      }
      List<String> done = new ArrayList<>();

      for (char a = 'A'; a <= 'Z'; a++) {
         String character = String.valueOf(a);
         prerequisitesForSteps.computeIfAbsent(character, s -> new ArrayList<>());
      }

     do {
         List<String> complete = seconds.getOrDefault(currentSecond, new ArrayList<>());
         availableWorkers += complete.size();
         done.addAll(complete);
         seconds.remove(currentSecond);
         if (seconds.isEmpty()) {
            // compensating for off-by-one error also present in the example
            System.out.println("Done at second " + (currentSecond - 1));
         }
         for (char a = 'A'; a <= 'Z'; a++) {
            String character = String.valueOf(a);
            List<String> stepList = prerequisitesForSteps.get(character);
            if (stepList != null && done.containsAll(stepList)) {
               if (availableWorkers > 0) {
                  seconds.computeIfAbsent(currentSecond + a - 4, s -> new ArrayList<>()).add(character);
                  availableWorkers--;
                  prerequisitesForSteps.remove(character);
                  break;
               }
            }
         }
         currentSecond++;
         System.out.println(currentSecond + ", " + availableWorkers + ": " + seconds);
      }  while (!seconds.isEmpty());

      StringBuilder sb = new StringBuilder();
      for (String string : done) {
         sb.append(string);
      }
      System.out.println(sb.toString());
   }


}
