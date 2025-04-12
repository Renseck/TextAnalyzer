class analyzer():
    
    def __init__(self, input_file: str, output_file = None):
        self.input_file = input_file
        self.output_file = output_file
    
    def read(self):
        """Read the entire file into memory and return the content."""
        with open(self.input_file, "r", encoding="utf-8") as file:
            return file.read()

    def read_lines(self):
        """Process the file line by line without loading it all into memory.
        Returns a generator that yields each line."""
        with open(self.input_file, "r", encoding="utf-8") as file:
            for line in file:
                yield line.rstrip('\n')
    
    def process_line_by_line(self, line_processor_func):
        """Process each line with a custom function and collect results.
        
        Args:
            line_processor_func: A function that takes a line string and returns a result
        
        Returns:
            A list containing the results of processing each line
        """
        results = []
        for line in self.read_lines():
            result = line_processor_func(line)
            if result is not None:
                results.append(result)
        return results

    def write(self, data):
        """Write data either to terminal or to an output file

        Args:
            data (array): The data to be written
        """
        if self.output_file is None:
            print(data)
        elif type(self.output_file) == str:
            with open(self.output_file, "w") as file:
                file.write(data)