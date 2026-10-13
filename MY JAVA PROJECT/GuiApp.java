import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Set;
import java.util.HashSet;
import java.util.Arrays;

public class GuiApp {
    public static void main(String[] args) {
        // Create the main window
        JFrame frame = new JFrame("Smart Resume Screener & Job Matcher");
        frame.setSize(600, 600);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout(10, 10));
        
        // Top panel: two text areas side by side
        JPanel inputPanel = new JPanel(new GridLayout(1, 2, 10, 10));
        
        JTextArea resumeArea = new JTextArea();
        resumeArea.setLineWrap(true);
        resumeArea.setBorder(BorderFactory.createTitledBorder("Paste Resume Text"));
        
        JTextArea jdArea = new JTextArea();
        jdArea.setLineWrap(true);
        jdArea.setBorder(BorderFactory.createTitledBorder("Paste Job Description"));
        
        inputPanel.add(new JScrollPane(resumeArea));
        inputPanel.add(new JScrollPane(jdArea));
        
        // Button
        JButton checkButton = new JButton("Check Match");
        
        // Bottom: result display area
        JTextArea resultArea = new JTextArea();
        resultArea.setEditable(false);
        resultArea.setBorder(BorderFactory.createTitledBorder("Result"));
        
        // What happens when button is clicked
        checkButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String resumeText = resumeArea.getText();
                String jdText = jdArea.getText();
                
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
                
                String suggestion;
                if (matchPercentage >= 80) {
                    suggestion = "Excellent match! Your resume is well aligned with this job.";
                } else if (matchPercentage >= 50) {
                    suggestion = "Decent match. Try adding the missing skills below.";
                } else {
                    suggestion = "Low match. Consider tailoring your resume.";
                }
                
                StringBuilder report = new StringBuilder();
                report.append(String.format("Match Score: %.2f%%\n\n", matchPercentage));
                report.append("Matched Skills: ").append(matchedKeywords).append("\n\n");
                report.append("Missing Skills: ").append(missingKeywords).append("\n\n");
                report.append("Suggestion: ").append(suggestion);
                
                resultArea.setText(report.toString());
            }
        });
        
        // Arrange everything in the window
        frame.add(inputPanel, BorderLayout.NORTH);
        frame.add(checkButton, BorderLayout.CENTER);
        frame.add(new JScrollPane(resultArea), BorderLayout.SOUTH);
        
        frame.setVisible(true);
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
}
    
