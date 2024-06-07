arn = "arn:aws:iam::123456789012:user/johndoe"
words = arn.split('/')
print(words[1])