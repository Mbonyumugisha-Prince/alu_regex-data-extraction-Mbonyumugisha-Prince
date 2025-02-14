import re

class DataExtractor:
    def __init__(self):
        #Email pattern
        self.email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        #Phone number pattern
        self.phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'

        #URL pattern
        self.url_pattern = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'

        #Credit card pattern
        self.credit_card_pattern = r'\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}'
        
        #Time pattern
        self.time_pattern = r'(?:(?:2[0-3]|[01]?[0-9]):[0-5][0-9](?:\s?[AaPp][Mm])?)'
        
        #Html tag pattern
        self.html_tag_pattern = r'<[^>]+>'

        #Hashtag pattern
        self.hashtag_pattern = r'#[A-Za-z0-9_]+(?![A-Za-z0-9_])'

        #Currency pattern
        self.currency_pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'

    def validate_input(self, text, pattern_type):
        """Validates if input matches expected format """
        if not text.strip():
            return False, "Input text is empty"

        patterns = {
            'email': (self.email_pattern, "Invalid email format. Expected format: user@example.com"),
            'url': (self.url_pattern, "Invalid URL format. Expected format: https://www.example.com"),
            'phone': (self.phone_pattern, "Invalid phone number format. Expected format: (123) 456-7890 or 123-456-7890"),
            'credit_card': (self.credit_card_pattern, "Invalid credit card format. Expected format: 1234 5678 9012 3456"),
            'time': (self.time_pattern, "Invalid time format. Expected format: 14:30 or 2:30 PM"),
            'html': (self.html_tag_pattern, "Invalid HTML tag format. Expected format: <tag> or <tag attribute='value'>"),
            'hashtag': (self.hashtag_pattern, "Invalid hashtag format. Expected format: #example"),
            'currency' : (self.currency_pattern, "Invalid currency format. Expected format: $19.99 or $1,234.56")
        }   

        if pattern_type not in patterns:
            return False, "Invalid pattern type." 
        
        pattern, error_message = patterns[pattern_type]
        matches = re.findall(pattern, text)

        if not matches:
            return False, error_message
        return True, matches
    
    def extract_with_validation(self, text, extraction_type):
        """Extracts data from text using a specified pattern"""
        is_valid, result  = self.validate_input(text, extraction_type)
        if not is_valid:
            return [], result   # Return empty list and error message
        
        return result, None  # Return matches and no error
    
def main():
    extractor = DataExtractor()

    print("\nWelcome to the Data Extractor!")
    print("This tool can extract various types of data from your text.")

    while True:
       print("\nAvailable extraction options:")
       print("1. Email addresses (e.g., user@example.com)")
       print("2. URLs (e.g., https://www.example.com)")
       print("3. Phone numbers (e.g., (123) 456-7890)")
       print("4. Credit card numbers (e.g., 1234 5678 9012 3456)")
       print("5. Time formats (e.g., 14:30 or 2:30 PM)")
       print("6. HTML tags (e.g., <p> or <div class='example'>)")
       print("7. Hashtags (e.g., #example)")
       print("8. Currency amounts (e.g., $19.99)")
       print("0. Exit")
        
       choice = input("\nEnter your choice (0-8): ")

       if choice == '0':
            print("Thank you for using Data Extractor!")
            break
            
       if choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print("Invalid choice. Please try again.")
            continue
            
       text = input("\nEnter the text to analyze: ")

       print("\nResults:")
       print("-" * 50)

       # Map choices to extraction types
       extraction_types = {
           '1': 'email',
           '2': 'url',
           '3': 'phone',
           '4': 'credit_card',
           '5': 'time',
           '6': 'html',
           '7': 'hashtag',
           '8': 'currency'
       }

       matches, error = extractor.extract_with_validation(text, extraction_types[choice])

       if error:
           print("Error:", error)
       else:
           if matches:
               print("Extracted data:")
               for match in matches:
                   print(f"- {match}")
           else:
               print("No valid matches found in the input text.")

       input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()                      