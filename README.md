# Canvas Grade Reading and Updating Project

This project aims to read and update student grades in Canvas based on an Excel file.

## Requirements

- Python 3.6 or higher
- Pandas 1.2.4 or higher
- A Canvas account with course reading and grade download permissions
- An Excel file with grades downloaded from Canvas

## Installation

1. Clone or download this repository to your computer.

2. Install the necessary dependencies with the following command in your terminal:

pip install pandas


## Usage

1. Ensure you have an Excel file with grades from Canvas for the course you want to process.

2. Open the `grade_reader.py` file in your preferred code editor.

3. Modify the path to the Excel file in line 5 of the code to match the location of your downloaded file:

```python
file_path = 'path/to/your/grades_file.xlsx'
```
Modify the group and activity codes in lines 8 to 14 of the code to match those used in the course you want to process.

Run the grade_reader.py file from the terminal or your code editor.

Contributions
Contributions are welcome. If you have suggestions or improvements for this project, please create a pull request or contact the repository owner.

## Canvas API Integration
This project also includes an integration with the Canvas API for reading and updating grades on the platform. Here are two available functions for interacting with Canvas:

## Read Grades
The read(group, activity) function allows you to retrieve student grades in a specific group and activity in Canvas. You need to provide the group ID and activity ID.

