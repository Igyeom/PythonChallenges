a=input();print(eval("'"+a+"'"+''.join([f".replace('{i}','{i+'o'*i.islower()+'O'*i.isupper()+i}')"for i in"bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"])))

# dirty one-liner (154B/154C)
