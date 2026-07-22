# Test cases for simple calculator
## 1. Addition
### TC-ADD-001: Addition of two positive numbers
- **Test Case Id:**TC-ADD-001
- **Test Case Description:**Verify that the calculator correctly adds two positive numbers.
- **Preconditions:** The calculator application is open and ready to accept input.
- **Test Steps:** 
 1. Enter '5' as the first number.
 2. Select the addition '+' opperator.
 3. Enter '3' as the second number.
 4. Click the '=' button.
- **Expected Results** The calculator should display '8' as the result.
### TC-ADD-002: Addition of a positive number and a negative number
- **Test Case Id:**TC-ADD-002
- **Test Case Description:** Verify that the calculator correctly adds a positive and a negative number.
- **Preconditions:** The calculator appliation is open and ready to accept input.
- **Test Steps:**
 1. Enter '5' as the first number.
 2. Select the addition '+' opperator.
 3. Enter '-2' as the second number.
 4. Click the '=' button.
- **Expected Results** The calculator should display '3' as the result.
### TC-ADD-003: Addition of two decimal numbers
- **Test Case Id:** TC-ADD-003
- **Test cases Description:** Verify that the calculator correctly adds two decimal numbers.
- **Preconditions:** The calculator application is open and ready to accept input.
- **Test Steps:**
 1. Enter '1.5' as the first number.
 2. Select the addition '+' opperator.
 3. Enter '2.3' as the second number.
 4. Click the '=' button.
- **Expected Results** The calculator should display '3.8' as the result.
## 2. Subtraction
### TC-SUB-001: Subtraction of two positive numbers
- **Test case id:** TC-SUB-001
- **Test cases description:** Verify that the calculator correctly subtracts two positive numbers.
- **Preconditions:** The calculator application is open and ready to accept input.
- **Test Steps:**
 1. Enter '5' as the first number.
 2. Select the Subtractor '-' opperator.
 3. Enter '2' as the second number.
 4. Click the '=' button.
- **Expected Results** The calculator should display '3' as the result.
### TC-SUB-002: Subtraction of two positive numbers
- **Test case id:** TC-SUB-002
- **Test cases description:** Verify that the calculator correctly subtracts two positive numbers.
- **Preconditions:** The calculator application is open and ready to accept input.
- **Test Steps:**
 1. Enter '2' as the first number.
 2. Select the Subtractor '-' opperator.
 3. Enter '5' as the second number.
 4. Click the '=' button.
- **Expected Results** The calculator should display '-3' as the result.
### TC-SUB-003: Subtraction of two decimal numbers
- **Test case id:** TC-SUB-003
- **Test cases description:** Verify that the calculator correctly subtracts two decimal numbers.
- **Preconditions:** The calculator application is open and ready to accept input.
- **Test Steps:**
 1. Enter '5.5' as the first number.
 2. Select the Subtractor '-' opperator.
 3. Enter '2.25' as the second number.
 4. Click the '=' button.
- **Expected Results** The calculator should display '3.25' as the result.
## 3. Multiplication
### TC-MUL-001: Multiplication of two positive numbers
- **Test case id:** TC-MUL-001
- **Test cases description:** Verify that the calculator correctly Multiply two positive numbers.
- **Preconditions:** The calculator application is open and ready to accept input.
- **Test Steps:**
 1. Enter '5' as the first number.
 2. Select the multiplication '*' opperator.
 3. Enter '2' as the second number.
 4. Click the '=' button.
- **Expected Results** The calculator should display '10' as the result.
### TC-MUL-002: Multiplication of a positive number and a negative number
- **Test case id:** TC-MUL-002
- **Test cases description:** Verify that the calculator correctly Multiply a positive number and a negative number.
- **Preconditions:** The calculator application is open and ready to accept input.
- **Test Steps:**
 1. Enter '5' as the first number.
 2. Select the multiplication '*' opperator.
 3. Enter '-2' as the second number.
 4. Click the '=' button.
- **Expected Results** The calculator should display '-10' as the result.
### TC-MUL-003: Multiplication with decimal numbers
- **Test case id:** TC-MUL-003
- **Test cases description:** Verify that the calculator correctly Multiply with decimal numbers.
- **Preconditions:** The calculator application is open and ready to accept input.
- **Test Steps:**
 1. Enter '5' as the first number.
 2. Select the multiplication '*' opperator.
 3. Enter '2.5' as the second number.
 4. Click the '=' button.
