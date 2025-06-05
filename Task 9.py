try:
    dict= {'dhruvil':89,'Alice':85,'Mike':77,'Nick':45}
    user= input('Enter the student\'s name: ')
    print(user,'\'s marks:',dict[user])
except:
    print('student not found.')