'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here

    count = 0

    # for i in range(3,0,-1):
    rem_3 = n % 3 if n // 3 > 0 else 0
    rem_2 = rem_3 % 2 if rem_3 // 2 > 0 else 0
    rem_1 = rem_2 % 1 if rem_2 // 2 > 0 else 0
    print(rem_3, rem_2, rem_1)



    
    # count += n//3
    remainder = n%3

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
