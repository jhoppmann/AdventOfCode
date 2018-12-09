package de.jhoppmann.aoc2018.day8;

import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * @author jhoppman
 */
public class Input {

	public static List<Integer> input = loadInput();

	private static List<Integer> loadInput() {
		try {
			File f = new File("src/de/jhoppmann/aoc2018/day8/input");
			System.out.println(f.getAbsolutePath());
			FileReader fileReader = new FileReader(f);
			BufferedReader reader = new BufferedReader(fileReader);
			String input = reader.readLine();
			String[] values = input.split(" ");
			List<Integer> output = new ArrayList<>();
			for (String value : values) {
				output.add(Integer.valueOf(value));
			}

			return output;
		} catch (IOException e) {
			e.printStackTrace();
		}

		return Collections.emptyList();
	}
}
