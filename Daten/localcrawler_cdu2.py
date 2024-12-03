def cleanUp(text, debug):
    if text is None:
        return "ERROR: Text was empty"

    lines_output = []
    lines = text.split('\n')

    for index, line in enumerate(lines):
        #Minus entfernen
        line_clean_1 = line_remove_minus(line, debug)
        #Seitenzahlen entfernen
        line_clean_2 = line_remove_seitenzahl(line_clean_1, debug)
        lines_output.append(line_clean_2)
        if debug:
            print(f"\033[92mProcessing line {index + 1}:\033[0m")
            print(line_clean_2)
        #print(line)
    #text = remove_numbers(text)

    #print(str(len(lines)) + " Zeilen eingelesen: " + str(lines))
    #for index, line in enumerate(lines):
    #    line_cleaned = text_remove_seitenzahl(line, debug)
    #    output += line_cleaned+"\n"
    #zeile = remove_seite(zeile)
    #text = remove_dots(text)
    lines_output_str = str(lines_output)
    return lines_output_str


def line_remove_minus(line, debug):
    DEBUG_ATTATCHMENT_MARKER_MINUS = '\033[93m[Minus entfernt]\033[0m'
    if line.endswith('-'):
        line = (line[:-1])
        if debug:
            line += DEBUG_ATTATCHMENT_MARKER_MINUS
    return line

def line_remove_seitenzahl(text, debug):
    if isinstance(text, str):
        if "Seite" in text:
            if (debug):
                print("Seite in Text.")
            position = text.index("Seite")
            i = 0
            while position + i + 6 < len(text) and text[position + i + 6].isdigit():
                if (debug):
                    print("i = " + str(i))  # + " = " + str(text[i+6]))
                i += 1

                # suche "von", schneide ebenfalls ab
                if text[position + i + 6:position + i + 11] == " von " and text[position + i + 11].isdigit():
                    if (debug):
                        print("'von' erkannt.")
                    i += 5
                    while position + i < len(text) and text[position + i].isdigit():  #text[position + i].isdigit():
                        i += 1
            text = text[:position] + text[position + i + 6:]
        return text
    else:
        return text


#awodihawoihdb Seite 5 von 5

def remove_dots(text):
    if "• " in text:
        text = text.replace("• ", "")
        return text
    else:
        return text


def remove_numbers(text):
    if not text.isDigit():
        index = len(text)
        while index > 0 and index > len(text) - 5 and (text[index - 1].isdigit() or text[index - 1] == '-'):
            index -= 1
            #print("index:"+text[index])
        #print(text)
        return text[:index]
    else:
        return ''


input_text = """1. Neue Verantwortung Deutschlands in der Welt – aus Überzeugung für
Frieden, Freiheit und Menschenrechte
66
67
68
69
70
71Unser Unions-Versprechen: Wir arbeiten für ein weltoffenes Deutschland, das in einem Bündnis
von Demokratien gemeinsam mit unseren transatlantischen und europäischen Partnern die glo-
balen Herausforderungen gestaltet. Unser Ziel heißt: Sicherheit und Frieden, Freiheit und Wohl-
stand für die Menschen in Deutschland. Das Modernisierungsjahrzehnt, mit dem wir Deutsch-
land weltpolitikfähig machen, kann nur mit neuer außenpolitischer Stärke gelingen.
72
73
74
75Die Pandemie hat uns erneut gezeigt, wie vernetzt unsere Welt ist. Weder das Coronavirus noch
der Klimawandel oder die digitale Transformation machen an Grenzen halt. Wir können die gro-
ßen weltweiten Menschheitsaufgaben nur lösen, wenn wir sie gemeinsam global anpacken. Es
ist in unserem eigenen Interesse, dass wir international mehr Verantwortung übernehmen.
76
77
78
79
80
81
82Die Bedingungen dafür haben sich gravierend verändert: Wir befinden uns inmitten eines welt-
weiten Epochenwechsels. Die große wirtschaftliche Dynamik in Asien und der Aufstieg Chinas
verändern das internationale Machtgefüge. Wir erleben die Missachtung des Völkerrechts und
Regelbrüche durch bedeutende Staaten des internationalen Systems, und wir sehen, dass sich
weltweit populistische Strömungen ausbreiten, auch in demokratischen Staaten. Hinzu kommt:
Neue Technologien bestimmen nicht nur unseren Alltag, sondern sind auch ein relevanter Faktor
der internationalen Politik.
83
84
85
86
87
88Es reicht nicht, auf Krisen nur zu reagieren. Daher werden wir eine Sicherheitsarchitektur schaf-
fen, die bessere Koordinierung und einen vorausschauenden strategischen Ansatz möglich
macht. Die Grundlage unseres weltweiten politischen Handelns ist und bleibt dabei das christli-
che Menschenbild. Wir bekennen uns dazu, dass Deutschland aktiv zur internationalen Krisen-
bewältigung und zur Gestaltung der Weltordnung beiträgt - in der Europäischen Union, der
NATO, den Vereinten Nationen und weiteren internationalen Organisationen.
89
901.1. Stärkung der werte- und regelbasierten internationalen Ordnung
91Bündnis der Demokratien schmieden
92
93
94
95
96
97
98
99Demokratien und autoritäre Staaten ringen um den globalen Gestaltungsanspruch im 21.
Jahrhundert. Es geht um den Fortbestand unserer freiheitlich-demokratischen Ordnung, die
autoritäre Staaten in Frage stellen und zu destabilisieren versuchen. Aus dieser Systemri-
valität ergeben sich für uns die Verpflichtung und der Anspruch, die internationale regel-
und wertebasierte Ordnung wieder zu stärken. Denn sie ist Voraussetzung dafür, dass wir
in Sicherheit und Frieden, Freiheit und Wohlstand leben können. Wir wollen, dass Deutsch-
land und Europa gestärkt aus dieser Herausforderung hervorgehen – gemeinsam mit den
USA und zugleich auf eigene Fähigkeiten bedacht."""  #input("Gib den Text ein: ")
output = cleanUp(input_text, True)
print("Cleaned Text: " + output)
