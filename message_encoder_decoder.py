import random
original_msg = input("Enter your message: ")
choice = input("Enter the operation - encode or decode? ")

def encoding(passed_value):
    final_msg = ""
    words = passed_value.split(" ")
    for word in words:
        encoded_msg = ""
        if(len(word)<3):
            for i in range(0,len(word)):
                encoded_msg += word[len(word)-(i+1)]  # simply reverse the string 
                        
        else:
            for i in range(1,len(word)):
                encoded_msg += word[i]  # copy the word except first character
            encoded_msg += word[0]      # appending first character to the end
            random_char = list("abcdefghijklmnopqrstuvwxyz")
            left_random = random.choice(random_char)+random.choice(random_char)+random.choice(random_char)
            right_random = random.choice(random_char)+random.choice(random_char)+random.choice(random_char)
            encoded_msg = left_random + encoded_msg + right_random  # adding 3 random random_char at start and end

        final_msg += encoded_msg
        final_msg += " "
    return final_msg

# x---------------------------------------------------------------------------------------------x

def decoding(passed_value):
    final_msg = ""
    words = passed_value.split(" ")
    for word in words:   
        decoded_msg = ""
        if(len(word)<3):
            for i in range(0,len(word)):
                decoded_msg += word[len(word)-(i+1)]  # simply reverse the string 
                
        else:
            partial_decoded_msg = word[3:-3]  #word[3:len(word)-3]
            decoded_msg += partial_decoded_msg[len(partial_decoded_msg)-1]
            for i in range(0,len(partial_decoded_msg)-1):
                decoded_msg += partial_decoded_msg[i]

        final_msg += decoded_msg
        final_msg += " "
    return final_msg       

# x----------------------------------------------------------------------------------------------x

if(choice.lower() == "encode"):
    return_value = encoding(original_msg)
    print(f"The encoded message is: {return_value}")
elif(choice.lower() == "decode"):
    return_value = decoding(original_msg)
    print(f"The decoded message is: {return_value}")
else:
    print("Invalid choice. Enter encode or decode")
