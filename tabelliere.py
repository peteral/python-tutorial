def tabelliere(zeilen):
    # parse into table
    parsed = list(map(lambda zeile: zeile.split(';'), zeilen))

    # calculate column sizes
    lengths = [0] * len(max(parsed, key=len))
    for line in parsed:
        for column_index, column in enumerate(line):
            lengths[column_index] = max(lengths[column_index], len(column))

    # format result
    result = list(map(lambda line: '|'.join(map(lambda c: c[1].ljust(lengths[c[0]]), enumerate(line))) + '|', parsed))

    # append header line
    result.insert(1, ''.join((map(lambda x: "-" * x + "+", lengths))))

    return result

for zeile in tabelliere([
    "Name;Strasse;Ort;Alter",
    "Peter Pan;Am Hang 5;12345 Einsam;42",
    "Maria Schmitz;Kölner Straße 45;50123 Köln;43",
    "Paul Meier;Münchener Weg 1;87654 München;65",]):

    print(zeile)