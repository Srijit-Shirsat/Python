# Condition notes

## Assignment 1.1 - Login Validation System

### Concepts Learned
- if / elif / else
- input validation
- strip()
- lower()
- len()
- condition ordering

### Key knowledge
- Always validate user input before processing.
- Check empty values before length validation.
- OR is used when any one condition should pass.
- AND is used when we want both condition to be true

### Mistakes made
- Using <= instead of < for minimum length checks.

--------------------------------------------------------------------------------------------------------------------------------------------------

# Assignment 1.2

## Concepts learned 
- Membership operator "in".
- if / else / elif.
- .strip().
- len().
- @ in username.
- multiple forbidden condition checks using OR. 

## Key Knowledge 
- Membership operator is used to check whether something exist inside something.
- It is used for username validation, so the user would enter a valid username without adding forbidden characters.
- We can also simply this by using regex to catch any forbidden character or mix of characters in username.
- To check something which doesn't exist in something, we can make use of "not in" too.

## Mistakes 
- We can use "in" operator in conditions to directly check for spaces in between two characters or username. We don't use username.strip() method here as .strip() doesn't consider spaces in between of characters but only consider spaces in beginning and end.  

