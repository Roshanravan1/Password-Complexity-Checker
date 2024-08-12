import string

def check_password_strength(password):
  """Checks the strength of a password based on given criteria.

  Args:
    password: The password to be evaluated.

  Returns:
    A string indicating the password strength.
  """

  length_sufficient = len(password) >= 8
  has_upper = any(char.isupper() for char in password)
  has_lower = any(char.islower() for char in password)
  has_digit = any(char.isdigit() for char in password)
  has_special = any(char in string.punctuation for char in password) 


  if all([length_sufficient, has_upper, has_lower, has_digit, has_special]):
    return "Strong password"
  elif any([length_sufficient, has_upper, has_lower, has_digit, has_special]):
    return "Medium password"
  else:
    return "Weak password"

# Example usage:
password = input("Enter your password: ")
strength = check_password_strength(password)
print("Password strength:", strength)