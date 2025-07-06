#Function to do the first level of compression
def compress(s):
	s += " "                      #Adding space to handle last group
	result =""                   #Intializing the result string
	count = 1                    #make the count=1 to start
	for i in range(1, len(s)):
		if s[i] == s[i - 1]:     #if the first and the second char matches then increment
			count += 1 
		else:
			result += s[i - 1] + str(count)   #add the character and the count of it
			count = 1          #reset the count to 1
	return result                #returning the final compressed string
		

#Function to do the second level of compression for removing the duplicate counts


def second_compress(s):
    result = ""
    i = 0
    group_chars = []
    group_count = ""

    while i < len(s):
        char = s[i]
        i += 1
        count = ""
        while i < len(s) and s[i].isdigit():
            count += s[i]
            i += 1

        if not group_chars:
            group_chars.append(char)
            group_count = count
        elif count == group_count:
            group_chars.append(char)
        else:
            result += "".join(group_chars) + group_count
            group_chars = [char]
            group_count = count

    # Add the final group
    if group_chars:
        result += "".join(group_chars) + group_count

    return result

          
#Function to decompress the string
def decompress(s):
	result = ""                 #Initialize the result string
	i = 0
	while i < len(s):           #collect digits after character
		char = s[i]
		i += 1
		count = ""
		while i < len(s) and s[i].isdigit():
			count += s[i]
			i += 1
		if count == "":  
			count = "1"
		result += char * int(count)   #Repeat the char for about count times
	return result               #returning the final decompressed string


#Function to check all the test cases for the above cases

def tests():
    testcases = ["aabcccccaaa", "abababab", "aaabbbccc"]		
    for test in testcases:
        print("original", test)

        first_compress = compress(test)
        print("first compress", first_compress)

        second = second_compress(first_compress)
        print("second compress", second)

        final_one = decompress(second)
        print("decompressed", final_one)

        print("           ")
tests()   #Run the tests      



