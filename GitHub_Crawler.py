import util_ghc as ughc

while True:
    raw_link = input("Enter the username: ")
    flag = 0
    raw_link = raw_link.strip()
    print("\nInfo for: "+raw_link)
    person = ughc.get_details(raw_link)
    try:
        print(person.get_desc())
    except:
        flag += 1
        pass

    try:
        repos = person.get_featured_repo_names()
        if len(repos) == 0:
            raise
        print("\n\tThe featured repositories are:")
        for repo in repos:
            print("\t\t"+repo)
    except:
        flag += 1
        pass

    try:
        print("\n\tThe location is: "+person.get_location())
    except:
        flag += 1
        pass

    try:
        counters_list = person.get_counters_list()
        print("\tRepositories: " + str(counters_list[0]).strip())
        print("\tStars: " + str(counters_list[1]).strip())
        print("\tFollowers: " + str(counters_list[2]).strip())
        print("\tFollowing: " + str(counters_list[3]).strip())
    except:
        flag += 1
        pass

    if flag == 4:
        print("There is no information about the username ",raw_link)
    

    Continue = input("Do you want to continue? (Y/N)")
    Continue = Continue.lower()
    if Continue == 'n':
        break
