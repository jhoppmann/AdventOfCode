package de.jhoppmann.aoc2018.day1;

import java.util.HashSet;
import java.util.Set;

/**
 * @author jhoppman
 */
public class DoubleFrequencyFinder {

	public static void main(String[] args) {
		Set<Integer> reached = new HashSet<>();
		boolean found = false;
		int frequency = 0;
		reached.add(frequency);
		while (!found) {
			for (Integer integer : NumberAdder.input) {
				frequency += integer;
				if (reached.contains(frequency)) {
					System.out.println(frequency);
					found = true;
					break;
				} else {
					reached.add(frequency);
				}
			}
		}
	}
}
