def count_letters(s):  
    """
    The function counts the number of occurrences of each letter in a given string, ignoring non-alphabetic characters and treating uppercase and lowercase letters as the same.
    
    :param s: The parameter `s` is a string that contains a series of characters. In this case, it appears to be a block of text with multiple lines
    :return: The function count_letters(s) returns a dictionary that contains the count of each letter in the given string.
    """
    # 初始化一个字典来存储每个字母的计数  
    counts = {}  
# The given code is a Python function that counts the number of occurrences of each letter in a given string. It ignores non-alphabetic characters and treats uppercase and lowercase letters as the same.
    # 对字符串中的每个字符进行迭代  
    for char in s:  
        # 如果字符是字母  
        if char.isalpha():  
            # 将字符转换为小写，以便不区分大小写  
            char = char.lower()  
            # 如果字典中已经有这个字母，增加计数  
            if char in counts:  
                counts[char] += 1  
            # 否则，向字典中添加这个字母，并设置计数为1  
            else:  
                counts[char] = 1  
    # 返回计数字典  
    sorted_counts = dict(sorted(counts.items(),key = lambda x: x[1], reverse = True))
    return  sorted_counts
  
# 给定的字符串  
s = """YIFQ FMZR WQFY VECF MDZP CVM R ZWNM DZVE JBTX CDDUMJ
   NDIF EFMD ZCDM QZKC EYFC JMYR NCWJ CSZR EXCH ZUNMXZ
   NZUC DRJX YYSM RTMEYIFZ WDYV ZVYF ZUMR ZCRW NZDZJJ
   XZWG CHSM RNMD HNCM FQCH ZJMX JZWI EJYU CFWD JNZDIR
"""
print(count_letters(s))
s = s.replace("Y",'o')
s = s.replace("F",'r')
s = s.replace("M",'i')
s = s.replace("Z",'e')
s = s.replace("R",'n')
s = s.replace("W",'d')
s = s.replace("C",'a')
s = s.replace("M",'i')
s = s.replace("D",'s')
s = s.replace("N",'h')
s = s.replace("J",'t')
s = s.replace("H",'c')
#----------------------------------------
s = s.replace("I",'u')
s = s.replace(' ','')
s = s.replace('\n','')
s = s.replace('Q','f')
s = s.replace('V','m')
s = s.replace('E','p')
s = s.replace('P','x')
s = s.replace('B','y')
s = s.replace('U','w')
s = s.replace('S','k')
s = s.replace('X','l')
s = s.replace('T','g')
s = s.replace('G','b')
s = s.replace('K','v')
print(s)
