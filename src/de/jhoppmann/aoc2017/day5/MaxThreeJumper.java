package de.jhoppmann.aoc2017.day5;

import java.util.Arrays;

public class MaxThreeJumper {

    public static void main(String[] args) {
        int[] jumpInstructions = Arrays.copyOf(Input.jumps, Input.jumps.length);

        int index = 0;
        int jumps = 0;
        int indexMax = 0;

        while (index >= 0 && index < jumpInstructions.length) {
            if (jumpInstructions[index] >= 3) {
                index += jumpInstructions[index]--;
            } else {
                index += jumpInstructions[index]++;
            }

            jumps++;
            if (index > indexMax) {
                indexMax = index;
                System.out.println("new max " + indexMax);
            }
        }

        System.out.println(jumps);
    }
}
