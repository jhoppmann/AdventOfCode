package de.jhoppmann.aoc2018.day14;

import java.util.ArrayList;
import java.util.List;

/**
 * @author jhoppman
 */
public class RecipeTrainer {

	public static int input = 293801;

	public static void main(String[] args) {
		String firstPart = findRecipeFor(293801, 10);
		System.out.println(firstPart);

		String secondPart = findSequence(293801);
		System.out.println(secondPart);
	}

	private static String findSequence(int sequence) {
		List<Integer> recipes = new ArrayList<>();
		recipes.add(3);
		recipes.add(7);
		int firstElf = 0;
		int secondElf = 1;

		while (!endsWithSequence(recipes, sequence)) {
			int sum = recipes.get(firstElf) + recipes.get(secondElf);
			if (sum >= 10) {
				recipes.add(1);
				sum -= 10;
			}
			recipes.add(sum);

			int newFirstElfPosition = firstElf + recipes.get(firstElf) + 1;
			int newSecondElfPosition = secondElf + recipes.get(secondElf) + 1;
			while (newFirstElfPosition > recipes.size() - 1) {
				newFirstElfPosition -= recipes.size();
			}
			while (newSecondElfPosition > recipes.size() - 1) {
				newSecondElfPosition -= recipes.size();
			}
			firstElf = newFirstElfPosition;
			secondElf = newSecondElfPosition;
		}
		return recipes.size() - String.valueOf(sequence).length() + "";
	}

	private static boolean endsWithSequence(List<Integer> recipes, int sequence) {
		String sequenceString = String.valueOf(sequence);
		if (sequenceString.length() + 2 > recipes.size()) {
			return false;
		}
		boolean firstMatches = true;
		for (int i = 0; i < sequenceString.length(); i++) {
			char number = sequenceString.charAt(i);
			int numAtPos = (int) number - 48;
			if (recipes.get(recipes.size() - 1 - sequenceString.length() + i) != numAtPos) {
				firstMatches = false;
				break;
			}
		}
		boolean secondMatches = true;
		for (int i = 0; i < sequenceString.length(); i++) {
			char number = sequenceString.charAt(i);
			int numAtPos = (int) number - 48;
			if (recipes.get(recipes.size() - 2 - sequenceString.length() + i) != numAtPos) {
				secondMatches = false;
				break;
			}
		}
		if (firstMatches) {
			System.out.println("First Matches, reduce answer by one");
		}
		if (secondMatches) {
			System.out.println("Second matches, reduce answer by two");
		}
		return firstMatches || secondMatches;
	}

	private static String findRecipeFor(int improvementRecipes, int useableRecipes) {
		List<Integer> recipes = new ArrayList<>();
		recipes.add(3);
		recipes.add(7);
		int firstElf = 0;
		int secondElf = 1;

		while (recipes.size() < improvementRecipes + useableRecipes) {
			int sum = recipes.get(firstElf) + recipes.get(secondElf);
			if (sum >= 10) {
				recipes.add(1);
				sum -= 10;
			}
			recipes.add(sum);

			int newFirstElfPosition = firstElf + recipes.get(firstElf) + 1;
			int newSecondElfPosition = secondElf + recipes.get(secondElf) + 1;
			while (newFirstElfPosition > recipes.size() - 1) {
				newFirstElfPosition -= recipes.size();
			}
			while (newSecondElfPosition > recipes.size()-1) {
				newSecondElfPosition -= recipes.size();
			}
			firstElf = newFirstElfPosition;
			secondElf = newSecondElfPosition;

		}

		StringBuilder result = new StringBuilder();
		for (int i = improvementRecipes; i < improvementRecipes + useableRecipes; i++) {
			result.append(recipes.get(i));
		}

		return result.toString();
	}

}

