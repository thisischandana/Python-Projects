import random
data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'social media platform',
        'country': 'United States'
    },

    {
        'name': 'Christiano Ronaldo',
        'follower_count': 215,
        'description': 'footballer',
        'country': 'Portugal'

    },

    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'

    }
]

def format_string():
    name = data["name"],
    follower_count = data["follower_count"],
    description = data["description"],
    country = data["country"]
    print(f"{name} has {description}")

account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

print(f" Comapre A: {format_string(account_a)}")
print(f" Comapre A: {format_string(account_a)}")z
