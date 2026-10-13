import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;
import java.util.Arrays;
import java.io.File;
import java.io.FileNotFoundException;

public class main {
    public static void main(String[] args) {
        // NEW (Day 6): Read text from files instead of manual typing
        String resumeText = readFile("resume.txt");
        String jdText = readFile("jobdescription.txt");
        
        if (resumeText == null || jdText == null) {
            System.out.println("Error: Could not read one of the files. Make sure resume.txt and jobdescription.txt exist in the project folder.");
            return;
        }
        
        System.out.println("Resume file loaded successfully.");
        System.out.println("Job description file loaded successfully.");
        
        Set<String> resumeKeywords = extractKeywords(resumeText);
        Set<String> jdKeywords = extractKeywords(jdText);
        
        Set<String> matchedKeywords = new HashSet<>(jdKeywords);
        matchedKeywords.retainAll(resumeKeywords);
        
        Set<String> missingKeywords = new HashSet<>(jdKeywords);
        missingKeywords.removeAll(resumeKeywords);
        
        double matchPercentage = 0;
        if (jdKeywords.size() > 0) {
            matchPercentage = ((double) matchedKeywords.size() / jdKeywords.size()) * 100;
        }
        
        printReport(matchPercentage, matchedKeywords, missingKeywords);
    }
    
    // NEW (Day 6): Reads a text file and returns its content as a String
    public static String readFile(String filename) {
        StringBuilder content = new StringBuilder();
        try {
            File file = new File(filename);
            Scanner fileScanner = new Scanner(file);
            
            while (fileScanner.hasNextLine()) {
                content.append(fileScanner.nextLine());
                content.append(" ");
            }
            
            fileScanner.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + filename);
            return null;
        }
        
        return content.toString();
    }
    
    public static Set<String> extractKeywords(String text) {
        text = text.toLowerCase();
        text = text.replaceAll("[^a-z0-9\\s]", "");
        String[] wordsArray = text.split("\\s+");
        
        Set<String> stopWords = new HashSet<>(Arrays.asList(
            "with", "and", "the", "a", "an", "of", "in", "on", "for", 
            "is", "are", "to", "at", "as", "by", "or", "looking", "experience"
        ));
        
        Set<String> keywords = new HashSet<>();
        for (String word : wordsArray) {
            if (!word.isEmpty() && !stopWords.contains(word)) {
                keywords.add(word);
            }
        }
        
        return keywords;
    }
    
    public static void printReport(double matchPercentage, Set<String> matched, Set<String> missing) {
        System.out.println("\n=======================================");
        System.out.println("        RESUME MATCH REPORT");
        System.out.println("=======================================");
        
        System.out.printf("Match Score: %.2f%%\n", matchPercentage);
        
        System.out.println("\nMatched Skills:");
        if (matched.isEmpty()) {
            System.out.println("  (None found)");
        } else {
            for (String skill : matched) {
                System.out.println("  - " + skill);
            }
        }
        
        System.out.println("\nMissing Skills:");
        if (missing.isEmpty()) {
            System.out.println("  (None! Your resume covers everything)");
        } else {
            for (String skill : missing) {
                System.out.println("  - " + skill);
            }
        }
        
        System.out.println("\nSuggestion:");
        if (matchPercentage >= 80) {
            System.out.println("  Excellent match! Your resume is well aligned with this job.");
        } else if (matchPercentage >= 50) {
            System.out.println("  Decent match. Try adding the missing skills above to improve your chances.");
        } else {
            System.out.println("  Low match. Consider tailoring your resume to include more relevant skills.");
        }
        
        System.out.println("=======================================");
    }
}