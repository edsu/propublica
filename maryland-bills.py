from propublica import State, Representative

state = State("md")

for rep in state.get_representatives():
    print("\n" + rep.name + " " + rep.id)
    for bill in rep.get_bills():
        if bill.congress == "116":
            print("- " + bill.title + " <" + bill.url + ">")


