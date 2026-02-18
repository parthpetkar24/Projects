# Password Manager

A simple command-line based Password Manager built with Python and Pandas. This application helps you generate secure random passwords and store them with associated application or website names for easy retrieval.

## Features

- **Generate Passwords**: Create secure 16-character passwords with letters and numbers
- **Store Passwords**: Save generated passwords with application/website labels
- **View All Passwords**: Display complete list of stored passwords
- **Search Passwords**: Find passwords by application or website name
- **Persistent Storage**: All passwords stored in CSV format for easy access
- **Case-Insensitive Search**: Find passwords regardless of capitalization

## Project Structure
```
Password Generator and Manager/
│
├── password.py         # Main application file
├── data.csv           # Password storage (created automatically)
├── requirements.txt   # Python dependencies
└── README.md         # Project documentation
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

3. **Run the application**:
```bash
   python password.py
```

The `data.csv` file will be created automatically in the same directory as the script on first use.

## Usage

### Main Menu
```
Operations Available:
1. Generate New Password
2. Store Password
3. View All Passwords
4. Search for Password
5. Exit
```

### Workflow

#### 1. Generate a New Password
```
Enter Operation: 1
New Generated Password: aB3dE5fG7hI9jK1lM
```
- Generates a 16-character password with random letters (uppercase and lowercase) and numbers
- Password is stored in memory temporarily for storage

#### 2. Store Password
```
Enter Operation: 2
Enter the Application or Website for the password: Gmail
Stored Successfully!
```
- Stores the most recently generated password
- Must generate a password first (Operation 1) before storing
- Requires a purpose/label (application or website name)

#### 3. View All Passwords
```
Enter Operation: 3
   Purpose           Password
0    Gmail  aB3dE5fG7hI9jK1lM
1  Netflix  xY2zA4bC6dE8fG0hI
2  Twitter  mN3pQ5rS7tU9vW1xY
```
- Displays all stored passwords in a formatted table

#### 4. Search for Password
```
Enter Operation: 4
Enter Application or Website: gmail
   Purpose           Password
0    Gmail  aB3dE5fG7hI9jK1lM
```
- Case-insensitive search
- Returns all matching entries

#### 5. Exit
```
Enter Operation: 5
```
- Exits the application

## Data Structure

### data.csv
| Column | Description |
|--------|-------------|
| Purpose | Application or website name |
| Password | Generated or stored password |

## Security Considerations

⚠️ **IMPORTANT SECURITY NOTICE** ⚠️

This is a basic password manager intended for **educational purposes only**. It has several security limitations:

### Current Limitations:
1. **Unencrypted Storage**: Passwords are stored in plain text in a CSV file
2. **No Master Password**: Anyone with file access can read all passwords
3. **No Encryption**: Data is not encrypted at rest or in transit
4. **File System Security**: Relies entirely on OS-level file permissions
5. **No Password Strength Options**: Fixed 16-character format only

### Recommendations for Real-World Use:
- **DO NOT** use this for storing sensitive passwords
- Use established password managers like:
  - Bitwarden (open source)
  - 1Password
  - LastPass
  - KeePass
- If you must use this tool:
  - Secure the data.csv file with appropriate permissions
  - Keep it on an encrypted drive
  - Never commit data.csv to version control

## Password Generation Details

- **Length**: 16 characters (actually 17 due to implementation)
- **Character Set**: 
  - Lowercase letters (a-z)
  - Uppercase letters (A-Z)
  - Digits (0-9)
- **Method**: Random selection from combined character pool
- **Entropy**: ~95 bits (approximately)

## Error Handling

The application handles:
- Invalid operation selections
- Attempting to store before generating a password
- Missing CSV files (auto-creates)
- Case-insensitive search matching

## Known Limitations

1. **Password generation creates 17 characters** instead of 16 (due to `while len(password)<=16`)
2. **No password editing** - must delete and re-add
3. **No password deletion feature**
4. **No duplicate checking** - can store same purpose multiple times
5. **No password history** - overwrites on regeneration
6. **No password strength validation**
7. **No backup/export features**
8. **Plain text storage** - major security risk

## Future Enhancements

### Security Improvements (CRITICAL)
- [ ] Add encryption for password storage (AES-256)
- [ ] Implement master password authentication
- [ ] Use secure key derivation (PBKDF2, Argon2)
- [ ] Add password hashing for verification

### Feature Enhancements
- [ ] Delete password functionality
- [ ] Update/edit existing passwords
- [ ] Password strength meter
- [ ] Customizable password length and character sets
- [ ] Password expiration tracking
- [ ] Password history
- [ ] Import/export functionality
- [ ] Duplicate entry prevention
- [ ] Backup and restore features
- [ ] GUI interface
- [ ] Browser integration
- [ ] Password sharing (encrypted)
- [ ] Two-factor authentication

## Troubleshooting

**Issue**: "Generate a Password first!!"
- **Solution**: Use Operation 1 to generate a password before trying to store it (Operation 2)

**Issue**: "Not Found!" when searching
- **Solution**: Check spelling and verify the entry exists using Operation 3

**Issue**: Module not found error
- **Solution**: Install pandas using `pip install -r requirements.txt`

**Issue**: "Invalid Operation!"
- **Solution**: Enter only numbers 1-5 for menu options

## Code Improvements Suggested
```python
# Fix password length (currently generates 17 chars)
while len(password) < 16:  # Changed from <=

# Add password deletion
def delete_password(purpose):
    # Implementation here
    pass

# Add duplicate checking in store_password
def store_password(purpose, password):
    # Check for duplicates before storing
    pass
```

## Best Practices

If using this tool (despite security warnings):
1. Keep data.csv in a secure location
2. Set restrictive file permissions (chmod 600 on Unix/Linux)
3. Never commit data.csv to version control
4. Add data.csv to .gitignore
5. Regularly backup your data.csv
6. Use for non-critical passwords only

## Contributing

This is an educational project. Contributions focusing on security improvements are especially welcome.

## Disclaimer

This software is provided "as is" without warranty of any kind. Use at your own risk. The authors are not responsible for any security breaches or data loss resulting from the use of this software.

## License

This project is open source and available for educational purposes only.


## Contact

For questions or suggestions, please open an issue in the project repository.
```
