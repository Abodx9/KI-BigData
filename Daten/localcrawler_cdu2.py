DEBUG_ATTACHMENT_MARKER_ROWNUMBER_OK = '\033[93m[Zeilennummer entfernt]\033[0m'
DEBUG_ATTACHMENT_MARKER_ROWNUMBER_ERROR = '\033[91m[Error: Zeilennummer nicht gefunden!]\033[0m'
DEBUG_ATTACHMENT_MARKER_MINUS = '\033[93m[Minus entfernt]\033[0m'
DEBUG_ATTACHMENT_MARKER_SEITENNUMMER = '\033[93m[Seitenzahl entfernt]\033[0m'

start_row_counter = -13


def cleanUp(text, debug):
    global start_row_counter

    if text is None:
        return "ERROR: Text was empty"

    lines_output = []
    lines = text.split('\n')

    # leere Zeilen löschen
    lines = [line for line in lines if line.strip() != "" and line.strip() != "Inhaltsverzeichnis"]

    # Inhaltsverzeichnis erstellen - For headline-recognition
    inhaltsverzeichnis = [line for line in lines if "......" in line]
    # remove dots maybe
    #print(inhaltsverzeichnis)

    lines = [line for line in lines if not "......" in line]  # TODO (erwischt nicht alle)


    for index, line in enumerate(lines):
        #Zeilennummern entfernen
        line_clean_1 = line_remove_rownumbers(line, debug)
        #Minus entfernen
        line_clean_2 = line_remove_minus(line_clean_1, debug)
        #Seitenzahlen entfernen
        line_clean_3 = line_remove_seitenzahl(line_clean_2, debug)
        lines_output.append(line_clean_3)
        if debug:
            print(f"\033[92mProcessing line {index + 1}:\033[0m")
            print(line_clean_3)
        #print(line)
        #start_row_counter += 1

    lines_output_str = str(lines_output)
    return lines_output_str




def line_remove_rownumbers(line, debug):
    global start_row_counter
    start_to_count = False

    if start_row_counter >= 0:
        start_to_count = True
    n = start_row_counter

    if line.strip().endswith(str(n)) and start_to_count:
        numbers_length = len(str(n))
        line = line[:-numbers_length].rstrip()
        if debug:
            line += DEBUG_ATTACHMENT_MARKER_ROWNUMBER_OK
    elif debug:
        line += DEBUG_ATTACHMENT_MARKER_ROWNUMBER_ERROR + ", n = " + str(n)

    start_row_counter += 1

    return line






def line_remove_minus(line, debug):
    if line.endswith('-'):
        line = (line[:-1])
        if debug:
            line += DEBUG_ATTACHMENT_MARKER_MINUS
    elif line.endswith('-' + DEBUG_ATTACHMENT_MARKER_ROWNUMBER_OK):
        line = (line[:-1] + DEBUG_ATTACHMENT_MARKER_ROWNUMBER_OK)
    elif line.endswith('-' + DEBUG_ATTACHMENT_MARKER_ROWNUMBER_ERROR):
        line = (line[:-1] + DEBUG_ATTACHMENT_MARKER_ROWNUMBER_ERROR)
    return line


def line_remove_seitenzahl(text, debug):
    if isinstance(text, str):
        if "Seite" in text:
            #if (debug):
                #print("Wort 'Seite' in Text.")
            position = text.index("Seite")
            i = 0
            while position + i + 6 < len(text) and text[position + i + 6].isdigit():
                #if (debug):
                    #print("i = " + str(i))  # + " = " + str(text[i+6]))
                i += 1

                # suche "von", schneide ebenfalls ab
                if text[position + i + 6:position + i + 11] == " von " and text[position + i + 11].isdigit():
                    #if (debug):
                        #print(DEBUG_ATTACHMENT_MARKER_SEITENNUMMER)
                    i += 5
                    while position + i < len(text) and text[position + i].isdigit():  #text[position + i].isdigit():
                        i += 1
            text = text[:position] + DEBUG_ATTACHMENT_MARKER_SEITENNUMMER + text[position + i + 6:]
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


