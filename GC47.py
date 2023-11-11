import re

personal_info, domain_name = input().split("@")
if len(personal_info) > 64 or len(domain_name) > 253:
    print("Invalid email. Length of email address did not match criteria.")
elif re.fullmatch(r"[A-Za-z0-9!#$%&'*+\-/=?^_`{|}~]+", personal_info) and re.fullmatch(r"[A-Za-z\-.]+", domain_name):
    print("Valid email. All checks passed.")
else:
    print("Invalid email. Some characters may be invalid.")
