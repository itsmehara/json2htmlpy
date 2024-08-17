# JSON to HTML Table Converter

This Python project provides a script to convert a nested JSON structure into an HTML file that represents the data in a tabular format. It can handle JSON objects with multiple levels of nesting, including lists containing dictionaries and vice versa.

## Features

- **Recursive Conversion**: The script processes nested dictionaries and lists, creating a well-structured HTML table.
- **Versatile Data Handling**: Supports JSON data with various complexities, including lists of dictionaries, lists of lists, and deeply nested structures.
- **Easy to Use**: Simply provide the JSON input and the desired output HTML file name.

## Project Structure

```
json2htmlpy/                # Root of the repository
├── json2htmlpy/            # Package directory (same name as the package)
│   ├── __init__.py         # Makes it a package; can be empty or contain initialization code
│   ├── jsontohtml.py       # Main Python script
├── setup.py                # Setup script for packaging
├── README.md               # Project’s README
├── LICENSE                 # License for the package
├── pyproject.toml
└── .github/
    └── workflows/
        └── python-publish.yml  # GitHub Actions workflow
```

## Getting Started

### Prerequisites

- Python 3.x
- Basic understanding of JSON structures

### Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/itsmehara/json2htmlpy.git
   cd json2htmlpy
   ```

2. **Prepare the Environment**
   - Ensure you have Python 3 installed on your system.
   - (Optional) Set up a virtual environment.
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

### Usage

1. **Place the JSON File**
   - Place the JSON file you wish to convert into the project directory or provide the path to the file.

2. **Run the Script**
   - Execute the Python script with your JSON data and desired output HTML file name.
   ```sh
   python json2htmlpy/jsontohtml.py sample_json.json output.html
   ```

   - You can also modify the script directly by changing the `sample_json` variable to your JSON structure.

3. **Check the Output**
   - The HTML file will be generated in the project directory or your specified location. Open the `output.html` file in any web browser to view the structured data.

### Example

Here is a sample JSON structure and the corresponding HTML output:

**Sample JSON:**

```json
{
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
```

**Generated HTML Table:**

- The `name`, `age`, and `address` fields appear as headers with their respective values.
- The `children` field is a list of dictionaries, each represented as a nested table.
- Complex nested structures are handled by recursively creating tables within tables.

### Customization

You can customize the script to adjust the appearance of the HTML table, including adding CSS styles, modifying table attributes, or extending the logic to handle more specific cases.

----

## Building and Installing

To build and install this package, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/itsmehara/json2htmlpy.git
   cd json2htmlpy
   ```

2. **Install Build Tools**  If you don't have the `build` package installed, you can add it with:
   ```bash
   pip install build
   ```

3. **Build the Package** Create distribution files (source and wheel):
   ```bash
   python -m build
   ```
   This will generate `.tar.gz` and `.whl` files in the `dist` directory.

4. **Install the Package** You can install the package locally using `pip`:
   ```bash
   pip install dist/json2htmlpy-0.1.0-py3-none-any.whl
   ```

   Alternatively, install in editable mode for development:

   ```bash
   pip install -e .
   ```

   This allows changes to the code to be immediately reflected without reinstalling.
   
----

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and create a pull request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

----

### License

Distributed under the MIT License. See `LICENSE` for more information.

# Contact

For any questions or issues, feel free to open an issue on the GitHub repository or contact me directly at [hara2help@gmail.com](mailto:hara2help@gmail.com).

