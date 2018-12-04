package de.jhoppmann.aoc2017.day1;

public class CalcHalfwayRound {

    public static void main(String[] args) {
        String input = CalcNumbers.input;
        int index = 0;
        int peek;
        int sum = 0;
        int offset = (int) (input.length() / 2d);
        while (true) {
            if (index == input.length()) {
                break;
            } else {
                peek = index + offset;
                if (peek >= input.length()) {
                    peek = peek - input.length();
                }
            }
            if (input.charAt(index) == input.charAt(peek)) {
                sum += (input.charAt(index) - 48);
                System.out.println(input.charAt(index)+ " (" + index +")" + " matches " + input.charAt(peek) + " (" + peek +")");
            }
            index++;
        }

        System.out.println("Sum: " + sum);
    }
}
