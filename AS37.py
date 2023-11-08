print(eval(f"'{input()}'"+''.join([f".replace('{i}','{i+'o'*i.islower()+'O'*i.isupper()+i}')"for i in"bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"])))

# dirty one-liner (149B/149C)
