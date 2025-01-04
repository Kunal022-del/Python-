# Password Generator Application

The Password Generator application is a Python-based desktop tool built using the `tkinter` library. It allows users to generate strong passwords for specific websites and save them for future use. The application ensures user convenience and security by checking for duplicate entries.

---

## Features
- **Generate Passwords:** Create strong passwords of customizable lengths.
- **Save Passwords:** Store generated passwords along with the associated website and user name.
- **Duplicate Check:** Avoid saving passwords for the same website and user multiple times.

---

## How to Run
1. Ensure you have Python installed on your system.
2. Save the script to a file (e.g., `password.py`).
3. Run the script using the command:
   ```
   python password.py
   ```

---

## Sample Output

### 1. Generating a Password
**Input:**
- **Site:** example.com
- **User Name:** Kunal Kundaliya   
- **Password Length:** 12  

**Output:**  
A message box displays:  
```
Generated Password for Kunal Kundaliya at example.com: A$3kLd&7@wT9
```

### 2. Saving a Password
**Input:**
- **Site:** example.com  
- **User Name:** Kunal Kundaliya
- **Generated Password:** A$3kLd&7@wT9  

**Output:**  
A message box displays:  
```
Password saved successfully.
```

**File Content (`password_1.txt`):**  
``` bash
User: Kunal Kundaliya 
Site: example.com
Password: A$3kLd&7@wT9
```

### 3. Duplicate Password Check
**Input:**  
- **Site:** example.com  
- **User Name:** Kunal Kundaliya  

**Output:**  
A message box displays:  
```
Error: Password for this site and user already exists.
```

---

## File Structure
- **password.py**: Main script for the application.
- **password_1.txt**: File where passwords are stored or by setting new filename by changing <strong>`<script filename>`</strong>

---
## Contact
For any questions or feedback, please reach out at 
```batch
[Kunalsep22@gmail.com].
```
---

