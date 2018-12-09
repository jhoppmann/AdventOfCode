package de.jhoppmann.aoc2018.day8;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static de.jhoppmann.aoc2018.day8.Input.input;

/**
 * @author jhoppman
 */
public class MetadataCalculator {

	public static void main(String[] args) {
		List<Integer> values = new ArrayList<>(input);

		Node tree = new Node(values);

		System.out.println("Metadata sum: " + tree.getSumOfMetadata());
		System.out.println("Value of root node: " + tree.calculateNodeValue());
	}
}
