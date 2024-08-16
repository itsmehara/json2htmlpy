import json

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
    <body>
    {html_table}
    </body>
    </html>
    '''
    
    # Write to an HTML file
    with open(output_file, 'w') as file:
        file.write(html_content)

# Sample JSON data (3 levels deep with dicts and lists)
sample_json = {
    "name": "John",
    "age": 30,
    "children": [
        {
            "name": "Anna",
            "age": 10,
            "hobbies": ["reading", "painting"]
        },
        {
            "name": "Tom",
            "age": 5,
            "hobbies": ["games", {"outdoor": "football", "indoor": "chess"}]
        }
    ],
    "address": {
        "street": "123 Maple Street",
        "city": "Wonderland",
        "postal": "12345"
    }
}

# Convert the sample JSON to HTML and save it to a file
convert_json_to_html(sample_json, 'output.html')
