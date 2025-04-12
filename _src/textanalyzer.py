from .analyzer import analyzer
import re
import json

class textAnalyzer(analyzer):
    
    def getSpaceCount(self, line: str):
        """Count spaces in a single line."""
        spaceCount = line.count(' ')
        return spaceCount

    def getWordCount(self, line: str):
        """Count words in a single line."""
        wordCount = len(re.findall(r'\w+', line))
        return wordCount
    
    def space2wordRatio(self, line: str):
        """Calculate the space to word ratio for a single line."""
        spaces = self.getSpaceCount(line)
        words = self.getWordCount(line)
        return spaces / words if words > 0 else 0
    
    def analyze_text(self):
        """Process the entire file line by line and provide aggregated analysis."""
        total_spaces = 0
        total_words = 0
        line_count = 0
        
        # Process each line
        for line in self.read_lines():
            if line.strip():  # Skip empty lines
                line_count += 1
                spaces = self.getSpaceCount(line)
                words = self.getWordCount(line)
                total_spaces += spaces
                total_words += words
        
        # Return analysis results
        return {
            "total_lines": line_count,
            "total_spaces": total_spaces,
            "total_words": total_words,
            "average_spaces_per_line": total_spaces / line_count if line_count > 0 else 0,
            "average_words_per_line": total_words / line_count if line_count > 0 else 0,
            "overall_space_to_word_ratio": total_spaces / total_words if total_words > 0 else 0
        }
    
    def analyze_line_by_line(self):
        """Analyze the text line by line and return detailed results for each line."""
        results = []
        
        for i, line in enumerate(self.read_lines()):
            if not line.strip():  # Skip empty lines
                continue
                
            spaces = self.getSpaceCount(line)
            words = self.getWordCount(line)
            ratio = spaces / words if words > 0 else 0
            
            results.append({
                "line_number": i + 1,
                "line": line[:50] + "..." if len(line) > 50 else line,  # Truncate long lines
                "spaces": spaces,
                "words": words,
                "space_to_word_ratio": ratio
            })
            
        return results
    
    def find_lines_with_pattern(self, pattern):
        """Find lines that match a specific regex pattern."""
        regex = re.compile(pattern)
        matching_lines = []
        
        for i, line in enumerate(self.read_lines()):
            if regex.search(line):
                matching_lines.append({
                    "line_number": i + 1,
                    "line": line
                })
                
        return matching_lines

    def extract_author_messages(self, author_name):
        """
        Extract all messages from a specific author.
        
        Args:
            author_name (str): The name of the author to search for (e.g., "Carla Rus:")
            
        Returns:
            list: A list of message strings from the specified author
        """
        messages = []
        
        for line in self.read_lines():
            if author_name in line:
                # Extract the message part (everything after the author name)
                message_part = line.split(author_name, 1)[1].strip()
                
                # Only include non-empty messages
                if message_part:
                    messages.append(message_part)
                    
        return messages
    
    def analyze_message_metrics(self, message):
        """
        Analyze a single message for spaces, words, and ratio.
        
        Args:
            message (str): The message to analyze
            
        Returns:
            dict: A dictionary containing the analysis metrics
        """
        spaces = self.getSpaceCount(message)
        words = self.getWordCount(message)
        ratio = self.space2wordRatio(message)
        
        return {
            "message": message[:50] + "..." if len(message) > 50 else message,
            "spaces": spaces,
            "words": words,
            "ratio": ratio
        }
    
    def analyze_author_messages(self, author_name, truncate_length=50):
        """
        Analyze all messages from a specific author.
        
        Args:
            author_name (str): The name of the author to analyze (e.g., "Carla Rus:")
            truncate_length (int): Length at which to truncate messages in the output
            
        Returns:
            dict: A dictionary containing the aggregated analysis and details of each message
        """
        # Extract all messages from the specified author
        author_messages = self.extract_author_messages(author_name)
        
        # Initialize counters
        total_spaces = 0
        total_words = 0
        
        # Analyze each message
        message_details = []
        max_ratio = 0
        
        for msg in author_messages:
            metrics = self.analyze_message_metrics(msg)
            message_details.append(metrics)
            
            # Update aggregated counts
            total_spaces += metrics["spaces"]
            total_words += metrics["words"]
            
            # Track maximum ratio
            if metrics["ratio"] > max_ratio:
                max_ratio = metrics["ratio"]
        
        # Calculate overall ratio
        overall_ratio = total_spaces / total_words if total_words > 0 else 0
        
        # Compile results
        results = {
            "total_messages": len(author_messages),
            "total_spaces": total_spaces,
            "total_words": total_words,
            "space_to_word_ratio": overall_ratio,
            "max_space_to_word_ratio": max_ratio,
            "messages": message_details
        }
        
        return results
    
    def output_author_analysis(self, author_name, output_format="console"):
        """
        Analyze and output results for a specific author's messages.
        
        Args:
            author_name (str): The name of the author to analyze (e.g., "Carla Rus:")
            output_format (str): Format to output results ("console" or "file")
            
        Returns:
            The analysis results dictionary
        """
        results = self.analyze_author_messages(author_name)
        
        if output_format == "console" or not self.output_file:
            # Print nicely formatted results to console
            print(f"\nAnalysis of {author_name} messages:")
            print(f"Total messages found: {results['total_messages']}")
            print(f"Total spaces: {results['total_spaces']}")
            print(f"Total words: {results['total_words']}")
            print(f"Overall space-to-word ratio: {results['space_to_word_ratio']:.2f}")
            print(f"Overall maximum space-to-word ratio: {results['max_space_to_word_ratio']:.2f}")
            
            # Optionally print individual message details
            # if results['messages'] and show_details:
            #     print("\nIndividual messages:")
            #     for i, msg_data in enumerate(results['messages'], 1):
            #         print(f"{i}. \"{msg_data['message']}\"")
            #         print(f"   Spaces: {msg_data['spaces']}, Words: {msg_data['words']}, Ratio: {msg_data['ratio']:.2f}")
        else:
            # Write results to output file
            self.write(json.dumps(results, indent=2))
            
        return results