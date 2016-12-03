from __future__ import division # integer division is lame

users = [
 { "id": 0, "name": "hero" },
 { "id": 1, "name": "dunn" },
 { "id": 2, "name": "sue" },
 { "id": 3, "name": "chi" },
 { "id": 4, "name": "thor" },
 { "id": 5, "name": "clive" },
 { "id": 6, "name": "hicks" },
 { "id": 7, "name": "devin" },
 { "id": 8, "name": "kate" },
 { "id": 9, "name": "klein" }
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
 (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


for user in users :
    user["friends"] = []

for i, j in friendships:
 # this works because users[i] is the user whose id is i
 users[i]["friends"].append(users[j]) # add i as a friend of j
 users[j]["friends"].append(users[i]) # add j as a friend of i


def number_of_friends(user):
  return len(user["friends"]) # length of friend_ids list


total_connections = sum(number_of_friends(user) for user in users) # 24


num_users = len(users) # length of the users list
avg_connections = total_connections / num_users # 2.4


print("total-connections = "  + str(total_connections))
print("average-connections = "  + str(avg_connections))
print("\n-------\n")

# create a list (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user))
for user in users]
sorted(num_friends_by_id, # get it sorted
key=lambda user_id, num_friends : num_friends, # by num_friends
reverse=True) # largest to smallest
# each pair is (user_id, num_friends)
# [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3),
# (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]


print(users[0])
