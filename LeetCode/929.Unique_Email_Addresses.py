def numUniqueEmails(self, emails):
    """
    :type emails: List[str]
    :rtype: int
    """
    setlis = []
    for e in emails:
        lis = e.split("@")
        name = lis[0]
        domain = lis[1]

        name = name.replace(".", "")
        index = 0
        if "+" in name:
            index = name.find("+")
            name = name[:index]
        setlis.append(name + "@" + domain)

    return len(set(setlis))