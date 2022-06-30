my_name = "Henry Tran"
pref_name = "Henry"
my_age = 17
python_experience = True
fav_hobbies = ["swimming", "sleeping", "video games", "watching anime"]
fav_things = {
  "movies" : "Koe no katachi", 
  "number" : 2,
  "hobbies" : fav_hobbies[2],
  "fav_anime" : "Shigatsu wa kimi uso",
}

print(my_name, pref_name, my_age, python_experience)
print("\n")
print(fav_hobbies)
print("\n")
print(fav_things)

all_vars = dict(vars())