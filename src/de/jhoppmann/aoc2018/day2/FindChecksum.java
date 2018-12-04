package de.jhoppmann.aoc2018.day2;

/**
 * @author jhoppman
 */
public class FindChecksum {

	public static void main(String[] args) {
		int exactlyTwo = 0;
		int exactlyThree = 0;
		for (String boxId : Input.input) {
			if (hasNLetters(boxId, 2)) {
				exactlyTwo++;
			}
			if (hasNLetters(boxId, 3)) {
				exactlyThree++;
			}
		}
		System.out.println(exactlyThree * exactlyTwo);
	}

	private static boolean hasNLetters(String boxId, int n) {
		for (char a = 'a'; a <= 'z'; a++) {
			if (boxId.length() - replacer(boxId, a) == n) {
				return true;
			}
		}
		return false;
	}

	private static int replacer(String boxId, char character) {
		String charString = String.valueOf(character);
		return boxId.replace(charString, "").length();
	}
}
