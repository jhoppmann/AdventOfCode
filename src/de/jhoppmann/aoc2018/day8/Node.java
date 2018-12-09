package de.jhoppmann.aoc2018.day8;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * @author jhoppman
 */
class Node {

	private int numChildren = 0;

	private int numMetadata = 0;

	private List<Node> children;

	private int[] metadata;

	Node( List<Integer> values) {
		if (values.size() >= 2) {
			numChildren = values.remove(0);
			numMetadata = values.remove(0);


			children = new ArrayList<>();
			while (children.size() < numChildren) {
				getRestAfterChild(values);
			}
			metadata = new int[numMetadata];
			for (int i = 0; i < numMetadata; i++) {
				metadata[i] = values.get(0);
				values.remove(0);
			}

		}
	}

	private void getRestAfterChild(List<Integer> values) {
		children.add(new Node(values));
	}

	int getSumOfMetadata() {
		int sumOfMetadata = Arrays.stream(metadata).sum();
		sumOfMetadata += children.stream().mapToInt(Node::getSumOfMetadata).sum();
		return sumOfMetadata;
	}

	int calculateNodeValue() {

		if (children.isEmpty()) {
			return Arrays.stream(metadata).sum();
		} else {
			int value = 0;
			for(int i = 0; i < metadata.length; i++) {
				if (metadata[i] <= children.size()) {
					value += children.get(metadata[i] - 1).calculateNodeValue();
				}
			}
			return value;
		}

	}
}
