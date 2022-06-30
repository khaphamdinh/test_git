'''
print ('hello world')
import sys
print (sys.executable)
#a = eval(input('Nhập biến bạn muốn: '))
#print ('Đây là biến ', type(a))
print ('Xin chào', 'thế giới', 'từ', 'Python', sep = '\t')
'''


'''
print(['Microsoft', 'Apple', 'Google'])
for word in ['xinh đẹp', 'xinh xẻo', 'cute', 'dễ thương']:
    print ('Em Chang rất chi là %s' %(word) )
'''


'''
str_list = ['hello','guys', 'python']
for i in range (1,2,3,4,5):
    print ('giá trị của i là: ',i)
'''


'''
str_list = [668, 'guys', 'python', 'abc', 'xyz']
for i in range (len(str_list)):
    word = str_list[i]
    print('giá trị của i là:',word)
'''


'''
datalist = [1452, 11.23, 1+2j, True, 'alo@122', (0,-1), [5,12], {"class":'V', "section":'A'}]
for i in range(len(datalist)):
    a = datalist[i]
    print ('Giá trị thứ %i của biến datalist là:'%(i),a, ', giá trị này thuộc kiểu:', type(a))
'''


'''
j = 0
for i in range(10): #0,1,2,3,4,5,6,7,8,9 #có nghĩa là lặp bao nhiêu vòng
    print('giá trị của j=',j)
    j = i * 2
'''


'''
a_list = [1, 'a', 2, 'b', 3, 'c', 'd', 'e', 4, 5, 6, 'f', 7, 'g','h', 8, 9, 'I', 10, 'k']
for ilist in a_list:
    print(ilist)
'''


'''
# Ex_1 during Sec_5 by my thought
password = input('Nhập password của bạn: ')
a = 'secrete' #Đây là pass users tạo
count = 0
while (password == a):
    print ('Chúc mừng bạn đã nhập đúng password')
    break
while (password != a):
    count = count + 1
    password = input('Sai password vui lòng nhập lại: ')
    if count > 2:
        print ('Bạn đã nhập sai quá 3 lần, tài khoản bị khóa')
        break
    if password == a:
        print ('Chúc mừng bạn đã nhập đúng password')    
'''


''' 
# Ex_1 during Sec_5 after all
# Vẫn còn bị lỗi nhập tới lần cuối cùng dù đúng máy vẫn báo sai --> chưa tìm ra lỗi
password = input('Nhập password của bạn: ')
first = True
count = 1
while first:
    if password == 'secrete':
        print ('Bạn đã nhập đúng')
        first = False
    else: 
        password = input('Sai password vui lòng nhập lại: ')
        count = count + 1
        if count >= 3:
            print ('Bạn đã nhập sai 3 lần, tài khoản bị khóa') 
            first = False
'''


'''
# Ex_2 during Sec_5 --> final result
num = int(input('Nhập 1 số bất kỳ từ 10 tới 20: '))
first = True
#A = [10,11,12,13,14,15,16,17,18,19,20]
#for i in range(10,21):
    #if i == range (10,21):
        #num_i = i

while first:
    if (10 < num < 21):
        print ('Chúc mừng bạn đã nhập đúng')
        first = False
    else:
        num = int(input('Nhập sai số rồi nhập lại đi: '))
'''


'''
# Ex_3 during Sec_5 -- my thought
import re
pw = input('Nhập password của bạn: ')
first = True
while (first):
    if re.search('a-z',pw) and re.search('A-z',pw) and re.search('0-9',pw) and re.search('$#@',pw) and 5<len(pw)<17: 
        print('Password is correct') #thiếu mở đóng ngoặc sau điều kiện If nên báo lỗi
        break
    else:
        pw = input('Nhập lại password của bạn: ')

# Ex_3 during Sec_5 -- final result
import re
pw = input('Nhập password của bạn: ')
while True:
    if (re.search("[a-z]",pw) and re.search("[A-Z]",pw) and
        5<len(pw)<17 and
        re.search("[0-9]",pw) and
        re.search("[$#@]",pw)) :
        print('Password is correct')
        break 
    else:
        pw = input('Nhập lại password của bạn: ')
'''