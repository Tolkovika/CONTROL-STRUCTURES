facebook = True
twitter = False
instagram = True

social_accounts = sum([facebook, twitter, instagram])

if social_accounts >= 2:
    print("You are a good influencer!")
else:
    print("You are not a good influencer.")
