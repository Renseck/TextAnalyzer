#!/usr/bin/env python3
from _src.textanalyzer import textAnalyzer

def main():
    # Create a text analyzer instance with input and output files
    analyzer = textAnalyzer("input.txt", "console")
    
    # Use the new author analysis feature to analyze Carla Rus's messages
    author_name = "Carla Rus:"
    analyzer.output_author_analysis(author_name)
    
    # # Alternative longer version
    # results = analyzer.analyze_author_messages(author_name)
    # # Output the results based on the output file setting
    # if analyzer.output_file:
    #     import json
    #     analyzer.write(json.dumps(results, indent=2))
    # else:
    #     print(f"\nAnalysis of {author_name} messages:")
    #     print(f"Total messages found: {results['total_messages']}")
    #     print(f"Total spaces: {results['total_spaces']}")
    #     print(f"Total words: {results['total_words']}")
    #     print(f"Overall space-to-word ratio: {results['space_to_word_ratio']:.2f}")
    #     print(f"Overall maximum space-to-word ratio: {results['max_space_to_word_ratio']:.2f}")


if __name__ == "__main__":
    main()