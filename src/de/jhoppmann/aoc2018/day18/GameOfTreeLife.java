package de.jhoppmann.aoc2018.day18;

import java.util.Arrays;


public class GameOfTreeLife {

   private static char[][] field = Input.getField();

   private static int[] generationsList = {10, 1000000000};

   public static void main( String[] args ) {
      for (int generations : generationsList) {
         char[][] calculated = calculateGenerations(generations, field);
         int allLumberyards = countAllLumberyards(calculated);
         int allTrees = countAllTrees(calculated);
         System.out.println(allLumberyards * allTrees);
      }
   }

   private static int countAll(char[][] field, char character) {
      int counter = 0;
      for (char[] outer : field) {
         for ( char inner :outer) {
            if (inner == character) {
               counter++;
            }
         }
      }
      return counter;
   }

   private static int countAllTrees( char[][] calculated ) {
      return countAll(calculated, '|');
   }

   private static int countAllLumberyards( char[][] calculated ) {
     return countAll(calculated, '#');
   }

   private static char[][] calculateGenerations( int generations, char[][] field ) {

      for (int generation = 1; generation <= generations; generation++) {
         char[][] nextGen = new char[field.length][field[0].length];
         for (int x = 0; x < field.length; x++) {
            for(int y = 0; y < field[x].length; y++) {
               nextGen[x][y] = getNextGenerationSymbol(field, x, y);
            }
         }
         field = nextGen;
      }
      System.out.println("After " + generations + " minute:");
      System.out.println(arrayToString(field));
      return field;
   }

   private static String arrayToString( char[][] field ) {
      StringBuilder sb = new StringBuilder();
      for (char[] inner : field) {
         for (char character : inner) {
            sb.append(character);
         }
         sb.append("\n");
      }
      return sb.toString();
   }

   private static char getNextGenerationSymbol( char[][] field, int x, int y ) {
      if (field[x][y] == '#') {
         if (countTrees(field, x ,y ) >=1 && countLumberyards(field, x, y) >= 1) {
            return '#';
         } else {
            return '.';
         }
      } else if (field[x][y] == '.'){
         int trees = countTrees(field, x, y);
         if (trees >= 3) {
            return '|';
         } else {
            return '.';
         }
      } else if (field[x][y] == '|') {
         if (countLumberyards(field, x, y) >= 3) {
            return '#';
         } else {
            return '|';
         }
      }

         return '.';
   }

   private static int countLumberyards( char[][] field, int x, int y ) {
      return countType(field, x, y, '#');
   }

   private static int countTrees( char[][] field, int x, int y ) {
      return countType(field, x, y, '|');
   }

   private static int countType( char[][] field, int x, int y, char c ) {
      int counter = 0;
      for (int i = x-1; i <= x+1; i++) {
         for (int j = y-1; j <= y+1; j++) {
            if ( (j >= 0 && i >= 0 && i < field.length && j < field[i].length) && !(i==x && j==y)) {
               if (field[i][j] == c) {
                  counter++;
               }
            }

         }
      }
      return counter;
   }

}
