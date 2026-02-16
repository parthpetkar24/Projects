# Library Management System

A simple command-line based Library Management System built with Python and Pandas. This system allows librarians to manage book inventory, track issued books, and handle book returns efficiently.

## Features

- **Add Books**: Add new books to the library catalog with ID, name, author, and publication year
- **Issue Books**: Issue books to borrowers with contact details and issue date tracking
- **Remove Books**: Remove books from the library by ID or name
- **Return Books**: Process book returns and update inventory automatically
- **View Current Books**: Display all available books in the library
- **View Issued Books**: Track all currently issued books and borrower information
- **Persistent Storage**: All data is stored in CSV files for easy access and portability

## Project Structure
```
Library Management System/
│
├── lib.py              # Main application file
├── index.csv           # Library catalog (available books)
├── issue.csv           # Issued books tracker
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## Requirements

- Python 3.10 or higher (uses `match` statement)
- pandas library

## Installation

1. **Clone or download the project files**

2. **Install required dependencies**:
```bash
   pip install -r requirements.txt
```

3. **Create the project directory**:
```bash
   mkdir "Library Management"
```

4. **Place the CSV files in the directory**:
   - Move `index.csv` and `issue.csv` to the "Library Management" folder
   - If these files don't exist, the program will create them automatically

## Usage

1. **Run the application**:
```bash
   python lib.py
```

2. **Navigate the menu**:
```
   Operations Available:
   1. Add Book
   2. Issue Book
   3. Remove book from Library
   4. View Current Books in Library
   5. View Issued Books
   6. Return Book
   7. Exit
```

3. **Follow the prompts** for each operation

### Example Workflows

#### Adding a Book
```
Enter Index of Operation: 1
Enter Book Id: 101
Enter Book Name: The Great Gatsby
Enter Book Author Name: F. Scott Fitzgerald
Enter Book Publication Year: 1925
```

#### Issuing a Book
```
Enter Index of Operation: 2
Enter Book Id to Issue: 101
Enter Borrower Name: John Doe
Enter Borrower Contact: 1234567890
Enter Issue Date: 2024-02-16
```

#### Returning a Book
```
Enter Index of Operation: 6
Enter Book Id: 101
```

## Data Structure

### index.csv (Library Catalog)
| Column | Description |
|--------|-------------|
| Id | Unique book identifier |
| Books | Book title (stored in lowercase) |
| Author | Author name (stored in lowercase) |
| Year | Publication year |

### issue.csv (Issued Books)
| Column | Description |
|--------|-------------|
| Id | Book identifier |
| Books | Book title |
| Author | Author name |
| Year | Publication year |
| Borrower_Name | Name of the person who borrowed the book |
| Contact | Contact number of the borrower |
| Issue_Date | Date when book was issued |

## Features in Detail

### Add Book
- Validates book ID (must be numeric)
- Prevents duplicate entries (same ID and name)
- Automatically converts book names and author names to lowercase for consistency

### Issue Book
- Displays current available books
- Validates book availability
- Records borrower information
- Automatically moves book from library catalog to issued books list

### Remove Book
- Offers two removal options: by ID or by Name
- Validates book existence before removal
- Updates the catalog automatically

### Return Book
- Displays currently issued books
- Validates book ID
- Automatically returns book to library catalog
- Removes from issued books list

## Error Handling

The system includes error handling for:
- Invalid numeric inputs
- Non-existent book IDs
- Missing files (auto-creates if needed)
- Invalid operation selections

## Known Limitations

1. Book names and authors are automatically converted to lowercase
2. No search functionality for partial matches
3. No date validation for issue dates
4. Single book instance only (no quantity tracking)
5. Requires manual creation of "Library Management" folder before first run

## Future Enhancements

- [ ] Add search functionality (by author, title, year)
- [ ] Implement due date tracking and overdue notifications
- [ ] Add quantity management for multiple copies
- [ ] Create a GUI interface
- [ ] Add data validation (dates, phone numbers)
- [ ] Implement user authentication
- [ ] Export reports (PDF/Excel)
- [ ] Add book categories/genres

## Troubleshooting

**Issue**: "No such file or directory: 'Library Management'"
- **Solution**: Create the "Library Management" folder in the same directory as lib.py

**Issue**: "Enter Valid Numerical Id"
- **Solution**: Ensure you're entering numbers only for Book ID

**Issue**: "Book Not Available in Library!"
- **Solution**: Check if the book exists in the current catalog using option 4

## Contributing

Feel free to fork this project and submit pull requests for any enhancements.

## License

This project is open source and available for educational purposes.

## Contact

For questions or suggestions, please open an issue in the project repository.
```