- **Expected Results** The calculator should display '12.5' as the result.
## 4. Division
### TC-DIV-001: Division of two positive numbers
- **Test case id:** TC-DIV-001
- **Test cases description:** Verify that the calculator correctly Divides two positive numbers.
- **Preconditions:** The calculator application is open and ready to accept input.
- **Test Steps:**
 1. Enter '6' as the first number.
 2. Select the division '/' opperator.
 3. Enter '2' as the second number.
 4. Click the '=' button.
- **Expected Results** The calculator should display '3' as the result.
### TC-DIV-002: Division by zero
- **Test case id:** TC-DIV-002
- **Test cases description:** Verify that the calculator correctly Divides by zero.
- **Preconditions:** The calculator application is open and ready to accept input.
- **Test Steps:**
 1. Enter '6' as the first number.
 2. Select the division '/' opperator.
 3. Enter '0' as the second number.
 4. Click the '=' button.
- **Expected Results** The calculator should display 'error' as the result.
### TC-DIV-003: Division of decimal numbers
- **Test case id:** TC-DIV-003
- **Test cases description:** Verify that the calculator correctly Divides two positive numbers.
- **Preconditions:** The calculator application is open and ready to accept input.
- **Test Steps:**
 1. Enter '6.4' as the first number.
 2. Select the division '/' opperator.
 3. Enter '2' as the second number.
 4. Click the '=' button.
- **Expected Results** The calculator should display '3.2' as the result.
## 5. BODMAS
### TC-BOD-001: Multiplication before Addition
- **Test case id:** TC-BOD-001 
- **Test cases description:** 
Verify that the calculator fllows the correct order of operations by performing multiplication before addition.
- **Preconditions:** The calculator application is open and ready to accept input.
- **Test Steps:**
 1. Enter the expression 2+3*4 
 2. Click the '=' button.
- **Expected Results** The calculator should display '14' as the result.
### TC-BOD-002: Parentheses change the order
- **Test case id:** TC-BOD-002
- **Test cases description:** 
Verify that the calculator fllows the correct order of operations by performing parentheses first.
- **Preconditions:** The calculator application is open and ready to accept input.
- **Test Steps:**
 1. Enter the expression (2+3)*4 
 2. Click the '=' button.
- **Expected Results** The calculator should display '20' as the result.
### TC-BOD-003: Division before addition
- **Test case id:** TC-BOD-003
- **Test cases description:** 
Verify that the calculator fllows the correct order of operations by performing division before addition.
- **Preconditions:** The calculator application is open and ready to accept input.
- **Test Steps:**
 1. Enter the expression 10+6/2 
 2. Click the '=' button.
- **Expected Results** The calculator should display '13' as the result.
## 6. INVALID INPUTS
### TC-INV-001: Non-numeric input
- **Test case id:** TC-INV-001 
- **Test cases description:** 
Verify that the calculator handles non-numeric input correctly.
- **Preconditions:** The calculator application is open and ready to accept input.
- **Test Steps:**
 1. Enter abc as the first input.
 2. select the addition operator(+)
 3. Enter '5' as the second input.
 4. calculate the result.
- **Expected Results** The calculator should display 'Error'
### TC-INV-002: special character as  input
- **Test case id:** TC-INV-002
- **Test cases description:** 
Verify that the calculator handles special character input correctly.
- **Preconditions:** The calculator application is open and ready to accept input.
- **Test Steps:**
 1. Enter '*' as the first input.
 2. select the addition operator(+)
 3. Enter '5' as the second input.
 4. calculate the result.
- **Expected Results** The calculator should display 'Error'
### TC-INV-003: Empty input field
- **Test case id:** TC-INV-003
- **Test cases description:** 
Verify that the calculator handles empty input field correctly.
- **Preconditions:** The calculator application is open and ready to accept input.
- **Test Steps:**
 1. Leave the first input field empty
 2. select the addition operator(+)
 3. Enter '5' as the second input.
 4. calculate the result.
- **Expected Results** The calculator should display 'Error'
### TC-INV-004: Unsupported operator
- **Test case id:** TC-INV-004
- **Test cases description:** 
Verify that the calculator handles Unsupported  input correctly.
- **Preconditions:** The calculator application is open and ready to accept input.
- **Test Steps:**
 1. Enter '5' as the first input.
 2. select the unsupported operator '^'.
 3. Enter '5' as the second input.
 4. calculate the result.
- **Expected Results** The calculator should display 'Error'