import json
import sys

def json_to_html_table(data):
    if isinstance(data, dict):
        # Start a new table for a dictionary
        html = '<table border="1">'
        for key, value in data.items():
            html += '<tr>'
            html += f'<th>{key}</th>'
            html += '<td>'
            html += json_to_html_table(value)
            html += '</td>'
            html += '</tr>'
        html += '</table>'
    elif isinstance(data, list):
        # Create a table for a list
        html = '<table border="1">'
        for item in data:
            html += '<tr>'
            html += '<td>'
            html += json_to_html_table(item)
            html += '</td>'
            html += '</tr>'
        html += '</table>'
    else:
        # Base case: if it's not a list or dict, return as plain text
        html = str(data)
    return html

def convert_json_to_html(json_input, output_file):
    # Convert JSON data to an HTML table
    html_table = json_to_html_table(json_input)
    
    # Wrap the table in basic HTML structure
    html_content = f'''
    <html>
    <head><title>JSON to HTML</title></head>
    <style>
    table, th, td {
      border: 1px solid black;
      border-collapse: collapse;
    }
    </style>    
    <body>
    {html_table}
    </body>
    </html>
    '''
    
    # Write to an HTML file
    with open(output_file, 'w') as file:
        file.write(html_content)

if __name__ == "__main__":
    # Check if the correct number of arguments are passed
    if len(sys.argv) != 3:
        print("Usage: python json_to_html.py <input_json_file> <output_html_file>")
        sys.exit(1)

    # Get the input and output file paths from command line arguments
    input_json_file = sys.argv[1]
    output_html_file = sys.argv[2]

    # Read the JSON data from the input file
    try:
        with open(input_json_file, 'r') as file:
            json_data = json.load(file)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        sys.exit(1)

    # Convert JSON to HTML and save the output
    convert_json_to_html(json_data, output_html_file)
    print(f"HTML table successfully generated and saved to {output_html_file}")
