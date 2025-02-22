import re


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

1357

• In bestimmten Bereichen können Prozessemissionen kontinuierlich gesenkt, jedoch 1358

nicht vollständig vermieden werden. Wir werden Forschung, Entwicklung und Pilotpro-1359

jekte unterstützen, um sicherzustellen, dass sie über sogenannte negative Emissionen in 1360

anderen Bereichen ausgeglichen werden können.

1361

 

1362

Emissionshandel ausbauen – Verbraucherinnen und Verbraucher entlasten

1363

Auf dem Weg zur Klimaneutralität setzen wir auf effiziente marktwirtschaftliche Instru-1364

mente als Leitinstrumente innerhalb eines Instrumentenmixes. Heute schon und in Zu-1365

kunft.

1366

• Wir setzen auf das Instrument des Emissionshandels und kompensieren entstehende 1367

Mehrbelastungen mit gezielten Entlastungen in den Bereichen Wohnen und Mobilität.

1368

Aufbauend auf dem europäischen Emissionshandel für Energie und Industrie wollen wir 1369

den europäischen Emissionshandel im Luftverkehr stärken und in weiteren Sektoren wie 1370

Mobilität und Wärme sowie dem Schiffverkehr so schnell wie möglich etablieren.

1371

• Davon ausgehend streben wir einen umfassenden europäischen Emissionshandel mit 1372

einheitlichem Preis und globaler Anschlussfähigkeit an.

1373

• Wir wollen den Aufwuchspfad der CO2-Bepreisung straffen und so schnell wie möglich 1374

zu einem Europäischen Emissionshandel für Mobilität und Wärme übergehen.

1375

• Die Einnahmen aus dem Emissionshandel werden wir in vollem Umfang an die Bürgerin-1376

nen und Bürger und an die Betriebe durch Stromverbilligung zurückgeben. Als erstes 1377

schaffen wir die EEG-Umlage ab.

1378

• Klimaneutralität wird ein Wettbewerbsvorteil unserer Wirtschaft werden. Investitionen 1379

in Klimatechnologien und Energieeffizienz zur CO2-Reduktion sollen künftig steuerlich 1380

besser abgesetzt werden können. Im Rahmen einer Klimaeffizienzreform wollen wir auf 1381

das Klimapaket aufbauen und energiebezogene Steuern, Umlagen und Entgelte stärker 1382

auf CO2-Ausstoß ausrichten.

1383

 

1384

Nachhaltigkeit wettbewerbsfähig machen

1385

Für uns ist klar: Maßnahmen zum Klimaschutz dürfen nicht an unseren Grenzen haltma-1386

chen.

1387

• Bei allen Maßnahmen werden wir darauf achten, dass Produktionsprozesse nicht in 1388

Drittstaaten mit geringeren Klimaschutzstandards verlagert und Emissionen dort wei-1389

terhin ausgestoßen werden (Carbon-Leakage-Schutz).

Seite 41 von 139

1390

• Um unsere Wirtschaft im weltweiten Wettbewerb vor Wettbewerbsverzerrungen zu 1391

schützen, streben wir international höhere Standards und angepasste Preise an. Zudem 1392

wollen wir in internationalen Klimakooperationen mit großen Volkswirtschaften ambiti-1393

onierte Standards etablieren. Ergänzend dazu wollen wir gemeinsam mit unseren euro-1394

päischen Partnern einen WTO-konformen CO2-Grenzausgleich (Carbon Border Adjust-1395

ment Mechanism) einführen.

1396

• Wir sehen zudem in Carbon Contracts for Difference ein wichtiges Instrument, um un-1397

sere Unternehmen beim Klimaschutz zu unterstützen.

1398

 

1399

Klimaschutz mit Innovationen und neuen Technologien vorantreiben

1400

Wir werden beim Klimaschutz entscheidend weiterkommen, wenn wir auf Innovationen 1401

und neue Technologien setzen. Dabei wollen wir sowohl Unternehmen als auch Verbrau-1402

cherinnen und Verbraucher unterstützen.

1403

• Wir werden Verbraucherinnen und Verbraucher bei Investitionen in besonders ressour-1404

censchonenden digitalen Technologien unterstützen. Sie müssen bei Konsum- und Pro-1405

duktionsentscheidungen auf einen Blick nachvollziehen können, welche CO2-Bilanz ein 1406

Produkt hat.

1407

• Gemeinsam mit unseren europäischen Partnern wollen wir die Möglichkeiten zur Ab-1408

scheidung und Speicherung von CO2 (CCS) sichern und fördern. Hierfür sind intakte 1409

Kohlenstoffkreisläufe (CCU) und damit die Technologien zur feststofflichen Speicherung 1410

(CCUS) ebenso wie der Aufbau einer CO2-Infrastruktur erforderlich.

1411

• Wir werden die Digitalisierung nutzen, um kosteneffizienter CO2 zu verringern und Star-1412

tups sowie kleine und mittlere Unternehmen fördern, die digitale Lösungen für Energie-1413

und Ressourceneffizienz entwickeln. Wir wollen insbesondere die Clean-Tech-Forschung 1414

fördern.

1415

 

1416

3.4. Unser Energiekonzept für die Zukunft

1417

Eine sichere, bezahlbare und klimafreundliche Energieversorgung ist für unser Industrie-1418

land Pflicht, nicht Kür.

1419

 

1420

Für einen intelligenten Energiemix sorgen

1421

Wir werden den Ausbau der Erneuerbaren Energien entscheidend voranbringen und daher 1422

deutlich schneller ausbauen, damit der stark steigende Energiebedarf gedeckt wird. Nur so 1423

wird die Energiewende in allen Bereichen gelingen, und nur so werden die Pariser Klimaziele 1424

erreicht werden. Wir setzen auf einen intelligenten und diversifizierten Energiemix, der 1425

nachhaltig und sicher ist. Dazu gehört die Energiegewinnung aus Sonne und Wind genauso 1426

wie nachhaltige Biomasse, Wasserkraft und Geothermie im ländlichen Raum. Hierbei wird 1427

die Akzeptanz der Bevölkerung ebenso entscheidend für den Ausbau der Erneuerbaren 1428

Energien sein wie Planungssicherheit und wenig Bürokratie.

Seite 42 von 139

1429

• Mit einem Sonnenpaket werden wir den Ausbau der Photovoltaik fördern. Genehmi-1430

gungsverfahren für Photovoltaikanlagen wollen wir möglichst einfach über eine Online-1431

plattform gestalten. Wir wollen, dass beim Bau von Freiflächen-Photovoltaikanlagen der 1432

Landwirtschaft keine zusätzlichen Flächen für naturschutzrechtlichen Ausgleich entzo-1433

gen werden, wenn Mindestkriterien für Naturschutz und biologische Vielfalt auf der An-1434

lagenfläche erfüllt werden.

1435

• Wir fördern den naturverträglichen Ausbau von Wind onshore und offshore sowie das 1436

Repowering von Anlagen. Wir wollen im Rahmen der Europäischen Offshore-Strategie 1437

und des nationalen Wind-See-Gesetzes auch grenzüberschreitende Energiekooperatio-1438

nen eingehen. Hierzu streben wir an, dass Flächen explizit für Erneuerbare Energien aus-1439

gewiesen werden. Dazu wollen wir prüfen, ob vermehrt Flächen entlang von Verkehrs-1440

wege im Rahmen von Vorrangflächen für die Nutzung durch Erneuerbare Energien ein-1441

gerichtet werden können.

1442

• Wir brauchen Energiespeicher, um die Schwankungen der Erneuerbaren Energie in wind-1443

und sonnenschwachen Zeiten auszugleichen. Wir werden die dafür notwendige Techno-1444

logieentwicklung und -umsetzung weiter fördern und prüfen, inwieweit wir den gespei-1445

cherten Strom von allen Umlagen und Entgelten befreien können.

1446

• Besonders unsere Handwerksbetriebe sind mit ihrer Expertise für die Energiewende ent-1447

scheidend. Wir werden sie dabei unterstützen, genügend Fachkräfte auszubilden und zu 1448

gewinnen. Hier kommt es besonders auf Aus- und Weiterbildung im Bereich neuer Tech-1449

nologien an.

1450

• Stromnetze sind die Lebensadern der Energiewende. Sie sind Garanten für die Versor-1451

gungsicherheit Deutschlands. Wir wollen prüfen, wie wir im Bereich der Übertragungs-1452

netze für mehr Kostenwettbewerb und beschleunigte Investitionen sorgen können. Wir 1453

wollen den Bau der notwendigen Stromleitungen beschleunigen. Wo immer möglich, sol-1454

len Trassen klug gebündelt und anwohnerverträglich realisiert werden.

1455

• Wir wollen die Forschung und Entwicklung von neuen Energieerzeugungsverfahren tech-1456

nologieoffen unterstützen. Wir müssen zu große Stromimportabhängigkeiten vermei-1457

den.

1458

• Wir müssen für bezahlbaren Strom sorgen. Deshalb werden wir die regulatorischen Kos-1459

ten senken. Mit Blick auf die Wettbewerbssituation unserer Industrie brauchen wir einen 1460

wettbewerbsfähigen Industriestrompreis.

1461

• Unser Marktstammdatenregister wollen wir zu einem digitalen, öffentlichen Echtzeit-1462

Energiekataster weiterentwickeln. So wollen wir Investitionssicherheit schaffen und Ge-1463

nehmigungen vereinfachen. Angelehnt an das Prinzip des Grundbuches wird transpa-1464

rent, welche Energieprojekte aktuell am Netz sind und welche wann und wo zukünftig 1465

entstehen.

1466

 

 

Seite 43 von 139

1467

Energieeffizienz fördern

1468

Zur Effizienzgewinnung setzen wir vor allem auf technologische Weiterentwicklung und In-1469

novationen – bei Produkten ebenso wie bei Verfahren. Hierzu gehören Quartiersansätze, 1470

die Wärmeeffizienz, der Ausbau und die Modernisierung der Wärme- und Stromnetze, die 1471

Digitalisierung und Betriebsoptimierungen ebenso wie der Ausbau von Speicherkapazitä-1472

ten und energetische Baustandards.

1473

• Um die energetische Sanierung von Wohn- und Gewerbeimmobilien noch besser zu för-1474

dern, werden wir die KfW-Programme attraktiver gestalten.

1475

• Die Steuerförderung der Gebäudesanierung wollen wir auf vermietete Immobilien und 1476

auf Gewerbeimmobilien ausdehnen.

1477

• Wir werden gewerbliche Investitionen, die einen Beitrag zur Energieeffizienz und CO2-1478

Reduzierung leisten, durch eine schnellere Abschreibung begünstigen.

1479

 

1480

Deutschland zum Wasserstoff-Land Nr. 1 machen

1481

Viele der für die Transformation notwendigen Technologien existieren bereits. Eine wich-1482

tige Rolle spielt dabei CO2-neutraler Wasserstoff – als vielseitiger Energieträger, flexibler 1483

Energiespeicher und wichtiger Grundstoff für chemische Prozesse. Wasserstoff ermöglicht 1484

eine Dekarbonisierung auch da, wo Erneuerbare Energie nicht direkt eingesetzt werden 1485

kann. Bedeutende industrielle Prozesse, etwa in der Stahl- und Zementindustrie, lassen sich 1486

nur mit Wasserstoff klimaneutral gestalten. Und auch im Bereich der Mobilität, kurz- und 1487

mittelfristig für den Lkw- und Schiffsverkehr, können wir durch den Einsatz von Wasserstoff 1488

erheblich zur Reduzierung von CO2 beitragen. Deshalb gilt es nun, die umfassende Wert-1489

schöpfungskette zur Wasserstofferzeugung inklusive der erforderlichen Netzinfrastruktur 1490

aufzubauen.

1491

• Wir werden die nationale Wasserstoff-Agentur stärken, um die Wasserstoffstrategie um-1492

zusetzen und internationale Kooperationen zum Import von Wasserstoff, den Infrastruk-1493

turausbau sowie die Umnutzung bestehender Systeme voranzutreiben.

1494

• Wir wollen Innovationszyklen beschleunigen, Power-to-X-Technologien zielgerichtet 1495

fördern und einen Marktrahmen für klimaneutrale Gase mit der hierfür nötigen Infra-1496

struktur auf Basis der vorhandenen Gasleitungen und -speicher sowie CO2-Transparenz 1497

in Europa schaffen.

1498

• Wir werden Deutschlands Position mit Forschung zur Serienfertigung von Elektrolyseu-1499

ren, Brennstoffzellen und durch die Einrichtung von Wasserstoff-Technologie- und Inno-1500

vationszentren ausbauen.

1501

• Mit dem Aufbau eines Europäischen Wasserstoffnetzwerks wollen wir sicherstellen, dass 1502

die zukünftige Nachfrage auf dem europäischen und globalen Wasserstoffmarkt bedient 1503

werden kann. Dazu wollen wir das Förderkonzept „H2 Global“ weiterentwickeln.

1504

• Wir werden Wasserstoff aus Erneuerbaren Energien gewinnen. Neben diesem sogenann-1505

ten grünen Wasserstoff werden wir in der Übergangszeit auch den blauen Wasserstoff Seite 44 von 139

1506

akzeptieren. Mit dem Aufbau eines starken europäischen Heimatmarktes für nachhal-1507

tige Wasserstofftechnologien fördern wir Deutschland nicht nur als Industriestandort.

1508

Wir tragen auch dazu bei, für Wasserstofftechnologien international große Anwen-1509

dungsmöglichkeiten zu schaffen, sodass ein globaler Wasserstoffmarkt entstehen kann.

1510

• Wir werden die Gasnetze in Deutschland schneller ausbauen und für die Einspeisung von 1511

Wasserstoff ertüchtigen.

1512

 

1513

3.5. Nachhaltiges Wirtschaften zum Schutz unserer Ressourcen 1514

Nachhaltiges Wachstum heißt, den wirtschaftlichen Fortschritt vom Ressourcenverbrauch 1515

zu entkoppeln. Die Schließung von Stoffkreisläufen sorgt für neue wirtschaftliche Potenzi-1516

ale und schützt unsere natürlichen Lebensgrundlagen.

1517

 

1518

Wegwerfgesellschaft beenden, Kreislaufwirtschaft stärken

1519

Kreislaufwirtschaft muss sich lohnen. Sie schont natürliche Ressourcen, spart Energie und 1520

Emissionen, schafft Arbeitsplätze und sichert Wohlstand und Wettbewerbsfähigkeit unse-1521

rer Wirtschaft. Unser Ziel sind Rohstoffe „Made in Germany“. Wir wollen die Rohstoffe, die 1522

unsere Industrie benötigt, vorrangig im eigenen Land gewinnen und Recyclingrohstoffe 1523

einsetzen. Das hilft dem Klimaschutz und macht uns unabhängiger von Importen aus dem 1524

Ausland.

1525

• Wir werden Anreize setzen, weniger Abfall zu produzieren, abfallarme Produkte zu ent-1526

wickeln und die Möglichkeiten einer stofflichen Wiedernutzung von Recyclingrohstoffen 1527

zu verbessern.

1528

• Mit der Förderung von Innovationen in Sortiertechnologien werden nutzbare Rezyklate, 1529

also aus Recyclingprozessen gewonnene Produkte entstehen, die am Markt gegenüber 1530

Primärmaterialien bestehen. Wir werden uns dafür einsetzen, den Einsatz von Rezykla-1531

ten in der EU wie auch in Deutschland zu fördern. Um die Nutzung von Rezyklaten, ins-1532

besondere im Kunststoffbereich deutlich zu verbessern, wollen wir auch verbindliche 1533

Ziele für ihren Einsatz in bestimmten Bereichen prüfen.

1534

• Wir wollen Recycling maximieren und Rohstoffsicherheit garantieren. In immer mehr 1535

Branchen werden Engpässe bei Rohstoffen – von seltenen Erden bis hin zu Holz oder 1536

Vorleistungsprodukten wie Chips – zu einem Hemmnis für unsere wirtschaftliche Ent-1537

wicklung und Versorgungssicherheit. Deshalb entwickeln wir eine Rohstoffsicherungs-1538

strategie für Deutschland.

1539

• Wir setzen uns für einen Einsatz von nachhaltig abgebauten Rohstoffen ein, die mög-1540

lichst lange genutzt werden können. Damit leisten wir einen wichtigen weltweiten Bei-1541

trag für den Ressourcen- und Klimaschutz. Wir wollen vor allem das Batterierecycling im 1542

Hinblick auf seltene Erden fördern und da, wo sie ökologische Vorteile bringen, Mehr-1543

wegprodukte fördern.

Seite 45 von 139

1544

• Wir wollen Doppelregulierungen und Inkonsistenzen, die Stoffkreisläufen entgegenste-1545

hen, abbauen und vermeiden – in Deutschland und in der EU. Dazu gehört ein Deponie-1546

verbot für unbehandelte Siedlungsabfälle und vor allem kunststoffhaltige Abfälle. Zu-1547

dem wollen wir die Forschung zu Re-Oil-Verfahren unterstützen und auch das chemische 1548

Recycling fördern.

1549

• Wir wollen Abfälle wiederverwerten und Exporte von Abfällen – insbesondere von Plas-1550

tik- und Kunststoffabfällen – zur bloßen Entsorgung verbieten. Es ist uns wichtig, dass 1551

wir ebenfalls zu Kunststoffalternativen weiterforschen, auch um die Vermeidung von 1552

Mikroplastik weiter voranzutreiben.

1553

 

1554

Dem Wald von Morgen neue starke Wurzeln geben

1555

Deutschland ist Waldland Nummer 1 in Europa. Unsere Wälder sind die grüne Lunge unse-1556

res Landes und unser wichtigster Klimaschützer. Sie produzieren Sauerstoff und speichern 1557

große Mengen von CO2. Ebenso sind sie wichtiger Wirtschaftsfaktor, sorgen für Wert-1558

schöpfung und Arbeitsplätze vor allem in ländlichen Regionen und sind unverzichtbar für 1559

die Biodiversität und unsere Erholung. Durch die Klimaveränderung ist der Wald geschädigt 1560

und bedroht. Wir haben in der Dürre der vergangenen Jahre und durch die nachfolgende 1561

Borkenkäferplage sehr viele wertvolle Wälder verloren.

1562

• Bund und Länder haben ein 1,5-Milliarden-Euro-Paket für die Wiederbewaldung, die An-1563

passung der Wälder an den Klimawandel und für die Unterstützung der nachhaltigen 1564

Forstwirtschaft geschnürt. Dieses Paket muss auch den Kleinwaldbesitzern zugänglich 1565

sein. Damit helfen wir den Waldeigentümerinnen und Waldeigentümern beim Aufbau 1566

klimastabiler Mischwälder mit standortangepassten Baumarten.

1567

• „Schützen durch Nützen“ ist unser Grundsatz für eine nachhaltige Bewirtschaftung un-1568

serer wertvollen Wälder. Wir stehen zu unserer multifunktionalen Forstwirtschaft, denn 1569

nur sie sichert Schutz-, Nutz- und Erholungsfunktion der Wälder gleichermaßen. Nach-1570

haltig bewirtschaftete Wälder und besonders die Verwendung von Holzprodukten mit 1571

langen Lebenszyklen verlängern die CO2-Speicherleistung des Waldes.

1572

• Damit wir die Klimaschutzziele erreichen, müssen wir neben der wichtigen Verringerung 1573

der Emissionen die CO2-Minderung von Wald und Holz stärken. Deshalb werden wir die 1574

Klimaschutzleistungen des Waldes unter Einbezug der Holzprodukte finanziell honorie-1575

ren und eine CO2-Bindungsprämie einführen. So kann die Klimaleistung des Waldes dau-1576

erhaft und verlässlich abgegolten werden und ein zentraler Baustein zur Honorierung 1577

weiterer Ökosystemleistungen des Waldes sein, die wir voranbringen wollen. Auch wer-1578

den wir den Einsatz von Holz als Bau-, Werk- und Brennstoff voranbringen und Hemm-1579

nisse abbauen. Dazu werden wir eine Holzbauoffensive starten.

1580

• In der Europäischen Union setzen wir uns dafür ein, dass der Waldschutz ein wichtiger 1581

Bestandteil des Green Deals wird und überall in Europa mehr für die Wälder getan wird.

Seite 46 von 139

1582

• Wir engagieren uns beim Schutz der internationalen Wälder und gegen illegalen Holz-1583

einschlag. Der Erhalt des Regenwaldes und weiterer wertvoller Naturwälder von welt-1584

weiter Bedeutung ist uns ein großes Anliegen.

1585

 

1586

Wasser als Ursprung allen Lebens und Wirtschaftens schützen

1587

Der Kampf gegen den Klimawandel ist auch ein Kampf für ausreichend Wasser. Wir müssen 1588

sicherstellen, dass für alle in unserem Land – Privathaushalte, Landwirte und Unternehmen 1589

– ausreichend Wasser vorhanden ist.

1590

• Wir werden ein Förderprogramm auflegen, das regionale Wasserkreisläufe stärkt.

1591

• Über Aufklärungskampagnen und modernes Wassermanagement werden wir das Allge-1592

meingut Wasser schützen. Das Wasser muss stärker in der Fläche gehalten werden, um 1593

unsere Böden, die Land- und Forstwirtschaft und die Ökosysteme widerstandsfähiger für 1594

Dürrezeiten zu machen.

1595

• Der Nutzung von Regenwasser wollen wir eine deutlich größere Aufmerksamkeit schen-1596

ken und hierzu das Konzept von Schwammstädten, etwa durch Anpassungen bei Stra-1597

ßenrändern zur Versickerung im Zuge von Modernisierungen, in Beispielkommunen tes-1598

ten.

1599

• Wir werden die Vorgaben der europäischen Wasserrahmenrichtlinie umsetzen. Wir stre-1600

ben an, freifließende Flüsse mit natürlichen Flussläufen als naturnahe Referenzflüsse 1601

auszuweisen. Hochwasserprävention an Flüssen und Küsten dient dem Schutz unseres 1602

Lebens und unserer Lebensgrundlagen. Daher werden wir uns für naturnahen Binnen-1603

und Außendeichbau und den Schutz unserer Auen einsetzen.

1604

• Wir werden noch stärker gegen die Verunreinigung unserer Gewässer mit Spurenstoffen 1605

und Medikamenten vorgehen. Wir werden die Strategie zur Prävention von Gewässer-1606

verunreinigung und den Dialog zu Spurenstoffen, Mikroplastik und Medikamentenver-1607

unreinigungen fortführen. Wir werden die Vorkommen an Trink-, Mineral-, Heil- und 1608

Grundwasser weiterhin besonders schützen.

1609

• Im Sinne des ganzheitlichen Meeres-, Küsten- und Gewässerschutzes unterstützen wir 1610

auch künftig die Zusammenarbeit von Bund und Ländern bei der Altlastenbeseitigung.

1611

 

1612

3.6. Vorfahrt für intelligente Mobilität

1613

Mobilität ist ein Ausdruck individueller Freiheit. Für uns als Wirtschaftsnation ist sie von 1614

großer Bedeutung und ein wichtiges Kapitel unseres Modernisierungsjahrzehnts. Wir wer-1615

den die Rekordinvestitionen in die Infrastruktur verstetigen.

1616

 

1617

Schiene ausbauen

1618

Eine starke Schiene und der Öffentliche Personennahverkehr sind ein bedeutender Faktor 1619

für die Dekarbonisierung des Verkehrs.

Seite 47 von 139

1620

• Wir werden den Schienenverkehr mit dem Deutschlandtakt stärken. Mit einem attrakti-1621

ven Angebot der Deutschen Bahn wollen wir maximale Synergien bei Güter- und Perso-1622

nenverkehr in unserem Schienensystem nutzen.

1623

• Deutschland muss weiterhin ein Mobilitäts- und Logistikdrehkreuz in Europa sein. Um 1624

das Schienennetz zukunftsfest zu machen, Lücken zu schließen, Strecken zu elektrifizie-1625

ren und mehr Kapazitäten zu schaffen, werden wir mehr in den bedarfsgerechten Infra-1626

strukturausbau investieren – insbesondere in die Digitalisierung von Schiene und Fahr-1627

zeugen (ETCS-Ausbau).

1628

• Wir werden dafür sorgen, dass Deutschland europaweite Verbindungen zu Tages- und 1629

Nachtzeiten unterstützt und hierfür den Bahnverkehrswegebau massiv beschleunigen.

1630

Nachtzüge gehören für uns zum Mobilitätsmix der Zukunft. In diesem Zusammenhang 1631

werden wir weiter in den Lärmschutz investieren.

1632

• Um das Stauaufkommen auf den Autobahnen zu reduzieren und Klimaziele zu erreichen, 1633

wollen wir mehr Güterverkehr von der Straße auf die Schiene und auf die Wasserstraße 1634

verlagern. Dazu werden wir in saubere Fahrzeuge und leistungsfähige Infrastruktur in-1635

vestieren, auch in neue Ladestationen für Binnenschiffe in Häfen (Landverstromung).

1636

• Wir werden den kombinierten Verkehr mit multi-modalen Terminals ausbauen und das 1637

Bundesprogramm „Zukunft Schienengüterverkehr“ ausweiten. Wir müssen hier auch die 1638

Steuern und Abgaben in den Blick nehmen. Dazu werden wir die Mittel für Maßnahmen 1639

zur Verbesserung des Schienengüterverkehrs des vordringlichen Bedarfs im Bedarfsplan 1640

Schiene erhöhen und weiterhin die Trassenpreise reduzieren.

1641

• Für den nächsten Bedarfsplan und bei der standardisierten Bewertung wollen wir stärker 1642

als bisher auch längerfristige Prognosen, Umstiegseffekte und Anwohnerinteressen ge-1643

wichten.

1644

 

1645

Automobilstandort Deutschland sichern

1646

Unsere Automobilindustrie ist weltweit führend, auch bei der Erforschung und Entwicklung 1647

innovativer Technologien, um ökologisch, ökonomisch und sozial nachhaltige Mobilitätsan-1648

gebote zu entwickeln. Wir wollen, dass in Deutschland weiterhin die besten Autos der Welt 1649

produziert werden – und zwar mit allen Antriebsformen.

1650

• Wir stehen vor einem Modernisierungsjahrzehnt für die Automobilindustrie. Immer 1651

mehr deutsche Automobilhersteller kündigen an, aus der Herstellung von Verbrenner-1652

motoren auszusteigen. Wir werden den Umstieg in emissionsfreie Mobilität für alle at-1653

traktiv gestalten und dazu einen Fahrplan vorlegen. Damit sorgen wir dafür, dass alle 1654

Interessen berücksichtigt werden – von Verbraucherinnen und Verbrauchern, Unterneh-1655

men inklusive der Zuliefererindustrie, von Beschäftigten und im Sinne eines nachhalti-1656

gen Einsatzes von Rohstoffen und Ressourcen.

Seite 48 von 139

1657

• Wir setzen dabei neben der Elektromobilität auch auf synthetische Kraftstoffe im Stra-1658

ßenverkehr und wollen sie – wie auch Wasserstoff – perspektivisch auch im Schwerlast-1659

verkehr einsetzen. Nutzfahrzeuge und schwere LKW könnten andere Antriebstechnolo-1660

gien erfordern. Hier müssen wir technologieoffen bleiben. Ein zusätzlicher Baustein soll 1661

die Verlängerung des Flottenerneuerungsprogramms für LKW sein.

1662

• Taxiunternehmen, Fahr- und Lieferdienste wollen wir bei der Umstellung auf Null-Emis-1663

sions-PKW durch Sonderabschreibungen, auch bei Ladesäulen, unterstützen.

1664

• Ein Dieselfahrverbot lehnen wir ebenso ab wie ein generelles Tempolimit auf Autobah-1665

nen. Stattdessen setzen wir auf innovative, moderne Verkehrssteuerung.

1666

• Für den weiteren Ausbau des elektrifizierten Verkehrs ist der Ausbau der Ladeinfrastruk-1667

tur entscheidend. Zur weiteren Beschleunigung wollen wir sie künftig in alle gewerbli-1668

chen und öffentlichen Neubauimmobilien integrieren und diese auch in Parkhäusern ver-1669

bessern. Unser Ziel ist es, das Ladesäulennetz so auszubauen, dass die Lademöglichkei-1670

ten ein Grund für den Wechsel auf Elektromobilität sind. Wir wollen, dass Schnelllade-1671

säulen bundesweit im Fernverkehr möglichst innerhalb von zehn Minuten erreicht wer-1672

den können und zudem das Bezahlsystem sowie die Anschlüsse vereinfacht und standar-1673

disiert werden.

1674

 

1675

Luft- und Schifffahrt zukunftsfest machen

1676

Die deutsche Luftverkehrswirtschaft verbindet uns mit der Welt. Sie soll zum Technologie-1677

führer für das klimaneutrale Fliegen werden. Zudem werden wir unsere Schifffahrt stärken 1678

und zukunftsfest machen.

1679

• Wir wollen, dass die Luftfahrt ein preislich wettbewerbsfähiger Verkehrsträger ist und 1680

der Luftverkehrsstandort Deutschland erhalten bleibt. Wir werden die Verbindungen auf 1681

der Schiene zu den Drehkreuzflughäfen bzw. internationalen Flügen ausbauen und das 1682

Umsteigen zwischen Flug und Zug für Kunden verbessern. Die Verkehrsträger sollen so 1683

vernetzt werden, dass ihre jeweiligen verkehrlichen, ökonomischen und ökologischen 1684

Vorteile optimal genutzt werden können.

1685

• Wir werden das Luftfahrtforschungsprogramm ausbauen und ein Technologie-Demonst-1686

rator-Programm einrichten.

1687

• Uns ist wichtig, dafür zu sorgen, dass am Standort Deutschland synthetische Kraftstoffe 1688

(SAF) entwickelt und produziert werden. Flüge, bei denen alternative Kraftstoffe einge-1689

setzt werden, wollen wir von der Luftverkehrssteuer befreien.

1690

• Ebenso wollen wir die positiven Aspekte des Fliegens und die Innovationskraft der Luft-1691

fahrt wieder stärker herausstellen und als Schlüsseltechnologie gezielt fördern. Die Ent-1692

wicklung von Flugtaxen ist zwar noch eine Vision für die Zukunft, aber sie wird zuneh-1693

mend realistischer.

Seite 49 von 139

1694

• Wir werden die maritime Wirtschaft und den Werftenstandort Deutschland stärken. Die 1695

deutsche Schiffbauindustrie, Schifffahrt und Häfen müssen international wettbewerbs-1696

fähig bleiben.

1697

• In der Binnenschifffahrt übernehmen wir mit einer stärkeren Förderung von alternativen 1698

Kraftstoffen wie E-Fuels und Wasserstoff die Technologieführerschaft. Wir werden die 1699

Nutzung von Ammoniak oder Methanol zur Marktreife bringen und in der Schifffahrt 1700

anwenden. Zudem werden wir die LNG-Technik ausbauen und ein Importterminal für 1701

verflüssigte Gase realisieren.

1702

 

1703

3.7. Eine Landwirtschaft, die stark und nachhaltig ist 1704

Eine starke und nachhaltige Landwirtschaft einschließlich Obst-, Gemüse-, Garten-, Wein-1705

bau sowie Imkerei und Fischerei ist in einem lebenswerten Deutschland unverzichtbar. Un-1706

sere Bäuerinnen und Bauern sichern nicht nur unsere Ernährung, sondern gestalten unsere 1707

Kulturlandschaft und sind die Grundlage unserer starken Lebensmittelwirtschaft. Ohne 1708

Landwirtschaft gibt es kein klimaneutrales Deutschland und keine Artenvielfalt.

1709

 

1710

Landwirtschaft stärken

1711

Wir stehen an der Seite unserer Bäuerinnen und Bauern. Unsere Landwirtschaft verdient 1712

mehr Wertschätzung und braucht mehr Wertschöpfung. Wir wollen sie aus dem Hamster-1713

rad der permanenten Effizienzsteigerung unter Industriebedingungen befreien. In unserem 1714

Modernisierungsjahrzehnt setzen wir auf Nachhaltigkeit und eröffnen allen Sparten der 1715

Landwirtschaft neue Wege, Perspektiven und Chancen.

1716

• Wir begleiten die Landwirtschaft verlässlich beim ökologischen Wandel.

1717

• Für Bäuerinnen und Bauern – und insbesondere die künftige Generation – schaffen wir 1718

attraktive und vielseitige Einkommensmöglichkeiten.

1719

• Für uns gehört Landwirtschaft unverzichtbar zu unserem Land, in die Mitte der Gesell-1720

schaft. Wir wenden uns strikt gegen ungerechtfertigte Feindseligkeit, pauschale Verur-1721

teilungen und Mobbing von Landwirtinnen, Landwirten und deren Kindern.

1722

• Wir setzen weiterhin auf realistische Darstellungen und Aufklärung über die Leistungen 1723

der Landwirtschaft schon in der Schule sowie den Dialog zwischen Landwirtschaft und 1724

Gesellschaft.

1725

 

1726

Mehr Tierwohl mit finanzieller Wertschätzung verknüpfen

1727

Unsere Tierhaltung gehört – im Hinblick auf die Qualität und Sicherheit ihrer Erzeugnisse, 1728

die Tierwohlstandards sowie die ressourcenschonende Produktion – zu den besten der 1729

Welt. Daran müssen wir festhalten und sie weiter umbauen – für noch mehr Tierwohl.

Seite 50 von 139

1730

• Wir werden Innovationen schnell umsetzen und Investitionen in Tierwohl fördern. Wir 1731

werden ein Tierwohlstall-Förderungsgesetz erlassen, emissionsarme Modellställe entwi-1732

ckeln und unsere Landwirte beim Umbau der Nutztierhaltung auf Grundlage der Emp-1733

fehlungen der Borchert-Kommission unterstützen.

1734

• Mit den Ergebnissen der Borchert-Kommission ist mehr Tierschutz zu haben. Damit wird 1735

der Umbau möglich. Wir werden das Finanzierungsmodell über staatliche Verträge absi-1736

chern und den Landwirten Planungssicherheit gewährleisten.

1737

• Wir werden die Investitionsbereitschaft in der Landwirtschaft stärken und wollen mit ei-1738

nem Bestandsschutz von 15 Jahren bei neuen Stallbauinvestitionen für Verlässlichkeit 1739

und Sicherheit sorgen.

1740

• Wir verbessern kontinuierlich den Tierschutz und gehen mit dem Ausstieg aus dem Kü-1741

kentöten voran.

1742

• Wir brauchen verlässlichere Regelungen für Tiertransporte. Unser Ziel ist, Fleisch statt 1743

lebende Tiere zu transportieren. Auch bei Zuchttieren muss sichergestellt sein, dass aus 1744

der EU kein langer Tiertransport in Drittstaaten genehmigt wird, bei dem die Einhaltung 1745

der Tierschutzvorgaben nicht absolut sichergestellt ist. Wir wollen Zuchttiertransporte 1746

so schnell wie möglich ganz durch den Export von Zuchtmaterial ersetzen. Tierschutz 1747

darf nicht an EU-Grenzen Halt machen.

1748

• Um unsere Weidetierhaltung zu sichern, setzen wir uns dafür ein, dass der strenge 1749

Schutzstatus des Wolfs im europäischen Naturschutzrecht überprüft und angepasst 1750

wird, da der günstige Erhaltungszustand der Wolfspopulation in einer Reihe von Bundes-1751

ländern schon erreicht ist. In diesen Bundesländern soll die Option für ein aktives Wolfs-1752

management eröffnet werden, das die Wolfspopulation langfristig sichert, aber das An-1753

wachsen der Population auf ein insgesamt akzeptables Niveau einreguliert.

1754

 

1755

Mit neuen Techniken ökologisch produktiver wirtschaften

1756

Digitalisierung und neue molekularbiologische Züchtungstechnologien können die Land-1757

wirtschaft umweltfreundlicher und wettbewerbsfähiger machen, Ernten stabil halten bei 1758

weniger Pflanzenschutzmitteleinsatz und geringerem Wasserverbrauch im Klimawandel. Es 1759

geht auch um unsere Verantwortung in der Welt.

1760

• Wir wollen einen verantwortungsvollen, auf klaren Regeln basierenden Einsatz der 1761

neuen Züchtungstechnologien ermöglichen. Wir setzen uns deshalb für eine Moderni-1762

sierung des europäischen Rechtsrahmens ein.

1763

• Die Digitalisierung der Landwirtschaft werden wir weiter fördern und dabei sicherstel-1764

len, dass Betriebe aller Größen davon profitieren können. Die Forschungsergebnisse aus 1765

den Experimentierfeldern „Smart Farming“ sollen schnell und breit in der Praxis ankom-1766

men.

1767

• Wir arbeiten mit Nachdruck an einer leistungsfähigen Dateninfrastruktur auf der gesam-1768

ten Fläche, werden Open-Data-Lösungen schaffen und eine staatliche digitale Plattform Seite 51 von 139

1769

für öffentliche Agrardaten aufbauen, um der Landwirtschaft Zugang zu den von ihnen 1770

benötigten öffentlichen Daten zu gewährleisten.

1771

• Auch werden wir den Agrardatenraum in GAIA-X entwickeln. Ziel ist es, die Interopera-1772

bilität von Daten der Landmaschinen herstellerübergreifend zu ermöglichen, damit 1773

Landwirte ihre Prozesse optimieren können. Wir wollen außerdem sicherstellen, dass die 1774

Hoheit über die Daten, die auf den Höfen und Betrieben erhoben werden („digitale Feld-1775

früchte“), beim Landwirt verbleibt.

1776

 

1777

Nachhaltige Landwirtschaft ermöglichen und honorieren

1778

Unser Ziel ist, den Landbau ökologisch verträglich und ökonomisch tragfähig weiterzuent-1779

wickeln – in Kooperation mit der Landwirtschaft und nicht gegen sie. Auf mehr als 10 Pro-1780

zent der Agrarflächen führen Bäuerinnen und Bauern schon heute spezielle Maßnahmen 1781

zum Schutz der Biodiversität aus. Die Landwirtschaft hat zwischen 1990 und 2020 ihren 1782

Ausstoß klimarelevanter Gase um rund 23 Prozent reduziert und damit das Etappenziel für 1783

2020 erfüllt. Gleichzeitig ist die Landwirtschaft – zusammen mit der Forstwirtschaft – der 1784

einzige Sektor, der eine Senke für Treibhausgase sein kann. Die Klimaleistungen und die 1785

Beiträge der Landwirtschaft zum Natur- und Artenschutz müssen bei zukünftigen politi-1786

schen Entscheidungen berücksichtigt und auch honoriert werden. Dabei müssen alle For-1787

men des nachhaltigen Landbaus profitieren – ökologisch wie konventionell.

1788

• Mit der neuen Gemeinsamen Agrarpolitik (GAP) ist ein Systemwechsel erfolgt hin zu 1789

mehr ökologischer Nachhaltigkeit. Uns ist wichtig, dass die GAP gleichzeitig einkom-1790

menswirksam bleibt. Wir werden kleine und mittlere Betriebe mit höheren Direktzahlun-1791

gen für die ersten Hektare angemessen fördern und die Umweltmaßnahmen (Eco-1792

Schemes und Agrarumweltprogramme) attraktiv ausgestalten.

1793

• Den Ökolandbau werden wir weiter verlässlich fördern und die Forschungsförderung 1794

verstärken, insbesondere um die Ertragsunterschiede zum konventionellen Landbau zu 1795

verringern. Die wachsende Nachfrage der Verbraucher soll möglichst mit heimischer 1796

Ware gedeckt werden können, weshalb wir auch die regionalen ökologischen Lebensmit-1797

telhersteller bei der Entwicklung der ländlichen Räume berücksichtigen.

1798

• Unser Ziel ist es, Nachhaltigkeit in der Land- und Forstwirtschaft sichtbar, messbar und 1799

bezahlbar zu machen. So können Landwirte mit Kohlenstoffspeicherung im Boden und 1800

besonders nachhaltigen Bewirtschaftungsformen wie zum Beispiel Agroforstsystemen, 1801

Agri-Photovoltaik, moorverträglicher Landwirtschaft wie Anbau von Torfmoosen und 1802

Paludikulturen auf renaturierten Feuchtflächen, mit heimischen Eiweißpflanzen als Al-1803

ternative zu Importsoja für das Tierfutter oder Rohstoffen für die Bioökonomie, Geld 1804

verdienen.

1805

• Natur-, Klima-, Arten- und Moorschutzleistungen werden wir durch Kooperationen und 1806

Anreize fördern.

Seite 52 von 139

1807

• Wichtig ist uns auch der Schutz der Bienen und Insekten, denn sie sind als Bestäuber 1808

systemrelevant für die Landwirtschaft und die Sicherung unserer Ernährung. Alle gesell-1809

schaftlichen Bereiche, nicht nur die Landwirtschaft, müssen einen Beitrag zum Insekten-1810

schutz leisten.

1811

 

1812

Anpassung der Landwirtschaft im Klimawandel und Risikoabsicherung unterstützen

1813

Die Landwirtschaft, der Garten- und Weinbau sowie die Fischerei sind genauso wie der 1814

Wald vom Klimawandel betroffen. Immer stärker ist sein Einfluss auf die Ernten zu erken-1815

nen. Trockenheit, Spätfröste und Starkregenereignisse nehmen zu. Wir werden die Bran-1816

chen bei der Anpassung begleiten und die Betriebe unterstützen, sich gegen Risiken abzu-1817

sichern.

1818

• Wir werden die Entwicklung angepasster Anbaumethoden im Rahmen der Ackerbaustra-1819

tegie des Bundesministeriums für Ernährung und Landwirtschaft, ressourcenschonende 1820

Bewässerungstechnologien und ein verbessertes Wassermanagement fördern.

1821

• Mit Zuschüssen zu Mehrgefahrenversicherungen werden wir die Betriebe in ihrer Fähig-1822

keit stärken, sich selbst gegen Dürre und andere Klimarisiken abzusichern. Das gilt als 1823

Erstes für unsere Obst-, Gemüse- und Weinbaubetriebe.

1824

• Die Gartenbaubetriebe unterstützen wir insbesondere bei der CO2-Einsparung und bei 1825

der Entwicklung klimafreundlicher Torfersatzprodukte. Marktverzerrungen im Rahmen 1826

der CO2-Bepreisung wollen wir vermeiden.

1827

• Auch die Anpassung der Fischerei im Klimawandel werden wir aktiv begleiten, ihre Wett-1828

bewerbsfähigkeit wie ökologische Nachhaltigkeit stärken und die regionale Erzeugung 1829

von Fisch als klimafreundliches und hochwertiges Nahrungsmittel sichern.

1830

 

1831

Das Unternehmertum Landwirtschaft stärken

1832

Wir wollen einen neuen Aufbruch in der Landwirtschaft. Landwirtinnen und Landwirte sol-1833

len ermutigt werden, junge Menschen ihre Chance in grünen Berufen sehen.

1834

• Wir werden die Junglandwirte-Prämie erhöhen und die Vielfalt der Landwirtschaft als 1835

Berufsfeld in einem Ideenwettbewerb sichtbar machen. Dazu gehören verschiedene For-1836

men des Landbaus, über Landtourismus, die Erzeugung und Vermarktung regionaler 1837

Spezialitäten bis hin zu neuen Herstellungsverfahren, wie Insektenfarming.

1838

• Wir werden günstige Rahmenbedingungen für Agrar-Startups schaffen und streben die 1839

Einrichtung eines Agri-FoodTech-Wagniskapitalfonds an.

1840

• Bei neuen Anforderungen an die Landwirtschaft wollen wir dafür sorgen, dass an anderer 1841

Stelle bestehende Anforderungen überprüft werden.

1842

 

 

Seite 53 von 139

1843

Gute Ernährung einfach machen

1844

Essen und Trinken sind Grundbedürfnisse und zugleich ein wichtiges gesellschaftliches Ele-1845

ment in unserem täglichen Miteinander. Wir wollen, dass allen auch in der heutigen Arbeits-1846

, Medien- und Konsumwelt ein möglichst gesundes und nachhaltiges Leben gelingt. Dafür 1847

braucht es Ernährungskompetenz und Motivation sowie gut zugängliche, passende Ange-1848

bote.

1849

• Wir werden gute Rahmenbedingungen für eine gesundheitsförderliche, ausgewogene 1850

und nachhaltige Ernährung schaffen. Es soll für Jede und Jeden beim Einkauf und beim 1851

Essen außer Haus einfach möglich sein, eine gesunde Wahl zu treffen.

1852

• Kinder bedürfen eines besonderen Schutzes. Die Weichen für das Essverhalten werden 1853

in frühen Jahren gelegt. Ernährungsbildung, Sport sowie Zugang zu gutem Kita- und 1854

Schulessen sollen für jedes Kind gewährleistet sein.

1855

• Es sind uns schon – auch im Dialog mit der Wirtschaft – wichtige Schritte gelungen, um 1856

eine gesündere Ernährung einfacher zu machen. So werden zum Beispiel Zucker, Fett 1857

und Salz in verarbeiteten Lebensmitteln reduziert. Das gilt insbesondere für an Kinder 1858

gerichtete Produkte.

1859

• Mit dem Nutri-Score wurde eine erweiterte visuelle Nährwertkennzeichnung in 1860

Deutschland eingeführt. Das national Erreichte wollen wir nun auch auf europäischer 1861

Ebene umsetzen.

1862

• Unsere in Deutschland breit aufgestellte ernährungswissenschaftliche Forschung wer-1863

den wir weiter ausbauen. Sie soll noch aktiver Ernährungswissen aufarbeiten und in die 1864

Breite kommunizieren. Unser Ziel ist, ernährungsmitbedingten Volkskrankheiten wie 1865

starkes Übergewicht, Diabetes oder Krebs noch besser vorbeugen zu können.

1866

 

1867

Mehr Transparenz für nachhaltige Erzeugung beim Lebensmittelkauf herstellen

1868

Wir wollen mehr Transparenz beim Lebensmitteleinkauf. Die Verbraucherinnen und Ver-1869

braucher sollen klar erkennen können, was in den Lebensmitteln steckt, woher sie kommen 1870

und wie sie erzeugt wurden. So bringen wir sie auch wieder näher mit der Landwirtschaft 1871

zusammen.

1872

• Unser Ziel ist eine verpflichtende europäische Haltungs-/Tierwohlkennzeichnung und 1873

auch auf EU-Ebene eine aussagekräftige, für die Verbraucherinnen und Verbraucher bes-1874

ser erkennbare Herkunftskennzeichnung für mehr Lebensmittel.

1875

• Immer mehr Menschen legen Wert auf regionale Lebensmittel. Sie sind für viele ein 1876

Stück Heimat. Wer sich mit regionalen, saisonalen Lebensmitteln ernährt, tut nicht nur 1877

etwas für die Umwelt, sondern unterstützt auch die heimische Landwirtschaft und stärkt 1878

regionale Wirtschaftskreisläufe. Wir wollen deshalb, dass Regionalität besser sichtbar 1879

wird. Wir werden das sogenannte Regionalfenster als Kennzeichnung weiterentwickeln 1880

und mehr Klarheit bei regionalen Lebensmitteln schaffen.

Seite 54 von 139

1881

• Zudem wollen wir ergänzend zum Öko-Siegel ein Nachhaltigkeitssiegel für konventio-1882

nelle Agrarprodukte entwickeln.

1883

 

1884

Unsere nachhaltige Lebensmittelerzeugung sichtbarer machen und international absichern

1885

• Zusammen mit der Branche werden wir eine Nationale Lebensmittel-Agentur auf den 1886

Weg bringen. Sie soll für heimische regionale Produkte, unsere hohen Standards und un-1887

sere Art zu produzieren, im In- und Ausland werben. So wollen wir mehr Wertschätzung 1888

für unsere Lebensmittel und unsere Landwirtschaft erreichen.

1889

• Marktpreise müssen fair sein und den Erzeugern ein auskömmliches Einkommen ermög-1890

lichen. Die Markt- und Produktionsrisiken dürfen nicht beim Erzeuger alleine liegen. Wir 1891

wollen eine faire Lieferkette mit Marktverantwortung von Verarbeitungsebene und Han-1892

del fördern.

1893

• Begleitend brauchen wir faire Handelsabkommen, die die hohen Standards der EU-Land-1894

wirtschaft respektieren und schützen. Für Importe in den Binnenmarkt müssen die glei-1895

chen Produktstandards gelten wie für heimische Lebensmittel. In Handelsabkommen 1896

soll zunehmend die Prozessqualität einbezogen werden: das heißt, die Umwelt-, Tier-1897

wohl- und Arbeitsschutzstandards bei der Lebensmittelerzeugung.

1898

 

1899

Lebensmittelverschwendung bekämpfen

1900

Unsere Nahrungsmittel sind unsere Lebensgrundlage. Sie dürfen aus ethischen, ökologi-1901

schen und auch wirtschaftlichen Gründen nicht achtlos verschwendet werden. 12 Millionen 1902

Tonnen weggeworfene Lebensmittel pro Jahr – 75 Kilogramm pro Person sind entschieden 1903

zu viel.

1904

• Unser klares Ziel ist die Halbierung bzw. deutliche Reduzierung der Lebensmittelver-1905

schwendung bis 2030.

1906

• Der Nationalen Strategie zur Reduzierung der Lebensmittelverschwendung werden wir 1907

noch mehr Nachdruck verleihen und alle Beteiligten, insbesondere auch junge Men-1908

schen, sensibilisieren.

1909

• Wir werden Lebensmittelspenden an die Tafeln, soziale Einrichtungen und Organisatio-1910

nen, die Lebensmittel retten, vereinfachen – soweit nötig auch durch gesetzliche Ände-1911

rungen.

1912

• Wir werden die Anpassung des Mindesthaltbarkeitsdatums prüfen und die Entwicklung 1913

von Apps und anderen digitalen Hilfsmitteln, zum Beispiel zur automatischen Preissen-1914

kung für Produkte nahe am Ablaufdatum, und innovative Verpackungslösungen, die zum 1915

Beispiel die Genießbarkeit anzeigen, fördern.

1916

 

Seite 55 von 139

1917

3.8. Modernes Recht für mündige Verbraucherinnen und Verbraucher 1918

Unser Leitbild für das Verbraucherschutzrecht sind mündige Verbraucherinnen und Ver-1919

braucher. Wir wollen nicht, dass sie bevormundet werden, sondern trauen ihnen zu, eigen-1920

verantwortlich und mündig zu entscheiden. Aufklärung und Information stehen für uns da-1921

bei im Vordergrund. Verbraucherschutz ist eine Querschnittsaufgabe. Wir schaffen einen 1922

klaren Rechtsrahmen und faire Regelungen: ob es um das Bauen und Wohnen, um das Rei-1923

sen, um Geldanlagen, Gesundheitsdienstleistungen oder um die Ernährung geht. So stärken 1924

wir das Verbrauchervertrauen und erreichen mehr Übersichtlichkeit bei Regulierung und 1925

Normklarheit.

1926

 

1927

Verbraucherrecht vereinfachen

1928

Verbraucherinnen und Verbraucher müssen auf einfachem Wege zu ihrem guten Recht 1929

kommen – auch mithilfe der Verbraucherschutzorganisationen. Daher werden wir die Ver-1930

braucherzentrale Bundesverband und die Stiftung Warentest weiter verlässlich fördern.

1931

• Im Verbraucherrecht sind Regelungen oft zu kompliziert, sodass sie ihre Wirkung verfeh-1932

len. Die Datenschutz-Grundverordnung zum Beispiel ermöglicht zwar einen souveränen 1933

Umgang mit persönlichen Daten, der einzelne Bürger kann dies jedoch nur mit viel Auf-1934

wand nutzen – etwa bei Einverständniserklärungen für die Daten- oder Cookie-Nutzung.

1935

Deshalb werden wir das gesamte bürgerliche Vertragsrecht, insbesondere den elektro-1936

nischen Rechtsverkehr, modernisieren.

1937

• Wir werden die Verbraucherschlichtung auf weitere Branchen mit passgenauen bran-1938

chenspezifischen Lösungen ausweiten. Sie ist ein geeignetes Instrument, um Rechts-1939

streitigkeiten zu vermeiden.

1940

• Verbraucherinnen und Verbraucher sollen Schäden mit sehr geringer Schadenshöhe 1941

(sog. Streuschäden) ersetzt bekommen, deren gerichtliche Verfolgung sich nicht lohnt.

1942

• Bei stornierten Flügen und Reisen kommen Verbraucherinnen und Verbraucher nur 1943

schwer an ihr Geld. Wir wollen deshalb im Reisevertragsrecht die Zahlungsfristen und 1944

insbesondere die Vorausleistungen neu regeln.

1945

 

1946

Digitale Instrumente für Verbraucherrechte nutzen

1947

Die Digitalisierung soll Verbraucherinnen und Verbrauchern das Leben einfacher machen: 1948

sei es bei Entschädigungen für Verspätungen, bei Vertragskündigungen oder Rückerstat-1949

tungen.

1950

• Nach dem Vorbild der Fluggastrechte-App wollen wir für viele Bereiche bundesweit ein-1951

setzbare Apps und digitale Hilfsmittel entwickeln lassen. Damit können sie schnell rele-1952

vante Informationen und Serviceleistungen erhalten, um ihre Rechte durchzusetzen.

Seite 56 von 139

1953

• Wir wollen einen Rechtsrahmen für sogenannte smart contracts schaffen. Beim Eintritt 1954

eines Schadensfalls, zum Beispiel bei einer Flugverspätung, wird automatisiert die Ent-1955

schädigung auf das Kundenkonto überwiesen – schnell, einfach und ohne jedes Formu-1956

lar.

1957

 

1958

Für Sicherheit in der digitalen Welt sorgen

1959

• Verbraucherinnen und Verbraucher sollen die Vorteile der digitalen Welt sicher nutzen 1960

können. Mit Einführung eines einheitlichen IT-Sicherheitskennzeichens, das die IT-Si-1961

cherheit von Produkten für Verbraucher sichtbar macht, ist IT-Produktsicherheit zu ei-1962

nem echten Verkaufsargument geworden. Auf diesem Weg wollen wir weitergehen.

1963

• Wir wollen einen klaren Rechtrahmen auf europäischer wie auf Bundesebene für digitale 1964

Plattformen schaffen. Haftung, Sicherheit, Gewährleistung, Software-Updates, Nutzer-1965

bewertungen und Produktrankings sind hierfür wichtige Gesichtspunkte.

1966

• Verbraucherinnen und Verbraucher sollen ohne Bedenken Online-Geschäfte tätigen, 1967

Steuern zahlen oder sich bei Ämtern anmelden können. Dafür wollen wir eine sichere 1968

digitale europäische Identität schaffen. So entsteht eine Alternative zu den Plattforman-1969

meldungen und Identifikationsangeboten der großen Anbieter wie Google, Apple, Face-1970

book oder Amazon. Wir wollen ein Identitätsdiebstahlsregister einführen, bei dem Ver-1971

sandhändler und Inkasso-Dienstleister vor einem Tätigwerden die Bestelladressen ab-1972

gleichen.

1973

• Wir sorgen für mehr Datentransparenz bei digitalen Angeboten. Wir wollen einfache, 1974

verständliche Allgemeine Geschäftsbedingungen. Verbraucherinnen und Verbraucher 1975

sollen wissen, was mit ihren Daten geschieht, wenn sie damit vermeintlich „kostenlose“

1976

Dienste bezahlen und aktiv über die Nutzung ihrer Daten entscheiden. So wollen wir zum 1977

Beispiel volle Transparenz darüber herstellen, welche Daten im Rahmen von SmartHome 1978

und digitalen Assistenten erhoben und wie sie verwendet werden. Die Datenkompetenz 1979

in der Verbraucherbildung und -aufklärung wollen wir weiter stärken.

1980

• Wir wollen allen ermöglichen, schnell und sicher im Internet unterwegs zu sein und 1981

gleichzeitig eine mündige Entscheidung über die Nutzung der eigenen Daten zu treffen.

1982

Dafür müssen Einverständniserklärungen und Cookie-Einwilligungen einfacher und kla-1983

rer erteilt werden können. Neue Möglichkeiten eröffnet ein freiwilliger Datenspende-1984

pass.

1985

• Wir werden den Wechsel zwischen Anbietern erleichtern, indem Schnittstellen und tech-1986

nische Standards für die Datenmitnahme geschaffen werden. Wir wollen die Interopera-1987

bilität von Messenger-Diensten verbessern.

1988

 

 

Seite 57 von 139

1989

4. Neue Fairness und soziale Sicherheit – für den gesellschaftlichen Zusam-1990

menhalt

1991

 

1992

Unser Unions-Versprechen: Wir arbeiten dafür, dass wir eine Gesellschaft bleiben, die zusam-1993

menhält: Junge und Ältere, Starke und Schwächere. Unser christliches Menschenbild gibt uns 1994

hierfür den Kompass an die Hand: Individuelle Freiheit und gemeinschaftliche Verantwortung 1995

sind keine Gegensätze, sondern sie bedingen einander. Mit den Prinzipien der Sozialen Markt-1996

wirtschaft sorgen wir dafür, dass jeder Mensch in unserem Land eine gute medizinische und 1997

pflegerische Versorgung erhält und dass jedem geholfen wird, der Hilfe braucht. Wir sorgen für 1998

eine verlässliche Rente und einen Neustart bei der privaten Vorsorge, damit sie sich mehr lohnt.

1999

Die Pandemie hat gezeigt, wie stark unser Gesundheitssystem ist und wie wichtig vor allem die 2000

Frauen und Männer sind, die in den Krankenhäusern, Pflegeheimen und vielen anderen Orten 2001

ihren mitmenschlichen Dienst tun. Wir haben aber auch gesehen, dass wir mehr tun müssen, 2002

damit unser Gesundheitswesen auch nach der Krise weiter zu den besten der Welt zählt. Ange-2003

sichts der demografischen Entwicklung ist es eine große Herausforderung, unsere sozialen Si-2004

cherungssysteme zukunftssicher zu machen und die unterschiedlichen sozialen Angebote besser 2005

miteinander zu verbinden, um Hilfen wie aus einer Hand anzubieten.

2006

Mit unserem Modernisierungsjahrzehnt sorgen wir dafür, dass Deutschland auch in Zukunft ei-2007

nes der verlässlichsten und stabilsten Sozialversicherungssysteme der Welt hat. Dabei gilt das 2008

Prinzip der Sozialen Marktwirtschaft, dass der Gemeinschaft, auch den Schwächeren, ein Leben 2009

in Würde ermöglicht. Das ist gelebte Solidarität, und damit unterscheiden wir uns von vielen 2010

anderen Nationen auf der Welt. Damit sich jeder, unabhängig von seinem früheren Einkommen, 2011

darauf verlassen kann, dass er gut versorgt wird, wenn er einen Unfall hat, wenn er krank, pfle-2012

gebedürftig, arbeitslos oder erwerbsunfähig wird.

2013

 

2014

4.1. Finanzielle Sicherheit im Alter

2015

Die Rente ist mehr als ein Einkommen im Alter. Sie ist Lohn für Lebensleistung. Für uns 2016

gelten dabei drei klare Prinzipien. Erstens: Leistung muss ich lohnen. Wer ein Leben lang 2017

gearbeitet oder Kinder erzogen hat, muss mehr haben als jemand, der nicht gearbeitet hat, 2018

und er sollte nicht auf Sozialhilfe angewiesen sein. Deshalb haben wir mit der Grundrente 2019

dafür gesorgt, dass kleine Renten nach langer Erwerbstätigkeit bedarfsgerecht aufgestockt 2020

werden. Zweitens: Rente muss ein Leben in Würde ermöglichen. Sie muss immer mehr sein 2021

als nur Armutsbekämpfung. Und drittens: Die Rente muss nachhaltig, sicher und solide fi-2022

nanziert sein.

2023

 

2024

Vertrauen und Verlässlichkeit sichern

2025

Die beste Rentenpolitik ist eine gute Wirtschaftspolitik. Denn je mehr Menschen sozialver-2026

sicherungspflichtig arbeiten, desto besser ist es für die Rente. Das haben die letzten zehn 2027

Jahre gezeigt, die im ganzen Land zu deutlichen Rentensteigerungen geführt haben.

Seite 58 von 139

2028

• Wir werden die Rentnerinnen und Rentner weiterhin verlässlich an der allgemeinen Ein-2029

kommensentwicklung beteiligen.

2030

• Um das Vertrauen in die Altersvorsorge weiter zu stärken und Rentnerinnen und Rent-2031

ner zu entlasten, werden wir eine Doppelbesteuerung von Renten verhindern und da-2032

her die Vorgaben des Bundesfinanzhofs schnellstmöglich umsetzen.

2033

• Freiwillige Beiträge in der Gesetzlichen Rentenversicherung in jeglicher gewünschten 2034

Höhe werden wir zulassen, maximal bis zur jeweiligen Beitragsbemessungsgrenze.

2035

 

2036

Sozialbeirat zum Alterssicherungsbeirat weiterentwickeln

2037

Wir stehen für eine zukunftsfeste Alterssicherung auf drei Säulen: der gesetzlichen Renten-2038

versicherung, der betrieblichen und der privaten Vorsorge. Die gesetzliche Rentenversiche-2039

rung wird dabei für die meisten Menschen die zentrale Säule bleiben. Wir wollen ein Ren-2040

tenrecht, das Generationengerechtigkeit sichert und Leistungen sowie Lasten fair und 2041

nachvollziehbar verteilt. Um das Vertrauen der aktiven Generation von heute in das System 2042

der gesetzlichen Rentenversicherung von morgen zu stärken, brauchen wir eine klare Per-2043

spektive, die auch für die nächsten 30 Jahre trägt.

2044

• Wir werden, wie von der Rentenkommission der Bundesregierung unter Beteiligung der 2045

Sozialpartner und der Wissenschaft vorgeschlagen, den bisher nur für die gesetzliche 2046

Rentenversicherung zuständigen Sozialbeirat zu einem Alterssicherungsbeirat weiter-2047

entwickeln.

2048

• Der Alterssicherungsbeirat soll alle drei Säulen der Altersvorsorge in den Blick nehmen 2049

und eine Empfehlung für die Festlegung der verbindlichen und perspektivischen Halteli-2050

nien bei Rentenniveau und Beitragssatz abgeben.

2051

• Dabei steht die Union für Verlässlichkeit: Wir behalten das Vorsorgeniveau im Auge und 2052

schützen die Beitragszahlerinnen und Beitragszahler vor Überforderung.

2053

 

2054

Beschäftigte besser schützen, Leistungen anerkennen

2055

Unsere Lebenserwartung wächst erfreulicherweise immer weiter. Das Renteneintrittsalter 2056

steigt daher in kleinen Schritten auf 67 Jahre im Jahr 2030 an. Wir wollen den Menschen 2057

helfen, das tatsächliche Regelrenteneintrittsalter zu erreichen.

2058

• Wir wollen die medizinische und berufliche Rehabilitation als wichtige Instrumente stär-2059

ken und die Leistungsfähigkeit der Versicherten – nach Krankheit oder Unfall – wieder-2060

herstellen. Die Träger in den gesetzlichen Sozialversicherungszweigen müssen daher die 2061

Zusammenarbeit – zum Beispiel in regionalen, trägerübergreifenden Reha-Kompetenz-2062

Zentren – noch mehr intensivieren, um die Zusammenarbeit und das hohe Niveau der 2063

Rehabilitation weiter zu verbessern.

2064

• Ein Unfall oder eine schwere Krankheit kann jeden treffen. Daher haben wir in den letz-2065

ten Jahren die Erwerbsminderungsrente deutlich verbessert. Mit Blick auf die Menschen, 2066

die bereits eine Erwerbsminderungsrente beziehen, wollen wir, dass diese beim Wechsel Seite 59 von 139

2067

von der Erwerbsminderungsrente in die Altersrente auch von den Verbesserungen der 2068

Jahre 2014 und 2019 profitieren.

2069

 

2070

Selbstständige besser absichern

2071

Um den sozialen Schutz von Selbstständigen zu verbessern, wollen wir eine Altersvorsor-2072

gepflicht für alle Selbstständigen einführen, die nicht bereits anderweitig abgesichert sind.

2073

• Selbstständige sollen zwischen der gesetzlichen Rentenversicherung und anderen insol-2074

venzsicheren und zugriffsgeschützten Vorsorgearten wählen können. Wir werden Lö-2075

sungen entwickeln, die auf bereits heute selbstständig Tätige Rücksicht nehmen und 2076

Selbstständige in der Existenzgründungsphase nicht überfordern.

2077

• An den berufsständischen Versorgungswerken halten wir fest.

2078

 

2079

Vor Armut im Alter besser schützen

2080

Wir werden verdecke Altersarmut bekämpfen.

2081

• Wir wollen, dass Bezieher staatlicher Transferleistungen im Rentenalter grundsätzlich in 2082

ihrem Wohneigentum bleiben und eine angemessene Notlagenreserve als Anerkennung 2083

der Lebensleistung behalten können. Dafür sollen die gesetzlichen Regelungen zur Ver-2084

mögensverwertung und zum Schonvermögen in der Grundsicherung im Alter angepasst 2085

werden.

2086

• Wir wollen Aussiedler und Spätaussiedler sowie jüdische Kontingentflüchtlinge besser-2087

stellen und rentenrechtliche Benachteiligungen beseitigen.

2088

 

2089

Betriebliche Altersvorsorge stärken

2090

Wir wollen, dass noch mehr Menschen betrieblich für ihr Alter vorsorgen und damit an der 2091

guten wirtschaftlichen Entwicklung unseres Landes teilhaben. Eine auskömmliche Alterssi-2092

cherung hängt auch von der zusätzlichen Vorsorge ab.

2093

• Wir werden die Mitnahme der Ansprüche aus einer betrieblichen Altersvorsorge beim 2094

Jobwechsel weiter verbessern.

2095

• Mit dem Betriebsrentenstärkungsgesetz und der stärkeren Förderung von Geringverdie-2096

nern haben wir deutliche Impulse gesetzt, damit noch mehr Menschen die betriebliche 2097

Altersversorgung nutzen. Wir wollen die Wirkungen und die Voraussetzungen für das 2098

Sozialpartnermodell evaluieren und mögliche Hindernisse bei der weiteren Verbreitung 2099

abbauen.

2100

• Gerade mit Blick auf Geringverdiener wollen wir ein Konzept einer „Betrieblichen Al-2101

tersvorsorge für alle“ entwickeln, um diese wichtige Säule der Altersvorsorge weiter zu 2102

stärken und noch attraktiver zu machen.

2103

 

 

Seite 60 von 139

2104

Private Vorsorge neugestalten

2105

Bei der privaten, staatlich geförderten Altersvorsorge brauchen wir einen Neustart. Wir 2106

wollen sie effizienter, transparenter und dadurch attraktiver und einfacher machen.

2107

• Wir werden Kriterien für ein Standardvorsorgeprodukt festlegen. Dieses Produkt ist ver-2108

pflichtend für alle Arbeitnehmerinnen und Arbeitnehmer, es sei denn, sie widersprechen 2109

der Einbeziehung (Opt-Out).

2110

• Das Standardprodukt soll ohne Abschlusskosten und mit möglichst niedrigen Verwal-2111

tungskosten auskommen.

2112

• Dabei soll es eine attraktive und unbürokratische Förderung durch den Staat geben.

2113

• Neben Produkten mit einer Leistungsgarantie sollen auch Produkte ohne Leistungsga-2114

rantie angeboten werden.

2115

• Wir verbinden mit diesen Maßnahmen die Erwartung, dass mehr Menschen privat vor-2116

sorgen. Sollte sich diese Erwartung nicht erfüllen, werden wir das Produktportfolio um 2117

ein staatlich organisiertes Standardvorsorgeprodukt erweitern und prüfen, ob wir zu ei-2118

nem stärkeren Maß an Verbindlichkeit kommen müssen.

2119

 

2120

Generationenvertrag weiterdenken

2121

Wir wollen ein Konzept entwickeln, um in Deutschland eine neue Form der kapitalgedeck-2122

ten Altersvorsorge zu etablieren.

2123

• Dafür kann eine Generationenrente für eine Altersvorsorge von Geburt an ein guter 2124

Baustein sein. Wir werden prüfen, wie man die Generationenrente mit einem staatli-2125

chen Monatsbeitrag zur Anlage in einem Pensionsfonds - mit Schutz vor staatlichem 2126

Zugriff – ausgestalten kann. Unser Ziel ist es, mit einem attraktiven Instrumentenmix, 2127

Altersarmut wirksam zu vermeiden.

2128

 

2129

4.2. Soziale Sicherheit in allen Lebenslagen

2130

Prinzip des Forderns und Förderns erhalten

2131

Soziale Sicherheit in Deutschland soll nicht nur Armut verhindern, sondern jedem ein Leben 2132

in Würde ermöglichen. Dazu stehen wir. Ein bedingungsloses Grundeinkommen wird es mit 2133

uns aber nicht geben.

2134

• Wir starten eine Offensive zur beruflichen Aus- und Weiterbildung in der Grundsiche-2135

rung für Arbeitsuchende, um zum Beispiel Sprachkompetenzen und Ausbildungsfähig-2136

keit zu verbessern. Wir werden jedem ein Angebot machen, damit die Betroffenen wie-2137

der für sich selbst und andere sorgen können. Wir stehen zum Fördern und Fordern. Des-2138

halb werden wir auch die Sanktionsmechanismen im SGB II beibehalten.

2139

• Damit mehr geringqualifizierte Arbeitslose an einer Aus- und Weiterbildungsmaßnahme 2140

teilnehmen, werden wir die Rahmenbedingungen verbessern.

Seite 61 von 139

2141

• Die Anrechnung von Einkommen im SGB II wollen wir neu ausgestalten, um damit mehr 2142

Anreize zur Aufnahme einer Beschäftigung zu setzen und einen schrittweisen Ausstieg 2143

aus Hartz IV zu fördern. Ziel muss sein, möglichst viele Menschen aus Hartz IV wieder in 2144

Arbeit zu bringen.

2145

• Hinzuverdienstregeln für Jugendliche und junge Erwachsene bis zum 21. Lebensjahr und 2146

während der Ausbildung zum ersten berufsqualifizierenden Abschluss in Bedarfsge-2147

meinschaften werden wir im Rahmen des Jugendschutzes ebenfalls deutlich ausweiten.

2148

• Wir werden das SGB-II-Leistungsrecht so vereinfachen, dass sich damit der Verwaltungs-2149

aufwand und die Zahl der Gerichtsverfahren deutlich reduziert. Die dadurch gewonne-2150

nen Personalressourcen werden wir für eine stärkere Betreuung der Leistungsempfänger 2151

zur Verfügung stellen.

2152

• Insbesondere Personen, die auf ein langes Arbeitsleben zurückschauen können, empfin-2153

den einen Wohnungswechsel bei Beantragung von Grundsicherungsleistungen als zu-2154

tiefst ungerecht. Deshalb wollen wir vertraute Wohnsituationen schützen.

2155

 

2156

Inklusion im Alltag leben

2157

Menschen mit Behinderungen haben das Recht auf eine barrierefreie Gestaltung ihrer Um-2158

welt, damit sie am alltäglichen Leben in allen Bereichen ganz selbstverständlich teilhaben 2159

und sich einbringen können.

2160

• Wir wollen erreichen, dass Menschen mit Einschränkungen, ältere Menschen oder zeit-2161

weise Erkrankte das tun können, was für alle selbstverständlich ist: den ÖPNV benutzen, 2162

einen Geldautomaten aufsuchen oder die Nachrichtensendung verfolgen. Dafür werden 2163

wir das Behindertengleichstellungsgesetz weiterentwickeln.

2164

• Unser Ziel ist ein inklusiver erster Arbeitsmarkt. Das Potenzial von Fachkräften mit Be-2165

hinderungen bleibt vielfach noch immer ungenutzt. Gemeinsam mit den Schwerbehin-2166

dertenvertretungen wollen wir das betriebliche Eingliederungsmanagement stärken so-2167

wie Frühwarnsysteme und effiziente Präventivmaßnahmen ausbauen.

2168

• Werkstätten für behinderte Menschen sind wichtig, weil sie dort am Arbeitsleben teil-2169

nehmen können. Für ein zukunftsfähiges Entgeltsystem werden wir die Berechnung des 2170

Werkstattlohns neu regeln und gleichzeitig die derzeitige Deckelung des Arbeitsförde-2171

rungsgeldes aufheben. Damit haben die Werkstattbeschäftigten mehr Geld in der Tasche 2172

und die Werkstätten werden finanziell entlastet.

2173

• Wir setzen uns dafür ein, dass jeder Mensch ein Recht auf digitalen Zugang hat, auch 2174

Menschen, die in Einrichtungen leben. Eine barrierefreie Medienvielfalt in Deutschland 2175

spielt für uns eine zentrale Rolle. Menschen mit Behinderungen sollen ihr Recht auf in-2176

formatorische Selbstbestimmung wahrnehmen können.

2177

 

Seite 62 von 139

2178

4.3. Leistungsfähiges Gesundheitswesen

2179

Unser Leitbild ist eine medizinische und pflegerische Kultur, die dem ganzen Menschen 2180

dient. In der Corona-Pandemie hat unser Gesundheitssystem gezeigt, welche Stärken es hat 2181

und an welchen Schwächen wir arbeiten müssen. In einem zukunftsfähigen Gesundheits-2182

wesen setzen wir deshalb auf stärkere vernetzte Zusammenarbeit der einzelnen Akteure 2183

und nutzen das Potenzial der Digitalisierung. Zur Finanzierung der gesetzlichen Kranken-2184

versicherung setzen wir weiter auf einkommensabhängige paritätische Beiträge, Eigenbe-2185

teiligung und einen Steueranteil für versicherungsfremde Leistungen (wie beispielsweise in 2186

der Pandemiebekämpfung), der dynamisiert und an die tatsächlichen Kosten der versiche-2187

rungsfremden Leistungen und deren Entwicklung gekoppelt wird.

2188

 

2189

Gesundheitswesen zukunftsfähig gestalten

2190

Eine umfassende Versorgung der Bürgerinnen und Bürger und den Erhalt unseres sehr gu-2191

ten Gesundheitssystems erreichen wir mit der bewährten Selbstverwaltung, der freien 2192

Arzt- und Therapiewahl sowie mit dem Zusammenspiel von gesetzlichen und privaten Kran-2193

kenversicherungen. Eine Einheitsversicherung und Schritte dahin lehnen wir ab.

2194

• Wir werden Bürokratie reduzieren, damit Ärztinnen und Ärzte sowie Pflegepersonal 2195

mehr Zeit für Patientinnen und Patienten haben und Gesundheits- und Pflegeberufe at-2196

traktiver werden.

2197

• Mit dem Fahrplan für die Einführung einer elektronischen Patientenakte haben wir die 2198

jahrelange Stagnation der Digitalisierung im Gesundheitswesen überwunden. Wir wer-2199

den an die e-Health-Strategie den Prozess „Digitale Gesundheit 2025“ anschließen und 2200

diesen zu einer ressortübergreifenden eHealth-Roadmap „Digitale Gesundheit 2030“

2201

weiterentwickeln, die konkrete Handlungsempfehlungen für die digitalisierte Gesund-2202

heitsversorgung der Zukunft bis zum Jahr 2030 vorgibt. Die Patientinnen und Patienten 2203

der Zukunft werden – unter Wahrung des Schutzes ihrer Daten – ihre gesamte Kranken-2204

geschichte an einem Ort speichern und Ärzte und andere Leistungserbringer darauf zu-2205

greifen lassen können.

2206

• Digitale Versorgungsketten sollen Informationslücken zwischen Praxis und Krankenhaus 2207

beseitigen. Dabei spielt die Erstattungsfähigkeit digitaler Gesundheitsanwendungen 2208

eine zentrale Rolle.

2209

• Wir wollen weitere 500 Millionen Euro für eine Innovationsoffensive für Robotik und Di-2210

gitalisierung in der Pflege bereitstellen. Die Digitalisierung, der Einsatz von Smart-2211

Home-Technologien sowie der Einsatz modernster Roboter sind eine enorme Chance für 2212

eine hohe Lebensqualität im Alter und die Entlastung der Pflegekräfte.

2213

 

2214

Krankenhäuser und ambulante Versorgung stärken

2215

Deutschlands Krankenhäuser sind in Stadt und Land ein wichtiger Anker der medizinischen 2216

Versorgung. Im Einklang mit Rehabilitationseinrichtungen, niedergelassenen Ärzten und Seite 63 von 139

2217

Pflegeeinrichtungen haben sie bei der Bewältigung der Pandemie den Menschen in unse-2218

rem Land einen großen Dienst erwiesen. Die Krankenhäuser sind zusammen mit der leis-2219

tungsfähigen ambulanten Versorgung das Rückgrat unseres Gesundheitswesens.

2220

• Wir wollen, dass die Ziele einer bedarfsgerechten und flächendeckenden Grund- und Re-2221

gelversorgung in der Krankenhausplanung und insbesondere in der Krankenhausfinan-2222

zierung wesentlich stärker berücksichtigt werden, gerade mit Blick auf den ländlichen 2223

Raum.

2224

• Gleichzeitig wollen wir im Interesse der Patientensicherheit für komplexe Behandlungen 2225

eine stärkere Bündelung entsprechender klinischer Angebote.

2226

• Die mit dem Krankenhauszukunftsgesetz in der Pandemie begonnene Offensive des 2227

Bundes für mehr digitale Investitionen in den Krankenhäusern wollen wir weiterführen 2228

und verstärken. Mit dem virtuellen Krankenhaus wollen wir medizinisches Spezialwissen 2229

überall im Land gleichermaßen verfügbar machen. Televisiten und digitale fachliche Be-2230

ratungen zwischen mehreren Ärzten eröffnen neue Perspektiven zur besseren Patien-2231

tenversorgung vor Ort und können Erkrankten eine Verlegung ersparen.

2232

• Wir sorgen dafür, dass alle Bürgerinnen und Bürger einen digitalen, wohnortnahen und 2233

möglichst barrierefreien Weg, zum Beispiel zur Haus-, Fach-, Zahnarzt- und Notfallver-2234

sorgung, zu Apotheken, Hebammen, Physiotherapeuten, Gesundheitshandwerken und 2235

Sanitätshäusern haben. Wir setzen uns verstärkt für den flächendeckenden Ausbau des 2236

psychotherapeutischen Behandlungsangebots für Kinder und Jugendliche ein.

2237

• Die Kompetenzen der Heil- und Hilfsmittelerbringer werden wir stärker nutzen.

2238

 

2239

Ausbildung im Gesundheitswesen verbessern

2240

Wer die Versorgung von morgen sichern will, muss heute genügend ausbilden.

2241

• In den Gesundheitsberufen und in der Pflege werden wir die Aus- und Weiterbildung 2242

stärken und die Reform der Berufsgesetze vollenden.

2243

• Die auf den Weg gebrachte Abschaffung des Schulgeldes in den Gesundheitsberufen und 2244

die Einführung einer allgemeinen Ausbildungsvergütung wollen wir zügig umsetzen.

2245

 

2246

Selbstbestimmung und Patientensouveränität stärken

2247

Patientensouveränität ist die Grundlage für eine gute Gesundheitsversorgung. Deshalb 2248

wollen wir sie stärken. Auch im hohen Alter oder bei schwerer Krankheit muss der Mensch 2249

im Mittelpunkt stehen.

2250

• Wir wollen eine lebensbejahende Beratung für Menschen, die unheilbar und mit be-2251

grenzter Lebenserwartung erkrankt sind. Statt Sterbehilfe zu kommerzialisieren, werden 2252

wir dafür sorgen, dass wir den Zugang zur Hospiz- oder Palliativversorgung garantieren.

2253

 

 

Seite 64 von 139

2254

Öffentlichen Gesundheitsdienst modernisieren

2255

Die Pandemie hat die herausragende Bedeutung des Öffentlichen Gesundheitsdienstes 2256

(ÖGD) für einen wirksamen Schutz der Gesundheit der Bevölkerung deutlich werden las-2257

sen. Die Corona-Krise hat aber auch allen vor Augen geführt, dass eine nachhaltige Verstär-2258

kung des Öffentlichen Gesundheitsdienstes als eine unverzichtbare Säule des Gesundheits-2259

wesens dringend geboten ist.

2260

• Bund und Länder haben einen „Pakt für den Öffentlichen Gesundheitsdienst“ geschlos-2261

sen, um den ÖGD in seiner ganzen Aufgabenvielfalt und auf allen Verwaltungsebenen 2262

zu stärken und zu modernisieren. Der Bund stellt für die Umsetzung des Paktes insge-2263

samt Mittel in Höhe von vier Milliarden Euro bis 2026 zur Verfügung, um den Personal-2264

aufbau und die Digitalisierung in den unteren Gesundheitsbehörden zu unterstützen.

2265

Diesen Weg wollen wir weitergehen. Dazu werden wir rechtzeitig die notwendigen Mit-2266

tel bereitstellen.

2267

• Wir werden das Robert-Koch-Institut stärken und zum deutschen Public-Health-Institut 2268

ausbauen. Neben seiner wissenschaftlichen Arbeit muss es in Zukunft noch viel stärker 2269

bei der Bekämpfung von epidemischen Gesundheitsgefahren tätig sein und sich noch 2270

stärker mit den Gesundheitsbehörden der Länder und Kommunen, aber auch internatio-2271

nal vernetzen. Dafür braucht es die notwendigen personellen und finanziellen Ressour-2272

cen.

2273

• Für besonders versorgungskritische Wirkstoffe werden wir Maßnahmen wie eine staat-2274

liche Lagerhaltung oder Notfallkapazitäten schaffen, um eine Produktion auf Abruf zu 2275

ermöglichen.

2276

 

2277

Keine Drogen legalisieren, Suchtprävention stärken

2278

Eine Legalisierung illegaler Drogen lehnen wir ab. Zu groß sind die gesundheitlichen Folgen 2279

für den Einzelnen und die Auswirkungen auf Familie, Umfeld und Gesellschaft. Wer legali-2280

siert, der stellt gerade nicht Gesundheits- und Jugendschutz in den Mittelpunkt der Dro-2281

genpolitik, entzieht sich seiner Verantwortung und lässt Betroffene sowie ihre Angehörigen 2282

mit den Problemen allein. Das ist nicht unser Weg.

2283

• Was wir brauchen, sind Aufklärung sowie frühe und massentauglichere Sanktionen, die 2284

der Tat auf dem Fuße folgen und unmittelbar zur Wahrnehmung von Beratungs- und 2285

Therapieangeboten veranlassen.

2286

• Bei legalen Suchtmitteln setzen wir auf verantwortungsvollen Umgang. Dafür braucht es 2287

mehr Aufklärung, bessere Hilfsangebote und einen starken Jugendschutz, um den Ge-2288

fahren des Rauchens und des Alkoholmissbrauchs wirkungsvoll zu begegnen.

2289

 

2290

Deutschland wieder zur Apotheke der Welt machen

2291

Deutschland galt einst als „Apotheke der Welt“. An diese Erfolgsgeschichte wollen wir mit 2292

modernen Clustern anknüpfen.

Seite 65 von 139

2293

• Wir werden die Gesundheits- und Pflegewirtschaft als herausragenden Wirtschaftsfak-2294

tor in Deutschland weiter stärken und dabei sicherstellen, dass gut bezahlte und zu-2295

kunftssichere Arbeitsplätze geschaffen werden sowie Wertschöpfung in neuen Techno-2296

logien entsteht.

2297

• Wir wollen eine Souveränitätsoffensive bei der Medikamentenproduktion. Wir wollen ei-2298

nen freien Handel ohne einseitige Abhängigkeiten – insbesondere bei der Produktion 2299

von Arzneimitteln und medizinischer Ausstattung. Unser Ziel ist es, Deutschlands und 2300

Europas Unabhängigkeit zu stärken und die Wertschöpfungsketten souveränitätskriti-2301

scher medizinischer Produkte in die EU zurückzuholen. Dafür wollen wir mit unseren 2302

Pharma-Unternehmen dafür sorgen, dass kritische Schutzkleidung, medizinische Geräte 2303

sowie alle wichtigen Medikamente in mindestens einer Variante in Europa produziert 2304

werden.

2305

• Wir fördern neue Antiinfektiva und Impfstoffe durch geeignete Anreize von Forschung 2306

bis Erstattung.

2307

• Die schnelle Verfügbarkeit neuer Therapieoptionen und Arzneimittel für schwerkranke 2308

Patienten in Deutschland soll erhalten und durch die richtigen Anreize im Vergütungs-2309

system gestärkt werden.

2310

• Bei den „Benannten Stellen“, die für die Überprüfung neuer Medizinprodukte in der Eu-2311

ropäischen Union zuständig sind, werden wir darauf hinwirken, dass der Ausbau be-2312

schleunigt wird und dadurch innovative Medizinprodukte schnellstmöglich bei den Pati-2313

enten ankommen.

2314

• Wir werden prüfen, welche Maßnahmen in Betracht kommen, damit in Krisenfällen ver-2315

sorgungsrelevante Arzneimittel in ausreichender Menge in der EU zur Verfügung stehen, 2316

zum Beispiel durch eine entsprechende Änderung des europäischen Vergaberechts.

2317

• Wir werden prüfen, ob das deutsche Vergaberecht dahingehend geändert werden kann, 2318

dass Arzneimittelhersteller verpflichtet werden können, bei der Herstellung insbeson-2319

dere von versorgungsrelevanten Arzneimitteln in der EU hergestellte Wirkstoffe zu ver-2320

wenden.

2321

 

2322

Für mehr Lebensqualität forschen

2323

Von den Ergebnissen der Gesundheitsforschung profitieren Menschen in unserem Land 2324

und weltweit unmittelbar und direkt.

2325

• Um Innovationen für Patientinnen und Patienten entwickeln zu können, müssen for-2326

schende Pharmaunternehmen die Möglichkeit haben, pseudonymisierte Versorgungs-2327

daten zu erhalten.

2328

• Schnellere Genehmigungsverfahren stärken den Pharma- und Forschungsstandort 2329

Deutschland. In der Pandemie hat sich gezeigt, wie zügig die Prüfung und Genehmigung 2330

klinischer Studien seitens der Zulassungsbehörden für Arzneimittel und Impfstoffe in Seite 66 von 139

2331

Deutschland ohne Abstriche an der Qualität gelingen kann, wenn die Ressourcen gebün-2332

delt werden. Diese zügige Bearbeitung entsprechender Anträge wollen wir auch für die 2333

Zeit nach der Pandemie erhalten und werden daher das Paul-Ehrlich-Institut und das 2334

Bundesinstitut für Arzneimittel und Medizinprodukte finanziell und personell verstär-2335

ken.

2336

• Wir werden das Tempo für die Entwicklung neuer Medikamente erhöhen, indem wir ein-2337

heitliche Vorgaben schaffen – etwa beim Datenschutz, bei länderübergreifenden Stu-2338

dien oder der Einführung verbindlicher Musterverträge für klinische Prüfungen. Investo-2339

ren und Forscher können sich darauf verlassen, dass in Deutschland auch weiterhin der 2340

Patentschutz gilt.

2341

• Wir werden die wissenschaftliche Erforschung jener Krankheiten gezielt unterstützen 2342

(beispielsweise Demenz-Erkrankungen oder HIV), die gegenwärtig als unheilbar gelten.

2343

• Künstliche Intelligenz (KI) ist eine Schlüsseltechnologie. Wir setzen uns für ein Werte-2344

system ein, das Chancen von KI für die Gesundheitsversorgung nutzt und zugleich Risi-2345

ken minimiert. Wir wollen zudem, dass Wertschöpfung von KI in Deutschland entsteht 2346

und somit auch neue Arbeitsplätze geschaffen werden.

2347

 

2348

4.4. Gute Pflege für mehr Sicherheit und Halt

2349

Für uns hat die Menschenwürde eine besondere Bedeutung, wenn die geistigen und kör-2350

perlichen Kräfte im Alter nachlassen und der Mensch in vielfältiger Hinsicht auf die Unter-2351

stützung seiner Mitmenschen angewiesen ist. Angesichts steigender Zahlen alter und pfle-2352

gebedürftiger Menschen in unserer Gesellschaft bedarf es eines solidarischen Miteinan-2353

ders. Deshalb haben wir beispielsweise die Bezahlung von Pflegekräften verbessert. Prä-2354

vention und Rehabilitation werden wir stärker in den Mittelpunkt unserer Maßnahmen stel-2355

len, um den Eintritt von Pflegebedürftigkeit möglichst lange zu verhindern.

2356

 

2357

Versorgung stärken

2358

Wir wollen die Rahmenbedingungen in der Pflege weiter verbessern, indem wir diese als 2359

gesamtgesellschaftliche Aufgabe wahrnehmen.

2360

• Wir werden sowohl für die Pflegebedürftigen als auch für das Pflegefachpersonal und 2361

pflegende Angehörige bessere Möglichkeiten für gut organisierte, leistungsfähige, bere-2362

chenbare, zuverlässige und bedarfsgerechte Angebotsstrukturen schaffen.

2363

• Wir wollen die Trägervielfalt in der Pflege als Ausdruck einer pluralen Gesellschaft stär-2364

ken. Auch hier erhoffen wir uns vom Wettbewerb bessere Angebote.

2365

• Wir wollen die Pflegebereiche als Berufsgruppe an der Selbstverwaltung im Gesund-2366

heitsrecht beteiligen, indem wir uns für die Einrichtung einer Bundespflegekammer ein-2367

setzen.

Seite 67 von 139

2368

• Auch in der Pflege gilt es, die vielfältigen Chancen der Digitalisierung zum Wohle pfle-2369

gebedürftiger Menschen zu nutzen. So kann Digitalisierung in der Pflege durch die Wei-2370

terentwicklung technischer Assistenz- und Warnsysteme älteren Menschen mehr Sicher-2371

heit und Eigenständigkeit geben. Pflegekräfte sollen durch den digitalen Fortschritt 2372

spürbar entlastet werden, indem beispielsweise digitale Infrastrukturen ausgebaut und 2373

Pflegedokumentationen erleichtert werden.

2374

 

2375

Pflegeversicherung weiterentwickeln

2376

Die von der Union eingeführte Pflegeversicherung hat sich bewährt und wird auch in Zu-2377

kunft von uns stetig weiterentwickelt, um einen verlässlichen Beitrag zur Absicherung des 2378

Pflegerisikos und eine hohe Betreuungs- und Pflegequalität zu gewährleisten.

2379

• Betriebliche Pflegezusatzversicherungen sorgen dafür, dass Menschen das Pflegerisiko 2380

im Alter zusätzlich wirksam absichern können. Wir werden prüfen, wie wir das Instru-2381

ment der betrieblichen Pflegezusatzversicherung stärken und staatlich fördern können, 2382

damit möglichst viele Menschen davon profitieren können.

2383

• Um mit Blick auf den demografischen Wandel künftig unverhältnismäßig steigenden 2384

Beiträgen in der Pflegeversicherung entgegenzuwirken, wollen wir den Pflegevorsorge-2385

fonds bis 2050 verlängern.

2386

 

2387

Ambulante und stationäre Pflege verbessern

2388

Wir sind der festen Überzeugung, dass es nicht zu den Aufgaben eines Staates gehört, den 2389

einen geeigneten Ort für Pflege zu definieren. Vielmehr liegt die Entscheidung über den 2390

Wohn- und Pflegeort bei der pflegebedürftigen Person selbst. Der Pflegebedürftige soll ei-2391

genständig und selbstbestimmt oder gemeinsam mit Familienangehörigen entscheiden, 2392

wie und wo er wohnt. Wir wollen dieses Selbstbestimmungsrecht stärken und die Unter-2393

stützungsleistungen durch die Pflegeversicherung dorthin leiten, wo der Pflegebedürftige 2394

lebt.

2395

• Wir setzen uns für eine Dynamisierung des Pflegegeldes ein und befürworten die Einfüh-2396

rung einer Regeldynamisierung für alle Leistungen auf Grundlage der Lohnentwicklung.

2397

• Wir stehen neuen Wohn- und Betreuungsformen aufgeschlossen gegenüber und werden 2398

deren Einführung unterstützen. Wir sehen Mehrgenerationenhäuser als wichtige Anlauf-2399

stellen eines generationenübergreifenden Zusammenlebens. Denn diese bieten Unter-2400

stützung bei der Vermittlung von haushaltsnahen Dienstleistungen und im Bereich der 2401

familiären Pflege.

2402

• Familiäre Pflege muss eine noch gezieltere und flexiblere Unterstützung erfahren. Des-2403

halb setzen wir uns dafür ein, die bisherigen Leistungen für Angebote der Kurzzeit- und 2404

Verhinderungspflege sowie Betreuungsleistungen zu einem Budget zusammenzufassen.

Seite 68 von 139

2405

• Stationäre Pflegeeinrichtungen sollen die Möglichkeit haben, passgenaue Unterstüt-2406

zungsleistungen für pflegebedürfte Menschen in ihrem Umfeld zu erbringen, die nicht 2407

Bewohnerinnen und Bewohner der jeweiligen Einrichtung sind.

2408

• Pflege findet in den Quartieren der betroffenen Menschen statt. Deshalb werden wir die 2409

Länder und Kommunen darin unterstützen, quartiersbezogene und sektorenübergrei-2410

fende Versorgungskonzepte umzusetzen.

2411

 

2412

Pflegekräfte qualitätsvoll ausbilden

2413

Eine hohe Pflegequalität ist für die Betroffenen von zentraler Bedeutung. Dafür brauchen 2414

wir gut ausgebildete Pflegekräfte.

2415

• Zusammen mit den Ländern wollen wir eine bundesweite Harmonisierung der Assistenz-2416

ausbildung in der Pflege erreichen.

2417

• Es ist wichtig, attraktive Arbeitsbedingungen für alle in der Pflege Beschäftigten zu 2418

schaffen, die insbesondere auch eine verlässliche Gestaltung der Dienstpläne umfassen.

2419

• Wir wollen die Willkommenskultur für ausländische Pflegefachkräfte stärken und setzen 2420

uns für eine generelle Schulgeldfreiheit für Gesundheits- und Pflegeberufe ein, um dem 2421

wachsenden Bedarf an Pflege- und Gesundheitsleistungen gerecht zu werden.

2422

• Wir wollen die Ausbildung in der Pflege weiter stärken, indem wir eine bundesweite Ver-2423

gütung der Auszubildenden in der Pflegefachassistenzausbildung einführen.

2424

 

2425

4.5. Deutschlands Verantwortung für globale Gesundheit 2426

Die Pandemie zeigt, wie wichtig die internationale Zusammenarbeit bei Fragen der Gesund-2427

heit und der Gesundheitssicherheit ist. Die Weltgesundheitsorganisation (WHO) leistet ei-2428

nen wichtigen Beitrag zur weltweiten Bekämpfung der Pandemie. Gleichzeitig hat sich ge-2429

zeigt, dass die WHO ihr zentrales Mandat in der globalen Gesundheit aufgrund mangelnder 2430

Ressourcen aktuell nur unzureichend erfüllen kann.

2431

• Daher wollen wir sie nachhaltig stärken, finanziell, technisch und politisch. Deutschland 2432

ist im Verlauf der Corona-Krise bereits zum größten staatlichen Geldgeber der WHO

2433

avanciert und tritt vernehmbar für eine schlagkräftige WHO ein, zu der auch alle Mit-2434

gliedstaaten ihren Beitrag leisten.

2435

• Verschiedene Reformprozesse sind bereits angestoßen. Deutschland wird die Initiative 2436

zu einem internationalen Pandemievertrag zur Stärkung der globalen Gesundheitssi-2437

cherheit weiter aktiv unterstützen.

2438

• Deutschland ist auf dem Weg, ein international anerkannter Standort für Global Health 2439

zu werden, immer mehr Institutionen siedeln sich bei uns an. Diese Entwicklung wollen 2440

wir weiter befördern.

2441

 

 

Seite 69 von 139

2442

5. Neue Generationengerechtigkeit bei Finanzen und Steuern – aus Ver-2443

antwortung für unsere Kinder und Enkel

2444

 

2445

Unser Unions-Versprechen: Wir werden dafür sorgen, dass alle Menschen, die jeden Tag hart 2446

arbeiten und viel leisten, entlastet werden. Leistung muss sich lohnen. Wir werden auch Frei-2447

räume für unsere Unternehmen schaffen und dazu beitragen, dass sie wettbewerbsfähig blei-2448

ben. Gleichzeitig wollen wir so schnell wie möglich ohne neue Schulden auskommen. Das ist 2449

praktizierte Generationengerechtigkeit.

2450

Wir stehen dabei vor der Herausforderung, dass die finanziellen Spielräume durch die Corona-2451

Pandemie auf allen Ebenen begrenzt sind. Diese Spielräume durch höhere Steuern oder neue 2452

Schulden wieder zu vergrößern, würde den dringend benötigten wirtschaftlichen Aufschwung 2453

und damit Arbeitsplätze gefährden und wäre ungerecht gegenüber kommenden Generationen.

2454

Nur ein finanziell solider Staat ist handlungsfähig und kann die Zukunft gestalten.

2455

Wir brauchen ein neues, modernes Verständnis vom Staat. Er muss sich stärker zurückziehen 2456

und nicht alles bis ins Detail regeln wollen. Freiheit und Eigenverantwortung sind zwei Seiten 2457

ein und derselben Medaille. Zudem gilt, dass mehr Geld vom Staat nicht alle Probleme löst. Denn 2458

oft fehlt es eben nicht daran. Beim Digitalpakt oder Ausbau der Infrastruktur wurden Gelder 2459

nicht abgerufen. Andere Programme gehen an Bedürfnissen und Problemen vorbei. Deshalb 2460

werden wir noch stärker bestehende und künftige Ausgaben auf ihre Effizienz hin überprüfen 2461

und, wenn nötig, streichen.

2462

 

2463

5.1. Mit soliden Finanzen sicher in die Zukunft

2464

Corona hat uns gezeigt, wo wir die richtigen Grundlagen geschaffen haben, um auch in Kri-2465

senzeiten umfassend handlungsfähig zu bleiben. Unsere klare solide Finanzpolitik hat uns 2466

einen Spielraum ermöglicht, den andere Staaten so nicht hatten. Dadurch konnten wir in 2467

der Corona-Krise schlagkräftig handeln und Beschäftigte wie Unternehmen zielgenau un-2468

terstützen, als dies notwendig war. Dieses stabile Fundament werden wir erneuern und wei-2469

terentwickeln.

2470

Solide Finanzen sind nicht nur wichtig für die Stabilisierung privater Investitionen und ein 2471

gutes Wirtschaftswachstum in Deutschland. Es ist auch ein Gebot der Generationengerech-2472

tigkeit: Eine solide Finanz- und Haushaltspolitik muss stets die kommenden Generationen 2473

im Blick behalten. Es ist unser Ziel, die Handlungsspielräume für unsere Kinder und Enkel 2474

zu vergrößern, anstatt ihnen Schulden und damit Belastungen aufzubürden.

2475

• Wir bekennen uns zur grundgesetzlichen Schuldenbremse. Sie hat in der Krise ihre Funk-2476

tionsfähigkeit und Flexibilität bewiesen. Grundgesetzänderungen zur Aufweichung der 2477

Schuldenbremse lehnen wir ab.

2478

• Wir wollen so schnell wie möglich wieder ausgeglichene Haushalte ohne neue Schulden 2479

erreichen und die gesamtstaatliche Schuldenquote auf unter 60 Prozent reduzieren.

2480

• Wir werden mit Ende der Corona-Pandemie einen Kassensturz für die öffentlichen Haus-2481

halte einschließlich der Sozialversicherungen vollziehen. Das mündet in einen Fahrplan Seite 70 von 139

2482

für Investitionen in Wachstum, gezielte Entlastungen und ausgeglichene Haushalte. Un-2483

sere Überzeugung ist: Nachhaltiges Wachstum schafft neue Spielräume.

2484

• Wir werden den Bundeshaushalt zukunftsfest aufstellen und das Haushaltswesen auch 2485

auf Bundesebene nachhaltig modernisieren. Unser Ziel ist eine langfristig und generati-2486

onengerecht angelegte Haushaltsführung im Bund. Dazu kann eine doppische Haus-2487

haltsführung beitragen.

2488

• Immer wieder werden Fördermittel des Bundes nicht abgerufen oder verfehlen ihre Wir-2489

kung. Wir werden deshalb Ausgaben regelmäßig auf ihre Wirksamkeit und Notwendig-2490

keit prüfen und entbehrliche Ausgaben streichen. So kann das vorhandene Geld für wich-2491

tigere Zukunftsaufgaben eingesetzt und mit jedem Euro mehr erreicht werden.

2492

 

2493

5.2. Faire, leistungsgerechte und wettbewerbsfähige Steuern 2494

Wir wollen die Wirtschaft nach der Pandemie wieder in Schwung bringen. Auf diesem Weg 2495

wäre es falsch, Steuern zu erhöhen. Wir stehen weiter für eine verantwortungsvolle und 2496

solide Finanzpolitik. Wir versprechen nichts, was wir nicht einhalten können. Wir stellen die 2497

Weichen konsequent auf Wachstum, damit sich neue Spielräume ergeben.

2498

• Deutschland droht mit einer der höchsten Unternehmensbelastung der Welt zurückzu-2499

fallen. Weltspitze bei der Steuerbelastung und Weltspitze bei der Wettbewerbsfähigkeit 2500

– das passt auf Dauer nicht zusammen. Im Rahmen unseres umfangreichen Entfesse-2501

lungspakets werden wir mit einer Unternehmenssteuerreform die Besteuerung moder-2502

nisieren und wettbewerbsfähig machen.

2503

 

2504

Leistung muss sich lohnen

2505

Wer sich anstrengt, wer etwas wagt, soll auch dafür belohnt werden. Das ist praktizierte 2506

Leistungsgerechtigkeit. Wir wollen deshalb Spielräume, soweit sie sich eröffnen, nutzen, 2507

um die Menschen zu entlasten, die jeden Tag Leistung erbringen, damit sie mehr Netto vom 2508

Brutto haben. Dabei nehmen wir alle hart arbeitenden Menschen in den Blick. Egal ob Ver-2509

käuferin, Ärztin, IT-Spezialist oder Handwerker – wir wollen, dass alle sich vom verdienten 2510

Geld mehr leisten können.

2511

• Wir werden den Solidaritätszuschlag für alle schrittweise abschaffen und gleichzeitig 2512

kleine und mittlere Einkommen bei der Einkommensteuer entlasten.

2513

• Wir werden auch künftig die Wirkungen der sogenannten kalten Progression ausglei-2514

chen, indem wir den Einkommensteuertarif regelmäßig an die allgemeine Preisentwick-2515

lung anpassen.

2516

 

2517

Familien mit Kindern finanziell entlasten

2518

Wir wollen gezielt Familien finanziell stärken. Sie sind die Leistungsträger unserer Gesell-2519

schaft.

Seite 71 von 139

2520

• Wir halten am Ehegattensplitting fest und wollen unabhängig davon zusätzlich Ansätze 2521

entwickeln, um Kinder positiv zu berücksichtigen. Wir haben die finanzielle Situation von 2522

Familien spürbar verbessert, indem wir den Kinderfreibetrag und das Kindergeld zum 2523

1. Januar 2021 deutlich erhöht haben. Perspektivisch streben wir den vollen Grundfrei-2524

betrag für Kinder an und finden damit den Einstieg in ein Kindersplitting.

2525

• Wir haben auch den steuerlichen Entlastungsbetrag für Alleinerziehende auf 4.008 Euro 2526

verdoppelt. Wir wollen ihn perspektivisch auf 5.000 Euro weiter erhöhen.

2527

• Wir werden die steuerliche Berücksichtigung haushaltsnaher Dienstleistungen verbes-2528

sern. Sie entlasten Familien im Alltag und schaffen mehr Zeit für Familie und Beruf. So 2529

verringern wir auch Schwarzarbeit und tragen zur sozialen Absicherung der häufig weib-2530

lichen Beschäftigten bei.

2531

 

2532

Steuererklärung vereinfachen

2533

Wir setzen uns für ein einfaches und verständliches Steuerrecht ein. Die Kommunikation 2534

zwischen den Bürgerinnen und Bürgern und ihrem Finanzamt muss schneller und einfacher 2535

werden.

2536

• Wir werden dafür sorgen, dass die Steuererklärung, alle Anträge und der Schriftwechsel 2537

online erfolgen können. Ein digitaler Steuerbescheid muss künftig die Regel sein.

2538

• Die Steuererklärung muss in einfachen Fällen auch mit einer App erledigt und abgegeben 2539

werden können.

2540

• Steuerrechtliche Regelungen sollten grundsätzlich digital umsetzbar sein.

2541

• Wir werden die Steuererklärung für alle vereinfachen, vor allem für ältere Menschen, die 2542

Renten und Pensionen beziehen. Dafür wollen wir die vorausgefüllte Steuererklärung 2543

verbessern. Hierzu soll bereits ab Frühjahr 2022 für den Veranlagungszeitraum 2021 eine 2544

einfache Anwendung zur Verfügung stehen.

2545

 

2546

Steuern weltweit fair gestalten

2547

Wir stehen für Steuergerechtigkeit. Auch in Zukunft sollen alle angemessen zur Finanzie-2548

rung öffentlicher Leistungen beitragen. Niemand darf sich seiner Verantwortung für die 2549

Gesellschaft entziehen und sich ärmer rechnen, als er ist. Das gilt insbesondere für multi-2550

nationale Konzerne.

2551

• Wir werden weiter Steuerschlupflöcher schließen, Steuerhinterziehung sowie schädliche 2552

Formen des Steuerwettbewerbs wirksam unterbinden und aggressive Steuergestaltun-2553

gen bekämpfen.

2554

• Wir werden dabei nur dann erfolgreich sein, wenn wir uns mit unseren internationalen 2555

Partnern abstimmen. Die OECD hat sich mit ihrem Aktionsplan gegen Gewinnkürzungen 2556

und Gewinnverlagerungen grenzüberschreitend agierender Konzerne (BEPS) als inter-Seite 72 von 139

2557

nationaler Standardsetzer bewährt. Wir setzen weiter auf diese Institutionen, um insbe-2558

sondere einen international breit abgestimmten Konsens zur fairen Besteuerung global 2559

tätiger Konzerne herbeizuführen.

2560

• Wir setzen uns auf OECD-Ebene ebenfalls für eine faire Besteuerung der digitalen Wirt-2561

schaft ein. Große digitale Konzerne sollen ihre Steuern auch dort zahlen, wo sie ihre Um-2562

sätze erzielen.

2563

• Wir brauchen eine gemeinsame Körperschaftsteuer-Bemessungsgrundlage, damit Un-2564

ternehmen in Europa möglichst nach gleichen Regeln besteuert werden. Dabei müssen 2565

die Besonderheiten der deutschen Unternehmenslandschaft und -besteuerung ange-2566

messen berücksichtigt werden, um Wettbewerbsnachteile deutscher Unternehmen zu 2567

vermeiden. Dies schließt auch ein abgestimmtes Steuerverfahrensrecht mit ein.

2568

• Wir werden den Umsatzsteuerbetrug weiter eindämmen und Steuerschlupflöcher schlie-2569

ßen.

2570

• Wir setzen uns für eine europäische Finanztransaktionsteuer mit breiter Bemessungs-2571

grundlage ein. Sie darf jedoch Kleinanleger und die private Altersvorsorge nicht belas-2572

ten.

2573

 

2574

5.3. Vermögensbildung für jeden

2575

Teilhabe geht vor Umverteilung. Wir wollen, dass die Menschen in unserem Land Erfolg ha-2576

ben und sich Wohlstand aufbauen können. „Wohlstand für alle“ im 21. Jahrhundert heißt für 2577

uns: Vermögensaufbau für alle Menschen attraktiv gestalten – unabhängig von Beschäfti-2578

gungsverhältnis und Einkommen.

2579

 

2580

Beteiligung am Unternehmenserfolg verbessern

2581

Die Beteiligung der Arbeitnehmerinnen und Arbeitnehmer am eigenen Unternehmen ist 2582

ein originär christlich-soziales Anliegen. Sie entspricht der Idee der Subsidiarität, stärkt die 2583

Bindung zwischen Beschäftigten und Unternehmen und fördert die Sozialpartnerschaft.

2584

• Unser Ziel ist es, die Mitarbeiterkapitalbeteiligung weiter zu verbessern.

2585

• Für beteiligte Beschäftigte und Unternehmen muss ein klarer rechtlicher Rahmen mittels 2586

Betriebsvereinbarungen geschaffen werden.

2587

• Wir setzen uns für eine Harmonisierung der Regeln für die Mitarbeiterkapitalbeteiligung 2588

in der EU ein.

2589

 

2590

Vermögensbildung stärken und vermögenswirksame Leistungen ausweiten

2591

Gerade in Zeiten niedriger Zinsen sind unterschiedliche Anlageformen gefragt, um attrak-2592

tive Renditen zu erzielen und Vermögen für das Alter aufzubauen. Wir fördern verschiedene 2593

Formen:

2594

• Wir werden den Sparer-Pauschbetrag und die Arbeitnehmersparzulage erhöhen.

Seite 73 von 139

2595

• Wir werden die vermögenswirksamen Leistungen stärken und den Höchstbetrag, den 2596

Arbeitnehmer von ihrem Arbeitgeber erhalten können, erhöhen.

2597

• Gewinne aus vermögenswirksamen Leistungen sollten nach der Mindesthaltefrist steu-2598

erfrei sein.

2599

 

2600

Keine Vermögensteuer

2601

Wir lehnen zusätzliche Lasten wie eine Wiedereinführung der Vermögensteuer ab. Eine Ver-2602

mögensteuer würde uns alle treffen: Sie würde sowohl Hauseigentümer als auch Mieter be-2603

lasten und somit das Wohnen für alle verteuern. Sie würde Betriebsvermögen belasten und 2604

somit Arbeitsplätze für alle gefährden. Die Vermögensteuer ist eine Wohlstandsbremse.

2605

 

2606

5.4. Finanzplatz Deutschland stärken

2607

Nur als starker und wettbewerbsfähiger Finanzplatz kann Deutschland auch weiterhin aktiv 2608

die Regulierung der internationalen Finanzmärkte mitgestalten.

2609

• Innerhalb einer starken Banken- und Kapitalmarktunion wollen wir Deutschland zum 2610

führenden Finanzstandort, insbesondere für nachhaltige Produkte, ausbauen.

2611

• Wir werden vor allem Bürokratie für Finanzmarktteilnehmer abbauen, Regeln moderni-2612

sieren und die Rahmenbedingungen für Börsengänge verbessern.

2613

• Als starker Finanzplatz soll Deutschland für die Ansiedlung von EU-Institutionen attrak-2614

tiver werden.

2615

• Wir streben einen eigenen Börsenplatz nach dem Vorbild der NASDAQ an. Schnell wach-2616

sende Technologieunternehmen sollen sich an einer deutschen oder europäischen Börse 2617

finanzieren können, damit sie für diesen Wachstumsschritt nicht mehr in die USA ab-2618

wandern müssen.

2619

 

2620

Verbraucher und Anleger schützen

2621

Auch auf dem Finanzmarkt setzen wir auf einen fairen Wettbewerb, Schutz der Verbrau-2622

cherinteressen, finanzielle Bildung, Transparenz bei Finanzprodukten sowie eine starke 2623

Aufsicht.

2624

• Damit alle die Chancen verschiedener Anlageformen nutzen können, brauchen wir einen 2625

starken Verbraucher- und Anlegerschutz.

2626

• Wir wollen, dass alle von neuen, digitalen Zahlungsmöglichkeiten und Finanzdienstleis-2627

tungen profitieren. Dies gelingt, wenn die Kundendaten sicher sind, mit ihnen gesetzes-2628

konform und vertraulich umgegangen wird und durch angemessene Entgelte.

2629

 

 

Seite 74 von 139

2630

6. Neues Aufstiegsversprechen – für Deutschland als Chancen- und Fami-2631

lienland

2632

 

2633

Unser Unionsversprechen: Wir werden es unseren Familien leichter machen. Wir werden sie fi-2634

nanziell entlasten und ihnen geben, was für alle wichtig ist: Zeit füreinander, Sicherheit, mehr 2635

finanzielle Spielräume, gute Schulen und Kitas.

2636

Gleichzeitig versprechen wir, dass wir die Vereinbarkeit von Familie und Beruf weiter verbessern 2637

und die Chancengleichheit von Frauen und Männern fördern. Jede und jeder soll sich durch An-2638

strengung, Leistung und Fleiß etwas aufbauen und nach dem eigenen Glück streben können.

2639

Dieses Aufstiegsversprechen muss für alle unabhängig von der Herkunft und sozialen Verhält-2640

nissen gelten. Wir wollen Aufstieg durch Bildung für alle möglich machen und bekennen uns 2641

dabei zum bewährten Bildungsföderalismus.

2642

Corona hat aber auch Schwächen offengelegt. Das beginnt damit, dass wir in Sachen digitaler 2643

Bildung dringend anpacken und unsere Schulen modernisieren. Und es geht insgesamt um eine 2644

Politik, die Familien konsequent in den Mittelpunkt stellt. Der Schutz der Familie unter sich wan-2645

delnden Bedingungen ist eine Grundkonstante einer vom christlichen Menschenbild geleiteten 2646

Politik. In unserem Modernisierungsjahrzehnt müssen wir die nach wie vor bestehende 2647

Benachteiligung von Frauen angehen und ihnen gleiche Chancen wie Männern ermöglichen.

2648

Die Corona-Pandemie hat vor allem jungen Familien enorm viel abverlangt. Über Monate konn-2649

ten Kinder und Jugendliche kaum und nur im Wechselunterricht die Schule besuchen. Sie waren 2650

getrennt von ihren Freunden, sie verpassten so vieles, das zum Erwachsenwerden dazugehört.

2651

Eltern mussten gleichzeitig Kinder betreuen, beim digitalen Lernen unterstützen und ihre Arbeit 2652

von zu Hause erledigen.

2653

Familienfreundlichkeit ist Markenzeichen einer jeden unionsgeführten Bundesregierung.

2654

 

2655

6.1. Mehr Zeit, Raum und Unterstützung für Familien

2656

Familien benötigen Zeit füreinander, Raum für ihre Entfaltung und finanzielle 2657

Unterstützung zu ihrer Absicherung. Wir stehen für Familienfreundlichkeit und wollen, dass 2658

sich möglichst viele Menschen für ein Leben mit Kindern entscheiden.

2659

• Unser Ziel ist es, das Elterngeld weiter zu stärken und gerade Väter zu ermutigen, 2660

stärker als bisher das Elterngeld zu nutzen. Wir wollen die Partnermonate beim 2661

Elterngeld um weitere zwei auf insgesamt 16 Monate ausweiten, wenn sowohl Vater als 2662

auch Mutter Elternzeit nehmen.

2663

 

2664

Familien mehr Zeit geben

2665

Wir wollen eine familiengerechte Arbeitswelt und keine arbeitsmarktgerechten Familien.

2666

Uns ist wichtig, dass Eltern in bestimmten Lebensphasen ihre Arbeitszeit reduzieren und in 2667

anderen Zeiten mit ganzer Kraft ihrem Beruf nachgehen können. Dies gilt insbesondere in 2668

der „Rushhour des Lebens“, in der zumeist Berufsleben und Familiengründung Seite 75 von 139

2669

zusammenfallen. Wir werden Wahlfreiheit durch mehr Zeitsouveränität über das ganze 2670

Berufsleben ermöglichen.

2671

• Wir wollen das bestehende Instrument der Zeitwertkonten praktikabler gestalten und 2672

als Familienzeitkonten für die Vereinbarkeit von Familie und Beruf nutzbar machen.

2673

Dieses Konzept hat sich bereits bewährt, weshalb wir seine Verbreitung weiter fördern 2674

wollen.

2675

• Eltern sollen angesparte Zeiten einsetzen können, um in der Familienphase ohne 2676

finanzielle Nachteile weniger zu arbeiten. Auch staatliche Fördermittel sollen auf 2677

Familienzeitkonten gebucht werden können.

2678

 

2679

Familienleistungen einfach bündeln

2680

Familien sollen ihre kostbare und oft knappe Zeit miteinander verbringen – und nicht mit 2681

unnötiger Bürokratie.

2682

• Wir wollen Familienleistungen maximal vereinfachen. Sie sollen automatisiert, digital 2683

und aus einer Hand Familien zur Verfügung stehen. Geburtsurkunde, Kindergeld, 2684

Elterngeld und Kinderzuschlag sowie das Bildungs- und Teilhabepaket sollen digital 2685

beantragt werden können.

2686

• Wir wollen es so unbürokratisch und einfach wie möglich machen, Familienleistungen zu 2687

bekommen. Leistungen müssen, wo immer möglich, automatisiert erfolgen.

2688

• Haushaltsnahe Dienstleistungen entlasten Familien im Alltag und schaffen mehr Zeit für 2689

Familie und Beruf. Deshalb werden wir die Absetzbarkeit von haushaltsnahen 2690

Dienstleistungen verbessern.

2691

 

2692

Durch flexibleres und mobiles Arbeiten mehr Freiräume schaffen

2693

Gerade Beschäftigte mit Kindern wollen ihre Arbeitszeiten zunehmend flexibler gestalten 2694

oder von zu Hause arbeiten. Dies ist auch im Interesse der Arbeitgeber. Wir wollen die Fle-2695

xibilitätsspielräume zugunsten beider Seiten ausweiten und dabei den Arbeits- und Ge-2696

sundheitsschutz weiter stärken.

2697

• Wir wollen auch künftig möglichst vielen Beschäftigten die mobile Arbeit ermöglichen 2698

und setzen auf sozialpartnerschaftliche Regelungen der Tarifvertrags- und Betriebspar-2699

teien, die mobiles Arbeiten ermöglichen und den Arbeitsschutz gewährleisten.

2700

• Darüber hinaus wollen wir auf nationaler und auf EU-Ebene die rechtlichen Vorausset-2701

zungen dafür schaffen, dass Arbeiten von überall in Europa gerade für kleine und mittel-2702

ständische Unternehmen rechtssicherer wird. Daher werden wir die Regelungen im Ar-2703

beits-, Sozialversicherungs- sowie Steuerrecht überprüfen und gegebenenfalls anpassen.

2704

 

 

Seite 76 von 139

2705

Familien mit Kindern finanziell entlasten und Wohneigentum ermöglichen

2706

Wir wollen Familien und Alleinerziehende noch stärker entlasten und sie dabei unterstüt-2707

zen, den Traum vom Eigenheim zu erfüllen. Sie sind die starke Mitte und die Leistungsträger 2708

unserer Gesellschaft.

2709

• Wir haben die finanzielle Situation junger Familien spürbar verbessert, indem wir den 2710

Kinderfreibetrag und das Kindergeld zum 1. Januar 2021 deutlich erhöht haben. Einen 2711

weiteren Schritt werden wir abhängig von der wirtschaftlichen Lage verwirklichen. Per-2712

spektivisch streben wir den vollen Grundfreibetrag für Kinder an und finden damit den 2713

Einstieg in ein Kindersplitting.

2714

• Wir haben auch den steuerlichen Entlastungsbetrag für Alleinerziehende auf 4.008 Euro 2715

verdoppelt. Wir wollen ihn perspektivisch auf 5.000 Euro weiter erhöhen.

2716

• Wir werden das KfW-Wohneigentumsprogramm für Familien ausweiten. Wer Kinder hat, 2717

soll stärker davon profitieren. Dazu sollten Darlehen, Tilgungszuschüsse oder Zinsverbil-2718

ligungen nach Anzahl der Kinder gestaffelt werden. Ebenso wollen wir energetische Sa-2719

nierungen des Familieneigenheims fördern.

2720

• Den Ländern werden wir ermöglichen, einen Freibetrag bei der Grunderwerbsteuer von 2721

250.000 Euro pro Erwachsenem plus 100.000 Euro pro Kind beim erstmaligen Erwerb 2722

selbstgenutzten Wohnraums zu gewähren.

2723

 

2724

Kinder gesund aufwachsen lassen

2725

Unser Alltag findet zunehmend in Räumen und vor dem Bildschirm statt. Das gilt auch für 2726

Kinder und Jugendliche. Zu den Folgen gehören Übergewicht und Fehlernährung sowie 2727

abnehmende motorische Fähigkeiten. Unsere Offensive für gesundes Aufwachsen macht 2728

Kinder und Jugendliche fit. Sie stärkt ihre körperlichen, motorischen und sensorischen 2729

Fähigkeiten, ihr geistiges Leistungsvermögen und ihr Selbstbewusstsein.

2730

• Mit einem Bundesprogramm werden wir Länder und Träger von Bildungseinrichtungen 2731

dabei unterstützen, Ernährung und Bewegung systematisch in die Familienbildung sowie 2732

die Bildungs- und Erziehungspläne aufzunehmen. Gesunde Lebensführung soll ein ei-2733

genständiges Bildungsziel werden.

2734

• Darüber hinaus wollen wir alle Vorsorgeuntersuchungen bis zum Jugendalter verbindlich 2735

in den Leistungskatalog der gesetzlichen Krankenkassen aufnehmen.

2736

• Wir wollen die Nationale Diabetes-Strategie und den Nationalen Aktionsplan IN FORM

2737

im Bereich Familie, Kinderbetreuung und Schule weiter vorantreiben.

2738

 

2739

Modernes Familienrecht zum Wohl des Kindes

2740

Wenn sich Eltern trennen, ändert sich für Kinder viel. Wir sind der Überzeugung, dass es für 2741

Kinder in aller Regel am besten ist, wenn beide Elternteile gemeinsam Verantwortung für 2742

Erziehung und Entwicklung übernehmen. Eine Trennung der Eltern darf kein 2743

Beziehungsende für Kinder sein.

Seite 77 von 139

2744

• Wir wollen die familienrechtlichen Vorschriften im Unterhalts-, Sorge- und Umgangs-2745

recht anpassen. Zentral ist dabei nach wie vor das Wohl des Kindes. Wir wollen eine Auf-2746

enthalts- und Betreuungsregelung, die in jedem Einzelfall bestmöglich das Kindeswohl 2747

sicherstellt.

2748

 

2749

Kindern in Not helfen

2750

Wenn Kinder zu Opfern von Gewalt werden, brauchen sie unsere gemeinsame Hilfe.

2751

• Wir wollen Einrichtungen für die Erstversorgung von Kindern deutschlandweit etablie-2752

ren, die eine medizinische und psychologische Notfallversorgung mit der Aufnahme ju-2753

ristisch verwertbarer Befunde und gerichtsfesten Befragungen der Opfer kombinieren.

2754

Wir wollen über ein Bundesprogramm – wie bei Frauenhäusern – eine Anschubfinanzie-2755

rung zum Beispiel für die Ausstattung gewähren.

2756

• Mit dem Programm verbinden wir die aktuelle Justizreform zur Bekämpfung sexualisier-2757

ter Gewalt gegen Kinder mit einer umfassenden Opfererstversorgung – auch für Opfer 2758

von nichtsexualisierter Gewalt

2759

 

2760

Politische Bildung in der Jugendarbeit fördern

2761

Beteiligung schafft Akzeptanz für Politik und unser demokratisches System. Das gilt umso 2762

mehr in einem Land, in dem Menschen mit unterschiedlichen Nationalitäten und 2763

kulturellen Prägungen leben.

2764

• Wir setzen uns für eine Stärkung der politischen Bildung und Wertekunde ein: Nur wer 2765

weiß, wie Demokratie funktioniert, kann später auch demokratisch handeln.

2766

 

2767

Einsamkeit vermeiden

2768

Millionen Menschen in Deutschland fühlen sich einsam, jüngere wie ältere. Der Kampf 2769

gegen Einsamkeit ist in unserer älter werdenden Gesellschaft eine große Herausforderung.

2770

• Wir wollen eine umfassende Strategie gegen Einsamkeit entwickeln, die Antworten da-2771

rauf gibt, was Alleinstehende brauchen, worauf Vereinsamung zurückgeht, wo es Defi-2772

zite gibt und wie diesen präventiv begegnet werden kann – in allen Bereichen und auf 2773

allen Ebenen. Dazu werden wir die räumliche wie digitale Mobilität fördern.

2774

• Wir werden ehrenamtliche Strukturen und Netzwerke wie die aufsuchende Nachbar-2775

schaftshilfe und Sozialarbeit leichter zugänglich machen und auch im Rahmen generati-2776

onenübergreifender Wohnformen stärken.

2777

 

2778

6.2. Gleichberechtigte Chancen für Frauen und Männer

2779

Wir wollen eine moderne Gesellschaft, in der Frauen und Männer gleichberechtigt ihre 2780

Kompetenzen und Stärken entfalten und ihren Interessen nachgehen können. Frauen und 2781

Männer sollen gleichberechtigte Wertschätzung erfahren, wenn sie sich in der Familie, im 2782

Beruf oder im Ehrenamt engagieren. Deshalb wollen wir die Situation von Frauen in allen Seite 78 von 139

2783

Politikfeldern in den Blick nehmen und dort nachsteuern, wo Rahmenbedingungen verbes-2784

sert werden müssen.

2785

 

2786

Chancengleichheit beim beruflichen Aufstieg gewährleisten

2787

Ein wichtiger Schritt auf dem Weg zur Chancengleichheit von Frauen und Männern war das 2788

Gesetz für die gleichberechtigte Teilhabe an Führungspositionen in der Privatwirtschaft 2789

und im öffentlichen Dienst. Wir wollen die Chancengleichheit weiter verbessern.

2790

• Wir werden uns für mehr Familienfreundlichkeit auch in Führungspositionen einsetzen.

2791

• Unser Ziel ist es, geschlechterspezifische Lohn- und Rentenlücken zu beseitigen. Wir 2792

gehen die Unterschiede in der Altersvorsorge von Männern und Frauen genauso an wie 2793

das nicht akzeptable Einkommensgefälle bei gleicher Arbeit. Wir werden die Wirkung des 2794

Entgelttransparenz-Gesetzes weiter evaluieren und es, falls nötig, überarbeiten.

2795

 

2796

Frauen für MINT-Berufe begeistern und Karrieren in der Wissenschaft erleichtern

2797

Junge Frauen sind heute so gut ausgebildet wie nie zuvor. Dennoch ergreifen 2798

vergleichsweise wenige eine Ausbildung oder ein Studium im technisch-2799

naturwissenschaftlichen Bereich (MINT). Das soll sich ändern.

2800

• Wir wollen daher weiter gemeinsam mit Wirtschaft und Wissenschaft dafür werben, dass 2801

sich junge Menschen für naturwissenschaftlich-technische Berufe entscheiden. Hierzu 2802

wollen wir ihnen Qualifizierungs- und Karrieremöglichkeiten aufzeigen und sie mit 2803

Beratungsleistungen unterstützen.

2804

• Wir unterstützen Kooperationen von Hochschulen mit kommunalen Einrichtungen bei 2805

der Kinderbetreuung, um mehr junge Menschen für eine wissenschaftliche Karriere zu 2806

gewinnen. Wir befürworten dabei flexible Öffnungszeiten am Abend und an den 2807

Wochenenden.

2808

• Wir setzen uns ein für familienfreundliche Anstellungsmodelle insbesondere in der 2809

Postdoc-Phase.

2810

 

2811

6.3. Aufstieg durch Bildung

2812

Damit jedes Kind seine individuellen Lebenschancen nutzen kann und das Zukunftsverspre-2813

chen Aufstieg durch Bildung Bestand hat, müssen alle ihren Beitrag leisten: fürsorgliche 2814

und unterstützende Eltern, engagierte Erzieherinnen und Lehrkräfte, ermutigende und in-2815

spirierende Ausbilder und Professoren. Jedes Kind soll seinen Möglichkeiten entsprechend 2816

von Anfang an gefördert werden, gerade auch in sozial schwierigen Lagen. Der Grundstein 2817

für Aufstieg durch Bildung wird schon im frühen Kindesalter gelegt. Für uns gilt: Die Her-2818

kunft von Menschen darf nicht über ihre Zukunft entscheiden.

2819

• Eltern und Kinder haben ein Recht auf eine qualitativ hochwertige Kinderbetreuung, die 2820

verlässlich und dem Bedarf angemessen ist.

Seite 79 von 139

2821

• Wir werden den Kita-Ausbau und die Weiterentwicklung der Qualität auch über 2022

2822

hinaus weiter fördern. Damit helfen wir Kindern in ihrer Entwicklung und unterstützen 2823

Eltern bei der Vereinbarkeit von Familien und Beruf.

2824

• Wir werden die Einrichtungen der frühen Bildung zu qualitativ hochwertigen Bildungsor-2825

ten weiterentwickeln und so einen zentralen Beitrag leisten, um Herkunft und Bildungs-2826

erfolg zu entkoppeln.

2827

 

2828

Sprachliche Bildung für alle Kinder fördern

2829

Alle Kinder müssen ihre Bildungschancen von Anfang an ausschöpfen können. Kein Kind 2830

darf zurückbleiben. Nur so können wir unser Versprechen „Aufstieg durch Bildung“ einlö-2831

sen.

2832

• Wir werden den Erwerb der deutschen Sprache so früh wie möglich fördern, insbeson-2833

dere durch verbindliche, fortlaufende und standardisierte Diagnoseverfahren. Ab einem 2834

Alter von drei Jahren kommen verbindliche Sprachstands-Tests mit qualitativ wirksamen 2835

Sprachförderangeboten für alle Kinder hinzu.

2836

• Dort, wo ein besonderer Sprachförderbedarf festgestellt wird, muss eine verpflichtende, 2837

qualitativ wirksame und durchgehende Sprachförderung in einer Kindertagesstätte oder 2838

Vorschule erteilt werden.

2839

• Für jedes dieser Kinder soll ein individueller Sprachförderplan erstellt werden, der För-2840

derziele, Dauer und Umfang der konkreten Maßnahmen neben der durchgängigen, inte-2841

grierten Sprachförderung umfasst. Jedes Grundschulkind muss grundsätzlich vor seiner 2842

Einschulung der deutschen Sprache mächtig sein, um dem Unterricht von der ersten 2843

Klasse an folgen zu können.

2844

• Wir unterstützen das Bundesprogramm „Sprach-Kitas: Weil Sprache der Schlüssel zur 2845

Welt ist“ und wollen die sprachliche Bildung in diesem Bereich weiter fördern. Uns ist es 2846

wichtig, dass wir Kinder mit sprachlichem Förderbedarf noch mehr in den Fokus nehmen.

2847

 

2848

Schulen in sozial schwierigen Lagen besonders stärken

2849

Damit jedes Kind seine Chancen nutzen kann, wollen wir die Schulen vor allem in sozial 2850

schwierigen Lagen weiter stärken.

2851

• Die Bund-Länder-Initiative „Schule macht stark“ fördert beste Bildungschancen für so-2852

zial benachteiligte Schülerinnen und Schüler. Diese Initiative wollen wir stärken und so 2853

weiterentwickeln, dass Schulen bestmöglichste individuelle Förderung anbieten können.

2854

 

2855

Nach Corona durchstarten

2856

Viele Kinder und Jugendliche wurden in der Corona-Pandemie in ihrer Entwicklung beson-2857

ders beeinflusst. Vor allem die Lernschwächeren brauchen Aufmerksamkeit, damit sie Rück-2858

stände aufholen und ihre Lernmotivation zurückgewinnen können.

Seite 80 von 139

2859

• Damit niemand zurückbleibt, haben wir ein Unterstützungsprogramm für die Jahre 2021

2860

und 2022 in Höhe von einer Milliarde Euro aufgelegt. Es gilt, sowohl ihre Lese- und 2861

Sprachkompetenz als auch ihre Lesefreude zu stärken.

2862

• Gemeinsam mit den Ländern und den Hochschulen rufen wir Lehramtsstudierende, Se-2863

niorlehrkräfte, Anbieter von Nachhilfeleistungen und Volkshochschulkräfte auf, schul-2864

begleitend sowie während der Ferien die Kinder und Jugendlichen zielgenau beim Auf-2865

holen zu unterstützen.

2866

• Mit einer weiteren Milliarde Euro helfen wir Kindern und Jugendlichen, die sozialen und 2867

psychischen Folgen der Corona-Pandemie zu bewältigen. Die Mittel investieren wir in 2868

frühe Bildung, Ferienfreizeiten, Familienerholung und zusätzliche Sozialarbeit.

2869

• Hinzu kommt eine Einmalzahlung in Höhe von 100 Euro für Kinder aus Familien, die auf 2870

Hartz IV angewiesen sind oder nur ein geringes Einkommen haben.

2871

 

2872

Digitale Bildung stärken

2873

Es ist die Aufgabe unserer Bildungseinrichtungen, Kinder und Jugendliche zu selbstbe-2874

stimmten und verantwortungsbewussten Persönlichkeiten heranzubilden. Dazu benötigen 2875

sie Fachwissen und Kompetenzen genauso wie Wertebewusstsein und Urteilskraft. Hinzu 2876

kommen Team- und Kollaborationsfähigkeit, Resilienz, Kreativität, Forscher- und Gründer-2877

geist sowie problemlösungsorientiertes und kritisches Denken.

2878

• Wir wollen, dass die Schülerinnen und Schüler das lebensbegleitende Lernen, insbeson-2879

dere die Fort- und Weiterbildung, als permanente, eigenverantwortlich wahrzuneh-2880

mende Aufgabe begreifen. Dazu gehört eine Lernumgebung, die ihre Kompetenzen för-2881

dert.

2882

• Wir wollen, dass pädagogische Konzepte und die Ausbildung von Lehrerinnen und Leh-2883

rern weiterentwickelt werden. Digitale Kompetenz muss umfassend in den Unterricht 2884

integriert werden. Wir wollen bundesweite Bildungskompetenzzentren mit dem Ziel auf-2885

bauen, lehrerbildende Hochschulen, Forschungsinstitute und Lehrerfortbildungseinrich-2886

tungen in den Ländern zu vernetzen und Erkenntnisse der Bildungsforschung direkt für 2887

Lehrerbildung praktisch nutzbar zu machen. Die erfolgreich etablierte Qualitätsoffen-2888

sive Lehrerbildung soll, was die Inhalte betrifft, weiterentwickelt werden.

2889

• Neben den Kulturtechniken Lesen, Schreiben und Rechnen benötigen die Schülerinnen 2890

und Schüler digitale Kompetenzen. Diese umfassen ein technisches und informatisches 2891

Grundverständnis ebenso wie Medienkompetenz. Dabei geht es insbesondere um die 2892

Fähigkeit, Medien zu nutzen, Inhalte sowie die Funktionsweise von digitalen Technolo-2893

gien und künstlicher Intelligenz zu bewerten.

2894

• Wir werden die politische Bildung in allen Jahrgangsstufen der allgemeinbildenden und 2895

beruflichen Schulen stärken. Unsere rechtsstaatlich verfasste, freiheitliche, plurale und 2896

repräsentative Demokratie ist nicht selbstverständlich. Sie muss stets aufs Neue erlernt, Seite 81 von 139

2897

gelebt und verteidigt werden. Dazu brauchen wir überzeugte Demokratinnen und De-2898

mokraten, die sich den komplexen Anforderungen der Welt im 21. Jahrhundert stellen.

2899

• Soziale Netzwerke wie Facebook, Instagram oder TikTok senken die Hemmschwelle, 2900

Mitschülerinnen und Mitschüler herabzuwürdigen oder zu bedrohen. Aufgabe von 2901

Schule, Eltern und Gesellschaft ist es, aktiv gegen diese Formen des Cybermobbings und 2902

Cyberbullyings vorzugehen.

2903

 

2904

Gleichwertigkeit der Bildungssysteme garantieren

2905

Die Gleichwertigkeit von beruflicher und akademischer Bildung ist uns ein Herzensanlie-2906

gen. Daher werden wir wieder mehr Gewicht auf die Ausbildung junger Menschen als Fach-2907

arbeiter und Handwerker legen, um dem Fachkräftemangel in diesen Bereichen wirksam zu 2908

begegnen.

2909

• Eine Karriere in der beruflichen Bildung muss als gleichwertige Alternative zum Studium 2910

für jeden und jede erkennbar sein. Der Deutsche Qualifikationsrahmen (DQR) hat sich 2911

als bildungspolitisches Transparenzinstrument bewährt.

2912

• Duale Studiengänge leisten einen wichtigen Beitrag bei der Verknüpfung von beruflicher 2913

und akademischer Qualifizierung. Wir wollen sie weiter ausbauen, vor allem in den Inge-2914

nieurwissenschaften, Informatik, Betriebswirtschaftslehre sowie in den Sozial- und Ge-2915

sundheitswissenschaften.

2916

 

2917

Nationale Bildungsplattform aufbauen

2918

Im Transformationsprozess wächst die Bedeutung digitaler Lehr- und Lernangebote. Daher 2919

wollen wir bestehende und neue digitale Bildungsplattformen zu einem bundesweiten und 2920

europäisch anschlussfähigen Plattform-System verknüpfen.

2921

• Die Plattform ist Kernstück eines neuen digitalen Bildungsraums für Deutschland und 2922

einer Modernisierung der Bildung insgesamt. Es geht darum, allen Menschen – vom 2923

Schulkind bis zum Rentner – den Zugang zu digital gestützten Bildungsangeboten zu er-2924

leichtern.

2925

• Einen Schwerpunkt legen wir auf Weiterbildung und lebensbegleitendes Lernen. Es geht 2926

um das passende Angebot, das alle schnell finden und sicher nutzen können.

2927

• Für die Entwicklung von Prototypen, Curricula und didaktischen Konzepten stellen wir 2928

in einem ersten Schritt 150 Millionen Euro bereit.

2929

 

2930

Weiterbildungsförderung attraktiver gestalten

2931

Der weitaus größte Teil der Weiterbildung findet heute während der bezahlten Arbeitszeit 2932

statt. Unternehmen und Beschäftigte haben erkannt, dass dies für zukunftsfähige Arbeits-2933

plätze unerlässlich ist, vor allem mit Blick auf die Geschwindigkeit, in der sich der techno-2934

logische Wandel vollzieht.

Seite 82 von 139

2935

• Um die Beschäftigten mit den benötigten Zukunftskompetenzen auszustatten, wollen 2936

wir das Bundesprogramm Bildungsprämie ausbauen.

2937

• Zudem unterstützen wir Unternehmen und Beschäftigte im Strukturwandel mit passge-2938

nauen Informations- und Beratungsangeboten zur Weiterbildung.

2939

• Eine entsprechend vorausschauende Forschung zur Kompetenzentwicklung werden wir 2940

fördern.

2941

 

2942

BAföG und Aufstiegs-BAföG modernisieren

2943

Angesichts der sich rasch wandelnden Qualifikationsanforderungen kommt vor allem dem 2944

lebensbegleitenden Lernen eine Schlüsselrolle zu.

2945

• Wir wollen das BAföG flexibilisieren und zu einem Instrument der individuellen Förde-2946

rung des Lebensunterhalts von Bildung und Weiterbildung im Lebensverlauf weiterent-2947

wickeln.

2948

• Wer nach dem Bachelor-Abschluss zunächst Berufserfahrungen sammelt und erst später 2949

einen Master erwirbt, soll nach einer elternunabhängigen Einkommens- und Vermögen-2950

sprüfung künftig auch nach Vollendung des 35. Lebensjahres BAföG erhalten können.

2951

Dazu erweitern wir den Zweck des BAföG um eine zweite Berufsausbildung und ersetzen 2952

die bestehenden Altersgrenzen durch Höchstgrenzen.

2953

• Die Rückzahlung des Darlehens sowie ein angemessener sozialer und wirtschaftlicher 2954

Nutzen für den Zuschussanteil müssen vor Renteneintritt gegeben sein.

2955

• Wir wollen das Aufstiegs-BAföG fortentwickeln. Dass sich Arbeitnehmerinnen und Ar-2956

beitnehmer sowie Selbstständige auch während ihres Berufs weiterqualifizieren können, 2957

ist ein Schlüssel zur Chancengerechtigkeit sowie zur Gleichwertigkeit von beruflicher 2958

und akademischer Bildung. Mit dem Aufstiegs-BAföG adressieren wir sowohl die Le-2959

benswirklichkeit jedes einzelnen Menschen – insbesondere junger Familien – als auch 2960

die dynamische Entwicklung des Bildungswesens.

2961

 

2962

Vorfahrt für Alphabetisierungskurse

2963

Erwachsene, die Schwierigkeiten beim Lesen und Schreiben haben, sind häufig in Familien 2964

aufgewachsen, in denen nicht oder viel zu wenig vorgelesen wurde. Für sie bedeutet es eine 2965

unüberwindbare Hürde, ihren Kindern bei den Hausaufgaben zu helfen oder die Packungs-2966

beilage eines Medikaments zu lesen.

2967

• Wir sprechen uns dafür aus, dass allen Menschen ein Platz in einem Alphabetisierungs-2968

kurs angeboten werden muss. Unser Ziel ist ein Land, in dem jeder Einzelne lesen und 2969

schreiben kann.

2970

 

 

Seite 83 von 139

2971

7. Neuer Mut zur Innovation – aus Verantwortung für die Zukunft 2972

 

2973

Unser Unions-Versprechen: Wir schnüren ein Zukunftspaket für Deutschland, indem wir Inno-2974

vationen und neue Technologien konsequent fördern. Wir werden für eine neue Innovations-, 2975

Forschungs- und Gründerkultur sorgen, auch indem wir diesen Zukunftsfragen einen nie ge-2976

kannten neuen Stellenwert in der neuen Bundesregierung einräumen.

2977

Wir stehen dabei vor zwei Herausforderungen: Zum einen brauchen wir Innovationen und For-2978

schung mehr denn je, um im internationalen Wettbewerb um Märkte, Möglichkeiten und kluge 2979

Köpfe weiter erfolgreich zu sein. Dazu gehört, dass wir es auch wieder schaffen, dass Ideen 2980

„Made in Germany” auch zur Wertschöpfung „Make in Germany” führen.

2981

Zum anderen entsteht Zukunft nicht allein durch Förderprogramme und Gesetzestexte, sondern 2982

wir brauchen eine neue, starke Innovationskultur, in der gilt: Vorfahrt für Mut, Experimente, 2983

neue Ideen und neue Gründungen! Und in der auch gilt: Keine Angst vor Fehlern. Innovationen 2984

entstehen schließlich dann am besten, wenn der Staat sich nicht zu stark einmischt, sondern vor 2985

allem für beste Rahmenbedingungen sorgt.

2986

 

2987

7.1. Strategische Forschungs- und Innovationspolitik für Deutschland 2988

Globale Herausforderungen erfordern heute mehr denn je eine weitsichtige, verlässliche 2989

Forschungs- und Innovationspolitik: Dank exponentiell gewachsener Rechenleistungen und 2990

der globalen Vernetzung stehen wir vor einer Dekade technologischer Durchbrüche – in der 2991

Medizin, der Ernährung, der Raumfahrt oder der Robotik. Wichtig ist uns dabei, dass wir die 2992

Innovationen technologieoffen vorantreiben und das Potenzial der Wissenschaft voll nut-2993

zen, um die ganze Bandbreite an Möglichkeiten aufzuzeigen und zu erproben – immer unter 2994

Wahrung unserer ethischen Verantwortung. Die neuen Chancen für wirtschaftliche Dyna-2995

mik, Wohlstand und sozialen Zusammenhalt müssen wir jetzt ergreifen. Es liegt an uns allen 2996

– den Bürgerinnen und Bürgern, den Forschenden und den Unternehmen – die Chancen für 2997

intelligentes Wachstum zu nutzen, Lösungen für die großen Herausforderungen zu entwi-2998

ckeln und umzusetzen.

2999

• Zentral ist dabei unser Ziel, dass Wirtschaft und Staat bis 2025 3,5 Prozent des Bruttoin-3000

landsprodukts für Forschung und Entwicklung aufwenden.

3001

• Wir haben die steuerliche Forschungszulage während der Corona-Krise verdoppelt. Jetzt 3002

werden wir noch einmal nachlegen und die Bemessungsgrundlage auf 8 Millionen Euro 3003

pro Unternehmen erneut verdoppeln – für Innovationskraft x 4.

3004

• Deutschlands Ideen brauchen finanzielle Unterstützung, um daraus Innovationen im 3005

Weltmaßstab zu machen. Um Investitionen in Technologie und Innovationen von klei-3006

nen- und mittelständischen Unternehmen in der Wachstumsphase zu fördern, wollen wir 3007

die Anwendung eines Modells für Vorzugskapital (preferred equity) prüfen.

3008

• Wir werden die Exzellenzstrategie fortführen und für erfolgreiche Cluster neue Möglich-3009

keiten der dauerhaften institutionellen Förderung schaffen. Wir bekennen uns zu einem 3010

der wichtigsten Instrumente der Wissenschaftsförderung, dem Pakt für Forschung und Seite 84 von 139

3011

Innovation (PFI). Bund und Länder haben damit finanzielle Planungssicherheit für ein 3012

stabiles Wachstum und eine positive Entwicklung der außeruniversitären Wissenschafts-3013

organisationen geschaffen.

3014

• Wir nutzen dieses Instrument, um die Fraunhofer-Gesellschaft, die Helmholtz-Gemein-3015

schaft Deutscher Forschungszentren, die Leibniz-Gemeinschaft und die Max-Planck-Ge-3016

sellschaft gezielt zu unterstützen. Auf diese Weise stärken wir den Wissenschaftsstand-3017

ort Deutschland und verbessern seine internationale Wettbewerbsfähigkeit. Mit zusätz-3018

lichen Leistungskomponenten wollen wir exzellenten wissenschaftlichen Leistungen 3019

noch mehr Anerkennung verleihen. Darüber hinaus wollen wir exzellente Universitäten 3020

weiter kraftvoll unterstützen. Unser Ziel ist: mindestens eine deutsche Universität in die 3021

Top 20 der Welt zu bringen.

3022

 

3023

Projektförderung stärken

3024

Wir wollen die themen- und technologieoffene Projektförderung stärken, die vor allem für 3025

den Mittelstand wichtig ist.

3026

• Dazu werden wir die bewährten Programme ausweiten, insbesondere das Zentrale In-3027

vestitionsprogramm Mittelstand (ZIM), die Industrielle Gemeinschaftsforschung (IGF) 3028

und das Förderprogramm Innovationskompetenz INNO-KOM.

3029

• Anstelle von Kostenzuschüssen wollen wir einen Teil der Förderung von den erzielten 3030

und im Unternehmen verbliebenen Gewinnen abhängig machen. Damit verhindern wir 3031

Fehlanreize. Denn für uns gilt: Das Ergebnis soll belohnt werden, nicht der Prozess.

3032

 

3033

Mission Quantencomputer „Made in Germany“ starten

3034

Der sichere Umgang und die Verfügbarkeit von Quanten-Technologien der neuesten Gene-3035

ration bieten enorme Innovationspotenziale. Die Quantenkommunikation stellt einen 3036

neuen Sicherheitsstandard für die digitale Kommunikation sowie die IT-Infrastruktur dar.

3037

Quantenbasierter Kommunikation und Kryptografie gelingt es, sensible Daten bei Banken, 3038

Versicherungen, im Gesundheitssystem und bei kritischen Infrastrukturen noch besser zu 3039

schützen. In der Medizintechnik ermöglichen optimierte Abbildungsverfahren Fortschritte 3040

beispielsweise in der Krebserkennung.

3041

• Wir wollen bis 2025 in Deutschland einen konkurrenzfähigen Quantencomputer bauen.

3042

Damit dieses Vorhaben gelingt, müssen Forschung und Wirtschaft eng zusammenarbei-3043

ten. Zugleich setzen wir auf Kooperationen mit anderen führenden EU-Staaten und tra-3044

gen so dazu bei, unsere technologische Souveränität im Bereich der Quantentechnolo-3045

gien zu sichern.

3046

• Wir werden zusammen mit allen Partnern die Aus- und Weiterbildung zum Thema Quan-3047

tentechnologien voranbringen, indem frühzeitig Fachkenntnisse und Ausbildungsziele 3048

mit Bezug zu industriellen Anwendungen erhoben werden.

Seite 85 von 139

3049

• Deutschland soll internationaler Spitzenreiter bei Rechner- und Softwaretechnologien 3050

bleiben und als Standort der Grundlagenforschung mit einem trans- und interdisziplinä-3051

ren Ansatz wachsen. Deshalb wollen wir Hoch- und Höchstleistungsrechnen (High Per-3052

formance Computing) weiter ausbauen.

3053

 

3054

Deutschland zur Hochburg für Künstliche Intelligenz und Blockchain-Technologie entwi-

3055

ckeln

3056

Mit der KI-Strategie haben wir die Grundlage geschaffen, um Deutschland und Europa an 3057

die Weltspitze der Forschung und Anwendung von Künstlicher Intelligenz zu bringen. Dazu 3058

fördern wir die Spitzenforschung in den KI-Kompetenzzentren und stärken die Entwicklung 3059

von KI auf zentralen Anwendungsfeldern, wie der Arbeits-, Mobilitäts- oder Gesundheits-3060

forschung.

3061

• Erfolgreiche KI ist auf die Verfügbarkeit von Rechenleistung angewiesen. Das gelingt 3062

nur, wenn wir den Aufbau eigener Fähigkeiten für Forschung und Entwicklung sowie für 3063

Fertigung von Mikroelektronik stärker forcieren. Dazu werden wir technologische Ent-3064

wicklung und Produktion strategisch verzahnt entwickeln und im Aufbau unterstützen.

3065

• Wir werden gezielt neue KI-Professuren einrichten und den wissenschaftlichen Nach-3066

wuchs fördern, um die weltweit klügsten Köpfe an den KI-Forschungsstandort Deutsch-3067

land zu holen. Dazu wollen wir auch weitere KI-Campus mit attraktiven Bedingungen 3068

schaffen. Dabei gilt es sicherzustellen, dass jedes im KI-Campus entwickelte Patent in 3069

Deutschland bleibt. Damit schaffen wir die Grundlage für einen Innovationssprung bei 3070

der KI.

3071

• Wir wollen auch kleine und mittlere Unternehmen befähigen, Ergebnisse aus der KI-For-3072

schung besser zu nutzen. Dazu sollen KI-Lotsen die Unternehmen vor Ort aufsuchen und 3073

bei der Entwicklung ihrer KI-Potenziale unterstützen.

3074

• Wir haben bereits in der aktuellen Wahlperiode mit der Blockchain-Strategie gute 3075

Grundlagen geschaffen, die wir weiterentwickeln werden. Dazu wollen wir weitere An-3076

wendungsmöglichkeiten für die Blockchain schaffen. Oftmals scheitern heute neue An-3077

wendungen an rechtlichen Hindernissen, obwohl es technologisch sinnvoll und effizient 3078

wäre, Blockchain zu nutzen.

3079

 

3080

Zukunftstechnologie Raumfahrt fördern

3081

Raumfahrt ist eine Schlüsselindustrie der Zukunft – gerade für die Digitalisierung unseres 3082

Landes liegt im Orbit unseres Planeten ein großes Potenzial.

3083

• In den kommenden Jahren werden kleine Satelliten bei der Erdbeobachtung, der Um-3084

welt- und Klimaforschung sowie bei allen Big Data-Projekten immer stärker zunehmen.

3085

Wir unterstützen dabei das Copernikus-Programm. Als engagierte Weltraumnation set-3086

zen wir nicht nur auf etablierte Raumfahrtunternehmen aus Deutschland, sondern vor 3087

allem auch auf den Aufbau eines Newspace-Ökosystems und den starken deutschen 3088

Raumfahrtmittelstand.

Seite 86 von 139

3089

• In den letzten Jahren ist eine deutsche Industrie für kleine Launcher (Raketen) entstan-3090

den. Wir wollen diesen Markt für unser Land erschließen. Dazu gehört staatliche Nach-3091

frage im Rahmen einer Kleinsatelliteninitiative, der Zugang zu allen EU- und ESA-Start-3092

programmen, Raumfahrtfonds im Rahmen des Zukunftsfonds und ein offener Wettbe-3093

werb für die europäischen Träger der nächsten Generation.

3094

• Wir werden ein Weltraumgesetz beschließen, das gründer- und mittelstandsfreundlich 3095

ist.

3096

• Wir werden uns auf internationaler Ebene für eine nachhaltige Nutzung des Weltraums 3097

einsetzen, um auch nächsten Generationen den Zugang zum All zu ermöglichen.

3098

 

3099

Reallabore ausbauen

3100

Für neue Technologien und Innovationen, wie Künstliche Intelligenz, Bio-IT oder Quanten, 3101

müssen passgenaue Rahmenbedingungen und Regulierungsansätze entwickelt und erprobt 3102

werden.

3103

• Hierzu wollen wir zusätzliche Kapazitäten für Experimentierräume und Reallabore be-3104

reitstellen, ihre Finanzierung und Bewerbung stärken und über die Energieforschung 3105

hinaus auch andere Bereiche fördern.

3106

 

3107

Nationale Agentur für biomedizinische Forschung und Entwicklung gründen

3108

Die jüngsten Erfolge in der Impfstoffentwicklung knüpfen an die Tradition von herausra-3109

genden deutschen Forschern und Nobelpreisträgern, wie Robert Koch und Paul Ehrlich, an.

3110

Wir werden Deutschland wieder zu einer modernen Apotheke der Welt machen.

3111

• Dazu wollen wir im Modernisierungsjahrzehnt bis 2025 eine nationale Agentur für bio-3112

medizinische Forschung und Entwicklung gründen, die dabei hilft, Wertschöpfungsket-3113

ten von der Forschung bis zum Markt für Therapien, Impfstoffe und Medikamente zu 3114

bündeln und zu vernetzen.

3115

• Wir beschleunigen Zulassungsprozesse und sorgen dafür, dass die Patienten deutlich 3116

schneller von den Forschungserfolgen profitieren.

3117

 

3118

Biologie und Technik vereinen

3119

Wenn Biowissenschaften und Informationstechnologien zusammenwirken, kann das be-3120

deutende Innovationen hervorbringen: neue Behandlungsmöglichkeiten in der personali-3121

sierten Medizin oder visionäre Projekte in der IT, wie die digitale Datenspeicherung in DNA 3122

oder den 3D-Druck von biologischem Gewebe.

3123

• Um den Transfer von der Forschung in die Anwendung zu beschleunigen, wollen wir ein 3124

Bio-IT-Forschungszentrum aufbauen. Es soll Software, Methoden und Datenbestände in 3125

Deutschland und Europa miteinander verbinden und die Forschung auf internationalem 3126

Niveau vorantreiben.

Seite 87 von 139

3127

• Im Bio-IT-Zentrum werden Grundlagenforschung, anwendungsnahe Technologieent-3128

wicklung und Wirtschaft zusammenarbeiten und so Bio-IT-relevante Cluster bilden, die 3129

über erhebliches Industrie-Knowhow verfügen.

3130

 

3131

Das Potenzial sozialer Innovationen nutzen

3132

Um Herausforderungen durch Urbanisierung, Alterung oder Zuwanderung zu bewältigen, 3133

brauchen wir Offenheit für soziale Innovationen („Open Social Innovation“). Soziale Dienst-3134

leistungen wie Nachbarschaftshilfen und Beteiligungsplattformen zur Einbindung der An-3135

wohner können helfen, den Zusammenhalt zu stärken.

3136

• Wir wollen das Ehrenamt mit der digitalen Welt zusammenbringen und setzen deshalb 3137

auf ehrenamtliche Digitalbotschafterinnen und Digitalbotschafter. Sie geben ihre digi-3138

tale Expertise ehrenamtlich weiter und tragen so mit dazu bei, dass die Digitalisierung in 3139

der Breite der Gesellschaft im Alltag ankommt.

3140

• Wir werden die Hightech-Strategie durch eine soziale Innovationsstrategie ergänzen, 3141

um soziale und technologische Innovationen besser miteinander zu verzahnen.

3142

• Entsprechend werden wir Finanzierungsinstrumente, wie das EXIST-Gründerprogramm, 3143

den High-Tech Gründerfonds oder den INVEST-Zuschuss für Sozialunternehmen öffnen, 3144

auf ihre Besonderheiten abstimmen sowie zusätzliche Vernetzungs- und Beratungsan-3145

gebote bereitstellen.

3146

 

3147

Mehr Tempo und Freiräume für SPRIND schaffen

3148

Mit der Förderung von Sprunginnovationen, also der Entwicklung bahnbrechender neuer 3149

Technologien, wollen wir Deutschland an die Weltspitze heranführen.

3150

• Wir werden die 2019 gegründete Agentur für Sprunginnovationen (SPRIND) ressortun-3151

abhängig aufstellen und zu einem Reallabor ausbauen – mit flexiblen und agilen Instru-3152

menten zur Identifizierung, Entwicklung und Finanzierung von vielversprechenden Inno-3153

vationsprojekten.

3154

• Wir werden einen Globalhaushalt garantieren, die Agentur aus dem Gehaltsgefüge des 3155

öffentlichen Dienstes entlassen, von Vergaberegelungen in der Projektfinanzierung be-3156

freien und ermöglichen, Projekte in der vorwettbewerblichen Frühphase vollumfänglich 3157

zu fördern und sich an ihnen als Minderheitsgesellschafterin zu beteiligen.

3158

 

3159

Wissensintensive Gründungen mit dem Innovationsfreiheitsgesetz erleichtern

3160

Die Wissenschaft trägt mit ihrem Transfer von Ideen und Erfindungen in die Wirtschaft zur 3161

Innovations- und Wettbewerbsfähigkeit Deutschlands bei. Daher wollen wir gelungenen 3162

Transfer als Kategorie guter Wissenschaft etablieren.

Seite 88 von 139

3163

• Wir werden Technologiebiotope schaffen, die die weltweit besten Köpfe und innovativs-3164

ten Unternehmen anziehen und aus sich selbst heraus durch Exzellenz, gelebter Grün-3165

derkultur und Innovationen weltweit sichtbar wachsen. Hierfür garantieren wir Hand-3166

lungsfreiheit und eine verlässliche Grundfinanzierung, die weltweit einmalig sind.

3167

• Wir werden die konkreten Bedingungen für Ausgründungen verbessern: Mit einem In-3168

novationsfreiheitsgesetz wollen wir für Gründerinnen und Gründer aus Wissenschafts-3169

einrichtungen und Hochschulen bürokratische Hürden abbauen, vor allem im Beihilfe-3170

und Gemeinnützigkeitsrecht. Unterstützungsleistungen in der Phase vor der Gründung 3171

könnten so gemeinnützig durchgeführt werden, darunter Beratungsleistungen, Nutzung 3172

der Infrastruktur und die Erstellung von Machbarkeitsnachweisen.

3173

• Wir werden bürokratische Innovationsbarrieren überwinden, hierzu eine agile und funk-3174

tionale Administration aufstellen und in der Bundesregierung ein modernes Prozessma-3175

nagement etablieren, um Silodenken zu vermeiden.

3176

 

3177

Forschungskerne stärken und Schlüsseltechnologien schützen

3178

Wir wollen Ansiedlungen von Forschungseinrichtungen, auch aus der Wirtschaft und in Ost-3179

deutschland, weiter fördern. Grundlagenforschung und anwendungsorientierte Forschung 3180

verdienen gleichermaßen unser Augenmerk.

3181

• Wir werden Forschungsverbünde weiter finanziell unterstützen und Exzellenz stärken.

3182

• Das gilt vor allem für Schnittstellen für den Wissenstransfer aus Hochschulen und For-3183

schungseinrichtungen. Ausgründungen und Scale-ups wollen wir gezielt finanziell und 3184

rechtlich erleichtern.

3185

• EU-Restriktionen beim Transfer von Wissenschaft zur industriellen Anwendung wollen 3186

wir überwinden.

3187

• Um unser Wissen zu schützen, brauchen wir klare Regeln für Investoren aus Drittstaaten.

3188

Wir müssen uns entschlossen den Versuchen zu feindlichen Übernahmen von Patenten 3189

und Lizenzen deutscher Unternehmen entgegenstellen.

3190

 

3191

7.2. Die besten Köpfe für unser Land

3192

Attraktivitätsoffensive für die klügsten Köpfe aufsetzen

3193

Wir werden die Programme zur gezielten Ansprache und Gewinnung von herausragenden 3194

internationalen Wissenschaftlerinnen und Wissenschaftlern weiter ausbauen.

3195

• Wir unterstützen den Vorschlag auf europäischer Ebene, ein neues Tech-Visums-Pro-3196

gramm für hochqualifizierte Fachkräfte aufzusetzen, um die besten Köpfe der Welt ein-3197

facher nach Europa zu holen.

3198

• Wir werden die Förderung der Alexander-von-Humboldt-Stiftung (AvH), der Deutschen 3199

Forschungsgemeinschaft (DFG) und des Deutschen Akademischen Austauschdienstes 3200

(DAAD) ausbauen. Die Deutschen Schulen im Ausland werden wir in ihrer Arbeit stärken.

Seite 89 von 139

3201

• Internationalen Wissenschaftlerinnen und Wissenschaftlern wollen wir insbesondere 3202

nach der Promotion bessere Karriere- und Bleibeperspektiven in Deutschland bieten.

3203

Dazu müssen wir auch den Mut haben, bestehende Strukturen zu ändern und mehr Fle-3204

xibilität zu ermöglichen als bisher.

3205

• Herausragende Spitzenwissenschaftler und Innovationsträger wollen wir in unserem 3206

Land mit attraktiven Bedingungen halten.

3207

• Exzellente Forscherinnen und Forscher müssen über Senior Research-Programme die 3208

Möglichkeit haben – unabhängig von Ruhestandsgrenzen – ihr Potential in Deutschland 3209

weiter zur Geltung zu bringen.

3210

• Wir wollen die Wissenschaftskommunikation durch mehr Weiterbildungsangebote für 3211

Forschende ebenso wie Bürgerwissenschaftlerinnen und -wissenschaftler (Citizen Sci-3212

ence Formate) stärken.

3213

 

3214

Gründergeist wecken

3215

Die erfolgreichen Unternehmen von morgen müssen bereits heute bei uns gegründet wer-3216

den – das hat Deutschland stark gemacht. Gründerinnen und Gründer schaffen mit neuen 3217

Ideen neue Arbeitsplätze und neuen Wohlstand. Das Modernisierungsjahrzehnt soll daher 3218

auch ein Gründungsjahrzehnt werden. 2022 werden wir als Startschuss zum Deutschen 3219

Gründerjahr machen. Dazu gehört die Kultur einer zweiten Chance, denn Gründungen kön-3220

nen auch fehlschlagen. Wir wollen einen neuen Gründergeist von klein auf befördern und 3221

mehr Frauen zu Gründungen ermutigen.

3222

• Wir werden Unternehmensgründungen innerhalb von 24 Stunden online ermöglichen 3223

und dabei die Sicherheit im Rechtsverkehr wahren. Wir schaffen die besten Bedingungen 3224

für unsere Macherinnen und Macher.

3225

• Wir haben bereits den Meilenstein Zukunftsfonds I auf den Weg gebracht, der mindes-3226

tens 30 Milliarden Euro mobilisieren wird. Wir benötigen jetzt einen Rahmen, der grö-3227

ßere europäische Investitionen ermöglicht. Daher wollen wir den Zukunftsfonds auswei-3228

ten. Dazu gehört auch der Ausbau von Wagniskapital- bzw. Beteiligungsfinanzierungen 3229

für technologieorientierte Jungunternehmen.

3230

• Die steuerlichen und administrativen Hürden für die Niederlassung großer Venture Ca-3231

pital Fonds in Deutschland werden wir abbauen. Gleichzeitig wollen wir die Anlagebe-3232

dingungen für Versicherungsunternehmen und Pensionsfonds so verändern, dass sie 3233

sich stärker in Wagniskapital- und Beteiligungsfinanzierung engagieren können.

3234

• Unser Ziel ist, dass Beteiligungen an Startups erst dann besteuert werden, wenn aus den 3235

Beteiligungen Gewinne erzielt oder die Anteile veräußert werden. Wir wollen auch die 3236

Praktikabilität der Übertragung von Anteilen an Mitarbeiter deutlich verbessern. Dafür 3237

wollen wir eine eigene Anteilsklasse schaffen. Für die Weltspitze braucht es kluge und 3238

innovative Köpfe aus dem In- und Ausland. Die Beteiligung am Unternehmen ist in vielen 3239

Startups ein wichtiger Teil der Mitarbeiterbindung.

Seite 90 von 139

3240

• Wir setzen uns dafür ein, dass die Europäische Union die Rahmenbedingungen für den 3241

Digitalen Binnenmarkt weiter verbessert und Netzwerke schafft, um jungen Unterneh-3242

men die Skalierung ihrer Geschäftsmodelle zu erleichtern.

3243

 

 

Seite 91 von 139

3244

Nachfolge im Betrieb einfacher regeln

3245

Nachfolgeregelungen sind für uns wesentlicher Bestandteil der Gründungspolitik. Wir wol-3246

len mittelständische und familiär geführte Unternehmen, gerade im Handwerk, bei Be-3247

triebsübergaben unterstützen.

3248

• Dazu wollen wir bürokratische und gesetzliche Hürden reduzieren, Betriebsnutzungsge-3249

nehmigungen erleichtern und die Weiternutzung von Kundendaten nach Betriebsüber-3250

nahme vereinfachen.

3251

• Um den Erwerb der Unternehmensanteile durch eigene Mitarbeiter des Unternehmens 3252

zu erleichtern, ist die Mitarbeiterkapitalbeteiligung ein wichtiger Baustein. Die Finanz-3253

behörden sollten bei Beteiligungen die üblichen Bewertungsverfahren anwenden und 3254

realistische Marktpreise ermitteln.

3255

• Wir wollen auch Steuerentlastungen bei Unternehmensübergaben prüfen. Die Unter-3256

nehmensbörse nexxt-change wollen wir als Instrument für Nachfolger und Übergeber 3257

optimieren, sodass es zu keiner kostenpflichtigen Vermittlung oder Beratungsaufträgen 3258

kommt.

3259

 

3260
7.3 Digitale Transformationsoffensive

3261

Die digitale Transformation von Wirtschaft und Gesellschaft bietet enorme Chancen – 3262

wenn wir sie aktiv gestalten. Digitalisierung darf nicht als Ziel, sondern muss als Instrument 3263

verstanden werden, den Wohlstand in Deutschland und Europa zu bewahren und zu stei-3264

gern.

3265

 

3266

Plattformen als Kern der digitalen Wirtschaft befördern

3267

Digitale Plattformen sind ein zentraler Baustein der digitalen Wirtschaft, weil sie als 3268

Schnittstellen fungieren und Wachstum befördern. Darum tragen sie eine besondere Ver-3269

antwortung für den Wettbewerb. Mit dem Digitalisierungs-GWB haben wir als erstes Land 3270

der Welt einen neuen, zukunftsfähigen Rechtsrahmen geschaffen, der Tech-Giganten in die 3271

Schranken weist und gleiche Wettbewerbsbedingungen herstellt. Damit sichern wir den fai-3272

ren Wettbewerb, die Innovationskraft unserer Unternehmen und die Wahlfreiheit der Ver-3273

braucher in der Digitalwirtschaft. Dies wollen wir auch auf EU-Ebene über den Digital Ser-3274

vices Act und den Digital Markets Act gewährleisten.

3275

• Wir treten dabei für eine Gesetzgebung ein, die nutzerzentriert ist, kleinen und mittleren 3276

Unternehmen faire Bedingungen im digitalen Wettbewerb garantiert und Raum für In-3277

novationen schafft.

3278

• Wir werden den Rechtsrahmen für digitale Dienste mit besonderem Blick für die Platt-3279

formökonomie weiterentwickeln. Ziel ist, die besten Bedingungen für die Bereitstellung 3280

innovativer digitaler Dienste in Europa zu schaffen und einen Beitrag zur Online-Sicher-3281

heit und zum Schutz der Grundrechte zu leisten. Außerdem wollen wir eine solide und Seite 92 von 139

3282

dauerhafte Verwaltungsstruktur für die wirksame Beaufsichtigung der Anbieter von Ver-3283

mittlungsdiensten aufbauen. Dazu brauchen wir klare Verantwortlichkeiten, eine Re-3284

chenschafts- und Sorgfaltspflicht, einschließlich Melde- und Abhilfeverfahren für illegale 3285

Inhalte.

3286

• Sehr große Online-Plattformen haben besondere Auswirkungen auf unsere Wirtschaft 3287

und Gesellschaft. Sie müssen daher noch transparenter sein und geeignete Risikoma-3288

nagement-Instrumente entwickeln, um die Integrität ihrer Dienste vor manipulativen 3289

Techniken zu schützen. Möglichkeiten zur Verpflichtung von Interoperabilität oder dem 3290

Teilen von Daten mit kleineren Wettbewerbern müssen ebenfalls geprüft werden.

3291

 

3292

Digitale Souveränität sicherstellen

3293

Freiheit und Selbstbestimmtheit sind Grundsätze unserer freiheitlich-demokratischen 3294

Grundordnung. Die Souveränität des Einzelnen und die Souveränität des Staates sind 3295

Grundlage für die starke Position Deutschlands und Europas in der Welt und für unseren 3296

Wohlstand. Wir müssen diese Souveränität auch digital sicherstellen und zu einem Parame-3297

ter unseres digitalpolitischen Handelns machen. Für uns bedeutet digitale Souveränität 3298

nicht Abschottung.

3299

• Wir brauchen eine kluge Balance aus Maßnahmen für mehr digitale Autonomie und dem 3300

Management verschiedener internationaler Handlungsoptionen, um die Risiken der di-3301

gitalen Abhängigkeit beherrschbar zu machen.

3302

• Wir setzen uns dabei für einen vitalen Marktort Europa ein, der seine globale Stärke 3303

nutzt, um technologische Weltstandards zu setzen und unsere digitalen Leistungen zu 3304

befördern – wie beispielsweise „AI made in Europe“.

3305

• Um selbstbestimmt handlungsfähig zu bleiben, braucht Europa auch ganz konkret wie-3306

der eigene Hard- und Softwarehersteller, die weltweit wettbewerbsfähig sind. Anbieter-3307

vielfalt schützt am besten vor Abhängigkeiten. Vertrauenswürdige Technologien ent-3308

scheiden dabei über den Erfolg.

3309

 

3310

Bundesministerium für digitale Innovationen und Transformation schaffen

3311

Damit unser Land effizient die digitalen und technologischen Herausforderungen bewältigt 3312

und die Modernisierung des Staates zentral koordiniert wird, werden wir ein eigenes Bun-3313

desministerium schaffen.

3314

• Es soll eine Umsetzungseinheit für konkrete digitalpolitische Projekte sein, wie beispiels-3315

weise für die Corona-App oder den elektronischen Personalausweis.

3316

• Es soll die zentrale politische Steuerungsstelle für Innovationen und Digitalisierung wer-3317

den, die die Modernisierung des Staates und der Verwaltung vorantreiben und eine Vor-3318

bild- und Testfeldrolle innerhalb der Bundesregierung durch den Einsatz neuer Arbeits-3319

methoden und Technologien einnehmen.

3320

 

Seite 93 von 139

3321

Datenschutz und Datenschatz modern denken

3322

Datenschutz und Datenschatz sind keine Gegensätze für uns, im Gegenteil: Wir wollen bei-3323

des modern und auf Höhe der Zeit denken. Noch wird das Potenzial von Daten nicht aus-3324

reichend ausgeschöpft – ob im Gesundheitsbereich, bei der Mobilität oder in der Verwal-3325

tung. Damit Daten wirklich zum Treiber für Innovation werden, müssen Dateninfrastruktu-3326

ren leistungsfähiger, die Datennutzung umfassender und der Datenaustausch intensiver 3327

werden. Dabei sind Datensicherheit und Datenschutz Grundpfeiler zur Sicherung von Ver-3328

trauen in digitale Lösungen. Datenschutz ist allerdings kein „Super-Grundrecht“. Eine über-3329

triebene Auslegung von Datenschutzanforderungen darf nicht dazu führen, Innovationen 3330

zu hemmen und Verfahren bürokratisch zu verlangsamen.

3331

• Wir wollen Rechtsunklarheiten beseitigen und Behördenstrukturen straffen. Wir werden 3332

die Datenschutzaufsicht in Deutschland harmonisieren. Es muss die Möglichkeit zu einer 3333

verbindlichen Auskunft geben. Dabei soll das Prinzip gelten: Einer genehmigt für alle – 3334

analog zum Medienrecht zur Lizensierung von Fernsehsendern.

3335

• Wir werden uns dafür einsetzen, dass eine bessere Abstimmung und eine vergleichbare 3336

Auslegung auf europäischer Ebene erfolgt.

3337

• Grundsätzliche Fragen sollen einmalig und EU-weit verbindlich auf europäischer Ebene 3338

entschieden werden. Darüber hinaus sollen rein nationale Fragen ebenfalls einheitlich 3339

und rechtsverbindlich auf nationaler Ebene entschieden werden. Dazu wollen wir die Zu-3340

sammenarbeit der Behörden verbessern.

3341

 

 

Seite 94 von 139

3342

8. Neue Leistungsfähigkeit für einen modernen Staat – zum Wohl der 3343

Bürgerinnen und Bürger

3344

Unser Unions-Versprechen: Wir werden für einen verlässlichen, leistungsfähigen Staat sorgen 3345

und die Verwaltung einfacher und nutzerfreundlicher machen. Wir werden mit einem neuen 3346

Geist an Probleme herangehen, um sie im Sinne der Bürgerinnen und Bürger zu lösen. Unsere 3347

Problemlösung wird pragmatisch und unbürokratisch sein. CDU und CSU stehen gemeinsam für 3348

neues Machen und neuen Mut anstatt wie andere von Regelungen und Gesetzen zu träumen.

3349

Staat und Verwaltung sind allzu oft nicht mehr auf der Höhe der Zeit: zu analog, zu bürokra-3350

tisch, zu langsam, zu wenig vernetzt und zu misstrauisch. Deutschland lähmt sich selbst und 3351

droht, den Anschluss zu verlieren.

3352

Die Pandemie hat schonungslos aufgezeigt, wo in unserem Land staatliche Strukturen besser 3353

werden müssen. Unser Staat braucht einen strukturellen Modernisierungsschub. Wir müssen vor 3354

allem die Chancen der Digitalisierung nutzen, um Verwaltungsverfahren für die Bürgerinnen 3355

und Bürger einfacher, unkomplizierter und kürzer zu gestalten. Unser Staat muss einfacher, 3356

schneller, digitaler und krisenfester werden. Der Staat geht uns alle an, das sind nicht „die Be-3357

amten“ oder „die da oben“. Der Staat ist das organisierte „Wir“. Daher wollen wir die Bürger 3358

ermutigen, mitzumachen bei dieser Modernisierung. Mit neuem Geist und neuem Schwung wol-3359

len wir das angehen, zusammen mit Ländern und Kommunen. Und gemeinsam mit den Ideen 3360

und dem Engagement der Mitarbeiterinnen und der Mitarbeiter im öffentlichen Dienst.

3361

Wir wollen einen Staat, dem Bürger vertrauen und der sein Schutzversprechen auch in schwieri-3362

gen Situationen einlöst. Die Bewältigung der Corona-Krise hat die Stärken, aber auch die Schwä-3363

chen im Zusammenwirken der beteiligten Institutionen verdeutlicht. Deshalb wollen wir die ge-3364

wonnenen Erkenntnisse nutzen, um Aufgaben und Strukturen im Bevölkerungsschutz zu moder-3365

nisieren und weiterzuentwickeln.

3366

 

3367

8.1. Modernisierungsjahrzehnt für den Staat

3368

Wir stellen die Abläufe auf allen Ebenen auf den Prüfstand, damit unser Staat auf der Höhe 3369

der Zeit ist. Wir wollen eine aufgabengerechte Staatsorganisation mit klaren Verantwort-3370

lichkeiten, effizienten Verwaltungsstrukturen und schnelleren Verfahren. Zudem arbeiten 3371

wir für eine umfassende Digitalisierung der Verwaltung, einen modernen, offenen und 3372

durchlässigen öffentlichen Dienst und eine Innovationskultur, die neue Ideen zulässt. Dazu 3373

gehört eine moderne und innovative Verwaltungskultur: sie setzt auf Eigenverantwortung 3374

und Vertrauen.

3375

 

3376

Verwaltung modernisieren

3377

Wir wollen einen Staat, der den Menschen pragmatisch und unbürokratisch Chancen eröff-3378

net.

3379

• Wir brauchen eine Beschleunigung und Verkürzung der Verwaltungsprozesse. Bund, 3380

Länder und Kommunen müssen zusammenarbeiten und gemeinsam offene Standards Seite 95 von 139

3381

und Schnittstellen als Grundlage für eine Verwaltungsinfrastruktur schaffen, damit Be-3382

hörden besser miteinander kommunizieren können. Grundsätzlich gilt: digitale Vorfahrt!

3383

Alles, was digital werden kann, soll digital werden. Alles, was standardisiert werden kann, 3384

soll standardisiert werden.

3385

• Bund, Länder und Kommunen machen aktuell mit dem Onlinezugangsgesetz alle Leis-3386

tungen der Verwaltung für den Bürger online zugänglich – ein guter Schritt, der weiter 3387

konsequent beschleunigt werden muss und natürlich auch Unternehmen im Austausch 3388

mit der Verwaltung entlasten muss. Wir werden daher das digitale Unternehmenskonto 3389

weiter ausrollen und einem bundesweiten Praxistest unterziehen. Je schneller wir den 3390

Unternehmen die Verwaltungsdienstleistungen digital und über einen zentralen Zugang 3391

zugänglich machen können, desto besser. Deshalb wollen wir eine Unternehmensplatt-3392

form Deutschland als „Single Point of Contact“ für alle wirtschaftsrelevanten Verwal-3393

tungsleistungen der föderalen Ebenen zur Verfügung stellen.

3394

• Wir werden alle internen Verwaltungsvorgänge digitalisieren und beschleunigen. Dazu 3395

muss das Recht konsequent vereinfacht und auf die digitale Verwaltung ausgerichtet 3396

werden. Das digitale Verwaltungsverfahren muss zum Regelfall werden. Analoge, papier-3397

gebundene Prozesse sind – soweit überhaupt noch erforderlich – als Ausnahmefälle zu 3398

gestalten.

3399

• Wir werden außerdem alle Schriftformerfordernisse konsequent beseitigen.

3400

• Neue Angebote dürfen nicht nur in einzelnen (Pilot-)Kommunen oder Ländern langsam 3401

ausgerollt werden, sondern müssen schnellstmöglich in die Fläche. Zugleich werden wir 3402

dafür sorgen, dass auch Menschen ohne tiefere digitale Kenntnisse weiterhin alle Ver-3403

waltungsdienstleistungen problemlos in Anspruch nehmen können.

3404

• Der Ansatz, über den FIT-Store der Föderalen IT-Kooperation (FITKO) einen App-Store 3405

umzusetzen, muss noch konsequenter verfolgt werden. Wir werden daher zur Bereitstel-3406

lung der notwendigen Anwendungen einen App-Store für die Verwaltung mit digitalen 3407

Lösungen für Aufgaben der Verwaltung von der Kommune bis zum Bund schaffen – von 3408

der digitalen Reisekostenabrechnung bis zur Chatbot-Software. Wenn sich eine Lösung 3409

in einer Kommune als besonders effektiv herausstellt, können auch andere Verwaltun-3410

gen sie einfach herunterladen. Um dies sicherzustellen, wird die gesamtstaatliche Nut-3411

zung in allen Verträgen gewährleistet.

3412

• Der digitale Staat soll darüber hinaus Treiber von offenen Standards in der Wirtschaft 3413

und in seiner eigenen Verwaltung sein. Wir stehen zum Konzept des offenen Regierungs-3414

und Verwaltungshandelns (Open Government) und wollen – wo immer möglich – Offene 3415

Daten (Open Data) und quelloffene Lösungen zum Einsatz bringen. Offene Standards 3416

und allgemeine Schnittstellen werden deshalb als Vergabekriterien bei öffentlichen Aus-3417

schreibungen stärker berücksichtigt. So ermöglichen wir mehr Wettbewerb, damit die 3418

Auftragsvergabe kleinteiliger werden kann. Das fördert Transparenz und kann vor allem 3419

kleinen und mittleren Unternehmen sowie Startups nutzen.

3420

 

 

Seite 96 von 139

3421

Planungen, Genehmigungen und Vergaben beschleunigen

3422

Wir wollen Planungs- und Genehmigungsverfahren beschleunigen, um auf die Herausfor-3423

derungen der Zukunft schnell und adäquat zu reagieren.

3424

• Wir stellen die Bündelung der Planungsverfahren und derjenigen, die die Planverfahren 3425

tatsächlich durchführen, in den Mittelpunkt der Beschleunigungsanstrengungen eines 3426

neuen Planungsmodernisierungsgesetzes.

3427

• Wir werden auch auf EU-Ebene für eine Beschleunigung der Planungsverfahren eintreten 3428

und im Rahmen der Aarhus-Konvention dafür eintreten, schnelle Planungsverfahren zu 3429

ermöglichen.

3430

• Wir werden Beschaffungs- und Vergabeprozesse vereinfachen und im Rahmen der EU-3431

Vorgaben regionale Wertschöpfung vor Ort erleichtern. Krisenbedingt wurde das Verga-3432

berecht temporär vereinfacht, etwa durch eine Verkürzung der Fristen bei EU-Vergabe-3433

verfahren oder einer Anpassung der Schwellenwerte für beschränkte Ausschreibungen 3434

und freihändige Vergaben in Deutschland. Erleichterungen bei Vergabeverfahren sollten 3435

kein Alleinstellungsmerkmal konjunktureller Hilfsmaßnahmen sein, sondern in Dauer-3436

recht überführt werden.

3437

• Darüber hinaus ist eine grundsätzliche Entbürokratisierung und Digitalisierung dieser 3438

Prozesse dringend geboten. Öffentliche Fördermaßnahmen müssen schneller in kon-3439

krete Investitionsprojekte umgesetzt werden.

3440

• Die Stärkung der regionalen und der örtlichen Wirtschaft muss bei vergleichbarer Leis-3441

tung und angemessenem Preis als ein Kriterium der Auftragsvergabe zugelassen werden.

3442

Interkommunale Zusammenarbeit werden wir stärken, indem wir uns für eine kommu-3443

nalfreundliche Auslegung im Vergabe- und Umsatzsteuerrecht einsetzen.

3444

 

3445

Föderalismus erhalten – Strukturen modernisieren

3446

Zur strukturellen Modernisierung unseres Staates gehört aber auch ein moderner Födera-3447

lismus. Bürgernahe Verwaltung und gleichwertige Lebensverhältnisse dürfen kein Gegen-3448

satz sein. Gleichzeitig bietet der Föderalismus die Möglichkeit eines Wettbewerbs um die 3449

besten Konzepte. Das macht ihn stark – auch im internationalen Vergleich.

3450

• In einer Föderalismusreform werden wir einen neuen Zukunftspakt zwischen Bund, Län-3451

dern und Kommunen schmieden. Wir werden alles auf den Prüfstand stellen, eine Ana-3452

lyse der staatlichen Aufgaben erstellen und den Grundsatz der Subsidiarität konsequent 3453

anwenden.

3454

• Der Föderalismus muss passgenaue Lösungen vor Ort bieten, die Vielfalt unseres Landes 3455

widerspiegeln und gleichzeitig effizient sein. Dazu brauchen wir neue Kooperationsfor-3456

men zwischen den Ländern, um Herausforderungen wie die Digitalisierung der Bildung 3457

besser zu meistern als bisher.

Seite 97 von 139

3458

• Uns leitet das demokratische Prinzip klarer Verantwortlichkeit: Die Bürgerinnen und 3459

Bürger müssen wissen, wer wofür in unserem Staat Verantwortung trägt. Dazu werden 3460

wir die Finanzenbeziehungen von Bund, Länder und Kommunen zeitgemäß ordnen und 3461

eine aufgabengerechte Finanzverteilung festlegen. Wir wollen Mischfinanzierung künf-3462

tig vermeiden und mögliche Nachteile für die Länder und Kommunen im Gegenzug ent-3463

sprechend durch einen höheren Umsatzsteueranteil ausgleichen. Dabei verfahren wir 3464

nach dem Grundsatz: Das Geld folgt der Aufgabe.

3465

• Wir werden uns weiterhin dafür einsetzen, dass Städte und Gemeinden aus eigener Kraft 3466

die unterschiedlichen Herausforderungen vor Ort bewältigen können. Dazu brauchen 3467

Kommunen verlässliche Finanzierungsquellen, die neuen bürokratieintensiven Förder-3468

programmen grundsätzlich vorzuziehen sind. Wir werden die kommunal relevanten För-3469

derprogramme zusammenfassen und auf einer Online-Plattform bündeln, damit sie dort 3470

einfacher beantragt und abgewickelt werden können.

3471

• Wir brauchen dazu gemeinsame Standards und geeignete Schnittstellen. Es geht nicht 3472

darum, ein Produkt vorzugeben oder bundesweit durchzusetzen. Vielmehr müssen künf-3473

tig vorhandene Standards stärker genutzt bzw. bei Bedarf passende Standards und 3474

Schnittstellen gemeinsam entwickelt werden.

3475

• Auch neue organisatorische Vereinbarungen müssen getroffen werden. Der IT-Pla-3476

nungsrat hat mit der FITKO (Föderale IT-Kooperation) eine kleine, agile Organisation ge-3477

schaffen. Sie sollte personell und technisch gestärkt werden, sofern erforderlich.

3478

• In den Kernzuständigkeiten der Länder brauchen wir neue Kooperationsformen zwi-3479

schen den Ländern und eine engere Abstimmung. Bestehende Möglichkeiten der Koope-3480

ration zwischen den Ländern müssen stärker genutzt werden, um gemeinsame inhaltli-3481

che Standards nicht nur im IT-Bereich, sondern auch darüber hinaus zu definieren, das 3482

gilt insbesondere auch für den Abbau von Bürokratie.

3483

 

3484

Neue gesetzgeberische Zurückhaltung walten lassen

3485

Es gibt in Deutschland eine Neigung, jeden Lebenssachverhalt, jedes neue Problem mit ei-3486

nem Gesetz regeln zu wollen. Davon müssen wir uns freimachen. Für jedes einzelne Gesetz 3487

mag es gute Gründe geben, in der Summe ist es zu viel. Weniger Gesetze bedeutet: mehr 3488

Zeit für die Bundesministerien zur raschen Umsetzung und mehr Raum für den Deutschen 3489

Bundestag zur politischen Gestaltung und Kontrolle der Regierung.

3490

• In der 19. Wahlperiode wird der Bundestag etwa 500 Gesetze beschlossen haben. In der 3491

kommenden Wahlperiode wollen wir die Anzahl der Gesetze um 20 Prozent reduzieren.

3492

Auf EU-Ebene setzen wir uns ebenso dafür ein, weniger, dafür gezielter zu regulieren.

3493

• Die Bürgerinnen und Bürger erwarten, dass beschlossene Gesetze schnell und gut um-3494

gesetzt werden, dass beschlossenes Geld zügig ankommt oder investiert wird. Hier wol-3495

len wir deutlich besser werden, damit Investitionsmittel nicht mehr herumliegen, son-3496

dern auch tatsächlich ausgegeben werden. Im Deutschen Bundestag werden wir einmal Seite 98 von 139

3497

pro Jahr in einer Umsetzungswoche den Fortschritt und die Wirkung unserer Gesetzge-3498

bung transparent machen.

3499

• Wir wollen, dass sich die neue Bundesregierung stärker an Zielen und Kennzahlen bei 3500

der Erfolgskontrolle orientiert, damit das Neue auch tatsächlich bei Bürgerinnen und 3501

Bürgern ankommt.

3502

• Nahezu alle Gesetze verlangen etwas von Bürgern, Behörden oder Unternehmen. Die 3503

dazu notwendige Kommunikation, also der Austausch von Informationen und Unterla-3504

gen, muss digital erledigt werden können – beispielsweise zwischen den Behörden, wenn 3505

es um die Ausstellung von Dokumenten wie dem Reisepass geht, oder wenn ein Bürger 3506

Informationen an die Rentenversicherung senden muss. Die Digitalisierungstauglichkeit 3507

von Gesetzen muss am Anfang stehen. Wir werden einen Digital-TÜV vor die Gesetzes-3508

beratung setzen. Die zentrale Koordination dafür wird das neue Digitalministerium über-3509

nehmen.

3510

 

3511

8.2. Die Bürgerinnen und Bürger im Mittelpunkt

3512

Wir wollen den Staat und seine Verwaltung neu denken, und zwar vom Bürger und seinen 3513

Lebenslagen her, nicht von den Prozessen und Strukturen der staatlichen Behörden. Digital 3514

ist dabei das neue Normal. Wir werden einen Rechtsanspruch der Bürgerinnen und Bürger 3515

auf eine digitale Bürgeridentität (e-ID) schaffen. Diese soll vorhandene Zuordnungen, wie 3516

die Steuer-ID oder die Sozialversicherungsnummer, zusammenführen und auf allen Ebenen 3517

staatlicher Verwaltung genutzt werden können.

3518

Die Digitalisierung von Verwaltungsleistungen soll es Bürgern und Unternehmen so einfach 3519

und nutzerfreundlich wie möglich machen, mit der Verwaltung zu interagieren, Anträge zu 3520

stellen und Entscheidungen zu erhalten.

3521

 

3522

Bürgerservice „aus einer Hand“ bieten

3523

Wer eine Dienstleistung der Verwaltung beantragt, soll alle Formalitäten und Verfahren an 3524

einer einzigen Stelle, dem sogenannten Einheitlichen Ansprechpartner, erledigen können.

3525

• Wir werden dafür sorgen, dass erforderliche Informationen von Bürgern oder Unterneh-3526

men nur einmal erhoben werden und dann nur an einer einzigen Stelle in dem jeweils 3527

zuständigen Register notiert und auch nur dort aktualisiert werden. Die beschlossene 3528

Registermodernisierung setzen wir dazu mit Nachdruck um.

3529

• Mit automatisierten Entscheidungen werden wir diejenigen Verfahren beschleunigen, 3530

bei denen es kaum Ermessensspielräume gibt: Wer ein Kind bekommen hat, bekommt 3531

Kindergeld. Wer umgezogen ist, bekommt eine neue Meldebescheinigung. Verwaltungs-3532

prozesse, für die die Bürger heute noch verschiedene Anträge stellen oder mehrfach In-3533

formationen bereitstellen müssen, werden in automatisierter Abfolge geschehen, sobald 3534

beispielsweise die Geburt eines Kindes gemeldet wurde.

Seite 99 von 139

3535

• Unser längerfristiges Ziel ist es, dass Sozialleistungen zukünftig nicht nur bürokratieär-3536

mer, sondern auch praktisch „wie aus einer Hand" bei den Leistungsberechtigten ankom-3537

men. Damit helfen wir den Berechtigten und vermeiden Mehrfachleistungen. Denn un-3538

ser stark gegliedertes Sozialleistungssystem ist leistungsfähig, aber für den leistungsbe-3539

rechtigten Bürger nur mit Mühe zu verstehen.

3540

 

3541

Digitalen Verwaltungszugang der Bürger garantieren

3542

Aktuell gibt es bereits einige digitale Verwaltungsdienstleistungen, die die Bürgerinnen 3543

und Bürger nur in eingeschränktem Maße nutzen. Das hat verschiedene Gründe, allerdings 3544

sind viele Bürger auch noch nicht mit allen notwendigen Werkzeugen ausgestattet oder die 3545

Anwendungen sind noch nicht einfach genug gestaltet.

3546

• Wir wollen die persönliche Brieftasche für alle Verwaltungsvorgänge, für jeden auf dem 3547

eigenen Smartphone. Damit Bürger und Unternehmen so sicher und so einfach wie mög-3548

lich die digitale Verwaltung nutzen können, werden wir sie im Rahmen einer digitalen 3549

Grundversorgung mit elektronischen Identifizierungswerkzeugen, Signaturen und si-3550

cheren Postfächern ausstatten.

3551

• Wir werden den Personalausweis als Schlüsselelement zur umfassenden und vollen digi-3552

talen Identifizierung auf das Smartphone bringen und seine Anwendungsmöglichkeiten 3553

konsequent erweitern. Diese Lösung muss europaweit skaliert werden. Die Nutzung wird 3554

erst dann auch für die grenzüberschreitende Wirtschaft attraktiv, wenn die Lösung nicht 3555

nur in Deutschland funktioniert, sondern auch auf den umliegenden Märkten.

3556

 

3557

Teilhabe für alle sicherstellen

3558

CDU und CSU denken Politik von der Mitte der Gesellschaft und tragen damit eine Verant-3559

wortung für alle Bürgerinnen und Bürger. Diese Verantwortung nehmen wir auch im digi-3560

talen Wandel wahr. Dabei wollen wir niemanden zurücklassen. Daher behalten wir auch die-3561

jenigen im Blick, die nicht in einer digitalen Welt aufgewachsen sind und die weniger Kennt-3562

nisse in diesem Bereich haben.

3563

• Wir werden dafür sorgen, dass staatliche Leistungen, ganz besonders diejenigen zur Da-3564

seinsvorsorge, für jedermann einfach zugänglich bleiben. Das ist aber nur die Grundver-3565

sorgung.

3566

• Wir werden ambitionierter sein und Möglichkeiten zum digitalen Lernen schaffen. Nicht 3567

jeder muss digital werden, aber wer digital werden möchte, sollte dazu Hilfestellung be-3568

kommen können. Dies kann zunächst analog in den Volkshochschulen geschehen und 3569

später dann über Lernplattformen oder andere Online-Angebote. Alle interessierten 3570

Bürgerinnen und Bürger sollen sich auf eigene Initiative digital weiterbilden können, um 3571

die Möglichkeiten einer digitalen Welt nutzen zu können.

3572

• Wir wollen eine frühe Bürgerbeteiligung. Gerade digitalisierte Verfahren bieten hierfür 3573

enorme Potenziale. Das haben die diversen Hackathons im vergangenen und in diesem 3574

Jahr gezeigt. Bürger haben dabei konkret an Lösungsvorschlägen mitgearbeitet. Diese Seite 100 von 139

3575

Art der Bürgerbeteiligung wollen wir gezielt fördern und in der Verwaltungspraxis nach-3576

haltig etablieren.

3577

 

3578

8.3. Der öffentliche Dienst als moderner Arbeitgeber

3579

Die Mitarbeiterinnen und Mitarbeiter im öffentlichen Dienst haben in der Pandemie Groß-3580

artiges geleistet: In Kindergärten und Schulen, bei der Polizei, bei der Bundeswehr, in den 3581

Behörden. Beim Bund, bei den Ländern, in den Kommunen. Wir setzen darauf, dass nur mit 3582

ihren Ideen, aber auch mit ihrer Erfahrung und ihrem Engagement die Staatsmodernisie-3583

rung gelingt.

3584

Um die Chancen des digitalen Wandels in unserem Staatswesen voll auszuschöpfen und das 3585

Modernisierungsjahrzehnt aktiv voranzutreiben, brauchen wir einen leistungsfähigen öf-3586

fentlichen Dienst mit gut ausgebildetem und hoch motiviertem Personal, der sich mit Wirt-3587

schaft, Wissenschaft und Gesellschaft austauscht und der Mut zum Risiko hat. Wir brauchen 3588

öffentliche Einrichtungen, deren Beschäftigte staatliche Aufgaben zuverlässig und umfas-3589

send erledigen. Dabei stehen wir zu den bewährten beiden Säulen des öffentlichen Diens-3590

tes, den Tarifangestellten und dem Berufsbeamtentum.

3591

 

3592

Beschäftigte fördern, Talente anwerben, Dienstrecht modernisieren

3593

Ein digitaler Kulturwandel wird nur zusammen mit den Beschäftigten des öffentlichen 3594

Dienstes gelingen. Entscheidend ist dabei Wertschätzung und Offenheit für neue Ideen und 3595

Vorschläge.

3596

• Der öffentliche Dienst muss die besten Köpfe anziehen und ihnen Gestaltungsmöglich-3597

keiten geben. Dazu müssen Wechsel zwischen Wirtschaft, Wissenschaft und Verwaltung 3598

stärker ermöglicht und Anreize für neue Ideen und neue Wege – etwa über Modellpro-3599

jekte – gegeben werden.

3600

• Wir wollen von der Erfahrung der Beschäftigten des öffentlichen Dienstes profitieren.

3601

Um die Vorschläge aufzunehmen und auch die Zufriedenheit messbar zu machen, wollen 3602

wir eine digitale Plattform für Mitarbeiterbefragungen einführen, die in allen Bundesbe-3603

hörden anonym und behördenübergreifend durchgeführt werden.

3604

• Wir wollen die Mitarbeiterinnen und Mitarbeiter in der Verwaltung stärken und Karrier-3605

ewege flexibler machen. Wir brauchen im Bund und in allen Ländern ein modernes 3606

Dienstrecht, das für Offenheit und Durchlässigkeit steht und das den individuellen Leis-3607

tungen und Fähigkeiten der Mitarbeiterinnen und Mitarbeiter gerecht wird.

3608

• Wir werden die Beförderungsgrundlagen weiterentwickeln, sodass sich Rotations-, Pro-3609

jektverantwortung und ressortübergreifende Stationswechsel stärker lohnen, indem sie 3610

für eine Beförderung berücksichtigt werden. Dadurch werden Laufbahnen nicht bloß als 3611

lineare Vorgänge gestaltet, sondern es werden Rotation, Hospitation und Auslandsauf-3612

enthalte stärker gefördert. Nicht Wartezeiten, sondern die Qualifikation für die konkrete 3613

Aufgabe müssen für eine Beförderung entscheidend sein.

Seite 101 von 139

3614

• Um mehr Fachkräfte für die Verwaltung zu gewinnen, müssen neue Wege etwa bei der 3615

Vergütung beschritten werden, insbesondere im Bereich hochspezialisierter IT-Berufe.

3616

Die Einführung von Zulagen für IT-Fachkräfte ist ein richtiger Schritt, wird aber nicht 3617

ausreichen. Es erfordert grundsätzlich mehr Kreativität bei der Personalgewinnung und 3618

eine Flexibilisierung des Personaleinsatzes über Ressortgrenzen hinweg sowie zwischen 3619

Bund, Ländern und Kommunen.

3620

 

3621

Neue Sichtweisen willkommen – Vielfalt fördern

3622

Wir wollen neue Ideen und frische Impulse durch externe Mitarbeiterinnen und Mitarbeiter 3623

und ungewöhnliche Lebensläufe einbringen. Es braucht eine höhere Durchlässigkeit zwi-3624

schen öffentlichem Dienst und Privatwirtschaft für den wechselseitigen, auch zeitlich limi-3625

tierten Austausch von Mitarbeitern. Dazu sind erfahrene Quereinsteiger eine willkommene 3626

Bereicherung für den öffentlichen Dienst. Sie bringen vielfältige Erfahrungen aus der Praxis 3627

und neue Perspektiven mit.

3628

• Damit mehr von ihnen den Weg in die Verwaltung finden, müssen wir die Einstellungs-3629

voraussetzungen flexibilisieren. Wir wollen den Weg frei machen für Fachkräfte, die 3630

möglicherweise keinen formalen Abschluss in ihrer Fachrichtung haben, aber über jahre-3631

lange und erfolgreiche Berufserfahrung oder andere Qualifikationen verfügen.

3632

• Eine leistungsfähige und moderne Verwaltung braucht unterschiedliche Perspektiven.

3633

Wir setzen uns dafür ein, im öffentlichen Dienst bis 2025 gemäß der gerade beschlosse-3634

nen Reform eine gleichberechtigte Teilhabe von Frauen in Leitungsfunktionen auf allen 3635

Ebenen zu verwirklichen.

3636

• Die Vielfalt unserer Gesellschaft soll auch im öffentlichen Dienst sichtbar sein. Wir wer-3637

den auch dafür sorgen, dass keine Frau und kein Mann wegen der Erziehung der Kinder 3638

oder der Pflege von Angehörigen benachteiligt wird. Im öffentlichen Dienst sind diese 3639

Zeiten besser als bisher bei Beförderungen und Bewerbungen als Qualifikation zu be-3640

rücksichtigen. Damit wollen wir die Familienfreundlichkeit im Land verbessern.

3641

 

3642

Neue Formen der Zusammenarbeit etablieren

3643

Die aktuelle Form der Zusammenarbeit konzentriert sich sehr stark auf Zuständigkeiten 3644

und fördert Zusammenarbeit nicht stark genug. Verwaltungsarbeit muss agiler und umset-3645

zungsorientierter werden.

3646

• Wir werden interdisziplinäre Projektarbeit zum Standard in Verwaltungen machen. Die 3647

notwendige Transformation wollen wir begleiten, um die Bedeutung der Projektarbeit 3648

zu stärken, prozessbegleitende Beratung und Weiterbildung zu fördern und Rechtsfra-3649

gen zu klären. Jede angesprochene Behörde sollte sich an der Projektarbeit beteiligen.

3650

Dies gilt insbesondere zwischen den Verwaltungsebenen: Fachleute im Rechtswesen 3651

und bei übergeordneten Themen in den Bundes- und Landesministerien sollten mit den Seite 102 von 139

3652

ausführenden Praktikern in Städten und Gemeinden als Projektteams zusammenkom-3653

men, damit die besten Lösungen gemeinsam und direkt erarbeitet sowie gut umgesetzt 3654

werden können.

3655

• Wir werden in allen Geschäftsbereichen Modernisierungsteams schaffen, die vorange-3656

hen und Innovationen in strategischen Schwerpunktthemen erproben und optimieren, 3657

bevor sie aufwendig für ganze Ministerien etabliert werden. Gleichzeitig können solche 3658

Innovationseinheiten als “flexible Reserve” mit ihren Fähigkeiten strategisch relevante 3659

Projekte beschleunigen und querschnittlicher Arbeit zum Erfolg verhelfen.

3660

• Mit Reallaboren und digitalen Modellprojekten für die Verwaltung wollen wir dabei neue 3661

Arbeitsweisen auszuprobieren, um damit Projekte schneller und effizienter umzusetzen.

3662

Ein Neustart setzt Offenheit für Veränderung voraus, und die braucht Legitimation und 3663

Beteiligung.

3664

• Die Erfahrungen aus der Pandemie haben gezeigt, dass gute Zusammenarbeit auch von 3665

unterschiedlichen Orten aus funktionieren kann. So können wir Dienstreisen reduzieren, 3666

effizienter arbeiten und dabei noch Kosten einsparen. Wir bekennen uns zu den Verein-3667

barungen des Bonn/Berlin-Gesetzes. Wir werden mehr Bundesbehörden in den neuen 3668

Bundesländern ansiedeln.

3669

 

3670

Eine moderne Bundesverwaltung

3671

In der Bundesverwaltung sollen Aufgaben und Zuständigkeiten zusammengefasst und ge-3672

meinsam erledigt werden, wo immer dies möglich ist. Das Ressortprinzip darf nicht zum 3673

Hemmnis für die Modernisierung werden. Sich überlappende Zuständigkeiten, Doppel-3674

strukturen in verschiedenen Ressorts und Kompetenzstreitigkeiten zwischen den Ressorts 3675

bremsen die Handlungsfähigkeit Deutschlands.

3676

• Wir wollen weiterhin eine aktive Rolle des Bundeskanzleramts als Schaltstelle für das 3677

Regierungshandeln. Wir brauchen – gerade für ein Digitalministerium – eine Zusammen-3678

arbeit in der Bundesregierung, die klare Verantwortlichkeiten definiert, aber in den 3679

dringlichsten, gemeinsam definierten Reformbereichen auch eine kraftvolle Umsetzung 3680

ermöglicht.

3681

• Die Ministerien sollen dazu prüfen, ob Verwaltungsaufgaben an nachgeordnete Bereiche 3682

abgegeben werden können. So schaffen wir neue Synergien.

3683

• Wir werden den „Digital Service 4 Germany“ als Innovationstreiber für nutzerorientierte 3684

Softwareentwicklung in der Bundesregierung ausbauen und den Austausch zwischen 3685

Verwaltungsmitarbeitern und Digitaltalenten intensivieren. Unser Ziel ist die besten 3686

Softwareentwickler und IT-Köpfe für unser Gemeinwesen zu gewinnen.

3687

 

3688

Austausch zwischen den Ebenen verbessern

3689

Wir wollen klare Verantwortlichkeiten definieren und gleichzeitig die Kooperation und 3690

Kommunikation zwischen den Behörden in Bund, Ländern und Kommunen verbessern, um Seite 103 von 139

3691

krisenfester, schneller und effizienter zu sein. Es muss stets möglich sein, Lösungen aus ei-3692

nem Bundesland in ein anderes zu übertragen oder eine medienbruchfreie Kommunikation 3693

zwischen Bundesstelle, Kommunen und Dienstleistern herzustellen.

3694

 

3695

8.4. Digitale Infrastruktur

3696

Das Rückgrat des Modernisierungsjahrzehnts ist eine gute Infrastruktur – und zwar im ge-3697

samten Land. Unser Ziel ist es, bis spätestens 2024 alle weißen Flecken mit stationären oder 3698

mobilen Masten zu beseitigen und das Prinzip „neue Frequenzen nur gegen flächende-3699

ckende Versorgung“ gesetzlich festzuschreiben.

3700

• Wir werden mit der von uns gestarteten Mobilfunkinfrastrukturgesellschaft bis 2025 ein 3701

flächendeckendes 5G‐Netz in ganz Deutschland schaffen und bis 2025 insgesamt 15

3702

Mrd. Euro für Gigabit-Netze bereitstellen.

3703

• Wir werden den Netzausbau durch eine unbürokratische, digitale und rasche Genehmi-3704

gungspraxis beschleunigen. Wir werden Verfahren durch Digitalisierung und Standardi-3705

sierung vereinfachen und damit den notwendigen Aufwand senken.

3706

• Durch verstärkte Mitarbeiter-Weiterbildungen und Unterstützung durch Experten des 3707

Bundes und der Länder werden wir die Ressourcen aufseiten der kommunalen Verwal-3708

tungen steigern, die hier für einen begrenzten zeitlichen Rahmen sowohl rechtliche als 3709

auch technische Verfahren verstärkt betreuen müssen.

3710

• Über die Beschleunigung der Verfahren hinaus müssen wir Engpässe beim tatsächlichen 3711

Ausbau in Angriff nehmen. Die Möglichkeiten für alternative Verlegeverfahren müssen 3712

stärker genutzt werden. So sind beispielsweise alternative Verlegeverfahren in geringe-3713

rer Verlegetiefe bereits rechtlich möglich, treffen aber nach wie vor auf Skepsis. Bereits 3714

angelaufene Maßnahmen zur Aufklärung über diese sinnvollen Verfahren müssen daher 3715

konsequent verstärkt werden.

3716

• Darüber hinaus sollten die Verfahren schnell und umfassend zertifiziert werden, um 3717

mögliche Zweifel direkt auszuräumen.

3718

 

3719

8.5. Nachhaltiger Staat

3720

Wir wollen mit gutem Beispiel vorangehen und so schnell wie möglich eine CO2-neutrale 3721

Bundesverwaltung erreichen. Dabei muss die Verwendung von Ökostrom ebenso eine Rolle 3722

spielen wie die energetische Sanierung von Bundesgebäuden. Wir wollen, dass der Bund 3723

eine Vorreiterrolle im Bereich der Nachhaltigkeit und der Reduzierung von Plastikmüll ein-3724

nimmt.

3725

• Neben der Etablierung von Erneuerbaren Energien in Gebäuden wollen wir die Flotte so-3726

wie Regierungsflüge des Bundes über Elektroantriebe oder über synthetische Kraftstoffe 3727

dekarbonisieren.

Seite 104 von 139

3728

• Zur Steigerung der Biodiversität soll der Bund bei der Bewirtschaftung seiner Liegen-3729

schaften und Flächen vorangehen und dabei insbesondere die Dach- und Fassadenbe-3730

grünung stärken.

3731

• Als Großabnehmer für Zukunftstechnologien und Vorbild beim nachhaltigen Wirtschaf-3732

ten wird die Bundesverwaltung ihr Handeln und ihre Beschaffung an Nachhaltigkeitsin-3733

dikatoren ausrichten. Eine verbindliche Nachhaltigkeitsprüfung für alle Gesetze anhand 3734

der deutschen Nachhaltigkeitsstrategie für eine generationengerechte Politik wollen wir 3735

dazu verankern. Entsprechende Nachhaltigkeitsindikatoren bilden die wirtschaftlichen, 3736

sozialen und ökologischen Dimensionen unseres Lebens bestmöglich ab und schaffen 3737

eine verbesserte Gesetzesfolgenabschätzung für Deutschlands Zukunft.

3738

 

 

Seite 105 von 139

3739

9. Neue Stärke für mehr Sicherheit – aus Verantwortung für unsere Frei-3740

heit

3741

 

3742

Unser Unionsversprechen: Wir wollen, dass die Menschen in unserem Land auf ein Leben in Si-3743

cherheit und Freiheit vertrauen können: ob zu Hause, unterwegs auf Straßen oder Plätzen, in 3744

Bussen oder Bahnen, bei Tag oder Nacht, analog oder digital. Sie erwarten zu Recht einen star-3745

ken Staat, der sie schützt. Dafür werden wir weiterhin gemeinsam arbeiten.

3746

Wir stehen dabei fest an der Seite derjenigen, die täglich alle Anstrengungen unternehmen, um 3747

Sicherheit in Freiheit zu verteidigen. Ganz gleich ob Polizisten oder Rettungskräfte, Mitarbeiter 3748

der Ordnungsämter, Richter oder Staatsanwälte – sie alle genießen ein besonders großes Ver-3749

trauen. Ihrem Einsatz gebühren unser Respekt und unsere Unterstützung.

3750

Dank dieses Einsatzes können wir in Deutschland sicherer leben als in den meisten anderen Län-3751

dern der Welt. Doch Sicherheit und Freiheit werden jeden Tag aufs Neue herausgefordert: von 3752

Einbrechern, kriminellen Clans, gewaltbereiten Extremisten, internationalen Terroristen oder 3753

Angriffen im Cyberraum. Deshalb wollen wir die Wehrhaftigkeit unseres Rechtsstaates weiter 3754

stärken. Im Modernisierungsjahrzehnt der 20er Jahre setzen wir dabei auf ein Update aller Si-3755

cherheitsbehörden mit einem Dreiklang aus mehr Personal, besserer Ausstattung sowie zeitge-3756

mäßer Kompetenzen und Befugnisse.

3757

Für uns ist klar: Im Sinne der Subsidiarität und Bürgernähe sind die Länder zu Recht für die 3758

Polizei verantwortlich. Krisen und Katastrophen nehmen jedoch keine Rücksicht auf Grenzen 3759

von Regionen, Bundesländern oder Staaten. So wenig sich Straftäter durch Grenzen abhalten 3760

lassen, so wenig dürfen Grenzen eine wirksame Arbeit der Sicherheitsbehörden behindern. Die 3761

Möglichkeiten zu einer verstärkten Zusammenarbeit von Bund und Ländern müssen daher voll 3762

genutzt werden. Dort, wo Bund und Länder in Angelegenheiten der Sicherheit des Bundes zu-3763

sammenarbeiten, braucht es bei komplexen Struktur- und Ermittlungsverfahren auch eine stär-3764

kere Koordinierung – etwa im Kampf gegen die Feinde unserer Verfassung, gegen Terroristen, 3765

in der Abwehr von Gefahren aus dem Cyberraum oder bei bundesweiten, auch digitalen, Kata-3766

strophenfällen.

3767

 

3768

9.1. Mehr Sicherheit überall und jederzeit

3769

Sicher in den eigenen vier Wänden leben

3770

Um Einbrecher stärker abzuschrecken, haben wir härtere Strafen durchgesetzt. Dies allein 3771

aber reicht nicht. Wir müssen auch dafür sorgen, dass mehr Einbrüche aufgeklärt, Täter 3772

leichter gefasst und Wiederholungs- bzw. Serienstraftaten verhindert werden. Daher haben 3773

wir der Polizei zusätzliche Ermittlungsbefugnisse an die Hand gegeben. Wir setzen diesen 3774

Weg konsequent fort.

3775

• Wir wollen, dass künftig softwaregestützte Werkzeuge verstärkt zum Einsatz kommen, 3776

mit deren Hilfe sich die Tatmuster von Einbrechern vorhersagen lassen. So können be-3777

sonders gefährdete Wohngebiete erkannt und gezielt mit Polizeistreifen überwacht wer-3778

den.

Seite 106 von 139

3779

• Wir unterstützen Eigentümer und Mieter weiterhin dabei, Türen und Fenster besser zu 3780

sichern. Dafür werden wir die staatlichen Zuschüsse ausbauen.

3781

 

3782

Mehr Polizeipräsenz zeigen

3783

Wo Grenzen überschritten, Regeln missachtet oder Gesetze gebrochen werden, gilt null 3784

Toleranz. Sicherheit ist besonders dort wichtig, wo wir zu Hause sind, im Alltag und in un-3785

serer Nachbarschaft.

3786

• Wir wollen die Polizei von bürokratischen Aufgaben entlasten. So wird sie noch bürger-3787

näher und sichtbarer.

3788

• Wir brauchen mehr Polizistinnen und Polizisten auf Straßen und Plätzen – sowohl in der 3789

Stadt als auch in den ländlichen Räumen.

3790

• Auch in Zügen, auf Bahnhöfen und Flughäfen setzen wir auf Sicherheit durch stärkere 3791

Polizeipräsenz.

3792

• Wer Verwahrlosungen, verschmutzte Grünanlagen oder Fassadenschmierereien erlebt, 3793

fühlt sich nicht wohl und damit auch nicht sicher. Deshalb treten wir für saubere Ort-3794

schaften und gepflegte Stadtteile ein.

3795

 

3796

Videoschutz an öffentlichen Gefahrenorten ausbauen

3797

Kameras mit intelligenter Videosicherheitstechnik helfen unseren Polizistinnen und Poli-3798

zisten, Täter abzuschrecken und Straftaten aufzuklären. Dabei gilt: mehr Sicherheit und 3799

zielgerichteter Datenschutz durch moderne Technik, die effizient und innovativ ist. Wir 3800

werden immer wieder neu abwägen müssen, inwieweit das Recht des Einzelnen auf Schutz 3801

seiner persönlichen Daten mit dem grundgesetzlichen Auftrag in Einklang zu bringen ist, 3802

Sicherheit für alle Menschen zu gewährleisten.

3803

• An öffentlichen Gefahrenorten wie etwa vor und in Fußballstadien, an Bahnhöfen und 3804

weiteren Verkehrsknotenpunkten sowie in Bussen und Bahnen wollen wir den intelligen-3805

ten Videoschutz weiter ausbauen. Dabei wollen wir die Chancen der Digitalisierung und 3806

der Künstlichen Intelligenz noch besser nutzen.

3807

• Um die Fahndung nach schweren Straftätern, Gefährdern und Terroristen zu verbessern, 3808

wollen wir die Voraussetzungen dafür schaffen, dass die automatisierte Gesichtserken-3809

nung an Gefahrenorten in Deutschland eingesetzt werden kann.

3810

 

3811

Einsatzkräfte konsequent schützen

3812

Polizisten, Feuerwehrleute, Sanitäter und andere Einsatzkräfte stehen täglich mit ihrer Ar-3813

beit und oft auch mit ihrem Leben für unser aller Sicherheit ein.

3814

• Um diejenigen besser zu schützen, die uns schützen, werden wir die Mindeststrafe für 3815

tätliche Angriffe auf sechs Monate, für heimtückische Attacken auf ein Jahr Haft erhöhen Seite 107 von 139

3816

und damit als Verbrechen einstufen. Wenn der Täter eine Waffe oder ein anderes gefähr-3817

liches Werkzeug bei sich führt, soll eine Strafe bis zu zehn Jahren verhängt werden kön-3818

nen.

3819

• Polizistinnen und Polizisten müssen nicht nur gut ausgebildet, sondern auch gut ausge-3820

rüstet sein, damit sie uns und sich selbst gut schützen können. Wir wollen daher Aus-3821

und Fortbildung verbessern und für eine bestmögliche Ausstattung sorgen, wie etwa 3822

durch die flächendeckende Verwendung von Bodycams – auch bei Einsätzen in Wohn-3823

räumen. So können Einsatzsituationen beweissicher aufgezeichnet, Angreifer erkannt 3824

und Straftaten leichter verfolgt werden.

3825

• Wir wollen diejenigen strafrechtlich zur Verantwortung ziehen, die sich einer gewalttä-3826

tigen Menschenmenge anschließen, sich trotz polizeilicher Aufforderungen nicht entfer-3827

nen und dadurch aktive Gewalttäter schützen.

3828

• Um Polizisten und anderen Einsatzkräften sowie Soldaten den Rücken zu stärken, wollen 3829

wir deren Schmerzensgeldansprüche neu regeln. Auch wenn sie im Dienst beleidigt wer-3830

den, soll das dafür gerichtlich zugesprochene Schmerzensgeld vom Staat vorgestreckt 3831

werden. Der Staat holt sich das Geld anschließend beim Täter zurück.

3832

• Wir wollen die Ruhegehaltsfähigkeit der Polizeizulage prüfen.

3833

 

3834

9.2. Voller Schutz für Kinder und Frauen vor Gewalt und Missbrauch 3835

Mit sexuellem Missbrauch fügen Täter Kindern unermessliches Leid zu. Kindesmissbrauch 3836

zerstört Kinderseelen. Für uns haben Kindeswohl und Kindesschutz daher oberste Priorität.

3837

Wir stehen dafür, dass sich kein Täter sicher fühlen darf, und stellen Opferschutz vor Täter-3838

schutz. Vieles haben wir hier bereits erreicht – wie zuletzt die Bestrafung von Kindesmiss-3839

brauch als Verbrechen mit einer Mindesthaftstrafe von einem Jahr. Doch damit ist für uns 3840

der Kampf noch nicht gewonnen.

3841

 

3842

Sexuellen Kindesmissbrauch in aller Schärfe bekämpfen

3843

• Wir wollen den Einsatz der elektronischen Fußfessel bei Sexualstraftätern erweitern.

3844

• Wer sich an Kindern und Jugendlichen vergeht, darf nie wieder beruflich oder ehrenamt-3845

lich Umgang mit ihnen haben. Dazu ist ein lebenslanger Eintrag im erweiterten Füh-3846

rungszeugnis notwendig.

3847

• Wir haben durchgesetzt, dass Provider bei Kenntnis von Sexualstraftaten gegen Kinder 3848

die IP-Adressen an das Bundeskriminalamt melden müssen. Darüber hinaus müssen die 3849

Internetdienste verpflichtet werden, bei Kenntnis von sexuellem Missbrauch von Kin-3850

dern auch Bestandsdaten wie etwa hinterlegte Telefonnummern, E-Mail-Adressen oder 3851

Kreditkartendaten an die Ermittler weiterzugeben. Schließlich sollen die Provider die 3852

Möglichkeit erhalten, anhand der digitalen Fingerabdrücke von Missbrauchsbildern 3853

diese in ihren Datenbanken aufzuspüren.

Seite 108 von 139

3854

• Einzelne Täter härter zu bestrafen, reicht nicht aus, wenn gleichzeitig eine Vielzahl wei-3855

terer Täter nicht ermittelt werden kann. Wir wollen deshalb erneut darauf hinwirken, auf 3856

europäischer Ebene eine grundrechtskonforme Regelung zur Speicherung und zum Ab-3857

ruf von Telefonnummern und IP-Adressen zu schaffen, die den Einsatz der sogenannten 3858

Vorratsdatenspeicherung als schärfster Waffe im Kampf gegen den Kindesmissbrauch 3859

ermöglicht.

3860

• Wir setzen uns für einen zügigen Fortschritt bei den E-Evidence-Regelungen auf europä-3861

ischer Ebene ein, damit Ermittlungsbehörden europaweit leichter auf elektronische Be-3862

weismittel zugreifen können, wie etwa auf in einer Cloud gespeicherte E-Mails oder Do-3863

kumente.

3864

 

3865

Kinder präventiv schützen

3866

Wir brauchen eine umfassende Gesetzeskonzeption, die den Schutz des Kindes in den Mit-3867

telpunkt stellt. Hinsehen und Helfen ist wichtig.

3868

• Um Kinder und Jugendliche besser vor sexuellem Missbrauch und Gewalt zu schützen, 3869

brauchen wir eine groß angelegte Aufklärungs- und Sensibilisierungskampagne. Wir wol-3870

len, dass Kitas und Schulen zu zentralen Schutzorten vor sexueller Gewalt werden und 3871

verpflichtend sexualpädagogische Schutzkonzepte einführen.

3872

• Wir werden für kinderfreundliche Beschwerdeverfahren und geeignete Hilfsangebote 3873

auch für traumatisierte Kinder sorgen.

3874

• Regelmäßige Früherkennungsuntersuchungen eröffnen eine Möglichkeit, sexuellen 3875

Missbrauch von Kindern aufzudecken. Im Falle eines begründeten Verdachts sollte die 3876

Zusammenarbeit zwischen Ärzten und Jugendhilfe verbessert werden.

3877

• Wir müssen auch in der digitalen Welt unsere Kinder besser schützen. Wir werden ihre 3878

Medienkompetenz fördern und Telemedienanbieter zu besseren Kindesschutzkonzep-3879

ten verpflichten.

3880

• Es ist uns wichtig, dass Kinderschutz zum Pflichtfach für alle wird, die mit Kindern arbei-3881

ten: in der Erzieherausbildung, im Studium Soziale Arbeit, in der Pädagogik, in der Aus-3882

bildung für das Familiengericht, im Psychologiestudium und in der Ausbildung von Kin-3883

derärzten.

3884

• Kinder müssen so behutsam wie möglich behandelt werden, wenn sie als Opferzeugin-3885

nen und -zeugen auftreten. Wir wollen, dass die Rechtsansprüche der kindlichen Verfah-3886

rensbeteiligten, wie beispielsweise die audiovisuelle Zeugenvernehmung, beachtet und 3887

durchgesetzt werden.

3888

 

3889

Gewalt gegen Frauen rigoros ahnden

3890

Wir stehen an der Seite der Mädchen und Frauen, die Opfer von Gewalt wurden, und all 3891

jenen, die davon bedroht sind. Ihrem Schutz müssen wir uns als gesamte Gesellschaft ver-3892

pflichtet fühlen.

Seite 109 von 139

3893

• Wir brauchen mehr Transparenz über frauenfeindliche Straftaten. Deshalb wollen wir, 3894

dass diese eigens in der Polizeilichen Kriminalstatistik erfasst werden. Daraus müssen 3895

Lagebilder erstellt und Handlungsansätze für die Polizei abgeleitet werden.

3896

• Den Opfern von sexualisierter oder häuslicher Gewalt soll flächendeckend angeboten 3897

werden, die Spuren vertraulich und gerichtsfest dokumentieren zu lassen, ohne dass ein 3898

Ermittlungsverfahren von Amts wegen eingeleitet werden muss.

3899

 

3900

Prostituierte wirksamer schützen

3901

Nach wie vor gibt es trotz klarer Verbote Zuhälterei, Zwangsprostitution und Menschen-3902

handel. Dieser Zustand ist für uns inakzeptabel. Dabei gilt es, sowohl dem Schutzauftrag 3903

des Staates für die Schwächsten als auch der Gewährleistung der Berufsfreiheit gerecht zu 3904

werden.

3905

• Wir wollen Prostitution von Schwangeren sowie Heranwachsenden unter 21 Jahren ver-3906

bieten – mit einer entsprechenden Bestrafung der Freier.

3907

• Wir wollen darauf hinwirken, dass der Straßenstrich aufgrund der dort oft besonders 3908

menschenunwürdigen Bedingungen stärker reguliert wird.

3909

• Wir werden die Bund-Länder-Zusammenarbeit verbessern, damit das Prostituierten-3910

schutzgesetz effektiver durchgesetzt werden kann. Wir wollen eine deutlich schärfere 3911

Kontrolle des Prostitutionsgewerbes und intensivere Ermittlungen beim Menschenhan-3912

del.

3913

• Die Evaluierung des Prostitutionsschutzgesetzes wollen wir vorziehen. Wer Prostituierte 3914

ausbeutet oder sich der Zuhälterei schuldig macht, soll härter bestraft werden können.

3915

Den Ausstieg aus der Prostitution wollen wir stärker unterstützen.

3916

 

3917

9.3. Kein Raum für organisierte Kriminalität

3918

Überregional und behördenübergreifend enger zusammenwirken

3919

Straftäter sind heutzutage oft hochmobil, Banden agieren etwa bei Wohnungseinbrüchen, 3920

Menschen-, Drogen- und Waffenhandel längst grenzüberschreitend. Darauf reagieren wir 3921

in der Kriminalitätsbekämpfung.

3922

• Wir wollen, dass Polizei- und Ermittlungsbehörden in Deutschland noch enger überregi-3923

onal und behördenübergreifend zusammenwirken.

3924

• Auch auf europäischer Ebene werden wir organisierter Kriminalität, Mafia und kriminel-3925

len Clans durch eine wirksamere Zusammenarbeit – auch mit Blick auf EUROPOL und 3926

die Herkunftsländer der Täter – begegnen.

3927

• Die bereits verbesserte grenzüberschreitende polizeiliche Zusammenarbeit werden wir 3928

weiter ausbauen.

Seite 110 von 139

3929

• Um die Grenzfahndung in besonderen Gefahrenlagen weiter zu stärken, haben wir es der 3930

Bundespolizei ermöglicht, Auto-Kennzeichen mit automatischen Lesegeräten zu erfas-3931

sen. Wir wollen, dass überall in Deutschland mithilfe einer lagebildabhängigen Schleier-3932

fahndung kontrolliert werden darf. Das ist nicht nur in Grenzregionen wichtig, sondern 3933

auch auf international bedeutsamen Verkehrswegen und im Umfeld von Bahnhöfen und 3934

Flughäfen. Den bislang für die Bundespolizei geltenden Grenzkorridor wollen wir dafür 3935

ausdehnen.

3936

 

3937

Geldwäsche bekämpfen und Verbrechensgewinne abschöpfen

3938

Für jeden muss klar sein: Verbrechen lohnt sich nicht! Deshalb haben wir den Tatbestand 3939

der Geldwäsche bereits mehrfach verschärft und das Einziehen kriminell erlangter Vermö-3940

gen erleichtert. Wir folgen dem Prinzip „Follow the money“ und setzen genau dort an, wo 3941

es den Kriminellen am meisten weh tut: beim Geld.

3942

• Wir wollen Geldwäsche noch konsequenter bekämpfen und verfassungskonform regeln, 3943

dass bei Vermögen unklarer Herkunft künftig eine vollständige Beweislastumkehr gilt.

3944

• Grundstücke durch Barzahlung zu erwerben, soll nur mittels Banken möglich sein, die 3945

zuvor die Identität des Käufers und die Herkunft des Geldes im Rahmen einer bestehen-3946

den Geschäftsbeziehung zu prüfen haben; gleiches gilt beim Umtausch von Bargeld in 3947

Kryptowährung und umgekehrt.

3948

• Die polizeilichen Befugnisse des Zolls, die Steuerfahndung und die Finanzkontrolle 3949

Schwarzarbeit werden wir weiter stärken.

3950

• Wir setzen uns dafür ein, dass Frankfurt a. M. Sitz der neuen unabhängigen EU-Behörde 3951

zur Bekämpfung von Geldwäsche und Terrorismusfinanzierung wird.

3952

 

3953

9.4. Null Toleranz gegenüber kriminellen Familienclans 3954

Die von kriminellen Familienclans begangene organisierte Kriminalität stellt eine spezielle 3955

Bedrohung der Sicherheit dar – insbesondere in vielen Großstädten. Mit unserer Null-Tole-3956

ranz-Strategie und Politik der tausend Nadelstiche werden wir den Kontroll- und Verfol-3957

gungsdruck auf kriminelle Clans weiter erhöhen.

3958

 

3959

Parallelgesellschaften verhindern

3960

Das Gewaltmonopol des Staates ist für uns nicht verhandelbar.

3961

• Der Abschottung in kriminelle Parallelgesellschaften mit eigenen Regeln und eigener 3962

Gerichtsbarkeit sagen wir den Kampf an.

3963

• Mit fortlaufenden konsequenten und konzentrierten Einzelmaßnahmen, wie etwa wie-3964

derkehrenden Razzien, müssen kriminelle Clans weiterhin systematisch gestört werden.

3965

Sie dürfen keine ruhige Minute mehr haben. So zeigen wir auch bei kleineren Rechtsbrü-3966

chen: Der Staat ist da und lässt sich nicht auf der Nase herumtanzen!

Seite 111 von 139

3967

• Zur wirksamen Zusammenarbeit gegen Clankriminalität gehört es, länder- und behör-3968

denübergreifend zu ermitteln und auszuwerten, die Darstellung von Lageerkenntnissen 3969

zu verbessern, den internationalen Austausch zu verstärken sowie eine abgestimmte 3970

Vorgehensweise zur Bewältigung von Einsatzlagen zu erarbeiten.

3971

• Strafverfolgungs- und Sozialbehörden sowie im Bedarfsfall auch Schulbehörden müssen 3972

alle relevanten Daten austauschen können.

3973

• Wir haben dafür gesorgt, dass abgeschobene Schwerkriminelle und Gefährder, die trotz 3974

einer Einreisesperre wieder nach Deutschland zurückkehren, einfacher in Haft genom-3975

men werden können. Viele Clanmitglieder besitzen zwar die deutsche Staatsangehörig-3976

keit. Soweit dies jedoch nicht der Fall ist, sind bei kriminellen Mitgliedern sämtliche auf-3977

enthaltsrechtlichen Maßnahmen mit dem Ziel der Ausweisung und Abschiebung anzu-3978

wenden.

3979

 

3980

Ausstieg aus Clans unterstützen

3981

Durch Abschottung und negative Vorbilder krimineller Familienangehöriger sind Kinder in 3982

Clanfamilien oft an einer positiven Entwicklung gehindert. Dies stellt eine Gefährdung des 3983

Kindeswohls dar und erfordert schützende Maßnahmen.

3984

• Wir brauchen daher engen Kontakt zu diesen Familien und deren ständige Kontrolle sei-3985

tens der Jugendämter.

3986

• Clanmitglieder, die sich aus ihrem kriminellen Umfeld befreien wollen, bekommen un-3987

sere Hilfe. Dafür wollen wir gezielte, langfristig angelegte Aussteiger- und Zeugen-3988

schutzprogramme auflegen, die die Chance auf ein geregeltes Leben in Sicherheit eröff-3989

nen. Dabei sind vor allem junge Clanmitglieder sowie Frauen in diesen Familien in den 3990

Blick zu nehmen.

3991

 

3992

9.5. Schutz unserer Demokratie vor Extremisten und Terroristen 3993

Deutschland ist ein tolerantes und weltoffenes Land. Doch Toleranz und Weltoffenheit 3994

sollte niemand als Schwäche missverstehen. Extremisten und Terroristen gefährden unsere 3995

Sicherheit und den Frieden in unserem Land. Sie zu bekämpfen sowie unsere Freiheit und 3996

offene Gesellschaft zu verteidigen, sind zwei Seiten derselben Medaille.

3997

 

3998

Jeder Form von Extremismus entschieden entgegentreten

3999

Wir treten jeder Form von Extremismus und Rassismus, jeder Form von Gewalt und Terror 4000

entschieden entgegen – unabhängig davon, ob es sich um Rechts- oder Linksextremisten 4001

oder gewaltbereite Islamisten handelt.

4002

• Jede Form einer Schwächung des Verfassungsschutzes lehnen wir ab.

4003

• Der Rechtsextremismus bleibt die größte Bedrohung für unsere offene Gesellschaft und 4004

freiheitlich-demokratische Grundordnung. Dass rechtsextreme, ausländerfeindliche und Seite 112 von 139

4005

antisemitische Straftaten zugenommen haben, ist besorgniserregend. Wir setzen uns da-4006

für ein, Spezialeinheiten der Polizei für sogenannte „Cold Cases“ zu schaffen, um unge-4007

klärte schwere Straftaten mit möglicherweise rechtsextremistischem Hintergrund auf 4008

neue Ermittlungsansätze zu überprüfen.

4009

• Dem gewaltbereiten Linksextremismus muss konsequent begegnet werden. Wer das Ge-4010

waltmonopol des Staates in Frage stellt oder offen zur Gewalt gegen den Staat, seine 4011

Einrichtungen und seine Repräsentanten aufruft, darf keine Milde erwarten. Das gleiche 4012

gilt für diejenigen, die das Eigentum Dritter nicht respektieren oder kritische Infrastruk-4013

turen angreifen.

4014

• Der anwachsende Antisemitismus in unserem Land beschämt uns. Es liegt in unser aller 4015

Verantwortung, antisemitischem Hass entschlossen entgegenzutreten. Wir müssen An-4016

tisemitismus klar benennen und bekämpfen – egal, woher er kommt: ob von rechtsau-4017

ßen, linksaußen oder von migrantisch geprägten Milieus. Wir stehen mit aller Überzeu-4018

gung dafür ein, dass Jüdinnen und Juden in Deutschland immer eine Heimat haben, in 4019

Sicherheit leben und ihren Glauben praktizieren können. Den Austausch zwischen 4020

Deutschland und Israel wollen wir auf allen gesellschaftlichen Ebenen verstärken – ins-4021

besondere mit einem deutsch-israelischen Jugendwerk und mehr Stipendienprogram-4022

men.

4023

• Islamfeindlichkeit werden wir in unserem Land ebenso wenig tolerieren wie Antiziganis-4024

mus und andere rassistisch motivierte Abwertungen von Gruppen. Diese Form des Has-4025

ses, die geistige Brandstifter verbreiten wollen, richtet sich gegen uns alle und gegen 4026

das, was uns zusammenhält. Wir werden sie mit allen rechtsstaatlichen Mitteln bekämp-4027

fen und nicht zulassen, dass unser Land dadurch bedroht wird.

4028

• Der Islamismus ist eine extremistische politische Ideologie. Wir bekämpfen ihn mit der 4029

ganzen Härte unseres Rechtsstaates. Dieser Kampf gilt denen, die Hass und Gewalt schü-4030

ren und eine islamistische Ordnung anstreben, in der es keine Gleichberechtigung von 4031

Mann und Frau, keine Meinungs- und Religionsfreiheit und auch keine Trennung von Re-4032

ligion und Staat gibt. Er gilt denen, die unsere demokratische Grundordnung bekämpfen, 4033

das Existenzrecht Israels ablehnen, den inneren Frieden gefährden oder gegen Recht und 4034

Gesetz verstoßen.

4035

• Wir werden dafür sorgen, dass die ideologische Basis des Islamismus genauer in den Blick 4036

genommen wird. Wir dulden dabei keinerlei Rückzugsräume. Ebenso wollen wir mehr 4037

Transparenz bei ausländischen Geldgebern von Moscheen in Deutschland herstellen.

4038

• Wir wollen mit gesetzlichen Regelungen die Abwehrkräfte unserer Demokratie stärken.

4039

Dem Deutschen Bundestag sollen künftig regelmäßig Extremismus-Berichte der Bun-4040

desregierung vorgelegt werden, die gesamtgesellschaftliche Entwicklungen mit Blick auf 4041

Demokratiefeindlichkeit, Antisemitismus und Rassismus ausleuchten.

4042

 

 

Seite 113 von 139

4043

Hass und Hetze im Netz bekämpfen

4044

Zur Demokratie gehört Meinungsfreiheit. Soziale Medien sind wichtige Plattformen für 4045

Meinungsaustausch und demokratische Willensbildung. Dabei sind hetzerische Parolen im 4046

Netz nicht von der verfassungsrechtlich garantierten Meinungsfreiheit geschützt. Im Ge-4047

genteil: Sie bereiten den Boden für eine weitere Verrohung der Sprache wie der politischen 4048

Auseinandersetzung und tragen wesentlich zur Radikalisierung von Einzelpersonen und 4049

Gruppen bei.

4050

• Die Spirale der Verrohung von Sprache und politischer Auseinandersetzung wollen wir 4051

durchbrechen – mit allen Mitteln, die dem wehrhaften Rechtsstaat und einer selbstbe-4052

wussten demokratischen Gesellschaft zur Verfügung stehen.

4053

• Wir wollen, dass Ermittlungen der Strafverfolgungsbehörden bei besonders schweren 4054

Fällen gegebenenfalls auch ohne Anzeige eingeleitet werden können.

4055

• Wir brauchen eine Vielzahl präventiver Instrumente wie auch kostenloser Hilfsangebote 4056

für Betroffene.

4057

• Für die Betreuung besonders schwerer Fälle soll es Opferanwälte, für traumatisierte Op-4058

fer eine psychosoziale Prozessbegleitung geben.

4059

• Die Meinungsäußerungsfreiheit muss aktiv mit dem Schutz von Persönlichkeitsrechten 4060

und weiteren Rechtsgütern zum Ausgleich gebracht werden. Das virtuelle Hausrecht in 4061

den Nutzungsbedingungen der Diensteanbieter darf nicht dazu genutzt werden, die po-4062

litische Willensbildung als Kern der Demokratie zu beeinflussen. Dazu wollen wir insbe-4063

sondere das Recht der Allgemeinen Geschäftsbedingungen im Bürgerlichen Gesetzbuch 4064

verfassungskonform anpassen.

4065

 

4066

Radikalisierungen verhindern

4067

Dort, wo in unserer Gesellschaft Abschottung und Intoleranz um sich greifen, entsteht der 4068

Nährboden für Radikalisierungen. Vorbeugende Maßnahmen müssen daher möglichst früh 4069

und im unmittelbaren persönlichen Umfeld ansetzen.

4070

• Wir wollen mit gezielter Bildungsarbeit darauf hinwirken, dass jede und jeder problema-4071

tische Entwicklungen im persönlichen Umfeld frühzeitig erkennen und rechtzeitig rea-4072

gieren kann. Denn aufgeklärte und selbstbewusste Bürgerinnen und Bürger sind der 4073

stärkste Schutz für unsere Demokratie.

4074

• Insbesondere Schulen und Vereine, also Orte, an denen sich junge Menschen außerhalb 4075

ihrer Familien aufhalten wie auch Soziale Netzwerke spielen dabei eine bedeutende 4076

Rolle. Soziale Netzwerke in den Fokus zu nehmen, gehört daher zu den zentralen Aufga-4077

ben des Verfassungsschutzes, gerade mit Blick auf selbstradikalisierte Einzeltäter.

4078

• Wir wollen gezielt durch intensive Präventionsarbeit in Gefängnissen verhindern, dass 4079

sich Menschen dort radikalisieren und für Terrororganisationen gewinnen lassen.

Seite 114 von 139

4080

• Menschen, die sich in einem extremistischen Umfeld bewegen, dürfen wir nicht aufge-4081

ben. Wir setzen uns für die Beratung derjenigen ein, die sich bereits radikalisiert haben 4082

oder als gefährdet gelten. Wer aus einer extremistischen Szene aussteigen will, muss 4083

konkrete Hilfe bekommen.

4084

• Die Präventionsprogramme des Bundes gegen Extremismus wollen wir systematisch 4085

evaluieren, professionalisieren und standardisieren.

4086

• Wir wollen wieder eine Demokratieklausel einführen. Empfänger von Fördergeldern 4087

müssen sich klar und ausdrücklich zu unserer freiheitlich-demokratischen Grundord-4088

nung bekennen.

4089

 

4090

Alle zur Extremismusbekämpfung notwendigen Instrumente nutzen

4091

Wann immer möglich, sind zur Extremismusbekämpfung alle notwendigen Instrumente zu 4092

nutzen.

4093

• Dazu gehören Verbote von verfassungsfeindlichen Organisationen und Vereinen, Ver-4094

bote von Symbolen des Hasses und des Terrors, Einreise- und Aufenthaltsverbote, Aus-4095

weisungen, Abschiebungen und Grundrechtsverwirkungen.

4096

• Wir werden dafür sorgen, dass Gefährder mit allen gesetzlichen Möglichkeiten über-4097

wacht werden. Die personellen Ressourcen hierfür sind nicht beliebig erweiterbar. Des-4098

halb werden wir auch alle technischen Möglichkeiten zur wirksamen Überwachung nut-4099

zen – wie die elektronische Fußfessel – und uns für entsprechende Rechtsgrundlagen 4100

einsetzen.

4101

• Wir wollen die Möglichkeit schaffen, radikalisierte Gefährder in Sicherungsverwahrung 4102

zu nehmen, sobald sie strafrechtlich in Erscheinung treten und damit ihre Gewaltbereit-4103

schaft zeigen. Wer sich zum Beispiel im Ausland als Terrorist ausbilden lässt, ist eine 4104

große Gefahr und gehört ins Gefängnis. Die Sicherungsverwahrung wollen wir daher be-4105

reits für Ersttäter nutzen.

4106

• Das Werben um Sympathie für kriminelle oder terroristische Vereinigungen wollen wir 4107

wieder unter Strafe stellen.

4108

• Waffen gehören nicht in die Hände von Extremisten. Daher haben wir die Regelabfrage 4109

der Waffenbehörden beim Verfassungsschutz eingeführt und die gesetzliche Grundlage 4110

dafür geschaffen, dass bereits die Mitgliedschaft in einer verfassungsfeindlichen Verei-4111

nigung zur waffenrechtlichen Regelunzuverlässigkeit führt. Auf diesem Weg wollen wir 4112

weitergehen und den Datenaustausch zwischen den Behörden erleichtern.

4113

• Wir wollen die Möglichkeit schaffen, dass Richter direkt bei der Verurteilung eines ext-4114

remistischen Straftäters ein generelles, lebenslanges Waffenverbot aussprechen kön-4115

nen.

4116

• Die Mindeststrafe für illegalen Waffenhandel wollen wir deutlich erhöhen. Er soll künftig 4117

mit einer Freiheitsstrafe von nicht unter zwei Jahren geahndet werden.

Seite 115 von 139

4118

• Demokratie lebt von der Kontroverse. Zur Demokratie gehört Kritik. Und Demokratie 4119

verträgt Protest. Die Grenze ist aber überschritten, wenn Kommunalpolitiker und andere 4120

Repräsentanten des Staates angegriffen werden. Für uns gilt: Wehret den Anfängen. Wir 4121

werden nicht tolerieren, dass Menschen, die sich in politischen Ämtern ehrenamtlich en-4122

gagieren, von Verfassungsfeinden eingeschüchtert oder attackiert werden.

4123

 

4124

9.6. Stärkung unserer Sicherheitsbehörden

4125

Unsere Sicherheitsbehörden haben wir personell, materiell und strategisch massiv gestärkt.

4126

Diesen Weg setzen wir konsequent fort.

4127

 

4128

Zusammenarbeit der Sicherheitsbehörden intensivieren

4129

Das Gemeinsame Extremismus- und Terrorismusabwehrzentrum (GETZ) hat sich als Koope-4130

rations- und Kommunikationsplattform bewährt. Auch das Gemeinsame Terrorismusab-4131

wehrzentrum zur Bekämpfung des islamistischen Terrorismus (GTAZ) steht für eine gelun-4132

gene Zusammenarbeit und Aufgabenteilung zwischen Verfassungsschutz und Polizei sowie 4133

Bund und Ländern.

4134

• Wir werden die Zusammenarbeit aller Sicherheitsbehörden weiter intensivieren und ste-4135

tig an aktuelle Herausforderungen anpassen. Insbesondere geht es uns darum, die ge-4136

meinschaftlichen Aufgaben von Bund und Ländern im Umgang mit Gefährdern auch ge-4137

meinschaftlich wahrzunehmen.

4138

• Auch für niederschwellige Herausforderungen muss die Zusammenarbeit zwischen 4139

Bund und Ländern weiter verbessert werden. So müssen politisch motivierte Straftäter, 4140

die polizeilich bekannt sind und ihren Wohnort wechseln, automatisiert an die jeweils 4141

zuständige Staatsschutzstelle übergeben werden können.

4142

 

4143

Befugnisse für die digitale Welt wirksam gestalten

4144

Wir werden weiter dafür kämpfen, dass die Sicherheitsbehörden die Befugnisse erhalten, 4145

die sie für eine effektive Aufklärung im Vorfeld eines Anschlages brauchen. Denn es darf 4146

keinen technischen Vorsprung zwischen denen geben, die Anschläge planen, und denen, 4147

die diese verhindern sollen. Die Befugnisse von Polizei und Verfassungsschutz müssen auch 4148

in der digitalen Welt so wirksam sein, wie sie es in der analogen Welt sind. Wenn ein rich-4149

terlicher Beschluss eine Telefonüberwachung oder die Durchsuchung einer Wohnung er-4150

möglicht, muss Gleiches auch für verschlüsselte Nachrichten und Telefonate gelten, für das 4151

digitale Büro auf dem Computer oder Laptop.

4152

• Die Voraussetzungen für die Quellen-TKÜ und Online-Durchsuchung – sowohl bei der 4153

Gefahrenabwehr als auch bei der Strafverfolgung – wollen wir bundesweit anpassen, so-4154

dass diese Instrumente rechtssicher und effektiv eingesetzt werden können.

4155

• Wenn Gefahr droht, müssen unsere Behörden schnell und zuverlässig in der Lage sein, 4156

die Tatverdächtigen zu ermitteln. Bund und Länder müssen enger zusammenarbeiten Seite 116 von 139

4157

und für einen gemeinsamen Rechtsrahmen gemeinsame Software bereitstellen, die 4158

schnell einsatzbereit ist.

4159

• Wenn sich Bedrohungen, die Vorgehensweise der Täter oder die technischen Rahmen-4160

bedingungen verändern, müssen Eingriffsbefugnisse angepasst werden. Dazu gehört 4161

auch, die Möglichkeiten der Künstlichen Intelligenz zu nutzen, um frühzeitig Strukturen 4162

erkennen und ihnen entgegenwirken zu können. Daten, die im Rahmen von Ermittlungen 4163

anfallen, können so besser und zielgerichteter ausgewertet werden.

4164

 

4165

Terrorismusfinanzierung austrocknen

4166

Wir werden dafür sorgen, dass die Finanzierung des Terrorismus – national wie internatio-4167

nal – intensiver bekämpft wird.

4168

• Die Zentralstelle für Finanztransaktionsuntersuchungen (Financial Intelligence 4169

Unit/FIU) muss deutlich gestärkt und in die Lage versetzt werden, Netzwerke zur Finan-4170

zierung von Terror und Verbrechen international tätiger Banden aufzudecken und zu zer-4171

schlagen . Dafür ist es erforderlich, sie wieder an das Bundeskriminalamt anzukoppeln.

4172

• Angesichts der terroristischen Bedrohungen müssen im Notfall alle staatlichen Kräfte – 4173

auch die Bundeswehr – zum Schutz der Menschen in Deutschland eingesetzt werden 4174

können. In besonderen Gefährdungslagen muss es möglich sein, die spezifischen Fähig-4175

keiten der Bundeswehr im Innern unterstützend zu nutzen, um terroristische Gefahren 4176

bewältigen zu können – unter Führung der Polizei und im Rahmen festgelegter Grenzen.

4177

• Wir setzen auch weiterhin auf gemeinsame interdisziplinäre Übungen der Polizeien der 4178

Länder, der Bundespolizei sowie der nicht-polizeilichen Behörden und Organisationen 4179

mit Sicherheitsaufgaben.

4180

 

4181

9.7. Gefahrenabwehr im Cyberraum

4182

Auf dynamische Entwicklungen im Cyberraum reagieren

4183

Unsere Grundversorgung mit Wasser, Strom und Telekommunikation und viele andere 4184

hochsensible Prozesse laufen über vernetzte IT-Systeme, die fortlaufend attackiert werden.

4185

Die Angriffsmethoden werden immer ausgefeilter. Daher brauchen wir widerstandsfähige 4186

IT-Infrastrukturen und -Netze. Für uns gilt: Was in der analogen Welt verboten ist, muss 4187

auch in der digitalen Welt verboten sein. Cybersicherheit ist nicht statisch. Ein Schutzniveau 4188

heute ist kein Garant für eine erfolgreiche Abwehr der Angriffe von morgen.

4189

• Wir werden daher fortwährend beurteilen, was notwendig ist, um angemessen auf die 4190

dynamischen Entwicklungen im Cyberraum zu reagieren.

4191

• In letzter Konsequenz heißt das auch: Wir müssen bei schweren Cyber-Angriffen in der 4192

Lage sein, aktiv auf die Ursache einzuwirken, um sie zu beenden. Wir werden die dafür 4193

erforderlichen rechtlichen Regelungen und eigene technischen Fähigkeiten für ange-4194

messene aktive Maßnahmen schaffen.

4195

 

Seite 117 von 139

4196

Informationssicherheit und Cyber-Abwehr stärken

4197

Eine enge und vertrauensvolle Zusammenarbeit zwischen Bund und Ländern ist unabding-4198

bare Voraussetzung, um den Herausforderungen auch bei der Cybersicherheit wirkungsvoll 4199

begegnen zu können.

4200

• Um die Zusammenarbeit zwischen Bund und Ländern weiter zu vertiefen, werden wir 4201

das Bundesamt für Sicherheit in der Informationstechnik zu einer Zentralstelle für Fra-4202

gen der Informations- und Cybersicherheit ausbauen. Es soll neben dem Bundesamt für 4203

Verfassungsschutz und dem Bundeskriminalamt eine starke dritte Säule der Cyber-Si-4204

cherheitsarchitektur bilden.

4205

• Das Nationale Cyber-Abwehrzentrum wollen wir so weiterentwickeln, dass es in komple-4206

xen Schadenslagen bundesweit eine Abwehr von Gefahren und Angriffen koordinieren 4207

kann.

4208

• Wir müssen bei IT-Beschaffungsvorhaben mehr Geld in den Schutz gegen Cyber-Angriffe 4209

investieren. Wir schlagen daher vor, künftig einen bestimmten Anteil der Sachmittel für 4210

IT-Vorhaben des Bundes für Informationssicherheit aufzuwenden („Cyber-Quote“), um 4211

eine sichere Digitalisierung zu gewährleisten.

4212

 

4213

Cyber-Sicherheitsforschung vorantreiben

4214

• Die Cyber-Sicherheitsforschung in Deutschland wollen wir stark vorantreiben. Cyber-Si-4215

cherheit „Made in Germany“ muss ein Markenzeichen bleiben.

4216

• Wir wollen, dass Deutschland Weltmarktführer für sichere IT-Lösungen und attraktiver 4217

Standort für innovative Unternehmen der Cybersicherheit wird. Dazu gehören führende 4218

Verschlüsselungstechnik und Security-by-design-Lösungen, damit Hackerangriffe un-4219

möglich werden, sowie diskriminierungsfreie Algorithmen. Nur so können wir das Ziel 4220

der Digitalen Souveränität erreichen.

4221

• Wir wollen eine transparente Zertifizierung von IT-Produkten, der die Menschen ver-4222

trauen können. Dazu wollen wir das Bundesamt für Sicherheit in der Informationstechnik 4223

so ausstatten, dass es als zentrale Zertifizierungs- und Standardisierungsstelle im inter-4224

nationalen Wettbewerb bestehen kann.

4225

 

4226

Wirtschaft besser vor Cyber-Angriffen schützen

4227

Wir werden Strukturen schaffen, die es der Wirtschaft ermöglichen, ihre Schutzmaßnahmen 4228

gegen Cyber-Attacken zu erhöhen. Dies gilt insbesondere für kleine und mittlere Unterneh-4229

men, vom Handwerk bis zu Hidden Champions. Gerade diese Unternehmen sind heute noch 4230

unzureichend sensibilisiert und geschützt, obgleich sie wegen ihrer Innovations- und Wirt-4231

schaftskraft begehrte Angriffsziele internationaler Konkurrenten, fremder Nachrichten-4232

dienste und Krimineller sind. Die wirtschaftlichen Schäden, die dadurch entstehen, sind im-4233

mens – bis hin zur Insolvenz und damit einhergehend dem Verlust vieler Arbeitsplätze.

Seite 118 von 139

4234

• Zur besseren Beratung und Unterstützung dieser Unternehmen wollen wir die Rolle des 4235

Bundesamtes für Sicherheit in der Informationstechnik weiter ausbauen.

4236

• Um kleine und mittlere Unternehmen bei der Stärkung ihrer IT-Sicherheit noch wirksa-4237

mer zu unterstützen, wollen wir weitere steuerliche Anreize prüfen, wie beispielsweise 4238

schnellere Abschreibungsmöglichkeiten von Investitionen in IT-Sicherheit.

4239

• Anträge für Förderprogramme zur Sensibilisierung und Unterstützung wollen wir weiter 4240

vereinfachen und Antragsverfahren beschleunigen.

4241

 

4242

9.8. Wirksamer Bevölkerungsschutz

4243

Sicherheit bedeutet auch, Menschen in elementarer Not zu helfen. Dafür wollen wir Bevöl-4244

kerungsschutz und Katastrophenhilfe weiter stärken. Wir brauchen eine nationale Katastro-4245

phenschutzstrategie, damit Deutschland krisenfester wird.

4246

 

4247

Bevölkerungsschutz stärken und enger vernetzen

4248

Für bundesweite Krisenszenarien brauchen wir einen verlässlichen Rahmen. Die nächste 4249

Krise kann ihren Ursprung im Klimawandel haben, durch Extremwetterereignisse wie Dür-4250

ren, Trinkwassermangel, Waldbrände oder Hochwasser ausgelöst werden oder Folge von 4251

Cyberattacken oder Desinformationskampagnen sein. Durch die Zuständigkeitsverteilung 4252

auf unterschiedliche Bundesressorts, Länder, Städte, Landkreise, Gemeinden, Hilfsorgani-4253

sationen und das Technische Hilfswerk kann bundesweit ebenso wie regional zielgerichtet 4254

auf Entwicklungen reagiert werden. Gleichzeitig sind genau in diesem Zuständigkeitsge-4255

flecht funktionierende 360-Grad-Lageinformationen, etablierte gemeinsame Kommunika-4256

tionsroutinen, gute Koordination und gemeinsame Entscheidungsfindung der Schlüssel 4257

zum Erfolg.

4258

• Unser föderales System für den Bevölkerungsschutz in Deutschland ist leistungsfähig, 4259

flexibel und flächendeckend verfügbar. Die Anforderungen von heute sind allerdings an-4260

dere als früher. Wir wollen deshalb neue Kriterien für eine länderübergreifende Scha-4261

denslage entwickeln und zwischen Bund und Ländern einen modernen Bevölkerungs-4262

schutz etablieren.

4263

• Für eine engere Vernetzung und Verzahnung aller Akteure im Bevölkerungsschutz in 4264

Bund, Ländern, Kommunen und Hilfsorganisationen wollen wir nach dem Vorbild der 4265

Abwehrzentren des Bundes und der Länder im Bereich der Inneren Sicherheit eine ge-4266

meinsame Plattform bilden.

4267

• Wir wollen das Bundesamt für Bevölkerungsschutz und Katastrophenhilfe weiter aus-4268

bauen, sodass der Bevölkerungsschutz stärker als bisher in einem integrativen Netzwerk 4269

aller Akteure zusammenwirken kann.

4270

• Gerade bei biologischen Gefahren wie Pandemien oder Bioterrorismus ist das enge Zu-4271

sammenwirken von Innen- und Gesundheitsbehörden besonders wichtig. Deshalb wol-4272

len wir das Bundesamt für Bevölkerungsschutz und Katastrophenhilfe und das Robert Seite 119 von 139

4273

Koch-Institut in ihrer Zusammenarbeit sowie in ihrer jeweiligen Koordinierungsfunktion 4274

rechtlich, personell und technisch stärken. Dies gilt sowohl für die Risikoanalyse, die Pan-4275

demieplanung als auch die Koordinierung der Lagebewältigung.

4276

• Als Lehre aus der Corona-Pandemie wollen wir eine neue Nationale Reserve Gesund-4277

heitsschutz für wichtige medizinische Versorgungsgüter – wie etwa persönliche Schutz-4278

ausrüstung – schaffen und diese rechtlich sowie finanziell langfristig absichern. Gleiches 4279

gilt für die im Ausbau befindlichen THW-Logistikzentren.

4280

• Das Bundesamt für Bevölkerungsschutz und Katastrophenhilfe soll als zentrale Informa-4281

tionsplattform zu den nationalen Bevorratungen von Energie, Wasser, Gesundheit und 4282

Ernährung dienen.

4283

 

4284

Warnmedien modern gestalten, nicht-polizeiliche Gefahrenabwehr stärken

4285

Blinde Flecken im Warnsystem wollen wir schließen, damit sich die Menschen in unserem 4286

Land auf ein gut aufgestelltes und zuverlässiges Warnsystem in Krisenlagen und Gefahren-4287

situationen verlassen können.

4288

• Wir wollen die Warnmedien modern und zielgerichtet gestalten. Um sicherzustellen, 4289

dass Warnungen auch in Zukunft den richtigen Empfängerkreis schnell erreichen, muss 4290

der Warnmix aus digitalen und analogen Medien fortwährend angepasst werden. Hierzu 4291

gehört es auch, die Nutzung von Cell-Broadcasting-Technologie als ergänzenden Multi-4292

plikator im Warnmittelmix zu prüfen.

4293

• Mit Blick auf die sogenannte nicht-polizeiliche Gefahrenabwehr setzen wir auf ein Inves-4294

titionsprogramm, um das erfolgreich gestaltete Wachstum der Bundessicherheitsbehör-4295

den in den vergangenen Jahren auch auf diesen Bereich zu übertragen.

4296

• Wir wollen Hilfsorganisationen und Feuerwehren so ausstatten, dass sie noch besser auf 4297

große Schadensereignisse und langanhaltende Einsätze reagieren können.

4298

• Für die von Unglücken betroffenen Menschen und Regionen müssen schnell unbürokra-4299

tische Hilfsprogramme zur Verfügung stehen. Unfallversorgung und Notdienste funkti-4300

onieren nur im engen Zusammenwirken von Bund, Ländern, Städten, Landkreisen, Ge-4301

meinden und ehrenamtlichen Helfern vor Ort. Feuerwehren, Technisches Hilfswerk, Ret-4302

tungsdienste und freie Träger sind dabei unverzichtbar für unsere Daseinsvorsorge.

4303

• Das bewährte System des flächendeckenden Brand- und Katastrophenschutzes wollen 4304

wir erhalten und weiter fördern.

4305

 

4306

Bürgerschaftliches Engagement fördern, zivil-militärische Zusammenarbeit stärken

4307

Der große Anteil ehrenamtlicher Kräfte stellt nicht nur ein außergewöhnlich hohes Maß 4308

bürgerschaftlichen Engagements dar, sondern sichert auch ein flexibles System effizienter 4309

Gefahrenabwehr und Hilfeleistung.

Seite 120 von 139

4310

• Diejenigen, die sich aufopfernd und unentgeltlich rund um die Uhr für die Sicherheit ih-4311

rer Mitmenschen einsetzen, müssen dauerhaft unterstützt werden. Sie sind Vorbilder in 4312

unserer Gesellschaft.

4313

• Mit weiteren Anreizen wollen wir die vielen Frauen und Männer, die sich heute schon 4314

ehrenamtlich für die Sicherheit einsetzen, auch künftig für diese Aufgabe begeistern und 4315

weitere Menschen hierfür gewinnen.

4316

• Die Menschen in Deutschland sollen weiterhin darauf vertrauen können, dass ihnen die 4317

Bundeswehr mit ihren spezifischen Fähigkeiten im Katastrophen- und Bevölkerungs-4318

schutz auch im Inland rasch und wirksam hilft – sei es zur Hilfe bei Schnee- oder Hoch-4319

wasserkatastrophen oder sei es nach Großschadensereignissen.

4320

• Für biologische und pandemische Lagen – genauso wie für andere Großschadensfälle – 4321

setzen wir auf regelmäßige Übungen, um eine bessere Koordinierung zwischen Gesund-4322

heits- und Sicherheitskräften von Bund, Ländern und Kommunen zu erreichen.

4323

 

4324

9.9. Starke und bürgernahe Justiz

4325

Ein starker Rechtsstaat erfordert eine starke Justiz. Um Verbrechen wirksam bekämpfen zu 4326

können, brauchen wir daher auch gut ausgestattete, unabhängige Gerichte und leistungs-4327

fähige Staatsanwaltschaften. Die Menschen müssen sich darauf verlassen können, dass 4328

Recht und Gesetz konsequent durchgesetzt werden. Unsere Rechtsordnung gilt dabei für 4329

jeden, der in unserem Land lebt – unabhängig von seiner Herkunft oder Religion. Unser 4330

Rechtsstaat duldet keine Paralleljustiz, die unsere Gesetze und Gerichte verdrängen will.

4331

 

4332

Strafverfahren beschleunigen

4333

Einer raschen Reaktion von Polizei, Staatsanwaltschaft und Gerichten bei Straftaten kommt 4334

eine Schlüsselrolle zu.

4335

• Wir wollen schnellere Verfahren, bei denen die Strafe der Tat auf dem Fuße folgt. Dies 4336

muss gerade für straffällige Jugendliche gelten. Daher wollen wir, dass Jugendstrafver-4337

fahren beschleunigt und vereinfacht werden.

4338

• Täter zwischen 18 und 21 Jahren sollen in der Regel wie Erwachsene bestraft werden. Die 4339

Anwendung des Jugendstrafrechts muss in diesen Fällen eine Ausnahme bleiben.

4340

 

4341

Opferschutz Vorrang vor Täterschutz geben

4342

Opfer von Straftaten leiden insbesondere bei Gewaltverbrechen sehr lange unter deren Fol-4343

gen.

4344

• Die in den vergangenen Jahren in das Strafprozessrecht aufgenommenen Informations-4345

und Beteiligungsrechte für Opfer von Straftaten wollen wir daher ausbauen und mit Le-4346

ben füllen.

4347

• Dem Opferschutz wollen wir ein stärkeres Gewicht in der polizeilichen und justiziellen 4348

Aus- und Weiterbildung geben.

Seite 121 von 139

4349

• Wir wollen die psychosoziale Prozessbegleitung stärken und einen Rechtsanspruch auf 4350

kostenlose Opferhilfe umsetzen.

4351

• Auch unser Strafrecht wollen wir noch mehr auf den Opferschutz ausrichten und Inten-4352

siv- und Wiederholungstäter wirksam aus dem Verkehr ziehen. Dafür sollen Kettenbe-4353

währungsstrafen abgeschafft werden. Wird wegen einer Straftat innerhalb laufender Be-4354

währungszeit erneut eine Freiheitsstrafe aufgrund einer vorsätzlichen Straftat verhängt, 4355

so soll diese künftig grundsätzlich nicht erneut zur Bewährung ausgesetzt werden dür-4356

fen.

4357

 

4358

Unsere Justiz modernisieren

4359

Eine moderne Justiz- und Rechtspolitik muss verständlich und serviceorientiert sein, um 4360

von Bürgerinnen und Bürgern akzeptiert zu werden.

4361

• Wir wollen digitale Zugangsmöglichkeiten ausbauen und so den schnellen und kosten-4362

günstigen Zugang zu Rechtsprechung und Rechtsberatung sicherstellen. Dazu gehören 4363

auch zügige und kommunikationstechnisch zeitgemäße Verfahren.

4364

• Den Modernisierungsstau an unseren Gerichten wollen wir auflösen und für Richter und 4365

Staatsanwälte dieselben digitalen Arbeitsumgebungen schaffen, wie sie in der Anwalt-4366

schaft und freien Wirtschaft üblich sind.

4367

• Die gemeinsamen Anstrengungen von Bund und Ländern wollen wir in einem Pakt für 4368

den digitalen Rechtsstaat 2.0 bündeln.

4369

• Konflikte und Rechtsstreitigkeiten lassen sich oft auch außergerichtlich beilegen. Wir 4370

stärken deshalb alternative Lösungsansätze wie Mediation und Schiedsverfahren. So 4371

entlasten wir unsere Justiz von Bagatellangelegenheiten.

4372

 

 

Seite 122 von 139

4373

10. Neue Lebensqualität in Stadt und Land – aus Liebe zu unserer Heimat 4374

 

4375

Unser Unionsversprechen: Wir arbeiten für eine gute Lebensqualität überall in Deutschland. Ob 4376

großstädtischer Kiez, Kleinstadt oder Dorf: Wir respektieren und schützen jede Form von Hei-4377

mat. Wir sind eine offene Gesellschaft, in der alle ihre Träume verwirklichen können – und nie-4378

mand eingeredet bekommen darf, wie er zu wohnen und zu leben hat. Für uns ist Lebensqualität 4379

keine Frage der Postleitzahl, sondern ein universeller Auftrag, den wir ernstnehmen, weil wir der 4380

Schaffung von gleichwertigen Lebensverhältnissen in ganz Deutschland verpflichtet sind.

4381

In unserem Modernisierungsjahrzehnt gehen wir die Herausforderungen des guten Lebens für 4382

die Menschen an: vom bezahlbaren Wohnraum in Städten über neues Leben in Innenstädten und 4383

Dorfkernen nach der Corona-Krise, von der Bewahrung der Natur und wirtschaftlicher Entwick-4384

lung in allen Regionen bis hin zur guten Nahversorgung und Verkehrsanbindung.

4385

Auch hier setzen wir auf ein neues Denken: Wir werden nicht alle Probleme mit mehr Geld lösen 4386

können. Vielmehr brauchen wir einen vernünftigen Mix aus klugen Investitionen, neuen Freiräu-4387

men, Experimentierfeldern und Anreizsystemen sowie Stärkung von Eigeninitiativen. Gleichzei-4388

tig setzen wir uns für den Zusammenhalt in der Gesellschaft ein, stärken Ehrenamt und Sport, 4389

bieten Integration und schaffen moderne Bedingungen, damit sich Kultur und Kreativität nach-4390

haltig entwickeln können.

4391

 

4392

10.1. Gutes Wohnen in lebendigen Dörfern und Städten

4393

Die eigenen vier Wände sind unser Zuhause, ein ganz hohes Gut. In der Corona-Pandemie 4394

hat sich gezeigt, wie wichtig es ist, eine Wohnung zu haben, in der man sich wohlfühlt und 4395

Platz hat zum Leben und auch, um zumindest zeitweise dort zu arbeiten. Genug Wohnraum 4396

in einem intakten Umfeld ist ein Ziel von CDU und CSU. Wo Wohnraum teuer ist oder fehlt, 4397

wie in vielen Großstädten, heißt unsere Devise: mehr, schnell, modern und bezahlbar 4398

bauen. Wo Gebäude alt sind, gilt es, sie auf den heutigen Stand zu bringen und energetisch 4399

zu sanieren. Der Wunsch nach einem Eigenheim soll schneller in Erfüllung gehen. Eine Poli-4400

tik gegen Einfamilienhäuser ist gegen die Interessen der Menschen und mit uns nicht zu 4401

machen.

4402

 

4403

Mehr bezahlbaren Wohnraum schaffen

4404

Der beste Mieterschutz ist und bleibt ausreichender Wohnraum. Wir setzen nicht auf recht-4405

lich fragwürdige und ungeeignete Eingriffe, wie den Mietendeckel, sondern packen das 4406

Problem an der Wurzel. Nur wenn das Wohnungsangebot steigt, können Mieten stabil blei-4407

ben.

4408

• Unser Ziel ist, dass bis 2025 mehr als 1,5 Millionen neue Wohnungen entstehen. Wir füh-4409

ren unsere Wohnraumoffensive fort und setzen auf eine starke Wirtschaftsbranche, gute 4410

Bedingungen und Wertschätzung für unser Handwerk und die Freien und Planenden Be-4411

rufe.

Seite 123 von 139

4412

• Als Investitionsanreiz werden wir die derzeit befristeten Abschreibungsmöglichkeiten 4413

beim Mietwohnungsbau verlängern. Derjenige, der neue Mietwohnungen schafft, soll 4414

auch nach Ende 2021 fünf Prozent der Anschaffungs- und Herstellungskosten zusätzlich 4415

von der Steuer absetzen können.

4416

• Planungs- und Genehmigungsverfahren werden wir beschleunigen und gemeinsam mit 4417

den Ländern Umsetzungshemmnisse abbauen. Wir wollen die Anzahl der Bauvorschrif-4418

ten signifikant verringern. Ein Bauantrag für Wohnimmobilien soll regulär zwei Monate 4419

nach vollständiger Vorlage aller notwendigen Unterlagen abschließend bearbeitet sein 4420

– andernfalls gilt er grundsätzlich als genehmigt.

4421

• Wir wissen: Der Platz in Großstädten und Metropolregionen ist endlich. Deshalb gehört 4422

zu einer ehrlichen Baupolitik auch, das Umland zu stärken – vor allem durch eine starke 4423

Anbindung an Bus und Bahn sowie eine moderne Grundversorgung.

4424

 

4425

Nachhaltig, bezahlbar und altersgerecht bauen

4426

Nachhaltig und bezahlbar bauen heißt für uns, umweltfreundliche Baustoffe zu verwenden 4427

und flexibel Bauland auszuweisen, aber den Flächenverbrauch gering zu halten, barrierefrei 4428

zu bauen und den sozialen Wohnungsbau zu fördern.

4429

• Wir wollen das Bauen mit Holz und die Verwendung von Recyclingmaterial deutschland-4430

weit stärker voranbringen. Die Bauwirtschaft soll zu einer Kreislaufwirtschaft werden, 4431

die auf mehr heimischen Baustoffen – wie zum Beispiel Sand, Gips und Holz – basiert 4432

und Recyclingmaterial in Bauteilen nutzt.

4433

• Wir wollen das große Potenzial von Nachverdichtung, Aufstockung von Gebäuden, An-4434

und Ausbauten, Überbauung von Parkplätzen und Supermärkten und der Brachflächen-4435

entwicklung ausschöpfen. Deshalb werden wir die Brachlandentwicklung im Rahmen der 4436

Städtebauförderung verstärken und die Nachverdichtung fördern.

4437

• Mit dem Baulandmobilisierungsgesetz ist es für Kommunen einfacher geworden, Bau-4438

land auszuweisen und auch innerörtliche Flächen zu mobilisieren. Wir wollen ihre Mög-4439

lichkeiten – unter Beachtung des Grundsatzes Innen- vor Außenentwicklung – noch wei-4440

ter vergrößern und ihnen noch mehr Flexibilität einräumen.

4441

• Wir werden den sozialen Wohnungsbau weiter fördern und das Wohngeld ab 2022 regel-4442

mäßig anpassen. Wohnraum muss auch für Menschen mit geringem Einkommen bezahl-4443

bar sein. Beim sozialen Wohnungsbau werden wir mit den Ländern erörtern, ob sie auf 4444

jeden Bundes-Euro mindestens einen Euro drauflegen und zweckgebunden einsetzen.

4445

• Uns ist wichtig, dass Menschen möglichst lange in der eigenen Wohnung, im Haus oder 4446

im angestammten Wohnviertel leben können. Deshalb werden wir die dafür erforderli-4447

chen Investitionen in den altersgerechten und barrierefreien Umbau – insbesondere 4448

über KfW-Programme – unterstützen.

4449

• Wir wollen mehr Flächen für den Wohnungsbau mobilisieren. Dazu werden wir prüfen, 4450

wie Grundbesitzer, die landwirtschaftliche Flächen für Bauland zur Verfügung stellen, Seite 124 von 139

4451

die dabei erzielten Einnahmen steuerbegünstigt in den Mietwohnungsbau reinvestieren 4452

können. So entlasten wir Städte und Ballungsräume.

4453

 

4454

Gebäude energetisch sanieren

4455

Die energetische Sanierung unseres Gebäudebestands ist ein Muss. Nur so können wir die 4456

Klimaziele erreichen. Gleichzeitig müssen vor allem Mieter vor finanzieller Überlastung ge-4457

schützt sein.

4458

• Wir nehmen die Wohnungsbaugesellschaften in die Pflicht. Zudem werden wir die steu-4459

erliche Förderung der energetischen Sanierung, insbesondere von Betriebsgebäuden 4460

und von vermieteten Wohnungen, weiter verbessern.

4461

• Schrittweises Sanieren soll besser gefördert werden, da schon kleinere Maßnahmen 4462

wichtig und wirksam sind.

4463

• Wir werden „Mieterstrom“ voranbringen und noch bestehende Hemmnisse abbauen – 4464

auch um lokale Zusammenschlüsse zu erleichtern. Mieter sollen genauso von der Ener-4465

giewende profitieren wie Eigenheimbesitzer.

4466

 

4467

Dörfer und Städte vitalisieren

4468

Wir wollen unsere Innenstädte, Stadtteilzentren und Ortskerne erhalten. Sie müssen nach 4469

der Corona-Krise neugestaltet und in ihrer Funktion als Orte der Begegnung und Vielfalt 4470

gestärkt werden. Lebendige Fußgängerzonen, Marktplätze und der Einzelhandel vor Ort 4471

machen unsere Städte lebenswert. Gleichzeitig stehen unsere Einzelhändler mit der Digita-4472

lisierung und dem E-Commerce vor enormen Herausforderungen. Auch die Corona-Pande-4473

mie stellt für sie eine historische Belastung dar.

4474

• Deshalb werden wir einen Zukunftspakt für Innenstädte schmieden. Als wichtigen Teil 4475

des Pakts werden wir zusätzlich zu den bestehenden Städtebauprogrammen ein Förder-4476

programm „Attraktive Innenstadt“ auflegen, von dem auch kleinere Städte und Gemein-4477

den profitieren. Damit wollen wir deutlich mehr Mittel bereitstellen, beispielsweise für 4478

die Modernisierung von Fußgängerzonen oder den Umbau von Passagen und Ladenge-4479

schäften. Auch Dorf- und Innenstadtmanager mit einschlägigem Know-How sollen so ge-4480

fördert werden können.

4481

• Wir werden Smart-City-Konzepte entwickeln und ein eigenständiges Programm für mehr 4482

Grünflächen und natürliche Vielfalt in der Stadt auflegen.

4483

• Auch die Dorfkernsanierung werden wir noch stärker fördern. Alle Altersgruppen sollen 4484

mitten im Ort am öffentlichen Leben teilhaben können. Dazu werden wir den Wohnraum 4485

im Ortskern für Alt und Jung neu in den Blick nehmen, die dortige Ansiedlung von Un-4486

ternehmen und Startups mit Investitionszulagen fördern und den Ausbau der Mehrfunk-4487

tionshäuser und Dorfläden unterstützen.

4488

• Auf dem Land werden wir begleitend zum massiven Breitbandausbau Co-Working-4489

Spaces für kreatives Arbeiten fördern. So stärken wir Kleinstädte, Dörfer und ländliche Seite 125 von 139

4490

Räume und entlasten die Ballungszentren. Gleichzeitig tun wir etwas für den Klima-4491

schutz, weil viele Pendlerströme vermieden werden.

4492

 

4493

Den Traum vom Eigenheim verwirklichen

4494

Das eigene Haus und die eigene Wohnung sind viel mehr als Wohnraum, sie sind Zuhause, 4495

Zukunftsinvestition und Altersvorsorge. Wir unterstützen alle, die sich ein Eigenheim wün-4496

schen. Wohneigentum sollen sich auch Menschen mit normalem Einkommen und auch Fa-4497

milien leisten können. Wir wollen kein Deutschland, in dem sich nur Großverdiener ein 4498

Haus kaufen oder bauen können.

4499

• Wir werden das KfW-Wohneigentumsprogramm für Familien ausweiten. Wer Kinder hat, 4500

soll stärker davon profitieren. Dazu sollten Darlehen, Tilgungszuschüsse oder Zinsverbil-4501

ligungen nach Anzahl der Kinder gestaffelt werden.

4502

• Den Ländern werden wir ermöglichen, einen Freibetrag bei der Grunderwerbsteuer beim 4503

erstmaligen Erwerb selbstgenutzten Wohnraums von 250.000 Euro pro Erwachsenen 4504

plus 100.000 Euro pro Kind zu gewähren.

4505

• Fertighäuser im modularen Baustil können ein Mittel sein, Individualität und Ressour-4506

ceneffizienz gleichermaßen zu verbinden. Sie verdienen deshalb gerade mit Blick auf das 4507

familiäre Eigenheim mehr Aufmerksamkeit.

4508

• Die Sanierung im Bestand werden wir weiter fördern und eine neue Umbaukultur für 4509

mehr bezahlbaren Wohnraum und neues Leben in alten Gebäuden entfachen.

4510

• Attraktive Mietkaufmodelle sollen es vor allem jungen Menschen mit geringerer Kapital-4511

ausstattung ermöglichen, Wohneigentum zu erwerben. In diesem Zusammenhang prü-4512

fen wir auch die Unterstützung genossenschaftlicher Wohnmodelle.

4513

 

4514

10.2. Gleichwertige Lebensverhältnisse und wirtschaftliche Entwicklung in allen Regi-4515

onen

4516

Gleichwertige Lebensverhältnisse zu erreichen, ist eine zentrale Aufgabe für eine funktio-4517

nierende Gesellschaft. Dazu sind viele Anstrengungen notwendig – die Gleichbehandlung 4518

von Stadt und Land bei der digitalen Infrastruktur, die Stärkung unserer Dörfer und Städte 4519

in benachteiligten Regionen, neue Konzepte der Mobilität, Nahversorgung und Arbeit so-4520

wie die weitere Stärkung des Ehrenamts.

4521

 

4522

Zukunftsregionen schaffen: Stadt und Land zusammenbringen

4523

Wir haben ein gesamtdeutsches Fördersystem für strukturschwache Regionen geschaffen.

4524

Damit haben wir den Grundstein dafür gelegt, dass die Regionen, die im Struktur- oder de-4525

mografischen Wandel stehen, neue Kraft gewinnen und sich neu erfinden können. Struk-4526

turschwache Regionen und ländliche Räume werden wir weiter verlässlich fördern und dort 4527

massiv in die Infrastruktur jeder Art investieren.

Seite 126 von 139

4528

• Wir wollen die von Bund und Ländern getragene „Gemeinschaftsaufgabe Agrarstruktur 4529

und Küstenschutz“ als wichtiges Förderinstrument für die ländlichen Räume weiterent-4530

wickeln und damit insbesondere regionale Wertschöpfungsketten stärken.

4531

• Aus besonders strukturschwachen Gebieten werden wir Modellregionen machen. Hier 4532

fördern wir nicht nur Investitionen, sondern streben auch weniger Bürokratie an. Wer 4533

investiert, kann dort von Standards abweichen, die nicht sicherheits- und umweltrele-4534

vant sind. Genehmigungsverfahren werden wir beschleunigen.

4535

• Ländliche Regionen sollen Innovationsräume sein. Wir wollen, dass Startups leerste-4536

hende landwirtschaftliche Gebäude und ehemalige Stallungen nutzen können. Davon 4537

sollen vor allem Unternehmen der grünen Branche mit neuen Herstellungsverfahren für 4538

Lebensmittel oder neuen landwirtschaftlichen Verfahren, wie Vertical Farming, profitie-4539

ren. Hindernisse im derzeitigen Bau- und Planungsrecht werden wir beseitigen.

4540

• Stadt und Land müssen zusammengedacht werden. Bundesmittel werden wir deshalb 4541

zunehmend an gemeinsame Planungen in den Regionen binden und an räumlich sinn-4542

volle Planungsverbünde vergeben. Wir setzen vermehrt auf Regionalbudgets ohne the-4543

matische und organisatorische Vorgaben. So schaffen wir Platz für die Entwicklung neuer 4544

Ideen und pragmatischer Lösungen vor Ort.

4545

 

4546

Zukunft Ost – Chancen für das geeinte Deutschland schaffen

4547

Die Friedliche Revolution und die Deutsche Einheit haben sich bereits zum 30. Mal gejährt.

4548

Die Bürgerinnen und Bürger in Ostdeutschland haben in den vergangenen Jahren nicht nur 4549

einen tiefgreifenden gesellschaftlichen und wirtschaftlichen Umbruch gemeistert, sondern 4550

viele Regionen zu starken Clustern in Wirtschaft und Wissenschaft entwickelt. Wir wollen 4551

dies weiter stärken und gleichzeitig auch die ländlichen Regionen unterstützen. Wir wollen 4552

niemanden vergessen und mit unserer Politik die besondere Prägung der Menschen in den 4553

neuen Bundesländern nicht aus den Augen verlieren. Wir wollen die internationale Vernet-4554

zung besonders nach Mittel- und Osteuropa vorantreiben und die Verbindungen zu unse-4555

ren Nachbarländern weiter festigen. Gemeinsam mit unseren osteuropäischen Nachbarn 4556

werden wir ein starkes Europa sein.

4557

• Wir stehen zum vereinbarten Kohle-Kompromiss. Die Braunkohle-Regionen, die be-4558

troffenen Energieunternehmen, die Zulieferer und vor allem die Beschäftigten können 4559

sich auf uns verlassen.

4560

• Die Ansiedlung weiterer Bundesbehörden in Ostdeutschland, besonders im ländlichen 4561

Raum, werden wir fortsetzen. So wollen wir eine neue digitale Ausbildungsstätte der 4562

Bundeswehr in den neuen Bundesländern schaffen. Mit dem Schwerpunkt der Digitali-4563

sierung soll sie nicht nur als Ausbildungs-, sondern auch als berufsbegleitendes Weiter-4564

bildungszentrum für die Bundeswehr etabliert werden.

4565

• Die Verkehrsinfrastruktur nach Polen und Tschechien werden wir mit einem Sonderpro-4566

gramm intensiv ausbauen und dadurch unsere gemeinsamen Grenzregionen im Herzen 4567

Europas weiter stärken.

Seite 127 von 139

4568

• Die guten regionalen Kenntnisse und nachbarschaftlichen Erfahrungen der neuen Bun-4569

desländer in den Grenzregionen wollen wir nutzen, um den wissenschaftlichen Dialog 4570

und die Kooperation vor allem mit den mittel- und osteuropäischen Nachbarländern zu 4571

stärken. Wir werden die Wissenschaftsbeziehungen in die mittel- und osteuropäischen 4572

Staaten ausbauen, beispielsweise durch eine regelmäßige Wissenschaftskonferenz und 4573

die Gründung eines deutsch-tschechischen Forschungsinstituts.

4574

• Um das Innovationssystem im internationalen Maßstab auszubauen, müssen die besten 4575

wissenschaftlichen Talente mit Innovationsorientierung gezielt gefördert werden. Ge-4576

meinsam mit der Fraunhofer-Gesellschaft und führenden Universitäten werden wir da-4577

für einen Joint Innovation Track als Pilotprojekt fördern, um Wissenschaftlerinnen und 4578

Wissenschaftler in Richtung einer universitären Berufung weiterzuentwickeln, die aka-4579

demische Exzellenz mit einem außergewöhnlichen Verständnis für angewandte For-4580

schung verbinden. Diese gezielte Nachwuchsförderung zugunsten eines effizienten 4581

Technologietransfers soll in den neuen Bundesländern erprobt und bei Erfolg bundes-4582

weit ausgebaut werden.

4583

• Wir wollen das Weimarer Dreieck Frankreich – Deutschland – Polen stärken und das Ver-4584

ständnis füreinander fördern. Deshalb werden wir ein Jugendaustauschprogramm zwi-4585

schen diesen drei europäischen Staaten auf den Weg bringen und Anreize für neue Städ-4586

tepartnerschaften setzen.

4587

• Wir sind in dieser Legislaturperiode einen ersten Schritt zur Übernahme eines höheren 4588

Anteils bei den Erstattungen an die Rentenversicherung für die Ansprüche aus den Son-4589

der- und Zusatzversorgungssystemen der ehemaligen DDR gegangen. Damit haben wir 4590

die ostdeutschen Bundesländer entlastet. In der kommenden Legislaturperiode wollen 4591

wir einen weiteren Schritt gehen.

4592

• Mit der Überführung der Stasi-Akten ins Bundesarchiv sind eine dauerhafte Aufarbei-4593

tung und Beforschung dieses Aspektes der SED-Diktatur und die bewährte Form der Ak-4594

teneinsicht auch weiterhin gewährleistet. Zur Bewältigung der Folgen der Diktatur für 4595

die Betroffenen ist die Positionierung der Opferbeauftragten beim Deutschen Bundes-4596

tag ein wichtiger Meilenstein. Wir wollen Wissenschaft und Forschung zur SED-Diktatur 4597

auch in den kommenden Jahren explizit fördern und ausbauen.

4598

 

4599

Menschen für ländlichen Raum begeistern und Arbeitsplätze auf dem Land schaffen

4600

In vielen ländlichen Regionen werden Arbeitskräfte gesucht. Gerade junge Menschen, die 4601

zum Studieren in die Städte gegangen sind, sind sich der großen Chancen in ihrer Heimat 4602

oft gar nicht bewusst. Das werden wir ändern. Auch wollen wir mit Leuchttürmen im Grü-4603

nen neue qualifizierte Arbeitsplätze in strukturschwache Regionen bringen.

4604

• Wir unterstützen die flächendeckende Einrichtung von Heimatagenturen. Sie werden ak-4605

tiv um junge Menschen und Familien für die ländlichen Räume werben und der örtlichen 4606

Wirtschaft bei der Suche nach Fachkräften helfen.

Seite 128 von 139

4607

• Wir haben bereits begonnen, Behörden und Forschungseinrichtungen zu dezentralisie-4608

ren und vor allem im Osten Deutschlands anzusiedeln. In Zukunft wollen wir so auch den 4609

Strukturwandel in den ehemaligen Kohleregionen gestalten. Wir werden die Anstren-4610

gungen zur Verlagerung von Bildungs-, Forschungs- und Verwaltungseinrichtungen er-4611

höhen.

4612

• Ebenso werden Unternehmen, Hochschulen und Verbände durch unsere aktive Struktur-4613

politik unterstützt, sich in ländlichen Regionen anzusiedeln.

4614

 

4615

Wirtschaftsfaktor Tourismus ausbauen

4616

Tourismus ist ein wichtiger Wirtschaftsfaktor in Stadt und Land. Mit der Weiterentwicklung 4617

der nationalen Tourismusstrategie der Bundesregierung schaffen wir die Voraussetzungen 4618

für ein qualitatives und nachhaltiges Wachstum des Tourismus.

4619

• Die Tourismuswirtschaft und die touristische Infrastruktur berücksichtigen wir auch bei 4620

der Ausgestaltung eines gesamtdeutschen Fördersystems für strukturschwache Räume.

4621

• Die internationale Wettbewerbsfähigkeit des Deutschlandtourismus sichern wir mit ei-4622

ner Stärkung des Auslandsmarketings der Deutschen Zentrale für Tourismus.

4623

 

4624

Dörfer und Regionen smart machen

4625

Unser Anspruch ist: Alles muss vom Dorf aus erreichbar sein! Eine gute Versorgung mit al-4626

len Leistungen der Daseinsvorsorge, mit Gütern und Dienstleistungen ist möglich, wenn 4627

Vor-Ort-Angebote, digitale Möglichkeiten und eine gute Anbindung zusammengebracht 4628

werden.

4629

• Wir arbeiten mit Hochdruck an Gigabit-Anschlüssen und einer flächendeckenden Mobil-4630

funkanbindung, perspektivisch möglichst schnell mit 5G. Dort, wo die Wirtschaftlich-4631

keitsprüfung von Unternehmen zur Installation von Glasfaserleitungen scheitert, wer-4632

den wir die Kommunen in die Lage versetzen, den Breitbandausbau in Eigenregie voran-4633

zutreiben.

4634

• Gleichzeitig werden wir bereits digitale Anwendungen erproben und Rahmenbedingun-4635

gen für ihren Einsatz in allen Lebensbereichen schaffen. Wir werden integrierte Lösun-4636

gen für ländliche Regionen entwickeln und in „Digitalen Dörfern“ modellhaft umsetzen.

4637

• Mit einer neuen Smart-City und einer Smart-Country-Strategie werden wir Städte, Kom-4638

munen und Regionen bei der Digitalisierung unterstützen.

4639

 

4640

Gute medizinische Versorgung auf dem Land sichern

4641

Anspruch und Ziel von CDU und CSU ist eine gute medizinische Versorgung – unabhängig 4642

von Alter, Wohnort und Geldbeutel.

4643

• Zusammen mit den Ländern werden wir 5 000 zusätzliche Studienplätze für Humanme-4644

dizin schaffen und gleichzeitig die Landarztquote bei der Studienplatzvergabe über die 4645

heutige Grenze von zehn Prozent hinaus erhöhen.

Seite 129 von 139

4646

• Damit chronisch Kranke und ältere Patienten gut und kontinuierlich versorgt sind, brin-4647

gen wir die Telemedizin voran und setzen ergänzend zur klassischen Hausarztversor-4648

gung auf den Einsatz von Gemeindeschwestern.

4649

• Wir müssen alles daransetzen, die wohnortnahe geburtshilfliche Versorgung im ländli-4650

chen Raum zu sichern und die Pflegekapazitäten auszubauen.

4651

 

4652

Die beste Verkehrsinfrastruktur schaffen

4653

Wohlstand braucht eine Verkehrsinfrastruktur orientiert an den Bedürfnissen von Men-4654

schen, Wirtschaft und Umwelt. Wer gleichwertige Lebensverhältnisse will, muss auch die 4655

vielfältigen Realitäten in Stadt und Land anerkennen. Immer mehr Menschen wollen auf die 4656

Bahn oder das Fahrrad umsteigen, aber auch weiterhin – gerade auf dem Land – auf guten 4657

Straßen mit dem Auto oder dem Bus unterwegs sein können.

4658

• Wir setzen auf die beste Infrastruktur für unser Land. Wir werden unser Verkehrsnetz 4659

mit Schienen, Straßen und Wasserstraßen in Stand halten und weiter zukunftsfest ma-4660

chen. Dafür werden wir die von uns erreichten Rekordinvestitionen auf hohem Niveau 4661

verlängern.

4662

• Den Nationalen Radverkehrsplan werden wir mit Nachdruck umsetzen und fortentwi-4663

ckeln. Wir setzen auf gut ausgebaute und gut vernetzte Radwege, Radschnellwege sowie 4664

mehr Sicherheit für Radfahrer und mehr Abstellmöglichkeiten.

4665

• Wo Städte und Dörfer durch Verkehr belastet sind, werden wir für Entlastung durch 4666

smarte Verkehrsführungen und die Stärkung des ÖPNV sorgen. Wir werden aber auch 4667

weiterhin Ortsumgehungen bauen. Und wo es häufig Stau gibt, werden wir unsere Bun-4668

desstraßen und Autobahnen erweitern. Weniger Staus bedeuten mehr Klimaschutz.

4669

• Gleichzeitig sorgen wir für mehr Lärmschutz an den Verkehrswegen und werden die 4670

Lärmgrenzwerte überprüfen.

4671

 

4672

Überall nachhaltig mobil sein

4673

Menschen sollen so mobil sein, wie sie es möchten: individuell, flexibel und umweltfreund-4674

lich. Dabei ist uns die Wahlmöglichkeit zwischen den Verkehrsangeboten genauso ein An-4675

liegen wie die Vernetzung und Digitalisierung von Mobilitätsformen. Mobilität muss ein-4676

fach, flexibel und komfortabel für Jung und Alt sein – auf dem Land, in der Stadt und auch 4677

für mobilitätseingeschränkte Personen.

4678

• Unser Ziel ist es, überall ein bedarfsgerechtes Grundangebot im öffentlichen Verkehr 4679

sicherzustellen – auch auf dem Land. Wir wollen deshalb einen flächendeckenden Min-4680

deststandard schaffen, der allen Menschen einen gleichwertigen, barrierearmen und ein-4681

fachen Zugang zum ÖPNV gewährt. Den Deutschlandtakt werden wir im Fern- und Re-4682

gionalverkehr realisieren.

Seite 130 von 139

4683

• Je besser Menschen über das Angebot der Verkehrsunternehmen informiert sind, umso 4684

mehr werden sie den ÖPNV nutzen. Wir unterstützen deshalb den Betrieb digitaler, of-4685

fener und diskriminierungsfreier Mobilitätsplattformen als Eingangstür für alle Ange-4686

bote des öffentlichen Verkehrs einschließlich des ÖPNV.

4687

• Wir werden die Chancen der Digitalisierung für den ÖPNV und die Vernetzung verschie-4688

dener Verkehrsträger nutzen. Echtzeitinformationen mit alternativen Empfehlungen für 4689

die Weiterfahrt sind selbstverständlich, ergänzende Mobilitätsservices, Sharing-, Roller-4690

, Rad- und Fußverkehr müssen integriert werden.

4691

• Attraktive Verkehrskonzepte umfassen eine echte Verzahnung zwischen motorisiertem 4692

Individualverkehr und dem ÖPNV. Wir wollen Mobilitätsstationen entlang wichtiger Inf-4693

rastruktur entstehen lassen und durch vernetzte Wegeketten ein Rückgrat für die nach-4694

haltige Mobilität formen. Dafür werden wir bestehende Park & Ride-Angebote weiter-4695

entwickeln und beispielsweise solargetriebene Lademöglichkeiten für PKW, E-Roller und 4696

E-Bikes integrieren.

4697

• Eine wichtige Ergänzung des öffentlichen Verkehrs sind Poolingangebote und Bedarfs-4698

halte, für die wir bereits rechtsichere Rahmenbedingungen geschaffen haben und nun 4699

die neue Mobilität bei der Personenbeförderung voranbringen wollen.

4700

• Wir wollen die nachhaltige Gestaltung der Mobilität befördern und Entwicklungen über 4701

die Einrichtung von Reallaboren der Zukunftsmobilität anstoßen. So kann in Stadtteilen 4702

und Landkreisen erprobt und erlebt werden, wie die Mobilität der Zukunft aussieht und 4703

welche Angebote wir zukünftig deutschlandweit ausrollen können.

4704

 

4705

• Deutschland ist das Land der Ideen und der Innovationen, der kreativen Köpfe, Initiati-4706

ven, Wissenschaftler, Startups, der Industrie und des Mittelstands. Mit dem Deutschen 4707

Zentrum für die Mobilität der Zukunft wollen wir all das bündeln und verbinden. Dabei 4708

geht es uns ganz konkret darum, die Zukunftsfähigkeit des Mobilitätsstandorts Deutsch-4709

land zu stärken, Produktentwicklungen zu beschleunigen, für nachhaltige und innovative 4710

Mobilität - wie das autonome Fahren - zu begeistern.

4711

 

4712

Alle Verkehrsteilnehmer schützen

4713

• Deutschland braucht mehr Miteinander von Radverkehr, Fußverkehr, ÖPNV und moto-4714

risiertem Verkehr. Kommunen sollen mehr Spielräume bei der Gestaltung von fuß- und 4715

radverkehrsfreundlichen Räumen erhalten und beispielsweise Fahrrad-Vorrangrouten 4716

ausweisen können. Sicherheit für alle Verkehrsteilnehmer steht für uns dabei an erster 4717

Stelle.

4718

• Die Zahl der Getöteten und Schwerverletzten soll auf null sinken. In den letzten Jahren 4719

ist die Zahl der Verkehrstoten bereits deutlich gesunken. Die Einführung von Fahrassis-4720

tenzsystemen und automatisierten Fahrfunktionen zur Erhöhung der Sicherheit werden 4721

wir weiter vorantreiben und fördern. Dies gilt insbesondere für den LKW- und PKW-Ver-4722

kehr.

Seite 131 von 139

4723

 

4724

Schöpfung bewahren

4725

Der Erhalt der natürlichen Lebensgrundlagen, von Lebensräumen und Arten ist von zentra-4726

ler Bedeutung, auch um die biologische Vielfalt in Deutschland zu fördern. Wir wollen dazu 4727

unsere Schutzgebiete erhalten, weiterentwickeln und besser miteinander vernetzen.

4728

• Wir werden eine nationale Biodiversitätsstrategie vorlegen, die sich an den Zielen der 4729

Europäischen Biodiversitätsstrategie und des Übereinkommens über die biologische 4730

Vielfalt (CBD) orientiert.

4731

• Wir wollen sorgsam mit unseren Böden umgehen. Wir werden die Versiegelung weiter 4732

reduzieren und die Entsiegelung und die Nachnutzung von bereits versiegelten Flächen 4733

vorantreiben.

4734

• Dort, wo die Nutzung Eingriffe in Natur und Landschaft nach sich zieht, werden wir die 4735

Kompensationsvorschriften des Naturschutz- und des Baurechts überprüfen und Kom-4736

pensationsmaßnahmen so weiterentwickeln, dass sie zielgerichtet die Biodiversität in 4737

der Region fördern. Dabei setzen wir auf einen in die Landwirtschaft integrierten Aus-4738

gleich, auf die qualitative Aufwertung von Biotopen und den Einsatz von Ersatzgeldzah-4739

lungen für die Instandhaltung und den Erhalt von Biotopen.

4740

• Wir werden die bedrohten Arten, die auf der Roten Liste stehen, und ihre Lebensräume 4741

besser schützen. Hierzu werden wir das Monitoring sowie die Forschung weiter aus-4742

bauen, um so den Schutzstatus der Arten besser überprüfen zu können.

4743

• Die Biologische Vielfalt unserer Meere und Küsten ist ein großer Schatz. Deshalb gilt es, 4744

den Schutz der Ost- und Nordsee sowie des Wattenmeeres gemäß der Europäischen Bio-4745

diversitätsrichtlinie unter Berücksichtigung der Fischerei zu verbessern.

4746

• Wir werden ein nationales Klimaanpassungsgesetz zur Daseins- und Zukunftsvorsorge 4747

einbringen, um den Folgen des Klimawandels in der Stadt, auf dem Land sowie an den 4748

Küsten, Meeren und in den Bergen zu begegnen.

4749

 

4750

10.3. Stärkung von Zusammenhalt und Ehrenamt

4751

Die vor uns liegenden Herausforderungen brauchen einen starken gesellschaftlichen Zu-4752

sammenhalt. Er erwächst aus sozialen Beziehungen, einer positiven Verbundenheit der 4753

Menschen mit dem Gemeinwesen und einer ausgeprägten Gemeinwohlorientierung. Wir 4754

haben den Anspruch, eine aktive Bürgergesellschaft zu gestalten, in der sich jeder Einzelne 4755

für seine Mitmenschen einsetzen kann und dadurch Verantwortung übernimmt.

4756

 

4757

Ehrenamt fördern

4758

Bürgerschaftliches, freiwilliges und ehrenamtliches Engagement gehört zu den zentralen 4759

Elementen einer lebendigen Demokratie. Es ist eine der wesentlichen Grundlagen des ge-4760

sellschaftlichen Zusammenhalts. Wir haben das Ehrenamt immer gefördert und neue For-Seite 132 von 139

4761

mate – wie etwa die Mehrgenerationenhäuser, den Bundesfreiwilligendienst und die Deut-4762

sche Stiftung für Engagement und Ehrenamt – ins Leben gerufen. Der Erfolg spricht für sich: 4763

Heute engagiert sich fast jede dritte Person ab 17 Jahren ehrenamtlich. Die Zahl der ehren-4764

amtlich Tätigen steigt weiter an.

4765

• Wir wollen noch mehr junge Erwachsene für den Dienst an der Gesellschaft gewinnen.

4766

Wir wollen die Attraktivität der Freiwilligendienste – etwa durch die Anpassung des Ta-4767

schengelds, eine breite Angebotsauswahl und eine hohe Qualität der Angebote – weiter 4768

steigern und einen Rechtsanspruch einführen. Über die Möglichkeiten der Freiwilligen-4769

dienste soll vermehrt schon in den Schulen informiert werden.

4770

• Vorhaben, die das Ehrenamt unterstützen und auch in strukturschwachen und ländlichen 4771

Regionen von besonderer Bedeutung sind, werden wir fördern. Neben den Aktivitäten 4772

der Deutschen Stiftung für Engagement und Ehrenamt werden wir daher die Einrichtung 4773

von Anlaufstellen für das Ehrenamt in Kreisen und Gemeinden flankierend begleiten. Sie 4774

können die Ehrenamtlichen beraten, ihnen die Arbeit erleichtern und bei der Vernetzung 4775

und Qualifizierung helfen.

4776

• Zugleich wollen wir mehr Seniorinnen und Senioren, Menschen mit Zuwanderungsge-4777

schichte und Menschen mit Behinderung für das Ehrenamt gewinnen.

4778

 

4779

Religion als wertvollen Teil unserer Gesellschaft begreifen

4780

Wir betrachten es als wertvollen Bestandteil unseres Grundgesetzes, dass es Staat und Re-4781

ligion einerseits trennt und es andererseits ermöglicht, dass Religion unsere Gesellschaft 4782

bereichert. Die Kirchen und die Religionsgemeinschaften haben gerade auch in der Corona-4783

Pandemie einen unverzichtbaren Dienst am Nächsten geleistet und den Blick auf jene ge-4784

lenkt, die es in dieser Zeit am schwersten hatten.

4785

• Wir bekennen uns zum bewährten Konzept des Religionsverfassungsrechts und zum Ko-4786

operationsmodell zwischen Kirche und Staat. Religionsfreiheit kann es nur auf dem Bo-4787

den des Grundgesetzes geben, das dieser Freiheit Ausdruck verleiht.

4788

• Wir haben Vertrauen in das Potenzial von Religion, Werte zu vermitteln und einen wich-4789

tigen Beitrag für das Gemeinwesen zu leisten. Die Freiheit der Kirchen und Religionsge-4790

meinschaften, in die Gesellschaft hineinzuwirken, muss daher unantastbar bleiben.

4791

• Wir bekennen uns zum Schutz der christlichen Feiertage ebenso wie zur Sonntagsruhe.

4792

Der Religionsunterricht an Schulen ist dabei essenziell.

4793

• Wir setzen uns für die grundgesetzlich garantierte Religionsfreiheit aller Menschen ein.

4794

Diese Religionsfreiheit verstehen wir in einem positiven Sinne: Religionen sollen in der 4795

Öffentlichkeit eine starke Stimme sein. Dazu gehören der regelmäßige Austausch und 4796

der Dialog mit den verschiedenen Religionsgemeinschaften dieses Landes.

4797

• Wir halten es für wichtig, dass hierzulande predigende Imame auch in Deutschland und 4798

in deutscher Sprache ausgebildet werden. Das erleichtert die Integration.

4799

 

Seite 133 von 139

4800

10.4. Integration als Fundament des Miteinanders

4801

Wer in Deutschland lebt, ist Teil unserer Gesellschaft. Uns ist wichtig, dass Menschen mit 4802

Zuwanderungsgeschichte in allen Bereichen teilhaben können. Ihre Integration ist auch die 4803

Voraussetzung für gesellschaftlichen Zusammenhalt. Integration besteht für uns aus För-4804

dern und Fordern.

4805

• Voraussetzung für eine gelingende Integration ist ein Bekenntnis zu Deutschlands 4806

grundlegenden Werten und Normen, seiner Verfassung, seinen Gesetzen, seinen Insti-4807

tutionen, seiner Geschichte, Sprache und Kultur. Wir haben die Erwartung, dass die zu 4808

uns kommenden Menschen unsere Werte teilen, sich an unsere Gesetze halten und un-4809

sere Sprache sprechen.

4810

• Sprache hat überragende Bedeutung – für die gleichberechtigte Teilhabe, aber auch für 4811

die Identifikation mit unserem Land und unserer Kultur. Wir wollen den Spracherwerb 4812

beschleunigen und setzen dabei vermehrt auf digitale, flexible und zielgruppenspezifi-4813

sche Angebote.

4814

• Auch Zuwanderer und ihre Familien aus der Europäischen Union sollen durch gezielte 4815

Informations- und Sprachförderungsmaßnahmen bessere Unterstützung erhalten, um 4816

ihren Zuzug in qualifizierte Beschäftigung und die Integration der ganzen Familie von 4817

Anfang an zu fördern.

4818

• Für eine gezielte Frühförderung halten wir eine flächendeckende Sprachstanderhebung 4819

bei Kindern und die Einführung einer verbindlichen Sprachförderung für notwendig.

4820

Kommunale Integrationsfachkräfte werden wir durch ein Bundesprogramm fördern und 4821

dadurch insbesondere die Beratungsangebote in Kitas und Grundschulen verbessern.

4822

• Frauen und Mütter sind in Integrationskursen unterrepräsentiert und haben oft größere 4823

Schwierigkeiten bei der Arbeitsmarktintegration. Durch gezielte digitale Angebote wol-4824

len wir sie beim Spracherwerb unterstützen und mit niedrigschwelligen Beratungsange-4825

boten fördern. Damit wollen wir auch Kinder besser erreichen.

4826

 

4827

Chancen von Migrantinnen und Migranten verbessern

4828

Wir wollen die Arbeitsmarktintegration von Migranten zu einer Erfolgsgeschichte machen.

4829

Die Erwerbstätigenquote steigt kontinuierlich an. Die vielen Menschen mit erfolgreichen 4830

Integrationsgeschichten sind wichtige Vorbilder für gelingende Integration.

4831

• Wir wollen daher die Anerkennung und Übertragbarkeit ausländischer Qualifikationen 4832

weiter fördern und ein besonderes Gewicht auf die Arbeitsmarktintegration von Frauen 4833

legen.

4834

• Wir freuen uns über die Gründungsbereitschaft von Menschen mit Zuwanderungsge-4835

schichte. Mit einem befristeten Programm wollen wir Kenntnisse über Gründungs-4836

schritte, Kreditzugang und Zulassungsvoraussetzungen zielgerichtet vermitteln.

4837

• Chancengerechtigkeit soll es in der gesamten Gesellschaft geben – in der Wirtschaft, in 4838

der Bildung und auch im öffentlichen Dienst. Wir werben dafür, dass sich mehr junge Seite 134 von 139

4839

Menschen für eine berufliche Laufbahn im öffentlichen Dienst entscheiden. Dies stärkt 4840

auch die Identifikation von Menschen mit Zuwanderungsgeschichte mit unserem Staat.

4841

 

4842

Vertriebene und Aussiedler wertschätzen

4843

Wir bekennen uns zur Geschichte aller Deutschen – auch derer, die ein besonders schweres 4844

Kriegsfolgeschicksal erleiden mussten. Das kulturelle Erbe der Heimatvertriebenen und 4845

Aussiedler ist ein selbstverständlicher und wertvoller Teil unserer Identität. Ohne die Hei-4846

matvertriebenen wäre der Wiederaufbau unseres Landes nach dem Zweiten Weltkrieg so 4847

nicht gelungen. Aussiedler sind mit ihrem Können, ihrem Fleiß und ihrer kulturellen Tradi-4848

tion ein Gewinn für unser Land. Vertriebene und ihre Nachkommen, Aussiedler und deut-4849

sche Minderheiten im Ausland haben Brücken der Verständigung in Europa gebaut. Ein ge-4850

eintes, friedliches und starkes Europa ist eine entscheidende Grundlage für das vor uns lie-4851

gende Modernisierungsjahrzehnt. Der Verständigungs- und Gestaltungswille der Vertrie-4852

benen und Aussiedler sind uns hierfür eine wichtige Leitschnur.

4853

• Wir werden den verständigungs- und erinnerungspolitischen Einsatz der Vertriebenen-4854

und Aussiedlerverbände, den Kulturerhalt und die Kulturarbeit durch eine zukunftssi-4855

chere Förderung stärken. Nötig sind außerdem Akzente in Bildung und Forschung, um 4856

durch moderne Vermittlungsmethoden das Wissen hierüber zu festigen.

4857

• An der gesetzlich garantierten Aufnahme von Spätaussiedlern werden wir festhalten und 4858

weiterhin Eingliederungshilfen leisten. Fremdverschuldeter Altersarmut und renten-4859

rechtlichen Benachteiligungen bei Aussiedlern und Spätaussiedlern werden wir ent-4860

schieden begegnen.

4861

• Die deutschen Minderheiten und Volksgruppen in verschiedenen Ländern wollen wir 4862

weiterhin darin unterstützen, ihre Sprache und Kultur zu pflegen.

4863

• Uns ist wichtig, das Amt des Beauftragten der Bundesregierung für Aussiedlerfragen und 4864

nationale Minderheiten in einer exponierten Stellung in der Bundesregierung zu stärken.

4865

• Die Bundesförderung zur Pflege des Kulturgutes der Vertriebenen und Flüchtlinge und 4866

zur Förderung der wissenschaftlichen Forschung nach § 96 Bundesvertriebenengesetz 4867

wollen wir als einen Ankerpunkt der Vertriebenen- und Aussiedlerpolitik stärken.

4868

 

4869

10.5. Deutschland als Kulturnation

4870

Kultur ist wichtiger Standortfaktor. Sie ist aber vor allem eins: sie ist Ausdruck von Huma-4871

nität. Kultur stiftet Identität, Gemeinschaft und Zusammenhalt. Kulturelle Bildung und eine 4872

lebendige kulturelle Infrastruktur gehören als Teil der Daseinsvorsorge in den Alltag aller 4873

Bürgerinnen und Bürger. Die Möglichkeit, Kunst und Kultur – egal ob Breitenkultur oder 4874

Spitzenkultur - zu erleben, ist eine entscheidende Voraussetzung für gleichwertige Lebens-4875

verhältnisse in ganz Deutschland. Wir werden unsere erfolgreiche Kulturpolitik in den Kom-4876

munen, den Ländern und vor allem im Bund unter Einbezug der Kulturverbände konsequent 4877

fortsetzen.

Seite 135 von 139

4878

• Wir setzen alles daran, dass bis zur Pandemie erreichte hohe jährliche Wachstum der 4879

Kultur- und Kreativwirtschaft und deren beeindruckende wirtschaftliche Dynamik wie-4880

derzugewinnen. Diese Branche mit ihren 1,8 Millionen Erwerbstätigen steht wie kaum 4881

eine andere für kreative Erneuerung, aber auch für kulturelle Vielfalt und künstlerische 4882

Qualität.

4883

• Um die Folgen der Pandemie zu mildern, wird das Programm „Neustart Kultur“ für alle 4884

Akteure und Sparten fortgesetzt.

4885

• Mit Förderprogrammen wie etwa „Kultur im ländlichen Raum“, dem Denkmalschutz-Son-4886

derprogramm und dem Zukunftsprogramm Kino unterstützen wir die Kultur auf dem 4887

Land.

4888

• Wir stärken die Kultur- und Kreativwirtschaft und den Filmstandort Deutschland und da-4889

mit nicht nur die Kultur, sondern auch einen wichtigen Wirtschaftsfaktor. Dazu führen 4890

wir die Film-, Musik-, Literatur-, Verlags- und Games-Förderung fort und werden die För-4891

derinstrumente von Bund, Ländern und der Filmförderungsanstalt stärker aufeinander 4892

abstimmen.

4893

• Die deutsche Sprache ist ein besonders wichtiger Teil unserer Identität. Wir wollen sie 4894

weiterhin fördern und wertschätzen, als Kultur-, Amts- und Umgangssprache.

4895

• Wir bewahren unsere Traditionen. Für CDU und CSU ist der Kulturföderalismus in 4896

Deutschland mit seinem historisch gewachsenen Reichtum an regionalen Identitäten 4897

eine bereichernde Kraft der Vielfalt, die es zu wahren gilt. Wir stehen für die Pflege und 4898

den Erhalt alter Bräuche, Trachten und Volkstänze sowie heimatlichen Liedguts. Dabei 4899

werden wir insbesondere die Laien- und Amateurmusik sowie die freien Ensembles un-4900

terstützen.

4901

• Die vier nationalen Minderheiten in Deutschland – Dänen, Sorben, Friesen, deutsche 4902

Sinti und Roma – gehören mit ihren Traditionen zur kulturellen Vielfalt unseres Landes, 4903

die es zu bewahren gilt. Deshalb sollen bestehende Förderungen fortgeschrieben wer-4904

den.

4905

• Im Interesse der Nachhaltigkeit wollen wir unseren Beitrag dazu leisten, dass Kulturein-4906

richtungen, Filmproduktionen oder Kulturevents ihren ökologischen Fußabdruck deut-4907

lich verkleinern.

4908

• Die soziale Absicherung von Künstlern ist uns wichtig. Wir werden deshalb die Künstler-4909

sozialversicherung stärken und Künstler und Kreative besser absichern, indem wir den 4910

Schutz in der gesetzlichen Kranken - und Pflegeversicherung bei selbstständiger nicht-4911

künstlerischer Nebentätigkeit dauerhaft ausbauen. Zudem werden wir prüfen, wie die 4912

Arbeitslosenversicherung für Beschäftigte in der Kulturbranche weiterentwickelt wer-4913

den kann.

4914

 

4915

Erinnerungskultur lebendig halten

Seite 136 von 139

4916

Die Vorhaben zur Wahrung der Erinnerungskultur, die Aufarbeitung der NS-Zeit und der 4917

SED-Diktatur zur Schärfung des Bewusstseins der nachkommenden Generationen gegen 4918

Antisemitismus, Rassismus und Extremismus bleiben für uns dauerhafte Aufgaben.

4919

• Mit der Stiftung „Orte der deutschen Demokratiegeschichte“ werden wir an historischen 4920

Orten Rückschau auf demokratische Sternstunden halten, um die Kräfte der Zivilgesell-4921

schaft und die Wehrhaftigkeit unserer Demokratie zu stärken.

4922

• Das Bundesprogramm „Jugend erinnert“ wollen wir ausbauen und die Zeitzeugenarbeit 4923

in das digitale Zeitalter führen.

4924

• Die Provenienzforschung vor allem zum NS-Kunstraub wie auch zu Kulturgutentziehun-4925

gen während der SED-Diktatur und des Kolonialismus bleiben kulturpolitischer Schwer-4926

punkt.

4927

• Ebenso bleibt uns der Schutz von Künstlerinnen und Künstlern, die im Ausland verfolgt 4928

werden und in Deutschland Exil suchen, ein wichtiges Anliegen.

4929

 

4930

10.6. Eine moderne Medienlandschaft

4931

Für uns sind freie und pluralistische Medien Grundpfeiler einer verantwortungsvollen de-4932

mokratischen Gesellschaft. Die Weiterentwicklung eines vielfältigen und anspruchsvollen 4933

Mediensystems aus Presse, Rundfunk und Onlineangeboten bleibt ein zentraler Bestandteil 4934

unserer Medienpolitik.

4935

• Wir bekennen uns zu einem starken, unabhängigen öffentlich-rechtlichen Rundfunk. Wir 4936

setzen uns für eine Reform des Auftrags ein, der dem technischen Fortschritt und dem 4937

veränderten Nutzungsverhalten Rechnung trägt.

4938

• Wir wollen anregen und ermöglichen, dass Rundfunkanstalten stärkere Kooperationen 4939

eingehen und weitere Synergien schaffen – auch im Sinne der Beitragszahlerinnen und 4940

Beitragszahler.

4941

• Die Deutsche Welle wollen wir zum stärksten Auslandssender Europas aufbauen.

4942

• Alle Bürgerinnen und Bürger sollen sich gut darüber informieren können, was bei ihnen 4943

vor Ort geschieht. Dabei kommt es wesentlich auf Abonnementzeitungen und Anzeigen-4944

blätter an. Wir werden zielgerichtete Instrumente zur Förderung des Absatzes, der wei-4945

teren Unterstützung und des Vertriebs entwickeln, die neben finanzieller Unterstützung 4946

auch Erleichterungen für die Beschäftigung von Zustellern und Zustellerinnen umfassen.

4947

 

4948

Passenden Rahmen für digitale Mediennutzung setzen

4949

In den vergangenen Jahren hat sich die Meinungsvielfalt weltweit erhöht – durch den digi-4950

talen Wandel, zunehmende Medienkonvergenz, Innovationen und damit einhergehenden 4951

höheren Reichweiten. Zugleich sind durch den unregulierten Vormarsch der Digitalkon-4952

zerne Risiken entstanden: Meinungsdiskriminierung, Manipulation, Missbrauch von Markt-Seite 137 von 139

4953

und Meinungsmacht oder Verletzung der Privatsphäre. Es bedarf daher moderner und 4954

neuer Regelwerke und Kontrollmechanismen.

4955

• Unser Ziel ist es, die Medien- und Nachrichtenkompetenz aller Bürgerinnen und Bürger 4956

zu stärken. Zudem wollen wir das Schutzniveau für Jugendliche im Internet anheben. Die 4957

großen Digitalkonzerne müssen Verantwortung übernehmen und – wo nötig – reguliert 4958

werden.

4959

• Bürgerinnen und Bürger sollen auch in der digitalen Welt auf die Richtigkeit der Nach-4960

richten vertrauen können. Private und öffentlich-rechtliche audiovisuelle Medienange-4961

bote sowie journalistisch-redaktionelle Inhalte, deren Beitrag ein Wert für die Gemein-4962

schaft ist, sollen auf modernen Medienplattformen einfacher auffindbar sein.

4963

• Wir werden die Rahmenbedingungen so setzen, dass die Angebote der Kunst- und Krea-4964

tivwirtschaft in der digitalen Ära nachhaltig refinanziert werden können.

4965

 

4966

10.7. Engagierte Sportförderung

4967

Sport und Bewegung stärken die Gesundheit, das soziale Miteinander, die Bildung, die In-4968

klusion, die Integration und damit den Zusammenhalt in unserer Gesellschaft. Acht Millio-4969

nen Menschen engagieren sich in mehr als 90 000 Sportvereinen und leisten damit einen 4970

unverzichtbaren Beitrag für das Gemeinwohl und eine lebendige Zivilgesellschaft. Pande-4971

miebedingt haben viele Kinder und Erwachsene ihren Sport schmerzlich vermisst, Sportver-4972

eine und Sportstättenbetreiber wurden stark gebeutelt.

4973

• Wir werden die Sportentwicklung in allen Bereichen unterstützen und vor allem die Ge-4974

sundheitsprävention ausbauen.

4975

• Die Sportvereine sollen wieder voll durchstarten können. Deshalb werden wir sie bei der 4976

Bindung und Neugewinnung von Mitgliedern unterstützen.

4977

• Den Sanierungsstau der kommunalen und vereinseigenen Sportstätten und Schwimm-4978

bäder werden wir mit besonderem Fokus auf energetische Sanierung, Barrierefreiheit 4979

und Digitalisierung nachhaltig abbauen.

4980

• Den aufstrebenden E-Sport werden wir in Deutschland stärker unterstützen.

4981

• Damit der Sport seine gesellschaftliche Funktion erfüllen kann, braucht es engagierte 4982

Trainer und Übungsleiter. Wir werden für eine steuerliche Förderung ihrer Aus- und Wei-4983

terbildung sowie für ihre berufliche Anerkennung sorgen. Ebenso werden wir die Pro-4984

gramme gegen Diskriminierung und Rassismus und für Integration und Inklusion fort-4985

setzen und stärker fördern.

4986

• Zur Bekämpfung des sexuellen Missbrauchs im Kontext des Sports werden wir eine zent-4987

rale Stelle für „safe sports“ einrichten und bestehende Präventionsprogramme stärken.

4988

• Den Leistungssport werden wir weiterentwickeln und unseren Athletinnen und Athleten 4989

eine sichere und wertegebundene Basis für ihre Spitzenleistungen bieten. Dafür werden Seite 138 von 139

4990

wir noch bessere Trainings- und Wettkampfbedingungen etablieren, die Stützpunkt-4991

struktur modernisieren und die Organisation professionalisieren.

4992

• Die Kontrollinstanzen für den Kampf gegen Doping, Manipulation und Korruption sollen 4993

gestärkt werden. Sie müssen international stärker abgestimmt und auch kontrolliert wer-4994

den.

4995

• Wir unterstützen die Bewerbungen für internationale sportliche Großveranstaltungen in 4996

Deutschland. Diese müssen ökologisch, ökonomisch und sozial nachhaltig sein, wie auch 4997

auf eine breite gesellschaftliche Zustimmung stoßen. Das ist auch der Maßstab für eine 4998

Bewerbung um olympische Spiele in Deutschland.

Seite 139 von 139

 
"""

DEBUG_ATTACHMENT_MARKER_ROWNUMBER_FOUND = "'\033[94m[Zeilennummer entfernt]\033[0m'"
DEBUG_ATTACHMENT_MARKER_ROWNUMBER_NOT_FOUND = "'\033[93m[Zeilennummer noch nicht gefunden...]\033[0m'"
DEBUG_ATTACHMENT_MARKER_MINUS = "'\33[101m[Minus entfernt]\033[0m'"
DEBUG_ATTACHMENT_MARKER_SEITENZAHL = "'\33[95m[Seitenzahl entfernt]\033[0m'"
DEBUG_ATTACHMENT_MARKER_DOT = "'\33[105m[Aufzählungspunkt entfernt]\033[0m'"

row_counter = -13
row_number_counter = 1


def cleanUp(text, debug=False):
    global row_counter
    global row_number_counter

    if text is None:
        return "ERROR: Text was empty"

    output_raw_cleaned = []
    lines = text.split('\n')

    # leere Zeilen löschen
    lines = [line for line in lines if line.strip() != "" and line.strip() != "Inhaltsverzeichnis"]

    # Inhaltsverzeichnis erstellen - For headline-recognition
    #inhaltsverzeichnis = [line for line in lines if "......" in line]
    # remove dots maybe
    #print(inhaltsverzeichnis)

    #lines = [line for line in lines if not "......" in line]  # TODO (erwischt nicht alle)

    for index, line in enumerate(lines):

        # CLEAN lines

        # Zeilennummern
        line_clean_1 = line_remove_rownumbers(line, debug)
        # Trennzeichen
        line_clean_2 = line_remove_minus(line_clean_1, debug)
        # Seitenzahlen
        line_clean_3 = line_remove_pageNumber(line_clean_2, debug)
        # Punkte
        line_clean_4 = line_remove_dots(line_clean_3, debug)

        # ADD
        line_clean_4 = line_clean_4.strip()
        output_raw_cleaned.append(line_clean_4)

        #DEBUG
        if debug and line_clean_4 != "":
            print(
                f"\033[32m\n|- Processing line {index + 1}: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -|          " + line_clean_4 + "\033[0m" + "")

    # REMOVE blanc lines
    while "" in output_raw_cleaned:
        output_raw_cleaned.remove("")

    return output_raw_cleaned


def line_remove_dots(input, debug):
    text = input
    if "• " in text:
        text = text.replace("• ", "")
        if debug:
            print(DEBUG_ATTACHMENT_MARKER_DOT)
        return text
    else:
        return text


def line_remove_rownumbers(line, debug=False):
    global row_counter
    global row_number_counter
    start_to_count = False

    if row_counter >= 0:
        start_to_count = True

    n = row_number_counter
    end = str(n)
    line = line.strip()

    if line.endswith(end) and start_to_count:
        numbers_length = len(end)
        line = line[:-numbers_length].rstrip()
        if debug:
            print(DEBUG_ATTACHMENT_MARKER_ROWNUMBER_FOUND
                  + ": n = " + end + ", start-counter = " + str(row_number_counter))
        row_number_counter += 1
    elif debug:
        print(DEBUG_ATTACHMENT_MARKER_ROWNUMBER_NOT_FOUND
              + ", n = " + end + ", start-counter = " + str(row_number_counter))

    row_counter += 1

    return line


def line_remove_minus(line_given, debug=False):
    line_given = line_given.strip()

    if line_given.endswith("-"):
        if debug and len(line_given) > 0:
            print(
                f"{DEBUG_ATTACHMENT_MARKER_MINUS}: Zeile endet auf '-' ?: {line_given[-1] == '-'}" + " Letztes Zeichen: " + str(
                    line_given[-1]))
        line_given = (line_given[:-1])

    return line_given


def line_remove_pageNumber(text, debug=False):
    if isinstance(text, str):
        if "Seite" in text:
            position = text.index("Seite")
            i = 0
            while position + i + 6 < len(text) and text[position + i + 6].isdigit():
                i += 1

                # suche "von", schneide ebenfalls ab
                if text[position + i + 6:position + i + 11] == " von " and text[position + i + 11].isdigit():
                    i += 5
                    while position + i < len(text) and text[position + i].isdigit():
                        i += 1
            text = text[:position] + text[position + i + 6:]
            if debug:
                print(DEBUG_ATTACHMENT_MARKER_SEITENZAHL)
        return text
    else:
        return text


# UNUSED
def remove_numbers(text):
    if not text.isDigit():
        index = len(text)
        while index > 0 and index > len(text) - 5 and (text[index - 1].isdigit() or text[index - 1] == '-'):
            index -= 1
        return text[:index]
    else:
        return ''


#### Inhaltsverzeichnis
# extract headings from raw list into new list
# puts multi-line-headings into one appending
def create_inhaltsverzeichnis(data, limit_min, limit_max, start_data_from_index_on, ignore_data_from_index_on, debug):
    data_line_number = limit_min
    vz_index = data_line_number
    limit = limit_max
    if limit_max == 0:
        limit = len(data) - 1 - limit_min

    vz_dirty = []
    vz_line_cached = ""

    # remove whitespace
    data = [entry.strip() for entry in data]
    while "" in data:
        data.remove("")

    skip_entry = False
    # FILL vz_dirty
    while data_line_number < limit and vz_index < (len(data)):
        vz_index = data_line_number
        vz_lineContent = data[data_line_number]

        if debug:
            print("Debug merge multiliners: \nFor line                      " + str(vz_lineContent))
            print("line ist Front-Part          " + str(isVZEntry_part_front(vz_lineContent, vz_line_cached)) + "")
            print("line ist Back-Part           " + str(isVZEntry_part_back(vz_lineContent, vz_line_cached)) + "")
            print("line ist Complete           " + str(isVZEntry(vz_lineContent)) + "")
            if vz_line_cached != "":
                print("Cache: " + vz_line_cached)
            if vz_lineContent == "":
                print("--- blanc line ---\n")
            print("\n")

        if isVZEntry(vz_lineContent):
            # Single-line heading (no need to cache)
            vz_dirty.append(vz_lineContent)
            data_line_number += 1  # Increment data_line_number after adding

        elif vz_lineContent != "" and isVZEntry_part_front(vz_lineContent, vz_line_cached):
            # Start of multi-line heading, cache the front part
            vz_line_cached = vz_lineContent  # Fill cache
            # No data_line_number increase yet, wait for the back part
            data_line_number += 1

        elif vz_lineContent != "" and isVZEntry_part_back(vz_lineContent, vz_line_cached):
            # End of multi-line heading, merge the front and back parts
            vz_lineContent = vz_line_cached + " " + vz_lineContent
            if debug:
                print("MERGED = " + vz_lineContent + "\n")
            vz_dirty.append(vz_lineContent)
            vz_line_cached = ""  # Reset cache
            data_line_number += 1  # Increment data_line_number after successfully combining



        else:
            # Continue processing next line
            data_line_number += 1

    # REMOVE DOTS AND PAGENUMBERS
    headlines_plain = []
    for entry in vz_dirty:

        if len(entry) > 7:

            laenge = len(entry)

            counter = 6
            while counter < laenge - 1:  # suche ". "
                if entry[counter] == "." and entry[counter + 1] == " ":
                    break
                counter += 1

            counter2 = 0
            while (counter2 + counter + 2) < laenge:  # suche " .."
                if entry[counter + counter2] == " " and entry[counter + counter2 + 1] == "." and entry[
                    counter + counter2 + 2] == ".":
                    break
                counter2 += 1

            trimmed_entry = entry[:counter].strip() + entry[counter + counter2 + 3:].strip()
            cleaned_entry = re.sub(r'\.+$', '', trimmed_entry)  # lösche Punkte
            cleaned_entry = re.sub(r'^\d+(\.\d+)*\s*', '', cleaned_entry)
            cleaned_entry = re.sub(r'^\.\s*', '', cleaned_entry)

            if cleaned_entry[-1] == " ":
                cleaned_entry = cleaned_entry[:-1]
            headlines_plain.append(cleaned_entry)

    # FILL vz_clean
    # find equal headings from (vz_dirty) in raw text (data)-> safe indices in list
    # removes dots and numbers from headings -> clean
    heading_index_found_in_data = []
    multiliner_index_found_in_data = []
    vz_cleaned = []
    data_shortened = data[80:]  #= shorten_list(data, start_data_from_index_on, 0)

    #print(len(data_shortened))
    #print("\n" + str(len(headlines_plain)))
    #for entry in data_shortened:
    #    print(entry)
    counter = 0
    #### finde entry in data_shortened
    for entry in headlines_plain:  # iteriere inhaltsverzeichnis ohne Punkte
        found = False
        for index_in_data, entry_in_data in enumerate(data_shortened):  # iteriere über gekürzte raw-Daten
            # Direkter Vergleich
            if entry in entry_in_data and entry_in_data[0].isdigit():
                heading_index_found_in_data.append(index_in_data + start_data_from_index_on)
                if debug:
                    print(f"\nZeile                #{index_in_data}")
                    print(f"Original-Inhalt:     {entry_in_data}")
                    print(f"Headline-Inhalt:     {entry}")
                vz_cleaned.append(entry)
                found = True
                break

            # Fallback: Vergleiche erste 60 Zeichen
            elif entry[:60] in entry_in_data and entry_in_data[0].isdigit():
                heading_index_found_in_data.append(index_in_data + start_data_from_index_on)
                multiliner_index_found_in_data.append(index_in_data + start_data_from_index_on)
                if debug:
                    print(f"\n--- zweizeilig ---:")
                    print(f"Zeile                #{index_in_data}")
                    print(f"Original-Inhalt:     {entry_in_data}")
                    print(f"Headline-Inhalt:     {entry}")
                vz_cleaned.append(entry)
                found = True
                break  # Keine weitere Suche nötig

        # Wenn weder direkter Vergleich noch Fallback erfolgreich war
        if not found:
            counter += 1
            print(f"\nNot Found ({counter}):       {entry}")

    return headlines_plain, vz_cleaned, heading_index_found_in_data, multiliner_index_found_in_data


def isVZEntry(inhvz_line):
    return has_entry_part_front(inhvz_line) and has_entry_part_back(inhvz_line)


def isVZEntry_part_front(inhvz_line, cached_line):
    return has_entry_part_front(inhvz_line) and cached_line == ""


def isVZEntry_part_back(inhvz_line, cached_line):
    return has_entry_part_back(inhvz_line) and cached_line != ""


def has_entry_part_front(inhvz_line):
    return (inhvz_line[0].isdigit() and inhvz_line[1] == '.') or (inhvz_line[1].isdigit() and inhvz_line[2] == '.')


def has_entry_part_back(inhvz_line):
    return (((inhvz_line[-1].isdigit() and inhvz_line[-2] == ' ')
             or (inhvz_line[-1].isdigit() and inhvz_line[-2].isdigit() and inhvz_line[-3] == ' '))
            or (inhvz_line[-1].isdigit() and inhvz_line[-2].isdigit() and inhvz_line[-3].isdigit() and inhvz_line[
                -4] == ' '))


def shorten_list(input_list, start, end):
    if end == 0:
        end = len(input_list) - 1
    output_list = []
    for index, line in enumerate(input_list):
        if start < index <= end:
            output_list.append(line)
    return output_list


def make_string_from_list(input_list):
    output_string = ""
    for index, line in enumerate(input_list):
        output_string += line + "\n"
    return output_string


def print_one_index(inhaltsverzeichnisse, index):
    print("\nPrinting Index # " + str(index) + ":")
    print(inhaltsverzeichnisse[0][index + 1])  # TODO added +1
    print(inhaltsverzeichnisse[1][index])
    print(inhaltsverzeichnisse[2][index])


def print_all_index(inhaltsverzeichnisse, data):  # headlines_plain, vz_cleaned, heading_index_found_in_data, multiliner
    index = 0
    nextmultiliner = 0
    while len(inhaltsverzeichnis_done[1]) > index:
        print("\nEintrag #" + str(index) + ":")
        print("                                                 " + str(inhaltsverzeichnisse[0][index]) + "\n" +
              str("Headline aus Inhaltsverzeichnis:                 " + inhaltsverzeichnisse[1][index]) + "\n" +
              str("Data an Stelle des Index #" + str(inhaltsverzeichnisse[2][index]) + ":         "
                  + "           " + data[inhaltsverzeichnisse[2][index]]))
        if nextmultiliner < len(inhaltsverzeichnisse[3]) and inhaltsverzeichnisse[2][index] == inhaltsverzeichnisse[3][
            nextmultiliner]:
            print(str(data[inhaltsverzeichnisse[2][
                               index] + 1])+", Multiliner: "+str(inhaltsverzeichnisse[3][nextmultiliner]))  # finde in data die Zeile nach dem ersten Part des Multiliners
            nextmultiliner += 1
        index += 1


import csv


def write_CSV(inhaltsverzeichnisse, data, output_file="cdu.csv"):  # headlines_plain, vz_cleaned, heading_index_found_in_data, multiliner_index_found_in_data
    offset = 146

    headline_nummer = 0
    data_index = offset  # Start bei 0 für den ersten Eintrag in 'data'
    nextmultiliner = 0

    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Schreibe Header in die CSV-Datei
        writer.writerow(["Titel", "Paragraph"])

        # Gehe durch die Headlines in inhaltsverzeichnisse[1]
        while headline_nummer < len(inhaltsverzeichnisse[1]):
            headline = inhaltsverzeichnisse[1][headline_nummer]  # Die aktuelle Headline
            if headline_nummer+1 < len(inhaltsverzeichnisse[2]):
                zeile_der_headline_in_data = inhaltsverzeichnisse[2][headline_nummer+1]  # Der Index, der zu dieser Headline gehört
           # else ist letzte Headline

            print(f"Verarbeite Headline: {headline} (Index in Daten: {zeile_der_headline_in_data})")

            content = ""  # Start mit leerem Inhalt

            # Multiliner-Bedingung: Falls Multiliner aktiviert, überspringe die erste Zeile
            skipper = 1
            if nextmultiliner < len(inhaltsverzeichnisse[3]) and inhaltsverzeichnisse[2][headline_nummer] == inhaltsverzeichnisse[3][nextmultiliner]:
                print(
                    f"Ist Multiliner: Index in Data: {inhaltsverzeichnisse[2][headline_nummer]}, weil nächster Eintrag in Multiliner-Index-Liste = {inhaltsverzeichnisse[3][nextmultiliner]}")
                nextmultiliner += 1
                skipper = 2

            while data_index < len(data) and data_index != zeile_der_headline_in_data:
                if skipper <= 0:  # Nur solange nicht Headline-row
                    print(f"adding line: (Aktuelle Zeile:{data_index}, Nächste Headline bei Index {zeile_der_headline_in_data}): {data[data_index]}")
                    content += data[data_index] + " "  # Füge den Inhalt zur aktuellen Zeile hinzu
                else:
                    # Zusätzliche Absicherung:
                    if nextmultiliner < len(inhaltsverzeichnisse[3]):
                        print(
                            f"Überspringe: (data index:{data_index}, zeile_der_headline_in_data: {zeile_der_headline_in_data}, Next Multiliner: {inhaltsverzeichnisse[3][nextmultiliner] + offset}): {data[data_index]}")
                    else:
                        print(f"Überspringe: (data index:{data_index}, zeile_der_headline_in_data: {zeile_der_headline_in_data}, Kein weiterer Multiliner vorhanden)")

                data_index += 1  # Inkrementiere den Datenindex
                skipper -= 1

            # Füge letzte Daten hinzu
            if not headline_nummer + 1 < len(inhaltsverzeichnisse[2]):
                print(
                    f"Kein weiterer Headline-Index vorhanden: Headline #{headline_nummer} IST DIE LETZTE HEADLINE = Data-Index #{inhaltsverzeichnisse[2][headline_nummer]}")
                # Füge Daten nach letzer Zeile ein
                #data_index =+ 1 # Überspringe Headline händisch

                while data_index < len(data):
                    if data_index == inhaltsverzeichnisse[2][headline_nummer]: #letzte Überschrift
                        print(f"Überspringe Headline händisch: {data[data_index]}")
                        data_index += 1
                    print(
                        f"adding last lines: (Aktuelle Zeile:{data_index}, Nächste Headline bei Index {zeile_der_headline_in_data}): {data[data_index]}")
                    content += data[data_index] + " "
                    data_index += 1


            print(f"----------------------------Füge gemergte Daten hinzu--------------------------------\n")

            # Schreibe die aktuelle Zeile in die CSV-Datei
            writer.writerow(
                [headline, content.strip()])  # .strip() entfernt eventuelle führende oder nachfolgende Leerzeichen

            # Gehe zur nächsten Headline
            headline_nummer += 1

            # Wenn der Index mit dem nächsten Wert in 'inhaltsverzeichnisse[2]' übereinstimmt, gehe zur nächsten Zeile
            if data_index < len(data) and data_index == inhaltsverzeichnisse[2][headline_nummer]+1 if headline_nummer < len(
                    inhaltsverzeichnisse[2]) else False:
                print(
                    f"Neuer Index {data_index} entspricht {inhaltsverzeichnisse[2][headline_nummer]+1}. Neue Zeile wird begonnen.")
                content = ""  # Starte eine neue Zeile
                headline_nummer += 1  # Gehe zur nächsten Headline, falls der Index passt

        print("CSV-Datei wurde erfolgreich geschrieben.")



#########################################
#                                       #
#               MAIN                    #
#                                       #
#########################################


debug = False
# create raw cleaned list of text
output = cleanUp(input_text, debug)
# create inhaltsverzeichnis from list
inhaltsverzeichnis_raw = shorten_list(output, 3, 80)
inhaltsverzeichnis_done = create_inhaltsverzeichnis(output, 0, 81, 80, 0, debug)
if debug:
    print(make_string_from_list(inhaltsverzeichnis_raw))
    print("REMOVED DOTS:" + str(len(inhaltsverzeichnis_done[0])))
    for heading in inhaltsverzeichnis_done[0]:
        print(str(heading))
    print("\nCLEAN:" + str(len(inhaltsverzeichnis_done[1])))
    for heading in inhaltsverzeichnis_done[1]:
        print(str(heading))
    print("\nOCCURRENCIES:" + str(len(inhaltsverzeichnis_done[2])))

#for heading in inhaltsverzeichnis_done[2]:
#    print(str(heading))

#print(inhaltsverzeichnis_done[3])
#print_all_index(inhaltsverzeichnis_done, output)

data_without_vz = shorten_list(output, 0, 0)
inhaltsverzeichnis_done[2][70] = 4783
write_CSV(inhaltsverzeichnis_done, output)
print(inhaltsverzeichnis_done[2])
#print(inhaltsverzeichnis_done[3])
