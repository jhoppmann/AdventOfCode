package de.jhoppmann.aoc2018.day7;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import de.jhoppmann.aoc2018.day7.Input.InstructionStep;


public class InstructionStepSorter {

   public static void main( String[] args ) {
      List<InstructionStep> steps = Input.getInstructions();

      System.out.println(steps);

      Map<String, List<String>> prerequisitesForSteps = new HashMap<>();


      for ( InstructionStep step : steps) {
         List<String> prerequisites = prerequisitesForSteps.computeIfAbsent(step.opens, s-> new ArrayList<>());
         prerequisites.add(step.first);
      }
      List<String> done = new ArrayList<>();

      for (char a = 'A'; a <= 'Z'; a++) {
         String character = String.valueOf(a);
         prerequisitesForSteps.computeIfAbsent(character, s -> new ArrayList<>());
      }

      while (!prerequisitesForSteps.isEmpty()) {
         for (char a = 'A'; a <= 'Z'; a++) {
            String character = String.valueOf(a);
            List<String> stepList = prerequisitesForSteps.get(character);
            if (stepList != null && done.containsAll(stepList)) {
               done.add(character);
               prerequisitesForSteps.remove(character);
               break;
            }
         }
      }

      StringBuilder sb = new StringBuilder();
      for (String string : done) {
         sb.append(string);
      }
      System.out.println(sb.toString());


   }

}
