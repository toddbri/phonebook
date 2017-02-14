import os, pickle, sys
entry_file = "pb.entries"
def wfi():
    raw_input("Press enter to continue")

def display_menu():
    menu = '''
    Electronic Phone Book
    =====================
    1. Look up an entry
    2. Add an entry
    3. Delete an entry
    4. List all entries
    5. Quit
    '''
    option =0
    while not option in ["1","2","3","4","5"]:
        os.system("clear")
        print menu
        option = raw_input("What do you want to do(1-5)?")
    print ""
    return int(option)
pb ={}
if os.path.isfile(entry_file):
    pb=pickle.load(open(entry_file,"rb"))
print pb
option = 0
while option != 5:
    option = display_menu()
    if option == 1:
        lookup = raw_input("Name to search for ?")
        if lookup in pb.keys():
            print ""
            print "Found entry for %s:" % lookup
            for key in pb[lookup].keys():
                print "\t %s: %s" % (key,pb[lookup][key])
        else:
            print "No entries found for %s" % lookup
        wfi()
    elif option == 2:
        new_name = raw_input("New name?")
        if not new_name in pb.keys():
            new_email = raw_input("email?")
            new_phone = raw_input("phone?")
            pb[new_name]={"email":new_email,"phone":new_phone}
            pickle.dump(pb, open(entry_file,"wb"))
        else:
            print new_name + " already exists"
            wfi()

    elif option == 3:
        del_name = raw_input("Name to delete?")
        if del_name in pb:
            del pb[del_name]
            pickle.dump(pb, open(entry_file,"wb"))
        else:
            print "%s entry not found" % del_name
            wfi()

    elif option == 4:
        if len(pb)>0:
            for person in pb.keys():
                print person
                for detail in pb[person]:
                    print "\t %s: %s" % (detail,pb[person][detail])
        else:
            sys.stdout.write("\033[1;31m")
            print "No entries found in phonebook"
            sys.stdout.write("\033[0;0m")
        wfi()

print "Goodbye...thank you for playing"
