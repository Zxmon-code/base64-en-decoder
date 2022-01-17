import time
import base64

#ask for the name
name = input(str("What is your name: ")

#say hello to the person
print("Ok, then hello "+name)

def encoder():
    #ask for the word which is supposed to be encoded
    word = input(str("which word do you want to encode?: "))
    print("Ok, "+name+"the word "+word+"encoded is: ")
    time.sleep(3)
    
    #change the word variable into bytes, for base64 to encode
    word_bytes = word.encode('ascii')
    #encode the bytes
    base_bytes = base64.b64encode(word_bytes)
    #change the bytes back into ascii characters
    word_encoded = base_bytes.decode('ascii')
    #print the encoded words
    print(word_encoded)
    again_encoder()

def again_encoder():
       again = input(str(name+" do you want to encode another word? Type yes. If you want to proceed type no: "))

    again_l = again.lower()

    if again_l == "yes":
        encoder()

    elif again_l == "no":
        decoder()

    else:
        print(name+" it seem that your typing skills are an absolute abomination. maybe you should try that again but this time type yes or no.")

#call the encoder function
encoder()

def decoder():
    #ask for the string, that is supposed to be decoded
    message_encoded = input(str(name + " what word would you like to decode?: "))
    #turn the encoded message into base64 encodable bytes
    message_bytes = message_encoded.encode('ascii')
    #decode the bytes
    message_bytes_encoded = base64.b64encode(message_bytes)
    #turn the bytes into readable text
    message_decoded = message_bytes_encoded.decode('ascii')
    #print the decoded word
    print("Ok "+name+" the string "+message_encoded+" decoded is:")
    time.sleep(3)
    print(message_decoded)