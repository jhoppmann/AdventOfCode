package de.jhoppmann.aoc2018.day12;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class RuleFinder {

   private List<Rule> rules = new ArrayList<>();

   RuleFinder(String[] ruleStrings) {
      Arrays.stream(ruleStrings).forEach(s -> rules.add(new Rule(s)));
   }

   public boolean getStatusInNextGen(boolean[] input) {
      if (input.length > 5) {
         throw new IllegalArgumentException("Input doesn't have the right size");
      }

      for(Rule rule : rules) {
         if (rule.matches(input)) {
            return rule.output;
         }
      }
      throw new IllegalArgumentException("No matching rule found!");
   }

   public static class Rule{
      private boolean[] input = new boolean[5];
      private final boolean output;

      Rule (String rule) {
         rule = rule.trim();
         output = rule.endsWith("#");
         for (int i = 0; i < 5; i++) {
            input[i] = rule.charAt(i) == '#';
         }
      }

      public boolean[] getInput() {
         return input;
      }

      public boolean getOutput() {
         return output;
      }

      boolean matches(boolean[] plants) {
         return Arrays.equals(plants, input);
      }

   }

}
