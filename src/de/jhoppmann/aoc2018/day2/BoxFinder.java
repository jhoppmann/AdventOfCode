package de.jhoppmann.aoc2018.day2;

/**
 * @author jhoppman
 */
public class BoxFinder {
	public static void main(String[] args) {
		for (String first : Input.input) {
			for (String second : Input.input) {
				if (isOneOff(first, second)) {
					System.out.println(removeDifferingCharacter(first, second));
				}
			}
		}
	}

	private static String removeDifferingCharacter(String first, String second) {
		for (int i = 0; i < first.length(); i++) {
			if(first.charAt(i) != second.charAt(i)) {
				return first.substring(0, i) + first.substring(i+1);
			}
		}
		return null;
	}

	private static boolean isOneOff(String first, String second) {
		int foundDifferences = 0;
		for (int i = 0; i < first.length(); i++) {
			if (first.charAt(i) != second.charAt(i)) {
				foundDifferences++;
			}
		}
		return foundDifferences == 1;
	}
}
