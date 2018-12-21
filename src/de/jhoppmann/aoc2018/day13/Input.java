package de.jhoppmann.aoc2018.day13;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

/**
 * @author jhoppman
 */
public class Input {

	private static char[][] tracks;

	public static char[][] loadInput() {
		try {
			File f = new File("src/de/jhoppmann/aoc2018/day13/input");
			System.out.println(f.getAbsolutePath());
			FileReader fileReader = new FileReader(f);
			BufferedReader reader = new BufferedReader(fileReader);

			List<String> allLines = reader.lines().collect(Collectors.toList());
			int lines = allLines.size();
			int longest = allLines.stream().mapToInt(String::length).max().orElse(0);

			tracks = new char[lines][longest];

			int lineIndex = 0;
			for (String line : allLines) {
				tracks[lineIndex++] = line.toCharArray();
			}
		} catch (IOException e) {
			e.printStackTrace();
		}

		return tracks;
	}
}
