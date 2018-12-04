package de.jhoppmann.aoc2017.day5;

import java.util.Arrays;

public class Jumper {

    public static void main(String[] args) {
        int[] jumpInstructions = Arrays.copyOf(Input.jumps, Input.jumps.length);

        int index = 0;
        int jumps = 0;

        while (index >= 0 && index < jumpInstructions.length) {
            index += jumpInstructions[index]++;
            jumps++;
        }

        System.out.println(jumps);
    }
}
