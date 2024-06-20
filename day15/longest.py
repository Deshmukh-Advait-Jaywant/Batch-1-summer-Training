#longest palindromic substring
s="abdbsdabca"
left=0
right=len(s)-1
for i in range(len(s)):
    right=len(s)-1
    while left<=right:
        if s[left]==s[right]:
            left+=1
            right-=1
        
