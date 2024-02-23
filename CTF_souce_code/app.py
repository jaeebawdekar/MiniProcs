import base64

encryption_key=5
def decrypt_flag(input_flag):
    try:
       
        decrypted_flag = ''.join(chr(ord(c) // encryption_key) for c in base64.b64decode(input_flag).decode())
        return decrypted_flag
    except:
        return None


answer=decrypt_flag("xbzFhcW3xp/FqMa9xYXFj8akxZ7Gi8Wtxr3Ft8afxY/FgMO6w7rEicSO")
print(answer)