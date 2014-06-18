
def cls(lines=100):

    import os

    if os.name == "posix":
        os.system("clear")
    elif os.name in ("nt", "dos", "ce"):
        os.system("CLS")
    else:
        print(('\n' * lines))


def yesOrNo(prompt="(Y/N)?"):
    while 1:
        answer = raw_input(prompt)
        answer = answer.strip()
        answer = answer.lower()

        yes = ['yes', 'y', 'ye', 'yeah', 'tak', 'ja', 'mhm', 'yep']
        no = ['no', 'n', 'nah', 'nein', 'nie', 'ne', 'nope']

        if answer in yes:
            return True
        elif answer in no:
            return False
        else: 
            continue
