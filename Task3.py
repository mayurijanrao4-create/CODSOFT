import random
import string 
def password_generator():
    #Generate random password based on user specification
    print("\n"+"="*40)
    print("PASSWORD GENERATOR")
    print("="*40)

    try:
        length=int(input("enter the desired password length(minimum 4):"))
        if length<4:
            print("Password length should be at least 4 characters")
            return
        print("\nSelect password complexity")
        print("1.Leters only")
        print("2.Letters and Digits")
        print("3.Letters,digits and special characters")
        complexity=input("Enter choice(1-3)")
        if complexity=='1':
            characters=string.ascii_letters
        elif complexity=='2':
            characters=string.ascii_letters+string.digits
        elif complexity=='3':
            characters=string.ascii_letters+string.digits+string.punctuation
        else:
            print("Invalid complexity choice")
            return
        password=".join(random.choice(characters) for_in range(length))"
        print(f"\nGenerated password:{password}")
        print(f"Password length:{len(password)} characters")
        print(f"Password complexity:{'low'if complexity=='1'else 'mediun'if complexity=='2'else 'high'}")
        #Password strength analysis
        strength=0
        if any(c.islower()for c in password):
            strength+=1
        if any(c.isupper()for c in password):
            strength+=1
        if any(c.isdigit()for c in password):
            strength+=1
        if any(c in string.punctuation for c in password):
            strength+=1
        print(f"Password strength:{'weak'if strength<2 else 'medium'if strength<4 else'Strong'}")
    except ValueError:
        print("Error.Please enter a valid number ")
    print("="*40)
if __name__=="__main__":
    password_generator()

    
        
        

