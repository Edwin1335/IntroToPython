import regex as re


def extractSN(numbers):
    serialNumber = ""
    SList = []
    match = re.findall(r"\b[A-Z0-9]{7}\b|\b[A-Z0-9]{10}\b", numbers)
    for y in match:
        SList.append(y)

    if len(SList) > 1:
        closest = len(numbers)
        result = numbers.find('Serial', 0, len(numbers))
        if result == -1:
            result = numbers.find('SN', 0, len(numbers))
        if result == -1:
            result = numbers.find('S/N', 0, len(numbers))
        if result == -1:
            result = numbers.find('org_serial_no', 0, len(numbers))

        for i in range(result, len(numbers)):
            for matches in SList:
                if closest >= numbers.find(matches) > result:
                    closest = numbers.find(matches)

        for x in range(closest, closest + 10):
            serialNumber = serialNumber + numbers[x]

    # testing SList and serialNumber
    print(serialNumber)
    # print('\n', SList)
    return serialNumber

