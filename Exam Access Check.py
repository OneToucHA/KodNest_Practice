registered = input().strip()
fee_paid = input().strip()
identity_verified = input().strip()
system_check = input().strip()

# Check whether the student can access the online exam
if registered == "Yes":
    if fee_paid == "Yes" and identity_verified == "Yes":
        if system_check == "Pass":
            print("Access Granted")
        else:
            print("Access Denied: System Check Failed")
    else:
        print("Access Denied: Verification Pending")
else:
    print("Access Denied: Registration Incomplete")