package de.jhoppmann.aoc2017.day4;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class AnagramChecker {
    public static void main(String[] args) {
        int accepted =0;
        for (String passphrase : Input.inputStrings) {
            String[] words = passphrase.split("\\s");
            int numberWithoutAnagrams = findAnagrams(words);
            if (words.length == numberWithoutAnagrams) {
                accepted++;
            }
        }
        System.out.println(accepted);
    }

    private static int findAnagrams(String[] words) {
        Set<String> uniqueWords = new HashSet<>();
        for (String word : words) {
            uniqueWords.add(sortWordAlphabetically(word));
        }

        return uniqueWords.size();
    }

    private static String sortWordAlphabetically(String word) {
        char[] chars = word.toCharArray();
        Arrays.sort(chars);
        return String.valueOf(chars);

    }
}