input_text = """Das Programm für Stabilität

und Erneuerung.

GEMEINSAM FÜR EIN MODERNES DEUTSCHLAND.

Inhaltsverzeichnis

 

Einleitung ................................................................................................................... 4

 

1. Neue Verantwortung Deutschlands in der Welt – aus Überzeugung für Frieden,

Freiheit und Menschenrechte ............................................................................... 6

1.1. Stärkung der werte- und regelbasierten internationalen Ordnung ......................... 6

1.2. Deutschland als Stabilitätsanker in der globalen Welt ............................................... 7

1.3. Aufbruch für die transatlantische Partnerschaft ......................................................... 8

1.4. Stabilität in ganz Europa .................................................................................................. 9

1.5. Besondere Verantwortung Deutschlands gegenüber Israel ................................... 10

1.6. Neue Aufmerksamkeit für den asiatisch-pazifischen Raum ................................... 11

1.7. Moderne und voll einsatzbereite Bundeswehr ......................................................... 11

1.8. Für eine nachhaltige Entwicklung in der Einen Welt ............................................... 13

1.9. Für eine Entwicklungspartnerschaft mit Afrika ........................................................ 14

1.10. Internationaler Klimaschutz zur Bewahrung der Schöpfung ................................. 15

 

2. Neue Weltpolitikfähigkeit – mit Leidenschaft für ein starkes Europa .................. 17

2.1. Ein starkes Deutschland in einem starken Europa ................................................... 17

2.2. Mehr Europa in der Weltpolitik ................................................................................... 18

2.3. Nachhaltiges Europa ...................................................................................................... 20

2.4. Wettbewerbsfähiges und stabiles Europa.................................................................. 21

2.5. Unser Europa der Ordnung und Sicherheit ............................................................... 24

2.6. Für ein modernes, innovatives und digitales Europa ............................................... 28

2.7. Ein handlungsfähiges und bürgernahes Europa ........................................................ 30

 

3. Neuer Wohlstand – mit nachhaltigem Wachstum zum klimaneutralen

Industrieland ...................................................................................................... 33

3.1. Unser Entfesselungspaket für die Wirtschaft ........................................................... 34

3.2. Sichere Arbeit mit Zukunft ........................................................................................... 37

3.3. Deutschland als klimaneutrales Industrieland bis 2045 .......................................... 40

3.4. Unser Energiekonzept für die Zukunft ....................................................................... 42

3.5. Nachhaltiges Wirtschaften zum Schutz unserer Ressourcen ................................. 45

3.6. Vorfahrt für intelligente Mobilität .............................................................................. 47

3.7. Eine Landwirtschaft, die stark und nachhaltig ist ..................................................... 50

3.8. Modernes Recht für mündige Verbraucherinnen und Verbraucher ..................... 56

Seite 1 von 139

4. Neue Fairness und soziale Sicherheit – für den gesellschaftlichen

Zusammenhalt.................................................................................................... 58

4.1. Finanzielle Sicherheit im Alter ..................................................................................... 58

4.2. Soziale Sicherheit in allen Lebenslagen ...................................................................... 61

4.3. Leistungsfähiges Gesundheitswesen .......................................................................... 63

4.4. Gute Pflege für mehr Sicherheit und Halt ................................................................. 67

4.5. Deutschlands Verantwortung für globale Gesundheit ............................................ 69

 

5. Neue Generationengerechtigkeit bei Finanzen und Steuern –

aus Verantwortung für unsere Kinder und Enkel ................................................. 70

5.1. Mit soliden Finanzen sicher in die Zukunft ............................................................... 70

5.2. Faire, leistungsgerechte und wettbewerbsfähige Steuern ..................................... 71

5.3. Vermögensbildung für jeden ........................................................................................ 73

5.4. Finanzplatz Deutschland stärken ................................................................................ 74

 

6. Neues Aufstiegsversprechen – für Deutschland als Chancen- und Familienland .. 75

6.1. Mehr Zeit, Raum und Unterstützung für Familien ................................................... 75

6.2. Gleichberechtigte Chancen für Frauen und Männer ............................................... 78

6.3. Aufstieg durch Bildung .................................................................................................. 79

 

7. Neuer Mut zur Innovation – aus Verantwortung für die Zukunft ......................... 84

7.1. Strategische Forschungs- und Innovationspolitik für Deutschland ...................... 84

7.2. Die besten Köpfe für unser Land ................................................................................. 89

7.3 Digitale Transformationsoffensive .............................................................................. 92

 

8. Neue Leistungsfähigkeit für einen modernen Staat – zum Wohl der

Bürgerinnen und Bürger ..................................................................................... 95

8.1. Modernisierungsjahrzehnt für den Staat ................................................................... 95

8.2. Die Bürgerinnen und Bürger im Mittelpunkt ............................................................ 99

8.3. Der öffentliche Dienst als moderner Arbeitgeber .................................................. 101

8.4. Digitale Infrastruktur ................................................................................................... 104

8.5. Nachhaltiger Staat........................................................................................................ 104

 

9. Neue Stärke für mehr Sicherheit – aus Verantwortung für unsere Freiheit ......... 106

9.1. Mehr Sicherheit überall und jederzeit ...................................................................... 106

9.2. Voller Schutz für Kinder und Frauen vor Gewalt und Missbrauch ...................... 108

Seite 2 von 139

9.3. Kein Raum für organisierte Kriminalität .................................................................. 110

9.4. Null Toleranz gegenüber kriminellen Familienclans .............................................. 111

9.5. Schutz unserer Demokratie vor Extremisten und Terroristen ............................. 112

9.6. Stärkung unserer Sicherheitsbehörden .................................................................... 116

9.7. Gefahrenabwehr im Cyberraum ................................................................................ 117

9.8. Wirksamer Bevölkerungsschutz................................................................................. 119

9.9. Starke und bürgernahe Justiz ..................................................................................... 121

 

10. Neue Lebensqualität in Stadt und Land – aus Liebe zu unserer Heimat .............. 123

10.1. Gutes Wohnen in lebendigen Dörfern und Städten............................................... 123

10.2. Gleichwertige Lebensverhältnisse und wirtschaftliche Entwicklung in allen

Regionen ........................................................................................................................ 126

10.3. Stärkung von Zusammenhalt und Ehrenamt ........................................................... 132

10.4. Integration als Fundament des Miteinanders ......................................................... 134

10.5. Deutschland als Kulturnation ..................................................................................... 135

10.6. Eine moderne Medienlandschaft ............................................................................... 137

10.7. Engagierte Sportförderung ......................................................................................... 138

 

Seite 3 von 139

1

Einleitung

2

 

3

Deutschland ist ein starkes Land. Das ist vor allem ein Verdienst der Bürgerinnen und Bür-4

ger, die jeden Tag anpacken, damit es bei uns auch morgen gut läuft. Wir haben starke Be-5

triebe, innovative Startups und Weltmarktführer, herausragende Forscherinnen und For-6

scher und eines der besten Gesundheits- und Sozialsysteme der Welt. Wir sind ein weltof-7

fenes und sicheres Land; ein Land, das Verantwortung für Sicherheit und Frieden, Freiheit 8

und Wohlstand in Europa und weltweit übernimmt.

9

Die Corona-Krise hat unser Land und besonders Staat und Verwaltung herausgefordert und 10

offengelegt, dass wir in einigen Bereichen schneller, besser und mutiger werden müssen.

11

Wir brauchen einen kraftvollen Neustart nach der Krise. Wir wollen die 20er Jahre zu einem 12

Modernisierungsjahrzehnt für unser Land machen. Dabei wollen wir das Gute besser ma-13

chen. Denn klar ist: Wir können nicht zaubern, aber wir können und wir wollen arbeiten und 14

gestalten.

15

Wir haben in der unionsgeführten Bundesregierung vieles erreicht. Unsere Politik für 16

Wachstum und solide Finanzen hat die Grundlage dafür geschaffen, dass wir in der Pande-17

mie umfassend handeln konnten: zum Schutz der Bürgerinnen und Bürger vor dem Virus, 18

für die Impfstoffrevolution und umfassende Hilfen für Betriebe und Beschäftigte. Das ist 19

nicht selbstverständlich und nicht garantiert. Erfolg ist kein Schicksal, sondern das Ergebnis 20

harter Arbeit.

21

Unsere Richtung ist klar: Wir wollen den Wandel gestalten, damit Deutschland an der Spitze 22

bleibt. Aber unsere Vorstellung ist: Sicherheit im Wandel. Wir wollen stark aus der Krise 23

kommen und eine neue Dynamik schaffen. Eine Dynamik, die Wirtschaft und Klimaschutz 24

voranbringt, Arbeitsplätze sichert und neue schafft, Familien unterstützt und eine moderne 25

Arbeitswelt gestaltet. Dabei stürmen wir nicht blind ins Morgen, sondern halten Maß und 26

Mitte.

27

Das bedeutet auch: Wir werden nichts versprechen, was wir nicht einhalten können. Durch 28

die hohen Ausgaben zur Bekämpfung der Pandemie sind die finanziellen Spielräume des 29

Staates deutlich eingeschränkt. Neue Schulden oder Steuererhöhungen wären aber der fal-30

sche Weg. Wir setzen auf wirtschaftliches Wachstum, das unserem Staat finanzielle Spiel-31

räume eröffnet. Diese Spielräume wollen wir für die finanzwirksamen Vorhaben dieses Pro-32

gramms nutzen.

33

Wir brauchen auch einen Neustart im Verhältnis zwischen Staat und Bürger. Der Staat muss 34

sich nach der Pandemie wieder deutlich zurückziehen und den Bürgerinnen und Bürgern 35

sowie den Unternehmen mehr Freiraum lassen. Wir müssen aufhören, jedes Problem bis ins 36

Detail zu regeln oder mit mehr Geld lösen zu wollen. Wir wollen einen verlässlichen und 37

modernen Staat.

38

Unser Ziel ist, so schnell wie möglich wieder zurück zu einer Normalität zu gelangen, die 39

uns Liebgewonnenes und Vermisstes zurückgibt und in der wir klug das Morgen gestalten.

40

Wir wollen, dass Deutschland eine starke Heimat bleibt, in der möglichst viele Menschen Seite 4 von 139

41

nach ihrem persönlichen Glück streben können. Wir wollen eine Gesellschaft, die zusam-42

menhält und Einsatz belohnt, Aufstieg ermöglicht und die diejenigen schützt, die sich nicht 43

selbst helfen können. Wir wollen ein modernes Deutschland, das an morgen denkt, heute 44

handelt und gemeinsam ganz Großes weiterwachsen lässt: wirtschaftliche Stärke, konse-45

quenten Klimaschutz und soziale Sicherheit. Deshalb soll Deutschland deutlich vor Mitte 46

des Jahrhunderts eine klimaneutrale Industrienation werden. Und gemeinsam mit unseren 47

europäischen Freunden wollen wir dafür sorgen, dass Deutschland und die EU weltpolitik-48

fähiger werden.

49

Wir haben für diese Aufgabe die richtigen Werte und Prinzipien: Vernunft statt Ideologie, 50

Innovationen statt Verbote, Soziale Marktwirtschaft statt sozialistischer Umverteilung, 51

Chancen statt Ängste, Respekt statt Bevormundung für Familien, christliches Menschenbild 52

und gesellschaftliche Vielfalt statt vorgefertigter Lebensentwürfe für jeden Einzelnen. Wir 53

spielen vermeintliche Gegensätze und unterschiedliche Gruppen nicht gegeneinander aus.

54

Wir verbinden sie. Weil wir wissen: Gerade in einer individualisierten Gesellschaft ist es 55

wichtig, dass wir bei den großen Fragen in eine gemeinsame Richtung gehen, dass jeder die 56

Gewissheit hat, Teil eines Ganzen zu sein – ob jung oder alt, ob auf dem Land oder in der 57

Stadt, ob Arbeitnehmer oder Arbeitgeber. Zusammenhalt ist für uns Ausdruck von Verant-58

wortung – gegenüber den Bürgerinnen und Bürgern unseres Landes ebenso wie gegenüber 59

unserer Umwelt und den zukünftigen Generationen. Jeder von uns ist Teil dieser Verant-60

wortungsgemeinschaft, Teil einer Nation und einer Europäischen Union mit gemeinsamer 61

Kultur, gemeinsamer Geschichte, gemeinsamen Werten, gemeinsamen Zielen und einer ge-62

meinsamen Zukunft.

63

 

 

Seite 5 von 139

64

1. Neue Verantwortung Deutschlands in der Welt – aus Überzeugung für 65

Frieden, Freiheit und Menschenrechte

66

 

67

Unser Unions-Versprechen: Wir arbeiten für ein weltoffenes Deutschland, das in einem Bündnis 68

von Demokratien gemeinsam mit unseren transatlantischen und europäischen Partnern die glo-69

balen Herausforderungen gestaltet. Unser Ziel heißt: Sicherheit und Frieden, Freiheit und Wohl-70

stand für die Menschen in Deutschland. Das Modernisierungsjahrzehnt, mit dem wir Deutsch-71

land weltpolitikfähig machen, kann nur mit neuer außenpolitischer Stärke gelingen.

72

Die Pandemie hat uns erneut gezeigt, wie vernetzt unsere Welt ist. Weder das Coronavirus noch 73

der Klimawandel oder die digitale Transformation machen an Grenzen halt. Wir können die gro-74

ßen weltweiten Menschheitsaufgaben nur lösen, wenn wir sie gemeinsam global anpacken. Es 75

ist in unserem eigenen Interesse, dass wir international mehr Verantwortung übernehmen.

76

Die Bedingungen dafür haben sich gravierend verändert: Wir befinden uns inmitten eines welt-77

weiten Epochenwechsels. Die große wirtschaftliche Dynamik in Asien und der Aufstieg Chinas 78

verändern das internationale Machtgefüge. Wir erleben die Missachtung des Völkerrechts und 79

Regelbrüche durch bedeutende Staaten des internationalen Systems, und wir sehen, dass sich 80

weltweit populistische Strömungen ausbreiten, auch in demokratischen Staaten. Hinzu kommt: 81

Neue Technologien bestimmen nicht nur unseren Alltag, sondern sind auch ein relevanter Faktor 82

der internationalen Politik.

83

Es reicht nicht, auf Krisen nur zu reagieren. Daher werden wir eine Sicherheitsarchitektur schaf-84

fen, die bessere Koordinierung und einen vorausschauenden strategischen Ansatz möglich 85

macht. Die Grundlage unseres weltweiten politischen Handelns ist und bleibt dabei das christli-86

che Menschenbild. Wir bekennen uns dazu, dass Deutschland aktiv zur internationalen Krisen-87

bewältigung und zur Gestaltung der Weltordnung beiträgt - in der Europäischen Union, der 88

NATO, den Vereinten Nationen und weiteren internationalen Organisationen.

89

 

90

1.1. Stärkung der werte- und regelbasierten internationalen Ordnung 91

Bündnis der Demokratien schmieden

92

Demokratien und autoritäre Staaten ringen um den globalen Gestaltungsanspruch im 21.

93

Jahrhundert. Es geht um den Fortbestand unserer freiheitlich-demokratischen Ordnung, die 94

autoritäre Staaten in Frage stellen und zu destabilisieren versuchen. Aus dieser Systemri-95

valität ergeben sich für uns die Verpflichtung und der Anspruch, die internationale regel-96

und wertebasierte Ordnung wieder zu stärken. Denn sie ist Voraussetzung dafür, dass wir 97

in Sicherheit und Frieden, Freiheit und Wohlstand leben können. Wir wollen, dass Deutsch-98

land und Europa gestärkt aus dieser Herausforderung hervorgehen – gemeinsam mit den 99

USA und zugleich auf eigene Fähigkeiten bedacht.

100

• Dafür müssen wir gemeinsam die Zusammenarbeit mit unseren transatlantischen Part-101

nern wieder ausbauen und neue handlungsfähige Strukturen mit unseren weltweiten de-Seite 6 von 139

102

mokratischen Partnern entwickeln, gerade im indo-pazifischen Raum und in Lateiname-103

rika. Dieses Bündnis der Demokratien muss prägenden Einfluss auf die globale Ordnung 104

nehmen, insbesondere in der Klima-, Handels-, Digital- und Sicherheitspolitik.

105

• Dabei leitet uns der Gedanke der Freiheit und der unantastbaren Würde des Menschen.

106

Deshalb setzen wir uns für Frieden, Freiheit und Sicherheit, für die Wahrung der Men-107

schenrechte, für die Einhaltung und Weiterentwicklung des Völkerrechts, für nachhal-108

tige Entwicklung sowie den freien und fairen Welthandel ein.

109

• In unserem außenpolitischen Handeln suchen wir stets die internationale Partnerschaft 110

und den multilateralen Ansatz. Die Vereinten Nationen (VN) und ihre Organisationen 111

alleine können die universelle Gültigkeit ihrer Grundsätze und Ziele beanspruchen. Die 112

Vereinten Nationen sind und bleiben daher grundlegend für die internationale Ordnung 113

und die Bewältigung internationaler Herausforderungen. Sie müssen daher entschei-114

dungs- und handlungsfähiger werden.

115

 

116

Universelle Geltung der Menschenrechte durchsetzen

117

Die Menschenrechte gelten universell, sind unteilbar und unveräußerlich. Dem Versuch au-118

toritärer Staaten, diesen Konsens aufzuweichen, treten wir entschieden entgegen.

119

• Hierfür wollen wir die Menschenrechtsmechanismen stärken. Kinder, Menschen mit Be-120

hinderungen oder Flüchtlinge sind dabei besonders schutzbedürftig.

121

• Wir wollen auch dem Menschenrecht auf Religionsfreiheit weltweit Geltung verschaffen 122

und die kritische Lage religiöser Minderheiten verbessern. Insbesondere werden wir uns 123

weiterhin beharrlich für verfolgte Christen einsetzen.

124

 

125

1.2. Deutschland als Stabilitätsanker in der globalen Welt 126

Deutschland muss als stärkste Wirtschaftsnation Europas eine führende außen- und sicher-127

heitspolitische Rolle einnehmen. Wir müssen mehr als bisher bereit sein, zusammen mit 128

unseren Verbündeten und Partnern unter Wahrung der völkerrechtlichen und unserer ver-129

fassungsrechtlichen Vorgaben alle Instrumente unserer Außen-, Verteidigungs- und Ent-130

wicklungspolitik anzuwenden – auch militärische, wenn dies nötig ist.

131

• Wir wollen einen stärkeren strategischen Ansatz in der Außen- und Sicherheitspolitik in 132

einer regelmäßig vorzulegenden nationalen Sicherheitsstrategie bündeln, die parlamen-133

tarisch erörtert wird.

134

• Wir müssen die Vernetzung der Sicherheit auch in unserer Regierung abbilden. Daher 135

wollen wir im Bundeskanzleramt einen Nationalen Sicherheitsrat schaffen, der außen-136

und sicherheitspolitische Koordinierung, strategische Vorausschau und nachrichten-137

dienstliche Erkenntnisse des Bundes und der Länder zusammenführt.

138

• Wir werden die politischen Stiftungen weiterhin angemessen finanziell ausstatten. Sie 139

leisten einen wesentlichen Beitrag zur politischen Bildung, zur Studienförderung und zur Seite 7 von 139

140

wissenschaftlichen Forschung sowie im internationalen Bereich zur Stärkung der Demo-141

kratie, der Zivilgesellschaft und der Entwicklungszusammenarbeit.

142

 

143

1.3. Aufbruch für die transatlantische Partnerschaft

144

Beziehungen zu Amerika stärken

145

Die USA sind unser wichtigster weltpolitischer Partner. Mit Präsident Joe Biden verbinden 146

wir die Chance eines neuen Aufbruchs für die transatlantische Partnerschaft. Nur in enger 147

Abstimmung werden wir gestaltende Impulse in der Klima-, Handels-, Wissenschafts- und 148

Technologiepolitik setzen können. Unser Ziel muss sein, gemeinsam den Gegnern der Frei-149

heit zu trotzen, globale Standards zu setzen und unseren technologischen Vorsprung zu 150

wahren und auszubauen. Hierzu ist eine weitere Vertiefung unserer Handels- und Wissen-151

schaftsbeziehungen unabdingbar.

152

• Unser Ziel ist ein umfassender transatlantischer Wirtschafts-, Handels- und Zukunfts-153

raum. Um die Technologieführerschaft des wertegebundenen Westens zu bewahren, 154

müssen wir unsere Spitzenforschung und Produktanwendung eng abstimmen.

155

• Wir wollen zudem die gemeinsame Bekämpfung der Organisierten Kriminalität und des 156

Terrorismus intensivieren sowie klimaaußenpolitisch mit den USA eng zusammenarbei-157

ten.

158

• Auch mit Kanada sowie den demokratisch gefestigten Staaten Lateinamerikas und der 159

Karibik wollen wir enger kooperieren.

160

• Den Austausch mit den USA auf gesellschaftlicher Ebene wollen wir deutlich ausbauen.

161

Wir wissen: Völkerverständigung beginnt bei persönlichen Freundschaften und muss im-162

mer wieder neu wachsen in jeder Generation. Deshalb wollen wir ein deutsch-amerika-163

nisches Jugendwerk einrichten und das erfolgreiche Jugendaustauschprogramm (Parla-164

mentarisches Patenschaftsprogramm) des Bundestages mehr als verdoppeln.

165

 

166

Die NATO als Wertegemeinschaft und Sicherheitsbündnis begreifen

167

Die NATO ist das Rückgrat der euroatlantischen Sicherheit. Garantiert wird diese Sicherheit 168

durch die nukleare Teilhabe, die Beistandsklausel für den Bündnisfall und die Präsenz ame-169

rikanischer Soldaten in Europa.

170

• Solange es Staaten mit Atomwaffen gibt, die unsere Wertegemeinschaft aktiv herausfor-171

dern, braucht Europa weiterhin den nuklearen Schutzschirm der USA und bleibt die deut-172

sche Beteiligung an der nuklearen Teilhabe im Rahmen der NATO ein wichtiger Bestand-173

teil einer glaubwürdigen Abschreckung im Bündnis. Wir stehen dafür, dass Deutschland 174

sich entschlossen zur Fortsetzung seiner nuklearen Teilhabe innerhalb der NATO be-175

kennt und die notwendigen Mittel dafür bereitstellt.

176

• Es muss Europas Anspruch sein, als gleichberechtigter Partner gemeinsam mit den USA 177

für Freiheit, Frieden und Demokratie in der Welt einzustehen. Dazu gehört, dass wir 178

mehr Verantwortung im Verbund mit unseren Bündnispartnern übernehmen müssen – Seite 8 von 139

179

sowohl bei robusten Einsätzen als auch bei Friedensmissionen und der Entwicklungszu-180

sammenarbeit vor Ort.

181

• Wir wollen den europäischen Pfeiler in der NATO stärken. Deutschland wird im Moder-182

nisierungsjahrzehnt einen wichtigen Beitrag zur Umsetzung des Konzeptes „NATO

183

2030“ und zur Ausrichtung der NATO für die nächste Generation leisten. Wir Europäer 184

müssen stärker als bisher für Stabilität in unserer Nachbarschaft Sorge tragen und für 185

eine faire Lastenverteilung eintreten. Wir bekennen uns explizit zum 2%-Ziel der NATO.

186

 

187

Rüstungskontrolle und Abrüstung voranbringen

188

Unsere langfristige Vision ist eine Welt, in der nukleare Waffen als Abschreckung nicht 189

mehr nötig sind. Wir drängen daher auf mehr Dynamik in der Rüstungskontrolle und Abrüs-190

tung und unterstützen neue Initiativen, die zu mehr Sicherheit beitragen.

191

• Unser langfristiges Ziel bleibt die vollständige Abrüstung aller nuklearen Mittelstrecken-192

raketen und Marschflugkörper in Europa. Bestehende Abkommen müssen eingehalten 193

werden.

194

• Wir unterstützen Maßnahmen gegen die Weiterverbreitung von Massenvernichtungs-195

waffen und die dazugehörigen Raketentechnologien sowie die Ächtung autonom-töten-196

der Waffensysteme.

197

• Die Bundeswehr muss über alle modernen Technologien verfügen, die zur Verteidigung 198

nötig sind. Dazu zählen auch unbemannte und KI-integrierende Systeme.

199

 

200

1.4. Stabilität in ganz Europa

201

Östliche Partner der EU stärken

202

Wir wollen die Unabhängigkeit der östlichen Partner der EU stärken sowie ihre politische 203

und wirtschaftliche Modernisierung zu europäischen Rechtsstaaten tatkräftig fördern. Un-204

ser Ziel bleibt, die europäische Friedensordnung wiederherzustellen, die durch die völker-205

rechtswidrige Annexion der Krim durch Russland außer Kraft gesetzt wurde.

206

• Wir werden uns weiterhin für ein Ende des Konflikts in der Ostukraine und für eine Rück-207

kehr zum legitimen völkerrechtlichen Status der Krim einsetzen. Solange die russische 208

Regierung dazu nicht bereit ist, müssen die Sanktionen bestehen bleiben.

209

• Wir stehen an der Seite der Menschen in Belarus, die sich für Freiheit und Demokratie 210

einsetzen. Das Regime muss den Weg zu einem friedlichen Übergang freimachen oder 211

andernfalls die Härte unserer Sanktionen zu spüren bekommen.

212

 

213

Russland konstruktiv und entschlossen begegnen

214

Russland fordert unsere Werte heraus. Wir wollen nicht, dass daraus wieder eine ernsthafte 215

militärische Bedrohung für uns in Europa wird. Um eigene Interessen durchzusetzen, greift 216

die russische Regierung mittlerweile zu offenen Drohungen gegen NATO-Verbündete, zu 217

Cyberangriffen, zu Desinformation und Propaganda.

Seite 9 von 139

218

• Wir brauchen in der EU und NATO zum einen mehr politische Geschlossenheit und zum 219

anderen die Fähigkeit zur glaubhaften Abschreckung und Resilienz, um diesen Heraus-220

forderungen zu begegnen.

221

• Wir suchen zugleich weiter den Dialog und die Zusammenarbeit mit Russland dort, wo 222

gemeinsame Interessen bestehen. So ist beispielsweise weltweiter Klimaschutz ohne 223

Russland nicht wirkungsvoll und wirtschaftliche Zusammenarbeit im allseitigen Inte-224

resse.

225

 

226

Lebensbedingungen im Südlichen Mittelmeerraum verbessern

227

Die Sicherheit Deutschlands und Europas hängt mit der Stabilität der Staaten im südlichen 228

Mittelmeerraum sowie im Nahen und Mittleren Osten zusammen. Wenn dort Terror und 229

wirtschaftliche Perspektivlosigkeit herrschen, werden viele Menschen versuchen, nach Eu-230

ropa zu fliehen.

231

• Deutschland und Europa müssen mittels Prävention und Vermittlung mehr Verantwor-232

tung in der Region übernehmen. Durch humanitäre Hilfe für Flüchtlinge und Programme 233

wie die Beschäftigungsoffensive „Cash for Work“ verbessern wir die Lebensperspektiven 234

der Menschen vor Ort. Zugleich unterstützen wir die Staaten der Region im Kampf gegen 235

den Terrorismus.

236

• Gerade mit den Anrainerstaaten im Mittelmeerraum bieten sich auch neue Chancen der 237

Zusammenarbeit – etwa auf dem Feld des grünen Wasserstoffs – die der europäischen 238

Nachbarschaftspolitik neue Impulse verleihen und unsere Nachbarn enger an unsere 239

Wertegemeinschaft binden können.

240

 

241

1.5. Besondere Verantwortung Deutschlands gegenüber Israel 242

Wir bekennen uns zu der besonderen Verantwortung Deutschlands gegenüber Israel. Die 243

Sicherheit und das Existenzrecht Israels sind Teil der deutschen Staatsräson. Die Menschen 244

in Israel haben ein Anrecht darauf, frei von Angst, Terror und Gewalt leben zu können. Des-245

halb stehen wir zum Selbstverteidigungsrecht von Israel.

246

• Wir treten dafür ein, dass der Iran seine Verpflichtungen aus der Wiener Nuklearverein-247

barung von 2015 (JCPOA) strikt einhält und sein ballistisches Raketenprogramm und 248

seine aggressive Rolle in der Region beendet.

249

• Wir unterstützen alles, was ein friedliches Zusammenleben von Israelis und Palästinen-250

sern fördert und eine Zweistaatenlösung ermöglicht.

251

• Wir wollen auf dieser festen Basis unsere enge und freundschaftliche Zusammenarbeit 252

mit Israel in allen Politikbereichen weiter ausbauen, insbesondere beim Jugendaus-253

tausch, in der Hochtechnologie und bei der Förderung von Startups.

254

 

 

Seite 10 von 139

255

1.6. Neue Aufmerksamkeit für den asiatisch-pazifischen Raum 256

Asiatisch-pazifische Demokratien als Partner begreifen

257

Das 21. Jahrhundert wird wesentlich von den Ländern Asiens und des Pazifiks geprägt wer-258

den. Wir setzen uns daher für enge Partnerschaften mit ihnen ein. Demokratien wie Aust-259

ralien, Neuseeland, Japan, Indien und Südkorea, die für die Stärkung der regelbasierten in-260

ternationalen Ordnung eintreten, sind unsere natürlichen Kooperations- und Wertepart-261

ner. Mit der Entsendung einer deutschen Fregatte in den asiatisch-pazifischen Raum zeigen 262

wir Präsenz und setzen das richtige Signal in Abstimmung mit unseren Partnern.

263

 

264

China auf Augenhöhe begegnen

265

Die größte außen- und sicherheitspolitische Herausforderung geht heute von der Volksre-266

publik China aus. Sie ist Wettbewerber, Kooperationspartner, aber auch systemischer Ri-267

vale. China hat den Willen und zusehends auch den Machtanspruch, die internationale Ord-268

nung nach eigenen Vorstellungen zu prägen und zu verändern – und tut dies mit allen Mit-269

teln. China nimmt durch Technologie- und Infrastrukturinvestitionen Einfluss auf andere 270

Staaten und schafft geostrategische Abhängigkeiten. Wir brauchen daher einen zweifachen 271

Ansatz:

272

• Einerseits müssen wir dort, wo es nötig ist, Chinas Machtwillen in enger Abstimmung mit 273

unseren transatlantischen Partnern und anderen gleichgesinnten Demokratien mit 274

Stärke und Geschlossenheit entgegentreten. Das gilt insbesondere beim Schutz des geis-275

tigen Eigentums, unserer Hochtechnologie und unserer Daten, damit wir nicht in gefähr-276

liche Abhängigkeiten geraten.

277

• Andererseits wollen wir dort, wo es möglich ist, eine Zusammenarbeit mit China anstre-278

ben. Eine echte Partnerschaft ist nur im Rahmen eines fairen Wettbewerbs unter glei-279

chen Bedingungen und bei Wahrung des Prinzips der Gegenseitigkeit möglich.

280

• Damit diese Balance auf europäischer Ebene gelingt, setzen wir uns für eine europäische 281

China-Strategie und ein gemeinsames Vorgehen des Westens ein.

282

 

283

1.7. Moderne und voll einsatzbereite Bundeswehr

284

Glaubwürdige Sicherheitsvorsorge leisten

285

Der Schutz von Frieden und Freiheit ist die vornehmste Aufgabe des Staates. Die Bürgerin-286

nen und Bürger unseres Landes müssen sich auf eine glaubwürdige Sicherheitsvorsorge ver-287

lassen können. CDU und CSU sind Garanten dafür, dass Deutschland dies nicht zu Lasten 288

unserer Kinder und Enkel vernachlässigt. Wir verstehen uns als Parteien der Bundeswehr.

289

Wer wie unsere Soldatinnen und Soldaten Verantwortung in schwierigen Einsätzen über-290

nimmt, hat Anspruch auf die beste Ausrüstung.

291

• Wir werden allen unseren militärischen Verpflichtungen nachkommen und die Vollaus-292

stattung der Bundeswehr erreichen. Deshalb werden wir die Zahl der Soldatinnen und 293

Soldaten der Bundeswehr gemäß Personalstrukturmodell auf 203 000 aufstocken. Wir Seite 11 von 139

294

stehen zu unseren Zusagen im Rahmen der NATO und der EU, den Verteidigungshaus-295

halt auf zwei Prozent des Bruttoinlandsprodukts weiter zu erhöhen. Damit erhält auch 296

die Bundeswehr Planungssicherheit.

297

• Spätestens bis 2030 wollen wir die Bundeswehr dazu befähigen, mindestens zehn Pro-298

zent der militärischen Fähigkeiten des Bündnisses bereitzustellen. Damit leisten wir ei-299

nen entscheidenden Beitrag für eine faire Lastenteilung und für den Zusammenhalt in 300

der NATO. Dieser Beitrag ist Voraussetzung für unsere Bündnisfähigkeit – und damit in 301

unserem eigenen Interesse.

302

• Landesverteidigung ist heute Bündnisverteidigung. Deutschland kann dies nur gemein-303

sam mit seinen Partnern leisten. Deswegen muss die Bundeswehr den Weg der Koope-304

ration und Integration mit den Streitkräften in Europa und von Verbündeten weiter be-305

schreiten und dabei auf eine gemeinsame strategische Kultur hinarbeiten. An Auslands-306

einsätzen werden wir uns immer dann mit Bündnispartnern beteiligen, wenn deutsche 307

Sicherheitsinteressen gefährdet sind.

308

 

309

Bundeswehr als Teil der Gesellschaft begreifen

310

Die Soldatinnen und Soldaten der Bundeswehr arbeiten tagtäglich dafür, dass wir in Frie-311

den, Freiheit und Sicherheit leben können. Zugleich stehen sie bereit, um in Not- und Kata-312

strophenfällen auch im Inland zu helfen.

313

• Soldatinnen und Soldaten verdienen unseren Respekt und unsere Anerkennung.

314

• Die Bundeswehr hat einen festen Platz in der Mitte unserer Gesellschaft. Damit gehört 315

sie auch ganz selbstverständlich in unsere Schulen. Die Jugendoffiziere leisten hier eine 316

wertvolle Arbeit. Wir wollen sie ausbauen und dafür sorgen, dass der Besuch der Ju-317

gendoffiziere einen festen Platz in der Schullaufbahn hat.

318

• Das kostenlose Bahnfahren für unsere Soldatinnen und Soldaten ist ein voller Erfolg, den 319

wir fortsetzen und perspektivisch auf den öffentlichen Personennahverkehr ausweiten 320

wollen.

321

• Der Eid auf unser Land gehört in die Mitte unserer Gesellschaft. Deshalb wollen wir, dass 322

Gelöbnisse grundsätzlich in der Öffentlichkeit stattfinden.

323

• Um ihre Aufgaben erfüllen zu können, braucht die Bundeswehr eine einsatzbereite Re-324

serve. Wir wollen den freiwilligen Wehrdienst im Heimatschutz fortführen. Damit geben 325

wir jungen Menschen die Chance, eine Zeit lang in der Bundeswehr zu dienen und da-326

nach die Reserve zu stärken.

327

• Für Extremisten ist in der Bundeswehr kein Platz.

328

 

329

Beste Ausrüstung für die Bundeswehr gewährleisten

330

Die Bundeswehr muss optimal ausgerüstet und organisiert sein. Die Eckpunkte für die Bun-331

deswehr der Zukunft dienen dafür als Leitfaden. Wir werden das Beschaffungswesen erneu-332

ern, damit sie ihr Material zügig erhält.

Seite 12 von 139

333

• Wir müssen neue Fähigkeiten im Cyber- und Informationsraum sowie im Weltraum auf-334

bauen und streben eine rechtliche Regelung der militärischen Nutzung von KI, Cyber-335

und Weltraumfähigkeiten an.

336

• Zum Schutz unserer Soldatinnen und Soldaten und im Einsatz setzen wir uns für die mi-337

litärisch heute selbstverständliche Bewaffnung von Drohnen ein. Die jüngsten Kämpfe 338

um die Region Bergkarabach haben deutlich gemacht, wie stark kriegerische Auseinan-339

dersetzungen von Drohnen geprägt werden. Wir müssen unsere Soldatinnen und Solda-340

ten in die Lage versetzen, diese Gefahren zu ihrem Schutz wirksam abwehren zu können.

341

Wir wollen deshalb wirksame Fähigkeiten der Bundeswehr zur Drohnenabwehr, Luftver-342

teidigung und zum elektronischen Kampf deutlich stärken.

343

• Die Kosten für militärische Beschaffungen wollen wir durch die Entwicklung und Umset-344

zung gemeinsamer Rüstungsprojekte mit europäischen Partnern begrenzen. Dabei wol-345

len wir eine leistungsfähige wehrtechnische Industrie in Deutschland erhalten. Wir wol-346

len die für die europäische Verteidigungspolitik zentralen Schlüsselprojekte engagiert 347

vorantreiben. Rüstungsexporte sind dabei ein gestaltendes Element der Sicherheitspoli-348

tik. Deswegen setzen wir uns für einheitliche europäische Richtlinien ein.

349

• Wir wollen mit einem Bundeswehrplanungsgesetz dazu beitragen, dass Sicherheit unab-350

hängig von konjunkturellen Schwankungen und kurzfristigen Änderungen politischer 351

Stimmungsbilder als Kernaufgabe des Staates verlässlich finanziell gesichert bleibt.

352

 

353

1.8. Für eine nachhaltige Entwicklung in der Einen Welt 354

Entwicklungszusammenarbeit stärken

355

Die Ziele der Vereinten Nationen für eine nachhaltige Entwicklung der Agenda 2030, das 356

Pariser Klimaschutzabkommen und die Menschenrechte sind unser Leitbild für eine ge-357

rechte Globalisierung, für eine friedliche und nachhaltige Entwicklung in der Welt. Dabei 358

sind folgende Ziele und Ansätze für uns vorrangig:

359

• Wir können eine Welt ohne Hunger erreichen. Sie ist möglich, wenn Konflikte gelöst, 360

steigende Beträge in Ernährungshilfen geleistet und die Erträge der Landwirtschaft welt-361

weit gesteigert werden.

362

• Im Rahmen der bilateralen Zusammenarbeit unterstützen wir Menschen in den am we-363

nigsten entwickelten Ländern, damit sie Zugang zu staatlicher Grundversorgung wie Bil-364

dung, Wasser, Ernährung und Gesundheit bekommen.

365

• Um künftigen Pandemien vorzubeugen, werden wir im Rahmen der globalen Gesund-366

heitspolitik die Wechselbeziehungen von Mensch, Tier und Umwelt (One-Health-An-367

satz) stärker als bisher beachten.

368

• Wir wollen die Entwicklungszusammenarbeit und strategische Außenwirtschaftsförde-369

rung stärker verknüpfen. So erleichtern wir es Unternehmen, in moderne und digitale 370

Arbeitsplätze in Entwicklungsländern zu investieren und so den Wohlstand für alle zu 371

fördern.

Seite 13 von 139

372

• Wenn Staat und Wirtschaft enger kooperieren, können zudem Menschenrechte sowie 373

soziale und ökologische Mindeststandards besser sichergestellt werden. Außerdem wol-374

len wir gemeinsam das berufliche duale Ausbildungssystem auf die jeweiligen Gegeben-375

heiten vor Ort anpassen und noch stärker fördern.

376

• Bei all unseren Ansätzen wollen wir insbesondere Frauen und Mädchen stärken. Wir set-377

zen uns für ihr Recht auf Selbstbestimmung und Familienplanung ein.

378

 

379

Entwicklungszusammenarbeit verlässlich finanzieren

380

Deutschland gehört zu den wenigen Ländern, die in den vergangenen beiden Jahren 0,7 Pro-381

zent des Bruttonationaleinkommens für öffentliche Entwicklungszusammenarbeit ausge-382

geben haben, wie es weltweit als Ziel vereinbart wurde.

383

• Wir wollen auch in Zukunft 0,7 Prozent des Bruttonationaleinkommens für öffentliche 384

Entwicklungszusammenarbeit ausgeben. Damit wollen wir dazu beitragen, die durch die 385

Pandemie ausgelösten Entwicklungsrückschritte in vielen Ländern der Welt rasch wieder 386

umzukehren. Das ist auch im Interesse Deutschlands.

387

• Um die vorhandenen Mittel bestmöglich einsetzen zu können, ist eine noch intensivere 388

Abstimmung und Arbeitsteilung – vor allem im Rahmen der Europäischen Union – nötig.

389

Darüber hinaus wollen wir neue Geber von Entwicklungsgeldern wie China auf gemein-390

same Standards verpflichten. Auch in Zukunft wollen wir eng mit den Kirchen und Nicht-391

regierungsorganisationen in der Entwicklungszusammenarbeit kooperieren.

392

• Wir erwarten von den Partnerländern bei der Entwicklungszusammenarbeit auch eine 393

enge Kooperation bei der Bekämpfung von Fluchtursachen und illegaler Migration (zum 394

Beispiel Rücknahme eigener Staatsangehöriger).

395

 

396

1.9. Für eine Entwicklungspartnerschaft mit Afrika

397

Eine friedliche, wirtschaftliche und ökologische Entwicklung unseres Nachbarkontinents 398

Afrika ist im deutschen und europäischen Interesse. Unsere Afrikapolitik gestalten wir auf 399

Basis eines modernen und differenzierten Afrikabildes. Afrika ist für uns auch ein Kontinent 400

mit einer ehrgeizigen jungen Generation, großer wirtschaftlicher Dynamik und hoher Inno-401

vationskraft.

402

• Wir wollen den Marshallplan mit Afrika zu einer vertieften institutionellen Partnerschaft 403

in Form eines EU-Afrikarats weiterentwickeln. Die EU muss attraktive Angebote der Zu-404

sammenarbeit unterbreiten, die auf Transparenz und finanzieller Nachhaltigkeit beru-405

hen und das lokale Potenzial ausschöpfen. Die Afrikanische Kontinentale Freihandels-406

zone bietet die Chance für weitere Öffnungsschritte des EU-Binnenmarkts, für den Kli-407

maschutz und für die Kooperation in Zukunftstechnologien.

408

• Nachhaltige Entwicklung in Afrika ist ohne Investitionen privater Unternehmen nicht 409

möglich. Daher setzen wir bei der Zusammenarbeit mit Afrika auf die Prinzipien der So-410

zialen Markwirtschaft. Besondere Bedeutung dabei haben der Zugang zu Kapital sowie Seite 14 von 139

411

staatliche Garantien zur Risikoabsicherung bei Handel, Investitionen und Projekten. Un-412

verzichtbar sind Anstrengungen bei der Korruptionsbekämpfung und für Rechtsstaat-413

lichkeit, die wir fordern und fördern. Wir wollen dazu beitragen, die Chancen der Digita-414

lisierung, der Erneuerbaren Energien oder nachhaltiger Mobilität zu nutzen. In Partner-415

schaft mit der deutschen Wirtschaft und im Rahmen unserer europäischen Klimaaußen-416

politik treiben wir so die Energiewende in Afrika voran.

417

• Afrika ist für die langfristige Sicherheit Europas von zentraler Bedeutung. Dies zeigt 418

nicht zuletzt die anhaltende Migration in Richtung Europa. Wir wollen die Staaten und 419

Gesellschaften Afrikas im Laufe des Jahrzehnts dazu befähigen, selbst und mithilfe der 420

Afrikanischen Union den Terrorismus zu bekämpfen und für ihre eigene Sicherheit zu 421

sorgen.

422

 

423

1.10. Internationaler Klimaschutz zur Bewahrung der Schöpfung 424

Überlebensfragen der gesamten Menschheit und deshalb Schwerpunkte unserer Klima-Au-425

ßenpolitik sind das Erreichen der Klimaziele sowie die Bewahrung der Artenvielfalt und der 426

Wälder. Wir setzen uns für ein Bündnis zur Stärkung innovativer klimafreundlicher Techno-427

logien weltweit ein. Wo der Klimawandel die Sicherheit gefährdet, muss die internationale 428

Gemeinschaft präventiv handeln.

429

• Dafür wollen wir die Schlichtungsmöglichkeiten der Vereinten Nationen verstärken.

430

• Wir wollen im Rahmen der internationalen Klimafinanzierung die Entwicklungsländer bei 431

der Anpassung an den Klimawandel und beim Umweltschutz durch den Transfer von 432

technischem Wissen unterstützen. Daher streben wir im Rahmen unserer europäischen 433

Clean-Tech-Initiative eine enge Klimapartnerschaft mit Ländern in Asien, in der arabi-434

schen Welt und in Lateinamerika an.

435

• Die Herausforderungen der Erderwärmung sind global. Deshalb wollen wir, dass 436

Deutschland als weltweit führendes und modernes Industrieland hier im Rahmen der In-437

ternationalen Gemeinschaft einen übergeordneten Beitrag leistet. So wollen wir bei-438

spielsweise den Aufbau und die Finanzierung von Abfallsammel- und Sortiersystemen 439

unterstützen sowie die Zusammenarbeit gegen die Meeres- und Umweltverschmutzung 440

intensivieren.

441

• Wir setzen uns dafür ein, dass internationale Kohlenstoffsenken wie Regenwälder ge-442

schützt werden und ihre Leistung honoriert wird. Unser ist Ziel ist, dass langfristig ein 443

globaler Emissionshandel etabliert wird.

444

• Wir wollen moderne Handelspolitik auch als Instrument dazu nutzen, hohe Standards 445

und wirksame Maßnahmen für den Klimaschutz global durchzusetzen.

446

• Zur Eindämmung der Erderwärmung ist entscheidend, dass Entwicklungs- und Schwel-447

lenländer ihre Wirtschaft von Anfang an klimafreundlich aufbauen. Wir wollen, dass in-448

ternationale Erfolge beim Klimaschutz auch in nationalen Klimabilanzen berücksichtigt 449

werden – zusätzlich zu den eigenen Klimaschutzmaßnahmen in Deutschland. Denn jede Seite 15 von 139

450

eingesparte Tonne CO2 zählt – egal, wo sie eingespart wird. Wir wollen uns deshalb dafür 451

einsetzen, dass sich die nächste Klimakonferenz in Glasgow darauf verständigt, neben 452

den ambitionierten Klimaschutzmaßnahmen auf nationaler und europäischer Ebene 453

auch Emissionsminderungen durch Klimaschutzprojekte in Entwicklungs- und Schwel-454

lenländern auf nationale Klimaziele anteilig anzurechnen. Dabei müssen Doppelanrech-455

nungen wirksam ausgeschlossen werden.

456

 

 

Seite 16 von 139

457

2. Neue Weltpolitikfähigkeit – mit Leidenschaft für ein starkes Europa 458

 

459

Unser Unions-Versprechen: Wir arbeiten für ein modernes Europa, das weltpolitikfähig ist, um 460

die globalen Herausforderungen gemeinsam zu meistern. Dafür muss Europa handlungsfähiger, 461

mutiger und entschlossener werden. Denn nur wenn es Europa gut geht, geht es auch Deutsch-462

land gut.

463

Europa wird herausgefordert – von innen und von außen. Innerhalb Europas setzen Populisten 464

von links und rechts die europäische Demokratie unter Druck. Zusätzlich erschweren Nationa-465

lismus und Eigeninteressen einiger EU-Mitgliedsstaaten immer wieder gemeinsame europäische 466

Lösungen oder verhindern ein Auftreten der EU mit einer Stimme. Und schließlich ist die EU in 467

zentralen Bereichen, wie etwa der Verteidigungspolitik, nicht so handlungsfähig, wie wir uns das 468

wünschen.

469

Auch von außen sehen wir den europäisch-abendländischen Leitgedanken der Demokratie wie 470

auch der Sozialen Marktwirtschaft unter Druck und im Wettbewerb mit konkurrierenden Ge-471

sellschafts- und Wirtschaftsmodellen. Freier Welthandel mit offenen Märkten, der uns Wohl-472

stand gebracht hat, ist keine Selbstverständlichkeit mehr.

473

Unsere Antwort auf diese Herausforderung lautet: Mehr Europa! Denn nur gemeinsam mit un-474

seren europäischen Partnern werden wir die Herausforderungen meistern. Dafür brauchen wir 475

schnellere und dynamischere Entscheidungen dort, wo es europäische Lösungen und entschlos-476

senes Handeln auf internationaler Ebene braucht. Dabei gilt die Formel: Nicht jedes Problem in 477

Europa ist ein Problem für Europa. Gleichzeitig werden wir das Modernisierungsjahrzehnt auch 478

auf Europa erstrecken: Wir investieren in Technologien und Innovationen, damit Europas Wirt-479

schaft auch in Zukunft Garant für Wohlstand, Arbeitsplätze und Nachhaltigkeit bleibt. Wir in-480

vestieren in Europas Sicherheit, ob nach innen oder außen, damit auch unsere Kinder und Enkel 481

in Europa in Frieden, Freiheit und Sicherheit leben können.

482

 

483

2.1. Ein starkes Deutschland in einem starken Europa

484

Europa wollen – Europa machen

485

Die Europäische Union ist und bleibt das größte politische Erfolgsprojekt unserer Zeit. Sie 486

hat den Menschen in Deutschland und Europa Frieden, Freiheit, Demokratie, Sicherheit und 487

Wohlstand gebracht. Auch wenn nicht immer alles perfekt läuft: Die Menschen in unserem 488

Land profitieren tagtäglich von Europa.

489

• Deshalb haben wir von Anfang an den Prozess der europäischen Einigung leidenschaft-490

lich vorangetrieben und Brücken zwischen Ost und West gebaut.

491

• Wir wollen europäische Kooperation und Integration statt nationalistischer Abschot-492

tung. Nur so werden wir Deutschland und Europa widerstandsfähiger machen: bei Pan-493

demien, ökonomischen Krisen, terroristischen Bedrohungslagen und Cyberangriffen.

494

 

 

Seite 17 von 139

495

Deutsch-französischer Motor der europäischen Einigung sein

496

Mit überzeugten Europäern wie Konrad Adenauer, Helmut Kohl, Franz Josef Strauß, Theo 497

Waigel und Angela Merkel haben wir die europäische Einigung geprägt. Unsere unverrück-498

baren Prinzipien und europäischen Grundwerte der offenen Gesellschaft, der repräsentati-499

ven Demokratie, der Sozialen Marktwirtschaft, der Rechtsstaatlichkeit, der Subsidiarität, 500

der friedlichen Konfliktlösung und Konsensfindung in Europa leiten uns.

501

• Die enge deutsch-französische Freundschaft ist für uns elementar und hat durch den 502

Aachener Vertrag eine neue Dynamik bekommen, die jetzt mit Leben gefüllt werden 503

muss. Das gilt insbesondere etwa bei den großen Herausforderungen wie der Künstli-504

chen Intelligenz, der Wasserstofftechnologie und der Batteriezellforschung sowie bei 505

der sicherheits- und außenpolitischen Zusammenarbeit. Die deutsch-französische 506

Freundschaft ist und bleibt Motor für die europäische Einigung und Fortentwicklung – 507

aber nicht exklusiv, sondern als Initialzündung für mutige Schritte mit anderen.

508

• Wir wollen enge Abstimmungen und Austausch zu konkreten Problemlösungen. Unser 509

europäischer Ansatz achtet die berechtigten Interessen aller Mitgliedstaaten unabhän-510

gig von ihrer Größe. Die Zusammenarbeit mit unseren Nachbarn und Freunden im Bene-511

lux-Raum sowie unseren östlichen Nachbarstaaten, wie zum Beispiel Tschechien, hat 512

sich vor allem in der Pandemie bewährt.

513

• Für uns bleibt die enge Zusammenarbeit und die Pflege der Freundschaft mit Polen eine 514

zentrale Aufgabe deutscher Außenpolitik.

515

 

516

2.2. Mehr Europa in der Weltpolitik

517

Europa für den globalen Systemwettbewerb fit machen

518

Eine größere deutsche und europäische Unabhängigkeit und Sicherheit sind Grundvoraus-519

setzungen, um im globalen Systemwettbewerb bestehen zu können. Deswegen muss Eu-520

ropa mit einer Stimme sprechen, um weltpolitikfähig zu werden. In einer geopolitisch im-521

mer unsichereren und komplexeren Welt muss Europa im eigenen Interesse mehr außen-522

und sicherheitspolitische Verantwortung für sich und die Welt übernehmen.

523

• Wir wollen in der Außen- und Sicherheitspolitik Mehrheitsentscheidungen. Mehr Selbst-524

bewusstsein nach außen erreichen wir durch mehr Geschlossenheit nach innen. Dafür 525

müssen wir in der Europäischen Union schneller als bisher zu gemeinsamen Positionen 526

kommen und bereit sein, diese wirkungsvoll umzusetzen.

527

• Wir wollen eine verbesserte und flexible Sicherheitsarchitektur, die auch das Vereinigte 528

Königreich einbezieht, um unsere Positionen stärker einzubringen und mit unseren Part-529

nern zu koordinieren.

530

• Wir setzen uns für einen zusätzlichen, gemeinsamen ständigen Sitz der EU im Sicher-531

heitsrat der Vereinten Nationen ein.

Seite 18 von 139

532

• Wir werden mit einem Bündnis der Gestaltungswilligen die Initiative ergreifen, um die 533

außen- und sicherheitspolitische Koordinierung zu verbessern und die Wirksamkeit der 534

europäischen Verteidigung zu erhöhen.

535

• Wir wollen ein solches außen- und sicherheitspolitisches Kerneuropa nicht exklusiv ge-536

stalten. Es muss gerade auch jene Staaten miteinbeziehen, deren Sicherheitsinteressen 537

in besonderer Weise betroffen sind, etwa an der Ostflanke der NATO.

538

• Wir wollen im Rahmen der Europäischen Verteidigungsunion und PESCO langfristig ge-539

meinsame europäische Streitkräfte aufstellen. Dafür wollen wir die militärische Zusam-540

menarbeit der nationalen Streitkräfte weiter verbessern, noch stärker vernetzen und ge-541

meinsame europäische Einsatzfähigkeiten innerhalb und außerhalb der NATO ausbauen.

542

• Wir setzen auf intensivere verteidigungspolitische Zusammenarbeit im Sinne der ver-543

netzten Sicherheitspolitik. Nur so kann die Stärke der Europäischen Union – die Bünde-544

lung diplomatischer, militärischer und entwicklungspolitischer Mittel – voll zur Geltung 545

kommen.

546

• Wir bekennen uns uneingeschränkt zur NATO.

547

• Wir wollen die eigene Führungsfähigkeit für EU-Missionen durch die Errichtung eines 548

Europäischen Hauptquartiers realisieren.

549

• Wir wollen mithilfe der Europäischen Rüstungsagentur und des Europäischen Verteidi-550

gungsfonds gemeinsame Rüstungsprojekte und -beschaffung fördern. Die EU-Mitglied-551

staaten vermeiden so unnötige Ausgaben, erlangen bessere Verteidigungsfähigkeit und 552

entwickeln Schritt für Schritt eine gemeinsame Sicherheitskultur sowie gemeinsame eu-553

ropäische Rüstungsexportrichtlinien.

554

• Wir bauen die europäische Cyber-Brigade aus, um Cyberattacken, Terrorismus, Bedro-555

hung kritischer Infrastruktur und Desinformation europaweit erfolgreich abwehren und 556

selbst offensive Fähigkeiten entwickeln zu können.

557

 

558

Europa vertiefen vor erweitern

559

Es liegt in unserem Interesse, mit den Ländern in unmittelbarer Nachbarschaft zur EU mög-560

lichst enge und freundschaftliche Beziehungen zu pflegen. Dabei gilt für uns der Grundsatz: 561

Vertiefung vor Erweiterung.

562

• Wir stehen dazu, die Bindung der Westbalkanstaaten an die Europäische Union weiter 563

zu intensivieren, denn Sicherheit und Stabilität in unserer unmittelbaren Nachbarschaft 564

sind vom größten Interesse. Der innere Zusammenhalt der Europäischen Union darf je-565

doch durch die Aufnahme neuer Mitglieder nicht geschwächt werden. Kandidatenländer 566

müssen alle Beitrittskriterien voll und ganz erfüllen.

567

• Das Vereinigte Königreich bleibt auch nach dem Austritt aus der Europäischen Union 568

unser enger Partner. Wir werden darauf achten, dass die vertraglichen Zusicherungen Seite 19 von 139

569

für einen fairen Handel durch Einhaltung von vergleichbaren Sozial- und Umweltstan-570

dards sowie zur Wahrung des Friedens durch das Karfreitagsabkommen in Irland und 571

Nordirland eingehalten werden. Wir streben auch eine enge Zusammenarbeit bei der in-572

neren und äußeren Sicherheit und im Bereich der Wissenschaft an.

573

• Wir werden einen Großbritannien-Koordinator der Bundesregierung einsetzen, der die 574

vielfältigen bilateralen Beziehungen bündelt.

575

• Wir setzen uns dafür ein, die UK-German Connection zu einem Deutsch-Britischen Ju-576

gendwerk auszubauen und ein neues Parlamentarisches Patenschaftsprogramm des 577

Bundestages für ein Schüler-Austauschjahr in Großbritannien einzurichten.

578

 

579

Beziehungen zur Türkei neu ordnen

580

Die Türkei ist von großer strategischer und wirtschaftlicher Bedeutung für Deutschland und 581

die Europäische Union. Zudem sind unsere Länder vor allem durch Kontakte der Menschen 582

eng miteinander verbunden. Wir wollen deshalb weiter eng mit der Türkei zusammenarbei-583

ten und setzen auf einen offenen, kritischen und konstruktiven Dialog mit der türkischen 584

Führung. Wir wollen, dass Deutschland weiter die bilateralen Beziehungen und die zivilge-585

sellschaftliche Vielfalt in der Türkei stärkt.

586

Wir beobachten aber auch, dass sich die Türkei von dem Ziel entfernt, die politischen EU-587

Beitrittskriterien - Demokratie, Rechtsstaatlichkeit und die Achtung der Menschenrechte -

588

zu verwirklichen. Unsere Beziehungen zur Türkei brauchen neue Perspektiven. Eine Voll-589

mitgliedschaft der Türkei in der EU wird es mit uns nicht geben. Stattdessen werden wir 590

eine enge Partnerschaft vereinbaren.

591

• In einem ersten Schritt der Wiederannäherung sollen gemeinsame Interessen definiert 592

und vertragliche Vereinbarungen zur Umsetzung beschlossen werden.

593

• Die NATO ist eine Wertegemeinschaft. Ihre Mitglieder müssen sich zur Einhaltung von 594

Menschenrechten und Rechtsstaatlichkeit verpflichten. Die Türkei muss als NATO-Part-595

ner ihren Beitrag zur kollektiven Sicherheit leisten und die Verpflichtung zu sicherheits-596

politischen Konsultationen erfüllen.

597

 

598

2.3. Nachhaltiges Europa

599

European Green Deal zu einer europäischen Wachstumsgeschichte machen

600

Der European Green Deal ist eine umfassende und ambitionierte Nachhaltigkeitsstrategie 601

in den Bereichen Energie, Industrie, Kreislaufwirtschaft, Verkehr, Gebäude, Umweltschutz 602

und Biodiversität, Landwirtschaft und Lebensmittelwirtschaft. Wir unterstützen seine am-603

bitionierte Zielsetzung der Transformation unseres heutigen Lebens und Wirtschaftens hin 604

zu einer nachhaltigeren und ökologischeren Gesellschaft.

605

• Mit dem Green Deal machen wir Europa zum ersten klimaneutralen Kontinent der Welt.

Seite 20 von 139

606

• Wir wollen einen EU-Klimaaußenbeauftragten zur Stärkung und Bündelung der EU-607

Klimaaußenpolitik, der Europa als globalen Akteur im Einsatz für den Klimaschutz posi-608

tioniert. Er soll eine Europäische Clean-Tech-Initiative voranbringen, die Partnerschaften 609

bei modernsten Umwelttechnologien aufbaut.

610

• Wir werden den Green Deal zu einer echten Wachstumsstrategie, einem neuen nachhal-611

tigen Wachstumsmotor der EU, entwickeln. Dazu setzen wir auf marktwirtschaftliche In-612

strumente, auf Anreize statt auf Verbote, auf Innovationen und Wettbewerb und auf die 613

Zusammenarbeit mit Industrie und Landwirtschaft.

614

• Wir werden den europäischen Emissionshandel auf den Verkehr- und Wärmesektor aus-615

weiten. Mit mehr Ehrgeiz wird der Emissionshandel in allen Bereichen sicherstellen, dass 616

sich ein stabiler, fairer und transparenter Preis für Treibhausgase bildet.

617

• Wir wollen in Verbindung mit nachhaltiger Entwicklungshilfe Europa im globalen Roh-618

stoffwettbewerb stärken und eine europäische Alternative zur chinesischen Seiden-619

straße bieten.

620

• Wir wollen einen Green Deal, der mehr Arbeitsplätze schafft und mehr Wertschöpfung 621

in die Regionen Europas bringt. Deshalb müssen alle Strategien des Green Deals mit ei-622

ner Folgenabschätzung und mit Maßnahmen zur Begleitung des Übergangs verbunden 623

werden.

624

 

625

2.4. Wettbewerbsfähiges und stabiles Europa

626

Stabilitätskriterien für die Wirtschafts- und Währungsunion durchsetzen

627

Die Wirtschafts- und Währungsunion (WWU) und die Einführung des Euro sind Meilen-628

steine der europäischen Integration. Wir treten ein für eine echte Stabilitäts- und Wachs-629

tumsunion.

630

• Wir wollen die Fiskalregeln des Stabilitäts- und Wachstumspakts und des Fiskalvertrags 631

nach der Corona-Pandemie zügig wieder in Kraft setzen und sie weiterentwickeln, ohne 632

sie aufzuweichen.

633

• Wir wollen Ermessensspielräume beim Defizitverfahren einschränken und das Prinzip 634

der Konditionalität stärken. Verstöße gegen die Stabilitätskriterien müssen konsequent 635

sanktioniert werden.

636

• Die Europäische Union hat mit dem Aufbauinstrument „Next Generation EU“ in Verbin-637

dung mit dem Mehrjährigen Finanzrahmen 2021 bis 2027 angemessen und solidarisch 638

auf die Corona-Krise reagiert. Europa kann nur gemeinsam stark sein. Daher haben wir 639

uns für die Unterstützung der von der Krise besonders betroffenen Länder im Süden Eu-640

ropas eingesetzt.

Seite 21 von 139

641

• Die damit verbundene europäische Schuldenaufnahme ist befristet und einmalig. Sie ist 642

kein Einstieg in eine Schuldenunion – und darf es nie werden. Denn für eine verantwort-643

liche Finanz- und Haushaltspolitik in den Mitgliedstaaten müssen Haftung und Verant-644

wortung in einer Hand bleiben.

645

• Die Verträge sprechen eine klare Sprache: Jeder Mitgliedstaat haftet für seine eigenen 646

Schulden. Wir lehnen es weiterhin ab, mitgliedstaatliche Schulden oder Risiken zu ver-647

gemeinschaften. Denn wir wollen eine echte Stabilitätsunion und keine Schulden- und 648

Haftungsunion.

649

• Unser Europa steht für eine solide Haushaltspolitik. Haushaltsmittel müssen vor allem 650

für Maßnahmen eingesetzt werden, die einen europäischen Mehrwert schaffen. Sie müs-651

sen noch stärker auf europäische Zukunftsaufgaben konzentriert werden.

652

 

653

Europäische Wirtschaftspolitik besser abstimmen, Währungsunion stärken

654

Um die Wirtschafts- und Währungsunion zu stärken, müssen die nationalen Wirtschaftspo-655

litiken besser koordiniert und aufeinander abgestimmt werden.

656

• Wir wollen eine stärkere Rolle für den EU-Wirtschafts- und Währungskommissar, insbe-657

sondere zur Durchsetzung der Stabilitätskriterien. Die länderspezifischen Empfehlungen 658

sollten auf Schlüsselbereiche zielen – vor allem auf Strukturreformen und Haushaltskon-659

solidierung. Die Strukturfonds sollen dafür eingesetzt werden, Reformprozesse und In-660

novationen zu unterstützen.

661

• Europäische Finanzmarktregulierung (Taxonomie), Nachhaltigkeitsberichterstattung 662

und Lieferkettengesetzgebung bedürfen gerade für mittelständische Firmen präziser 663

globaler Wettbewerbsanalysen.

664

• Wir setzen uns für eine EU-Regelung für Lieferketten ein. Diese muss die Standards des 665

deutschen Lieferkettensorgfaltsgesetzes im EU-Binnenmarkt europaweit durchsetzen, 666

aber nicht verschärfen. So verhindern wir unterschiedliche und damit unpraktikable Re-667

gelwerke und schaffen faire Wettbewerbsbedingungen.

668

• Bei der A1-Bescheinigung für die Entsendung von Arbeitnehmern ins EU-Ausland setzen 669

wir uns für eine praxistaugliche Lösung ein, die vor Missbrauch schützt und gleichzeitig 670

unbürokratisch und möglichst digital handhabbar ist.

671

• Wir bekennen uns zur Unabhängigkeit der Europäischen Zentralbank (EZB). Geld- und 672

Finanzpolitik müssen getrennt bleiben. Wir lehnen deshalb eine monetäre Staatsfinan-673

zierung ab. Das übergeordnete Ziel der EZB bleibt die Wahrung der Geldwert- und Fi-674

nanzstabilität.

675

• Unsere Währung muss für das digitale Zeitalter gut gerüstet sein. Wir befürworten einen 676

digitalen Euro als schnelles, einfaches und sicheres Zahlungsmittel. Er darf Bargeld nur 677

ergänzen und die Preis- und Finanzstabilität nicht gefährden. Denn Bargeld ist gelebte 678

Freiheit. Daher halten wir am Bargeld als Zahlungsmittel weiterhin fest.

679

 

Seite 22 von 139

680

Europäische Finanzarchitektur krisensicher machen

681

Europa muss auf Wirtschafts- oder Finanzkrisen besser vorbereitet sein, damit diese schnel-682

ler und besser überwunden werden können. Dafür braucht es mehr Stabilität in ganz Eu-683

ropa.

684

• Wir wollen den Europäischen Stabilitätsmechanismus (ESM), die Bankenunion und die 685

Kapitalmarktunion unter Stabilitätsaspekten weiterentwickeln und vollenden.

686

• Für den Umgang mit Staaten, die von einer Wirtschafts- und/oder Finanzkrise betroffen 687

sind, benötigen wir geordnete Verfahren bis hin zu einem Insolvenzverfahren für Staa-688

ten.

689

• Zur Vollendung der Bankenunion müssen bestehende Risiken im Bankensystem zwin-690

gend reduziert werden. Bankenrettungen aus Steuermitteln und eine Vergemeinschaf-691

tung der Haftungsübernahme im Rahmen der europäischen Einlagensicherung lehnen 692

wir ab.

693

• Bei allen Änderungen auf europäischer Ebene müssen die Besonderheiten unseres be-694

währten Drei-Säulen-Systems aus Privatbanken, öffentlich-rechtlichen Banken und Ge-695

nossenschaftsbanken erhalten bleiben. Insbesondere dürfen die Kreditversorgung des 696

Mittelstands und die Finanzierung von Wohneigentum nicht aufgrund überzogener re-697

gulatorischer Anforderungen unnötig eingeschränkt werden. So sorgen wir dafür, dass 698

Krisen schnell und besser überwunden werden können.

699

 

700

Fairen Welthandel stärken

701

In Deutschland hängt jeder vierte Arbeitsplatz vom Export ab, in der deutschen Industrie 702

sogar mehr als jeder Zweite. Wir setzen auf einen freien Welthandel mit fairen internatio-703

nalen Wettbewerbsbedingungen statt auf Protektionismus und Abschottung.

704

• Wir wollen gemeinsam mit unseren Partnern den Multilateralismus durch eine Reform 705

der Welthandelsorganisation stärken und den Abschluss von Freihandelsabkommen 706

durch die Europäische Union vorantreiben. Insgesamt brauchen wir eine Verzahnung 707

von Handelsschutzmaßnahmen mit wettbewerbsrechtlichen Instrumenten.

708

• Wir wollen, dass europäische Handelspolitik konsequent auf Verbesserungen beim 709

Marktzugang für Güter und Dienstleistungen hinarbeitet, um Hemmnisse für europäi-710

sche Unternehmen auf Drittmärkten abzubauen. Dabei müssen Marktöffnungen gegen-711

seitig im gleichen Maß gewährt und Markenpiraterie eingedämmt werden.

712

• Wir wollen Anreize schaffen, dass unsere hohen Standards, zum Beispiel beim Umwelt-, 713

Verbraucher- und Arbeitnehmerschutz, international zum Standard werden. Denn unser 714

Ziel ist multilateraler, fairer und regelbasierter Handel, der Wohlstandsperspektiven für 715

alle eröffnet, den Kampf gegen den Klimawandel verstärkt, Kinderarbeit ächtet und auf 716

eine Verbesserung der Arbeitsbedingungen in anderen Ländern hinwirkt.

717

• Wir wollen Sanktionsmechanismen bei Verstößen gegen Nachhaltigkeits- und Klima-718

schutzaspekte etablieren und weiter stärken.

Seite 23 von 139

719

• Wir wollen besonders mit unseren transatlantischen Partnern in der Handelspolitik welt-720

weit unsere gemeinsamen Grundwerte und gemeinsame Standards etablieren.

721

• Wir machen uns für die überfällige Ratifizierung des Wirtschaftsabkommens der Europä-722

ischen Union mit Kanada (CETA) stark. Wir plädieren auch für die vollständige Umset-723

zung des Handelsabkommens der EU mit dem Mercosur-Raum, sofern sichergestellt 724

werden kann, dass gerade in der Landwirtschaft Produktions- und Produktstandards un-725

seren Maßstäben entsprechen.

726

• Wir streben einen raschen Neustart der Verhandlungen zwischen der EU und den USA 727

an: Wir wollen ein transatlantisches Handels-, Wirtschafts- und Investitionsabkommen 728

mit den USA, das auch ökologisch weltweit Maßstäbe setzt.

729

 

730

Für eine moderne europäische Industriepolitik eintreten

731

Die Stärkung der Wettbewerbsfähigkeit der europäischen Industrie ist angesichts der Ver-732

schärfung der globalen Rahmenbedingungen und der Rolle Chinas wichtiger denn je. Unser 733

Ziel ist es, dass Europa in den wichtigen industriellen Zukunftsfeldern wie Künstlicher In-734

telligenz, Quantentechnologie, Halbleiter, Wasserstoff oder Blockchain weltweit einen 735

Spitzenplatz einnimmt.

736

• Wir brauchen dafür eine ambitionierte europäische Technologie- und Industriestrategie.

737

Wir wollen in Europa die Fähigkeiten weiter fördern, Schlüsseltechnologien zu entwi-738

ckeln und herzustellen. Strategische Förderprojekte der EU müssen die vorhandenen 739

Stärken an europäischen Standorten, etwa der Mikroelektronik oder der Luft- und Raum-740

fahrt, im Sinne der globalen Wettbewerbsfähigkeit weiter ausbauen.

741

• Wir wollen das europäische Wettbewerbs- und Beihilferecht anpassen, um Verzerrungen 742

beim Handel und im Wettbewerb infolge von Staatssubventionen und Interventionen in 743

anderen Teilen der Welt auszugleichen. Hierfür muss die Europäische Union die Ver-744

handlungen mit anderen großen Industriestaaten vorantreiben.

745

• Wir müssen Wertschöpfungsketten innerhalb von Europa schließen und uns so unabhän-746

giger von anderen Teilen der Welt machen. Wir brauchen neue Souveränität für Europa 747

in allen systemrelevanten Wirtschaftsbereichen.

748

• Wir wollen das EU-Vergaberecht im Sinne des Bürokratieabbaus modernisieren.

749

 

750

2.5. Unser Europa der Ordnung und Sicherheit

751

Europas Grenzen schützen

752

Was wir in Europa brauchen, ist eine Sicherheitsunion. Mehr Sicherheit in und durch Europa 753

bedeutet auch mehr Sicherheit für Deutschland. Offene Grenzen in Europa sind ein Gewinn 754

für uns alle. Doch auch bei offenen Binnengrenzen und Reisefreiheit im Schengen-Raum 755

muss die innere Sicherheit in der Europäischen Union gewährleistet bleiben. Dafür müssen 756

die europäischen Außengrenzen wirksam geschützt werden. Nur gemeinsam als Europäi-Seite 24 von 139

757

sche Union können wir Drogenschmuggler, Menschenhändler, international agierende Ban-758

den, Gefährder und Terroristen wirksam bekämpfen. Um Europa als Raum der Freiheit, der 759

Sicherheit und des Rechts garantieren zu können, bedarf es auch einer effektiven Polizeiar-760

beit innerhalb der Grenzen Europas.

761

• Wir wollen die Europäische Grenzschutzagentur FRONTEX zu einer echten Grenzpolizei 762

und Küstenwache mit hoheitlichen Befugnissen ausbauen. Ihre personellen Kapazitäten 763

werden wir deutlich aufstocken.

764

• Wir wollen die relevanten, für die Grenzpolizei zugänglichen Datenbanken wie das 765

Schengen-Informationssystem und EURODAC so gestalten, dass alle Informationen ab-766

rufbar zur Verfügung stehen.

767

• Wir wollen, dass die Einreise an den Außengrenzen umfassend elektronisch überwacht 768

wird. Die bereits beschlossene Einrichtung des Ein- und Ausreiseregisters für Drittstaats-769

angehörige EES werden wir daher ebenso vorantreiben wie das Reiseinformations- und 770

Genehmigungssystem ETIAS.

771

• Angesichts der weiterhin akuten terroristischen Bedrohungen wollen wir die enge Zu-772

sammenarbeit der Polizeien und Nachrichtendienste weiter intensivieren.

773

• Wir wollen, dass die in unterschiedlichen Informationssystemen vorhandenen Daten so 774

verknüpft werden können, dass die Polizei- und Sicherheitsbehörden auf die von ihnen 775

benötigten Informationen schnell zugreifen können – zur Prävention von Anschlägen 776

ebenso wie zur Strafverfolgung nach terroristischen Taten.

777

• Wir wollen auch, dass die relevanten Daten zwischen den Polizei- und Sicherheitsbehör-778

den so umfassend ausgetauscht werden können, dass schnelle polizeiliche Reaktionen 779

möglich sind.

780

• Wir brauchen ein europaweites Tracking von Gefährdern, eine gemeinsame Gefährder-781

bewertung und nationale Gefährderlisten, die europaweit automatisch zusammenge-782

führt werden, ohne dass eine konkrete Abfrage des jeweiligen Täters erfolgen muss.

783

• Wir wollen EUROPOL als europäische Verbindungs- und Koordinierungsstelle so aus-784

statten und weiterentwickeln, dass es in wichtigen Bereichen zu einer Art europäischem 785

FBI wird. Das gilt insbesondere im Bereich der Cyberkriminalität und im Kampf gegen 786

Terrorismus. Die operativen polizeilichen Befugnisse verbleiben bei den Mitgliedstaa-787

ten.

788

 

789

Menschen in Not helfen, Migration wirksam ordnen und steuern

790

Die Europäische Union und Deutschland helfen Menschen, die in große Not kommen, weil 791

sie politisch verfolgt werden oder aufgrund der Genfer Flüchtlingskonvention. Wir beken-792

nen uns zum Grundrecht auf Asyl und den rechtlichen und humanitären Verpflichtungen 793

Deutschlands und Europas. Gezielte Zuwanderung ist dann ein Gewinn und eine Chance für 794

unser Land, wenn sie von gelungener Integration begleitet ist – in unseren Arbeitsmarkt 795

ebenso wie in unsere Gesellschaft. Das erwarten wir von Zuwanderern und darin wollen wir Seite 25 von 139

796

sie unterstützen. Wie erfolgreiche Einwanderungsgeschichten aussehen, zeigen die BioN-797

Tech-Gründer auf eindrucksvolle Weise. Sie sind nur eines von vielen Beispielen, die zeigen, 798

wie wir von den klügsten Köpfen aus aller Welt profitieren können. Das gilt auch für die 799

gesteuerte und gezielte Zuwanderung in den Arbeitsmarkt. Migration ist aber nur dann eine 800

Chance, wenn sie geordnet erfolgt und sich an klaren Regeln orientiert. Das gilt für die Ein-801

wanderung von Fachkräften ebenso wie für die Aufnahme von Schutzsuchenden und Ge-802

flüchteten. Eine Zuwanderung in die Sozialsysteme lehnen wir ab.

803

Unsere Politik steht daher im Zeichen einer wirksamen Ordnung und Steuerung von Mig-804

ration. Das bedeutet: Wir wollen keine illegale Migration und Ausreisepflichten durchset-805

zen. Dies ist die Voraussetzung dafür, dass wir notleidenden Menschen dauerhaft helfen 806

können. Wir vereinen Weltoffenheit und Konsequenz, Humanität und Ordnung.

807

• Wir haben Asylverfahren und Rückführungen gerechter, strukturierter und effizienter 808

gestaltet. Wir setzen unsere Anstrengungen fort, damit die Zahl der nach Deutschland 809

und Europa flüchtenden Menschen nicht nur dauerhaft niedrig bleibt, sondern sich wei-810

ter reduziert. Hierfür ist klar zwischen Menschen in Not und denen zu unterscheiden, die 811

unser Land wieder verlassen müssen, weil sie nicht schutzbedürftig sind.

812

• Wir wollen weitere sichere Herkunftsstaaten festlegen. Mit der Einstufung als sicherer 813

Herkunftsstaat können Bürgerinnen und Bürger aus einem solchen Staat, die in Deutsch-814

land Asyl beantragen, leichter und schneller in ihre Heimat zurückgeführt werden. An-815

reize würden abgebaut, damit sich diese Menschen ohne Aussicht auf Asyl nicht auf den 816

Weg nach Deutschland machen. Gleichwohl scheiterte die Einstufung weiterer Staaten 817

mit verschwindend geringen Anerkennungsquoten bei Asylanträgen im Bundesrat am 818

Widerstand einiger Länder, obgleich der Bundestag eine Ausweitung bereits beschlossen 819

hatte. Deshalb wollen wir die Möglichkeiten des europäischen Asylrechts nutzen, um ein 820

neues Konzept der sicheren Herkunftsstaaten, den „kleinen“ sicheren Herkunftsstaat, zu 821

schaffen. In einem gewöhnlichen Gesetzgebungsverfahren zur Einstufung eines Staates 822

wird der Staat sowohl im Sinne des Grundgesetzes als auch im Sinne der europäischen 823

Asylverfahrensrichtlinie als sicherer Herkunftsstaat eingestuft. Eine Einstufung als „klei-824

ner“ sicherer Herkunftsstaat im Sinne der Asylverfahrensrichtlinie wäre hingegen ohne 825

Zustimmung des Bundesrats und damit ohne Mitwirkung der Länder möglich. Davon un-826

berührt bleibt die im Grundgesetz garantierte Prüfung auf Asyl nach Art. 16 a.

827

• Wir lehnen eine Ausweitung des Familiennachzugs über die heute bestehenden Rege-828

lungen hinaus ab.

829

• Bleiberechtsmöglichkeiten Ausreisepflichtiger wollen wir stärker einschränken, um die 830

Anreize für illegale Zuwanderung weiter zu senken; insbesondere sollen Aufenthaltser-831

laubnisse bei Geduldeten an echte Integrationsvoraussetzungen geknüpft werden.

832

• Wir wollen Ausreisepflichten besser durchsetzen und dafür unter anderem Gewahrsam-833

seinrichtungen an den Verkehrsflughäfen schaffen, um Sammelabschiebungen zu er-834

leichtern. Auf Verstöße gegen eine Wiedereinreisesperre folgt unmittelbar die Abschie-835

behaft.

Seite 26 von 139

836

• Wir wollen Straftäter konsequent abschieben. Wer in Deutschland straffällig wird, hat 837

sein Gastrecht verwirkt.

838

• Den Druck auf Identitätstäuscher und Mitwirkungsverweigerer werden wir noch einmal 839

deutlich erhöhen. Dazu werden wir die rechtlichen Möglichkeiten ausbauen und verfüg-840

bare technische Mittel nutzen.

841

• Falschangaben im Asylverfahren müssen künftig auch strafbar sein, wenn sie gegenüber 842

dem Bundesamt für Migration und Flüchtlinge erfolgen.

843

• Zudem müssen Datenträger und insbesondere Mobiltelefone auch zur Klärung von Si-844

cherheitsbedenken ausgelesen werden dürfen. Wer den Staat über seine Identität 845

täuscht und seine Abschiebung verhindert, kann keinen Anspruch auf eine Duldung er-846

halten.

847

• Auch werden wir die Regelungen des Ausreisegewahrsams und der Abschiebungshaft 848

praxistauglicher ausgestalten.

849

 

850

Europäische Asyl- und Flüchtlingspolitik grundlegend reformieren

851

Die Versorgung von Schutzsuchenden ist weder eine alleinige Herausforderung Deutsch-852

lands noch der Staaten an den EU-Außengrenzen. Sie ist eine gemeinsame europäische Her-853

ausforderung. Vorrangiges Ziel muss es sein, Menschen in ihrer Heimat oder in deren Nähe 854

Lebensperspektiven zu eröffnen.

855

• Die Europäische Union muss mit den Hauptherkunftsländern die Zusammenarbeit wei-856

ter intensivieren und Fluchtursachen – wie etwa Armut – bekämpfen. Dazu ist insbeson-857

dere eine umfassende Partnerschaft mit unserem Nachbarkontinent Afrika und eine ak-858

tive Stabilisierungspolitik im Nahen und Mittleren Osten notwendig.

859

• Das Gemeinsame Europäische Asylsystem muss grundlegend reformiert werden. Der 860

Vorschlag der Europäischen Kommission einer fairen und solidarischen Verteilung der 861

Kosten und Lasten innerhalb der Mitgliedstaaten der Europäischen Union geht in die 862

richtige Richtung.

863

• Wir sprechen uns für die Einrichtung von europäisch verwalteten Entscheidungszentren 864

an den EU-Außengrenzen aus, in denen geprüft werden soll, ob ein Asylanspruch vorliegt 865

oder nicht. Perspektivisch kann sich daraus eine europäische Behörde entwickeln, die 866

auch die Mitgliedstaaten unterstützt und Koordinationsaufgaben übernimmt.

867

• Wir brauchen gemeinsame Standards im europäischen Asylrecht und eine europaweite 868

Harmonisierung der Aufnahmebedingungen – hinsichtlich Verfahren, Unterbringung 869

und Versorgung. Dies senkt die Anreize, die manche Mitgliedstaaten für Asylsuchende 870

attraktiver machen als andere.

871

 

 

Seite 27 von 139

872

In Europa das schützen, was uns wichtig ist

873

Im Rahmen der „Europäischen Säule sozialer Rechte“ sollen die Mitgliedstaaten dabei un-874

terstützt werden, insbesondere global agierende Konzerne stärker in die soziale Verantwor-875

tung zu nehmen und Strukturen von Sozialpartnerschaften zu schaffen und auszubauen.

876

Denn gerechte Löhne entstehen nur durch Tarifverträge, die von den Sozialpartnern der 877

Mitgliedstaaten ausgehandelt werden.

878

• Wir stehen dafür, dass sich die EU auf Grundstandards bei Arbeitnehmerrechten sowie 879

Gesundheits-, Umwelt- und Verbraucherschutzstandards konzentriert. Eine europäische 880

Arbeitslosen-, Renten- oder Gesundheitsversicherung lehnen wir ab. Die sozialen Siche-881

rungssysteme sind in der Zuständigkeit der Mitgliedstaaten.

882

• Wir wollen die Anerkennung von Berufsqualifikationen vereinfachen und die Portabilität 883

von betrieblicher Altersvorsorge zwischen EU-Mitgliedstaaten verbessern, um die Ar-884

beitnehmermobilität weiter zu fördern.

885

 

886

2.6. Für ein modernes, innovatives und digitales Europa 887

Europa digital an die Spitze führen

888

Auch für Europa brauchen wir ein Modernisierungsjahrzehnt. Denn nur, wenn wir vereint in 889

nachhaltige europäische Zukunftsprojekte und -technologien investieren, sichern wir Wett-890

bewerbsfähigkeit und Arbeitsplätze von morgen hier bei uns in Europa.

891

• Wir wollen eine echte Digital- und Datenunion mit einem modernen Wettbewerbsrecht 892

auf Basis der Sozialen Marktwirtschaft, hochklassiger digitaler Infrastruktur, europäi-893

scher Speicher- und Rechenkapazitäten und eines einheitlichen Datenschutzrechts.

894

• Wir wollen als weltweiter Vorreiter für einen fairen und gerechten Wettbewerb in der 895

Digitalwirtschaft eine europäische digitale Marktordnung entwickeln und einführen – 896

mit einem modernisierten Wettbewerbsrecht und gleichen Regeln für alle. Zu einer 897

Marktordnung gehört auch eine faire und angemessene „Standgebühr “.

898

• Wir wollen, dass digitale Ökosysteme, in denen Politik, Wissenschaft, Forschung und 899

Wirtschaft für die Entwicklung und Finanzierung neuer digitaler Produkte zusammenar-900

beiten, auch in Europa etabliert werden. Wir setzen uns für einen deutlichen Ausbau der 901

Rahmenbedingungen für solche gemeinsamen Initiativen auf europäischer Ebene ein, 902

zum Beispiel bei Künstlicher Intelligenz oder Quantencomputern.

903

 

904

Innovationskraft Europas bündeln

905

Wir wollen das Ziel der Lissabon-Strategie mit Leben füllen: Europa soll zum innovativsten 906

Wirtschaftsraum der Welt werden. Europa und der gemeinsame Binnenmarkt tragen ganz 907

wesentlich zu unserem Wohlstand bei. Sie bilden das Rückgrat unserer global handelnden 908

Wirtschaft und vieler gut bezahlter Arbeitsplätze in Deutschland.

Seite 28 von 139

909

• Wir wollen den Binnenmarkt in allen Bereichen mit besonderem Blick auf Digitales, Ener-910

gie und Kapital weiter stärken und vertiefen. Zudem muss sich auch auf europäischer 911

Ebene eine strategische Außenwirtschaftspolitik etablieren.

912

• Wir brauchen Strukturreformen für mehr Wettbewerbsfähigkeit und private Investitio-913

nen, die Wachstum, Beschäftigung und Innovation schaffen.

914

• Wir wollen die anwendungsnahe Forschung und globale Wasserstoffstrategien aus-915

bauen, eine europäische Plattformwirtschaft etablieren und europäische Industriestan-916

dards weltweit durchsetzen.

917

• In der Personalisierten Medizin wollen wir auf den Forschungserfolgen der Corona-Impf-918

forschung aufbauend alle Ressourcen im Kampf gegen Krebs und Alzheimer bündeln und 919

eine europäische Gesundheitsunion gründen. Sie soll europäische Spitzenforschung 920

bündeln und intensivieren.

921

• Künstliche Intelligenz wollen wir für den Alltag nutzen: Menschen sollen innerhalb Euro-922

pas ohne Sprachbarrieren miteinander kommunizieren und gleichzeitig die Vielfalt ge-923

nießen können. Wir wollen die Forschung und Entwicklung der automatisierten Sprach-924

erkennung und -übersetzung in den kommenden Jahren zum Durchbruch verhelfen und 925

gleichzeitig ein Leitprojekt für die künstliche Intelligenz auf den Weg bringen.

926

 

927

Europäische Forschung und Bildung stärken

928

Forschung und Bildung der jüngeren Generationen werden europaweit über unseren zu-929

künftigen Wohlstand entscheidend sein. Die Hochschulen sind ein wichtiges Bindeglied 930

zwischen dem Europäischen Bildungs- und dem Europäischen Forschungsraum.

931

• Auf europäischer Ebene wollen wir einen einheitlichen, gemeinsamen Rechtsrahmen für 932

bestehende sowie zukünftige Europäische Hochschulen schaffen. Dadurch können die 933

Anerkennung der Abschlüsse und der Wissenschaftsaustausch deutlich verbessert wer-934

den.

935

• Wir wollen das Rahmenprogramm für „Horizont Europa“ zusammen mit dem öffentli-936

chen und privaten Sektor so umsetzen, dass die weltweit besten und innovativsten For-937

schenden ihre Projekte in Europa verwirklichen können. „Horizont Europa“ ist das größte 938

und ambitionierteste Forschungsprogramm der europäischen Geschichte. Damit wur-939

den die besten Voraussetzungen geschaffen, um exzellente Grundlagenforschung des 940

Europäischen Forschungsrats zu unterstützen, europaweite Karrierepfade weiter zu öff-941

nen und Forschungseinrichtungen europaweit besser zu vernetzen.

942

 

943

Schnelle und emissionsarme Mobilität voranbringen

944

Von zentraler Bedeutung für die wirtschaftliche Entwicklung in unserem Land und die Stär-945

kung Europas ist eine leistungsfähige Infrastruktur: Straßen, Zugverbindungen, aber bei-946

spielsweise auch leistungsfähige Stromtrassen sind die Grundlage für die Begegnung von 947

Menschen, den Austausch von Gütern und die Vernetzung unserer Länder. Deutschland Seite 29 von 139

948

und Europa brauchen eine entschlossene und kraftvolle Antwort auf globale Herausforde-949

rungen wie die Initiative Chinas zur Entwicklung einer neuen Seidenstraße.

950

• Deshalb wollen wir dieses Jahrzehnt nutzen, um mit unseren mittel- und osteuropäi-951

schen Nachbarn eine so enge infrastrukturelle Vernetzung zu erreichen, wie wir sie zum 952

Beispiel zwischen Deutschland, Frankreich und den Beneluxstaaten in den letzten Jahr-953

zehnten zum Wohle unserer Länder und ganz Europas entwickelt haben. Dazu werden 954

wir uns mit europäischer Unterstützung für ein Programm „grenzüberschreitende Ver-955

netzung und Infrastrukturausbau“ einsetzen, das verkehrs- und klimapolitisch neue Ak-956

zente setzt und auch die militärische Mobilität verbessert.

957

• Europa hat die Chance, der erste Kontinent CO2-neutraler Mobilität zu werden. Wir wol-958

len ihr zum Durchbruch verhelfen und damit weltweites Vorbild sein. Dafür wollen wir 959

den Wettbewerb der besten Ideen technologieoffen befördern.

960

• Wir setzen uns für einen besseren europäischen Hochgeschwindigkeitsschienenverkehr 961

als bequemen, sicheren, flexiblen und ökologisch nachhaltigen Verkehrsträger ein.

962

Schnelle, aufeinander abgestimmte Verbindungen nach Warschau und Prag sollen zu-963

künftig genauso selbstverständlich sein wie die stark genutzte Verbindung zwischen Pa-964

ris und den deutschen Metropolen. Hier kommt auch Nachtzügen eine besondere Be-965

deutung zu.

966

 

967

2.7. Ein handlungsfähiges und bürgernahes Europa

968

Europa institutionell fortentwickeln

969

Um den Herausforderungen der Zeit gewachsen zu sein, muss Europa das richtige Rüstzeug 970

zur Hand bekommen. Nur mit besser funktionierenden Institutionen und Abläufen kann 971

Europa die Zukunft gestalten.

972

• Wir wollen unser Europa gemeinsam mit den Bürgerinnen und Bürgern für die Heraus-973

forderungen der Zukunft stärken. Deshalb ist die Konferenz zur Zukunft Europas für uns 974

ein Aufbruch zu grundlegenden Reformen der EU. Wir wollen sie für eine europäische 975

Souveränitätsoffensive nutzen. Vertragsänderungen sind dabei kein Ziel an sich, aber ein 976

mögliches Instrument, um Europa handlungsfähiger zu machen.

977

• Wir wollen mehr Mehrheitsentscheidungen in Europa unter verstärkter Nutzung der 978

Brückenklauseln für schnellere Entscheidungen und entschlossenes Handeln. Wo keine 979

gemeinsame Lösung möglich ist, sollen Mitgliedstaaten die Möglichkeit öfter nutzen, im 980

Rahmen der Verträge voranzugehen und enger zusammenzuarbeiten.

981

• Wir wollen Europa stark und verantwortlich machen, wo Europa gemeinsam mehr errei-982

chen kann. Europäische Gesetzgebung ist gut, wenn grenzüberschreitender oder ge-983

samteuropäischer Mehrwert entsteht.

984

• In manchen Bereichen sind wir noch nicht so weit: So hat die Pandemiebekämpfung das 985

Fehlen von gemeinsam abgestimmten Maßnahmen auf europäischer Ebene aufgezeigt.

Seite 30 von 139

986

Gleichzeitig muss das, was in den Kommunen, Regionen und Mitgliedstaaten besser ge-987

leistet werden kann, auch dort verantwortet werden. Subsidiarität ist unser Leitgedanke 988

für Europa.

989

• Wir wollen gemeinsam mit unseren Europäischen Partnern die Pandemievorsorge und -

990

bereitschaft in der Europäischen Union weiter verbessern. Deshalb setzen wir uns dafür 991

ein, die Arbeiten an der Gesundheitsunion zügig abzuschließen. Durch die nachhaltige 992

Stärkung des Europäischen Zentrums für die Prävention und Kontrolle von Krankheiten 993

sowie der Europäischen Arzneimittelagentur, in guter Zusammenarbeit mit unseren na-994

tionalen Strukturen, wollen wir einen klaren EU-Mehrwert schaffen. Ein wesentlicher 995

Baustein wird die Sicherstellung der Versorgung mit Impfstoffen und krisenrelevanten 996

Arzneimitteln und Medizinprodukten sein. Daher werden wir den geplanten Aufbau ei-997

ner Europäischen Gesundheitskrisenagentur (HERA) konstruktiv begleiten und uns mit 998

unseren Partnern dafür einsetzen, die Abhängigkeit der EU von Drittstaaten zu reduzie-999

ren.

1000

 

1001

Europäische Demokratie stärken

1002

Die Achtung von Demokratie und Rechtsstaatlichkeit sowie die Werte der liberalen Demo-1003

kratie gehören zu den Grundfesten der Europäischen Union. Hierzu gehört auch die Trans-1004

parenz der europäischen Gesetzgebung für die Bürgerinnen und Bürger, die demokrati-1005

scher und insgesamt bürgernäher werden muss.

1006

• Wir setzen uns für neue Dialogformate zur Rechtsstaatlichkeit und zur konsequenten 1007

Ahndung von Verstößen ein – bis hin zur Streichung von EU-Mitteln und dem Entzug des 1008

Stimmrechts.

1009

• Wie die nationalen Parlamente muss auch das Europäische Parlament das Recht haben, 1010

eigene Gesetzentwürfe einzubringen. So werden wir das Herzstück der europäischen 1011

Demokratie, das gemeinsam gewählte Europäische Parlament, weiter stärken.

1012

• Wir setzen uns für die Einführung eines europäischen Wahlrechts mit einer Sperrklausel 1013

zur nächsten Europawahl ein. Für ein arbeitsfähiges Parlament darf es keine Zersplitte-1014

rung des Parlaments durch Kleinstparteien geben.

1015

• Um Exekutive und Parlament enger zu verbinden, drängen wir auf eine Stärkung des 1016

Spitzenkandidatenprinzips bei der Besetzung der Kommissionsspitze.

1017

• Wir setzen uns darüber hinaus für eine Verkleinerung der Europäischen Kommission ein.

1018

Europäische Handlungsfähigkeit muss das entscheidende Leitprinzip sein.

1019

• Wir werden die europapolitische Koordinierung der Bundesregierung weiter ausbauen, 1020

vereinfachen und stärken. Denn Deutschlands Stärke ist fest mit Europas Handlungsfä-1021

higkeit verbunden. Deshalb wollen wir damit die Positionen Deutschlands zum Wohle 1022

Europas klar formulieren und wirksam vertreten.

1023

• Für eine bessere Rechtssetzung und den Abbau von Bürokratiekosten weiten wir die Fol-1024

genabschätzung auf europäischer Ebene aus.

Seite 31 von 139

1025

 

1026

Europa für die Jugend erlebbar machen

1027

Wir setzen uns dafür ein, dass die Jugend Europas die Vorteile der Europäischen Union un-1028

mittelbar erleben kann.

1029

• Austauschprogramme wollen wir ausbauen.

1030

• Das Interrail-Ticket im Rahmen des „DiscoverEU“-Programms soll es künftig für jeden 1031

18-Jährigen kostenlos geben.

1032

• Wir wollen den Mitteleinsatz für ErasmusPlus verdoppeln. Denn der europäische Bil-1033

dungsraum und der Aktionsplan für digitale Bildung sind für die wirtschaftliche Erholung 1034

Europas und für künftiges Wachstum von entscheidender Bedeutung. Das Programm 1035

ErasmusPlus leistet hierzu einen wichtigen Beitrag.

1036

• Damit Europa im Großen und im Kleinen erlebbarer wird, fördern wir die grenzüber-1037

schreitende Zusammenarbeit. So können mehr persönliche Begegnungen ermöglicht 1038

werden – in Schule, Ausbildung, Studium und Beruf.

1039

• Zur Stärkung der europäischen Öffentlichkeit wollen wir zudem die Rechtsform eines 1040

europäischen Vereins einführen, um die grenzüberschreitende Zusammenarbeit in Zivil-1041

gesellschaft, Kultur und Sport voranzutreiben.

1042

 

 

Seite 32 von 139

1043

3. Neuer Wohlstand – mit nachhaltigem Wachstum zum klimaneutralen 1044

Industrieland

1045

 

1046

Unser Unions-Versprechen: Wir werden unsere Wirtschaft wieder in Schwung bringen und für 1047

sichere und zukunftsfähige Arbeitsplätze sorgen. Dabei verbinden wir nachhaltiges Wachstum, 1048

Klimaschutz und soziale Sicherheit miteinander. Wir wollen Interessen zusammenführen und 1049

nicht gegeneinander ausspielen. Mehr denn je wird dieser Grundsatz unsere Politik, unser Han-1050

deln und Entscheiden leiten.

1051

Die Corona-Pandemie hat auch in Deutschland zu einem massiven Wirtschaftseinbruch geführt.

1052

Wir konnten die Wirtschaft stabilisieren und Arbeitsplätze sichern, weil wir in einer großen ge-1053

meinsamen Kraftanstrengung schnell und entschlossen gehandelt haben. Gleichzeitig hat die 1054

Pandemie gezeigt, dass unser Land in einigen Bereichen nicht schnell, nicht agil und nicht mutig 1055

genug ist. Zu oft stellen wir den Fleißigen, den Tüchtigen und den Mutigen – im Handwerk, im 1056

Mittelstand und in den freien Berufen sowie in der Kultur- und Kreativszene – unnötige Hürden 1057

in den Weg, anstatt ihnen den Weg frei zu machen und ihrem Können und ihren Ideen zu ver-1058

trauen. Der Weg vom Problem zur Lösung führt zu oft und zu lange durch ein Dickicht voller 1059

Vorschriften und Bedenken.

1060

Es reicht nicht aus, nur an ein paar Stellschrauben zu drehen. Wir brauchen ein Modernisie-1061

rungsjahrzehnt in Deutschland. Wir müssen die Weichen neu stellen. Dabei werden wir noch 1062

stärker auf die Prinzipien der Sozialen Marktwirtschaft setzen. Sie verbindet Freiheit mit Sicher-1063

heit, Eigenverantwortung mit Gemeinwohl, wirtschaftliche Dynamik mit sozialem Ausgleich.

1064

Sie setzt auf Machen statt Meckern, auf Offenheit statt Abschottung, auf Erwirtschaften statt 1065

Verteilen, auf Ideen statt Verbote.

1066

Auf diese Prinzipien setzen wir auch im Kampf gegen den Klimawandel. Wir wollen jetzt, in die-1067

sem Jahrzehnt, die entscheidenden Schritte gehen, damit Deutschland bis 2045 ein klimaneut-1068

rales Industrieland wird. Unser christliches Menschenbild verpflichtet uns zur Bewahrung der 1069

Schöpfung und zum verantwortlichen Handeln gegenüber unseren Mitmenschen, gegenüber der 1070

Umwelt und gegenüber den zukünftigen Generationen. Wir wollen weiter Industrieland bleiben 1071

und hochqualifizierte industrielle Arbeitsplätze erhalten – gemeinsam mit der Wirtschaft und 1072

den Sozialpartnern und ohne Überforderung der Verbraucherinnen und Verbraucher.

1073

 

1074

Soziale Marktwirtschaft als Erfolgsmodell fortschreiben

1075

Die Soziale Marktwirtschaft ist die Wirtschaftsordnung unserer freiheitlichen Demokratie.

1076

Sie ist Fundament unseres Erfolgs als innovative, leistungsfähige und nachhaltige Volks-1077

wirtschaft. Sie verbindet Chancen für den Einzelnen mit sozialer Sicherheit in unserer Ge-1078

sellschaft. Sie ist die Ordnung, die wie keine andere Ökonomie, Ökologie und Soziales in 1079

Einklang bringt. Auf ihrer Grundlage haben Generationen von Frauen und Männern mit Bil-1080

dung, Fleiß und Leistung, Verantwortungsbereitschaft und Engagement Deutschland zu ei-1081

ner der wohlhabendsten Nationen der Welt gemacht; zu einem weltweit bewunderten öko-1082

nomischen und ökologischen Vorbild; zur Heimat hunderttausender Unternehmen, die mit 1083

ihrer Wettbewerbsfähigkeit und Innovationskraft zum gesellschaftlichen Wohlstand und Seite 33 von 139

1084

zur sozialen Sicherheit beitragen. Diese Erfolgsgeschichte wollen wir fortschreiben und die 1085

Leitplanken der Sozialen Marktwirtschaft erneuern.

1086

• Auch in Zukunft werden wir Wirtschaftskompetenz mit praktizierter Solidarität und ef-1087

fizientem Schutz der Umwelt und des Klimas verbinden.

1088

• Die nachhaltige, soziale, ökologische und digitale Marktwirtschaft ist unsere Soziale 1089

Marktwirtschaft des 21. Jahrhunderts.

1090

• Wir setzen auf Vertrauen in die Menschen, auf Freiheit statt Bevormundung, auf Frei-1091

räume statt Gängelung.

1092

• Wir setzen auf funktionierenden Wettbewerb, der Menschen die Chance gibt, das Beste 1093

aus ihren Fähigkeiten zu machen.

1094

• Gerade auch im Zeitalter der Globalisierung und Digitalisierung setzen wir auf die Ord-1095

nung des Marktes durch den Staat. Ein starker Staat ordnet die Wirtschaft und bestimmt 1096

die Regeln, nimmt aber selbst nicht am Geschehen teil.

1097

 

1098

3.1. Unser Entfesselungspaket für die Wirtschaft

1099

Ganz gleich, ob Selbstständige und kleine, mittlere oder große Unternehmen: In unserem 1100

Modernisierungsjahrzehnt müssen wir es schaffen, dass sie sich mehr auf ihr Kerngeschäft 1101

konzentrieren und neue Ideen umsetzen können. Ein modernes Deutschland ist auch eines, 1102

das Erfinderreichtum und Unternehmertum mehr Freiräume lässt.

1103

Wir werden daher ein umfangreiches Entfesselungspaket auf den Weg bringen, das Unter-1104

nehmen von Steuern und Bürokratie entlastet sowie Planungs- und Genehmigungsverfah-1105

ren beschleunigt. Unser Ziel: Die Macherinnen und Macher sollen ihre Tatkraft zuallererst 1106

dafür einsetzen, erfolgreich zu wirtschaften und nicht für die Erfüllung bürokratischer 1107

Pflichten. Denn das bringt unser Land voran.

1108

 

1109

Neue Belastungen verhindern

1110

Für uns ist klar: Damit die Wirtschaft wieder in Schwung kommt und wir gemeinsam neuen 1111

Wohlstand schaffen können, dürfen Unternehmen keine neuen Belastungen auferlegt wer-1112

den.

1113

• Wir wollen die Lohnzusatzkosten auf einem stabilen Niveau von maximal 40 Prozent hal-1114

ten.

1115

• Wir bleiben auch in Zukunft beim Grundsatz „Entlasten statt Belasten“. Gerade nach der 1116

Pandemie sind Steuererhöhungen der falsche Weg. Sie stehen dem notwendigen Auf-1117

schwung unserer Wirtschaft entgegen.

1118

• Wir werden den Solidaritätszuschlag für alle schrittweise abschaffen und gleichzeitig 1119

kleine und mittlere Einkommen bei der Einkommensteuer entlasten.

1120

• Wir treten entschieden allen Überlegungen zur Einführung neuer Substanzsteuern wie 1121

der Vermögensteuer oder der Erhöhung der Erbschaftssteuer entgegen. Beides würde Seite 34 von 139

1122

vor allem auch die wirtschaftliche Substanz Deutschlands gefährden und Arbeitsplätze 1123

kosten.

1124

 

1125

Unternehmensbesteuerung wettbewerbsfähig gestalten

1126

Deutschland droht mit einer der höchsten Unternehmensbelastung der Welt zurückzufal-1127

len. Weltspitze bei der Steuerbelastung und Weltspitze bei der Wettbewerbsfähigkeit – das 1128

passt auf Dauer nicht zusammen. Wir werden daher mit einer Unternehmenssteuerreform 1129

die Besteuerung modernisieren und wettbewerbsfähig machen.

1130

• Unser Ziel ist eine wettbewerbsfähige Unternehmensbesteuerung. Wir wollen die Steu-1131

erlast für Gewinne, die im Unternehmen verbleiben, perspektivisch auf 25 Prozent de-1132

ckeln. Das schafft Investitions- und Innovationskraft für die anstehenden Herausforde-1133

rungen. Dabei wollen wir Rechtsformneutralität herstellen, ob für Einzelunternehmer, 1134

Personengesellschaft oder Kapitalgesellschaft.

1135

• Wir wollen die Thesaurierungsbegünstigung und die Anrechnung der Gewerbesteuer 1136

verbessern und die Niedrigbesteuerungsgrenze im Außensteuerrecht reduzieren.

1137

• Wir verbessern die steuerliche Verlustverrechnung. Dazu erhöhen wir die Höchstbe-1138

tragsgrenzen beim Verlustrücktrag und beim Verlustvortrag deutlich.

1139

• Wir verbessern die Abschreibungsregeln. Dazu wollen wir die degressive Abschreibung 1140

für bewegliche Wirtschaftsgüter des Anlagevermögens wiedereinführen und die Ab-1141

schreibungsregeln für digitale Zukunftstechnologien verbessern, wie zum Beispiel Inves-1142

titionen in Serveranlagen, Künstliche Intelligenz, 3D-Druck oder die Fabrik 4.0.

1143

 

1144

Überflüssige Bürokratie abbauen

1145

Wir werden Unternehmen von Bürokratiekosten in Milliardenhöhe entlasten. Der Abbau 1146

überflüssiger Bürokratie wirkt wie ein Konjunkturprogramm und stärkt den Standort 1147

Deutschland.

1148

• Wir werden die Schwellenwerte für die Abgabe von Umsatzsteuervoranmeldungen er-1149

höhen, die Ist-Versteuerung ausweiten und die Informations- und Statistikpflichten be-1150

grenzen. Bei den Ausfuhrkontrollen wollen wir eine feste Bearbeitungsfrist von 30 Tagen 1151

einführen. Im Arbeits- und Sozialrecht wollen wir die Schwellenwerte, die sich an der 1152

Betriebsgröße orientieren, so weit wie möglich vereinheitlichen und vereinfachen.

1153

• Wir werden ein bürokratiefreies Jahr nach Gründung einrichten und im zweiten Grün-1154

dungsjahr bürokratische Belastungen auf ein Minimum reduzieren. Die Ausnahmen sol-1155

len vor allem für ausgewählte steuerrechtliche Regeln und Dokumentationspflichten gel-1156

ten. Damit schaffen wir mehr Freiraum für Gründerinnen und Gründer.

1157

• Wir werden die steuerlichen Betriebsprüfungen beschleunigen und modernisieren, da-1158

mit sie zeitnah, effizient und unbürokratisch erfolgen. Dies entlastet die Steuerpflichti-1159

gen, deren steuerliche Berater sowie die Finanzverwaltung und schafft umfassende 1160

Rechtssicherheit.

Seite 35 von 139

1161

• Wir werden die steuer- und sozialabgabenfreien Sachzuwendungen für Arbeitnehmer 1162

ausweiten und vereinfachen, um auch hier bürokratische Pflichten abzubauen.

1163

• Um vor allem Mittelstand und Familienunternehmen zu entlasten, sollen Erfolgskon-1164

trolle, Praktikabilität und Erfüllungsaufwände von Gesetzen durch einen Praxis-Check – 1165

bei frühzeitiger Beteiligung der Wirtschaft – geprüft werden. Innovative und weniger 1166

stark beschränkende Regelungen sollten in begrenzten Testräumen zunächst erprobt 1167

werden können.

1168

• Die von uns eingeführte Bürokratiebremse, das „One in, one out“-Prinzip, ist erfolgreich.

1169

Danach müssen neue Bürokratiekosten, die sich auf die Wirtschaft auswirken, an anderer 1170

Stelle wieder eingespart werden. Mit der Ausweiterung zu einer „One in, two out“-Regel 1171

sorgen wir für einen Entfesselungsschub.

1172

• Wir wollen Meldepflichten für die amtliche Statistik reduzieren. Für Unternehmen be-1173

deuten umfangreiche Statistikmeldungen einen hohen regelmäßigen Zeitaufwand, der 1174

zahlreiche Ressourcen bindet. Der Meldeaufwand beträgt für die betroffenen Unterneh-1175

men insgesamt mehrere Millionen Stunden. Gerade für viele Kleinst- und Kleinunterneh-1176

men sind die Meldepflichten eine überproportionale Belastung. Wir wollen daher die Be-1177

richtspflichten für die amtliche Statistik um 25 Prozent reduzieren.

1178

• Wir wollen auch EU-Vorgaben entbürokratisieren und diese grundsätzlich eins-zu-eins, 1179

das heißt, ohne zusätzliche Verschärfungen, umsetzen

1180

• Wir brauchen mehr Mut zu Pragmatismus als immer auf die 120-Prozent-Lösung zu set-1181

zen – auch bei der Definition von Standards sowie bei Verordnungen und Richtlinien. Zu 1182

hohe Anforderungen – bei öffentlichen Apps, beim digitalen Stromzähler oder bei Infra-1183

strukturvorhaben – führen dazu, dass Lösungen in Deutschland zunehmend teuer und 1184

kompliziert sind, zu lange dauern und sich damit am Ende nicht durchsetzen.

1185

 

1186

Planungs- und Genehmigungsverfahren beschleunigen

1187

Planungs- und Genehmigungsverfahren ziehen sich oft über Jahre hin und sind ein Hinder-1188

nis für neue Investitionen in Betrieben und Infrastrukturen. Wir werden sie beschleunigen 1189

und so für einen Modernisierungsschub sorgen.

1190

• Sämtliche Akten und Urkunden bei Planungsprozessen müssen digitalisiert werden. Wir 1191

wollen dabei die Chancen der Blockchain-Technologie nutzen.

1192

• Wir werden eine neue Beteiligungskultur schaffen, die mehr Transparenz in die Planung 1193

großer Bauprojekte bringt und alle Akteure früh einbindet.

1194

• Den Verwaltungsrechtsweg von Planungsverfahren werden wir verkürzen und das Ver-1195

bandsklagerecht straffen sowie zeitlich bündeln. Zugleich treiben wir unsere Initiative 1196

zur Entschlackung des EU-Planungs- und Umweltrechts weiter voran.

1197

• Wir setzen uns für einheitliche Standards bei umweltfachlichen und technischen Fragen 1198

sowie für eine bessere Vernetzung der Behörden untereinander ein, damit die fachlichen Seite 36 von 139

1199

Maßstäbe nicht erst in einem langwierigen Verfahren entwickelt werden. Zudem sollten 1200

Änderungen nach einem bestimmten Stichtag nicht mehr berücksichtigt werden müs-1201

sen. Dies würde die Planbarkeit von Infrastrukturprojekten verbessern und die Zeit vom 1202

Planungsbeginn bis zum Bau verkürzen.

1203

• Wir werden auf EU-Ebene für eine Beschleunigung der Planungsverfahren eintreten und 1204

uns im Rahmen der Aarhus-Konvention dafür einsetzen, schnelle Planungsverfahren zu 1205

ermöglichen.

1206

 

1207

Vergaberecht modernisieren

1208

Wir müssen es im Modernisierungsjahrzehnt schaffen, dass öffentliche Aufträge schneller, 1209

effizienter und einfacher vergeben werden.

1210

• Wir werden eine bundesweit einheitliche vergaberechtliche Regelung schaffen. Die un-1211

terschiedlichen Wertgrenzen für beschränkte Ausschreibungen, freihändige Vergaben 1212

und Verhandlungsvergaben und Direktaufträge in den Ländern müssen vereinheitlicht 1213

und auf ein angemessenes Maß zurückgeführt werden.

1214

• Betriebe müssen sich schnell und einfach auf öffentliche Aufträge bewerben können.

1215

Deshalb werden wir die E-Vergabe vereinheitlichen und die Vergabe öffentlicher Auf-1216

träge für Liefer-, Bau- und Dienstleistungen auf elektronischem Weg stärker vorantrei-1217

ben.

1218

 

1219

3.2. Sichere Arbeit mit Zukunft

1220

Der deutsche Arbeitsmarkt hat sich trotz der Corona-Pandemie als sehr robust erwiesen.

1221

Wir haben insbesondere mithilfe des Kurzarbeitergelds hunderttausende Arbeitsplätze ge-1222

sichert. Nun müssen wir diejenigen, die trotzdem ihren Job verloren haben, schnell wieder 1223

in Beschäftigung bringen. Dabei spielt nicht nur die Arbeitsvermittlung, sondern auch das 1224

lebensbegleitende Lernen eine entscheidende Rolle. Fort- und Weiterbildung sind der 1225

Schlüssel, um die vor uns liegenden Herausforderungen zu meistern. Unser Ziel bleibt die 1226

Vollbeschäftigung.

1227

 

1228

Sozialpartnerschaft stärken

1229

Die Sozialpartnerschaft, die Tarifautonomie und die Mitbestimmung haben wesentlich dazu 1230

beigetragen, dass Deutschland eine weltweit führende Industrienation geworden ist. Wir 1231

vertrauen auch in Zukunft auf die Sozialpartnerschaft.

1232

• Wir wollen, dass die Arbeitnehmerinnen und Arbeitnehmer auf eine verlässliche Mitbe-1233

stimmung setzen können und möglichst viele Beschäftigte durch Betriebs- und Perso-1234

nalräte vertreten werden. Hier sind zuallererst die Tarifpartner in der Pflicht. Ihre Auf-1235

gabe ist es, für gute Löhne und Arbeitsbedingungen zu sorgen und tragfähige Lösungen 1236

für den Wandel der Arbeitswelt zu finden.

Seite 37 von 139

1237

• Wir werden den Tarifpartnern möglichst großen Spielraum in der Gestaltung von Ar-1238

beitsregelungen lassen. Regelungen auf tariflicher, betrieblicher und vertraglicher Ebene 1239

werden den differenzierten Bedürfnissen eher gerecht. Wir werden die Tarifpartner da-1240

bei flankierend unterstützen und dort, wo es nötig ist, auch gesetzgeberisch eingreifen.

1241

• Die Allgemeinverbindlichkeitserklärung von Tarifverträgen leistet einen wichtigen Bei-1242

trag zur Erhöhung der Tarifgeltung in Branchen mit geringer Tarifbindung . Dieses Instru-1243

ment werden wir stärken.

1244

 

1245

Betriebsräte stärken

1246

Betriebsräte leben von der Legitimation durch die Belegschaft. Gerade wegen des digitalen 1247

Wandels und der Zunahme ortsungebundener Arbeitsplätze ist es wichtig, Betriebsräte 1248

durch elektronische Verfahren online wählen zu lassen.

1249

• Wir werden die Möglichkeit von Online-Wahlen schaffen, wenn der Wahlvorstand diese 1250

befürwortet – auch um die Wahlbeteiligung zu erhöhen.

1251

• Wie mit dem Betriebsrätemodernisierungsgesetz begonnen, werden wir auch in den 1252

kommenden Jahren in einer digitalen Arbeitswelt unsere Mitbestimmungskultur erhal-1253

ten und Mitbestimmungsrechte sichern.

1254

 

1255

Vielfalt des deutschen Arbeitsmarktes sichern

1256

Beschäftige und Unternehmen brauchen möglichst viele Gestaltungsspielräume, um ge-1257

meinsam gute Lösungen zu finden.

1258

• Werk- und Dienstverträge sind ein elementarer Bestandteil unseres funktionierenden 1259

Arbeitsmarkts. Sie unterstützen Spezialisierung, Aufgabenverteilung, Innovation, Quali-1260

tät, Selbstständigkeit und Arbeitsverhältnisse. Ihrer missbräuchlichen Anwendungen 1261

treten wir durch wirksame Arbeitsschutzkontrollen entschieden entgegen.

1262

• Wir werden die Zeitarbeit erhalten. Besonders für Geringqualifizierte und Langzeitar-1263

beitslose ist sie eine wichtige Brücke zur Arbeit, und auch für hochprofessionelle Fach-1264

kräfte immer häufiger eine frei gewählte Art der Arbeit. Konjunkturelle Schwankungen 1265

machen die Zeitarbeit zu einem wichtigen Flexibilisierungselement auf dem Arbeits-1266

markt, das nahezu vollständig tarifvertraglich geregelt ist.

1267

• Befristete Arbeitsverhältnisse sollen die Ausnahme sein. Wir lehnen die Ausweitung von 1268

Kettenbefristungen ab. Die sachgrundlose Befristung soll auch weiterhin in den Unter-1269

nehmen die Ausnahme bleiben und darf für den Beschäftigten grundsätzlich zwei Jahre 1270

nicht überschreiten. Missbrauch werden wir verhindern.

1271

• Minijobs bedeuten Flexibilität für Arbeitgeber und Arbeitnehmer vieler mittelständi-1272

scher Betriebe. Wir werden die Minijobgrenze von 450 Euro auf 550 Euro pro Monat er-1273

höhen und diese Grenze mit Blick auf die Entwicklung des Mindestlohns regelmäßig 1274

überprüfen.

1275

 

Seite 38 von 139

1276

Arbeitswelt der Zukunft gestalten

1277

Die Arbeitswelt ist im Wandel, insbesondere wegen der fortschreitenden Digitalisierung.

1278

Dies stellt neue Anforderungen an ein modernes Arbeitsrecht. Wir wissen zudem aus Erfah-1279

rung, wie wichtig es ist, dass Unternehmen ihre Beschäftigten auch in schwierigen Zeiten 1280

halten und auf Auftragsspitzen schnell reagieren können.

1281

• Wir wollen das Arbeitszeitgesetz reformieren und die Spielräume des EU-Rechts nutzen.

1282

Anstelle der täglichen soll eine wöchentliche Höchstarbeitszeit treten. Die Gesundheit 1283

und Sicherheit der Beschäftigten müssen dabei im Sinne des Arbeitnehmerschutzes ge-1284

währleistet bleiben. Dabei werden wir Missbrauch und Entgrenzung verhindern. Eine Ab-1285

weichung von der bisherigen Tageshöchstarbeitszeit kommt deshalb nur für nicht ge-1286

fahrgeneigte Berufe in Betracht.

1287

• Wir werden Personalpartnerschaften erleichtern und rechtssicherer machen. So können 1288

sich zwei Unternehmen im Rahmen einer Kooperation freie Personalkapazitäten mit Zu-1289

stimmung der Betriebsräte untereinander zur Verfügung stellen.

1290

• Wir werden Scheinselbstständigkeit verhindern und gleichzeitig mehr Rechtssicherheit 1291

für Selbstständige und ihre Auftraggeber schaffen. Daher haben wir in einem ersten 1292

Schritt noch 2021 das Statusfeststellungsverfahren für Selbstständige vereinfacht und 1293

beschleunigt. Die Auswirkungen werden wir genau beobachten und falls nötig Anpas-1294

sungen vornehmen. Die personelle Ausstattung der Clearingstelle wollen wir verbessern.

1295

• Neue Arbeitsformen (wie zum Beispiel Gig-, Click- und Crowdworking) sind in einer sich 1296

rasant verändernden Arbeitswelt auf dem Vormarsch. Wir werden die Entwicklungen in 1297

diesem Bereich aufmerksam begleiten und bei möglichen Fehlentwicklungen gesetzge-1298

berisch eingreifen.

1299

• Wir werden die Schaffung von Co-Working-Spaces gerade im ländlichen Raum unterstüt-1300

zen, um digitales Arbeiten nachhaltig, dezentral und zukunftsfähig zu organisieren.

1301

• Wir werden in den Jobcentern eine persönliche Begleitung mit niedrigem Betreuungs-1302

schlüssel ermöglichen und eine Offensive im Bereich der beruflichen Aus- und Weiter-1303

bildung starten. So können die Stärken und Fähigkeiten von Langzeitarbeitslosen besser 1304

erkannt und gefördert werden. Qualifizierungsmaßnahmen sind dabei einer schnellen 1305

Vermittlung in eine Helfertätigkeit vorzuziehen.

1306

 

1307

Fachkräfte sichern

1308

Damit wir auch in Zukunft die Fachkräfte haben, die unser Land braucht, setzen wir unter 1309

anderem auf gute berufliche Ausbildung, die zunehmende Beschäftigung von Frauen, Älte-1310

ren und Menschen mit Behinderungen auf dem ersten Arbeitsmarkt, die Qualifizierung von 1311

Langzeitarbeitslosen sowie den gesteuerten Zuzug gut ausgebildeter und leistungsbereiter 1312

Menschen aus den Mitgliedstaaten der EU und aus außereuropäischen Staaten. Deutsch-1313

land ist noch zu wenig Zielland für die klugen Köpfe der Welt.

Seite 39 von 139

1314

• Wir wollen die Potenziale der Binnenmarktmigration heben mit gezielten Sprach- und 1315

Qualifizierungsangeboten in ihren EU-Heimatländern.

1316

• Wir wollen unsere Auslandsinstitutionen stärker zu aktiven Botschaftern unseres Landes 1317

machen. Deutsche Unternehmen, Außenhandelskammern, deutsche Botschaften und 1318

Generalkonsulate, Goethe-Institute, Schulen im Ausland und den Deutschen Akademi-1319

schen Austauschdienst wollen wir dazu ermutigen, überall für Deutschland zu werben 1320

und über Möglichkeiten des Studiums und der Ausbildung in unserem Land zu informie-1321

ren.

1322

• Im Rahmen eines Pilotprojekts sollen „Fachkräfteeinwanderungs-Attachés“ an ausge-1323

wählten deutschen Botschaften in Drittstaaten ernannt werden. Sie sollen intensiv über 1324

die qualifizierte Zuwanderung nach Deutschland informieren und zuwanderungswillige 1325

Fachkräfte, beispielsweise im IT-Bereich, unterstützen.

1326

• Wir werden Möglichkeiten fördern, damit Schüler der Deutschen Auslandsschulen, die 1327

keine deutsche Staatsangehörigkeit haben, für ein Jahr nach Deutschland kommen und 1328

hier bei uns die Schule besuchen können („Deutschland-Jahr-Stipendium“).

1329

• Damit das Fachkräfteeinwanderungsgesetz seine volle Wirkung entfalten kann, werden 1330

wir die Anerkennung von Abschlüssen und die Zertifizierung von Qualifikationen ver-1331

bessern und das Antragsverfahren digitalisieren. Informationen zum Anerkennungsver-1332

fahren wollen wir frühzeitig vermitteln.

1333

• Für eine gezielte und gesteuerte Zuwanderung in den Arbeitsmarkt setzen wir weiterhin 1334

am Fachkräftebedarf von Mittelstand und Industrie an und berücksichtigen Qualifika-1335

tion, Alter, Sprachkenntnisse, den Nachweis eines konkreten Arbeitsplatzangebotes und 1336

die Sicherung des Lebensunterhaltes. Davon zu trennen ist die Hilfe für Menschen in 1337

Not. Das Asylrecht ist ein individuelles Schutzrecht und kein Ersatzeinwanderungsrecht.

1338

 

1339

3.3. Deutschland als klimaneutrales Industrieland bis 2045

1340

Die Pariser Klimaziele sind die Grundlage für unsere internationale Verantwortung als In-1341

dustrieland. Zum Erreichen brauchen wir innovative Technologien, wirtschaftliche Investi-1342

tionen und ein koordiniertes Handeln von Politik, Industrie und Gesellschaft. Nur wenn 1343

Technologien, Investitionen und Projekte in die Dekarbonisierung sich letztlich als wirt-1344

schaftlich erweisen, wird die Jahrhundert-Transformation gelingen. Nur wenn Investitionen 1345

in die Dekarbonisierung zu mehr Wettbewerbsfähigkeit führen, werden neue Arbeitsplätze 1346

und Wertschöpfungsketten entstehen.

1347

• Wir setzen verbindlich die Treibhausgasneutralität Deutschlands bis 2045 um. So schaf-1348

fen wir unseren deutschen Beitrag, um international den 1,5 Grad-Pfad zu beschreiten.

1349

Dabei setzen wir auf neue Technologien und Innovationen. Zusätzlich streben wir zum 1350

Erreichen der Pariser Klimaziele internationale Klimakooperationen an, um den Anstieg 1351

der globalen Durchschnittstemperatur zu begrenzen.

Seite 40 von 139

1352

• Unser Ziel ist, die Treibhausgasemissionen Deutschlands bis 2030 um 65 Prozent gegen-1353

über dem Referenzjahr 1990 zu reduzieren, um dann auf einem konkret beschriebenen 1354

Pfad im Jahr 2040 88 Prozent Minderung und im Jahr 2045 Treibhausgasneutralität zu 1355

erreichen. Deutschland wird hier als Industrieland eine große Verantwortung überneh-1356

men, damit bis 2050 weltweit CO2-Neutralität erreicht wird.

1357"""



input_text2 = """1. Neue Verantwortung Deutschlands in der Welt – aus Überzeugung für
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

input_text_test = """a
b
c

e-


e
f
awdadw ersg Seite 3 von 7s geg 
aw
Seite 3 von 73444
geasügle
"""


output = cleanUp(input_text, True)
print("Cleaned Text: " + output)
