def local_check_otp(attempt, correct_otp):
    return attempt == correct_otp
def brute_force_4digit_otp_simulation(correct_otp):
    for num in range(10000):
        attempt = f"{num:04d}"
        if local_check_otp(attempt, correct_otp):
            return attempt  
    return None
# Example:
print("Found OTP:", brute_force_4digit_otp_simulation("0427"))

