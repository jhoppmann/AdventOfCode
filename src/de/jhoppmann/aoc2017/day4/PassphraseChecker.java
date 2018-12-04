package de.jhoppmann.aoc2017.day4;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class PassphraseChecker {

    public static void main(String[] args) {
        int accepted = 0;
        for (String input : Input.inputStrings) {
            String[] words = input.split("\\s");
            Set<String> uniques = new HashSet<>(Arrays.asList(words));
            if (uniques.size() == words.length) {
                accepted++;
            }
        }

        System.out.println(accepted);
    }
}
