
hamlet_speech = "To be, or not to be, that is the question:\nWhether 'tis nobler in the mind to sufferThe slings and arrows of outrageous fortune, Or to take arms against a sea of troublesAnd by opposing end them. To die—to sleep,No more; and by a sleep to say we end The heart-ache and the thousand natural shocksThat flesh is heir to: 'tis a consummation Devoutly to be wish'd. To die, to sleep; To sleep, perchance to dream—ay, there's the rub:For in that sleep of death what dreams may come,When we have shuffled off this mortal coil,Must give us pause—there's the respectThat makes calamity of so long life. For who would bear the whips and scorns of time,Th'oppressor's wrong, the proud man'scontumely,The pangs of dispriz'd love, the law'sdelayTheinsolence of office, and the spurnsThat patient merit of th'unworthy takesWhen he himself might his quietus makeWith a bare bodkin? Who would fardels bear,To grunt and sweat under a weary life,But that the dread of something after death,The undiscovere'd country, from whose bournNo traveller returns, puzzles the will, And makes us rather bear those ills we haveThan fly to others that we know not of? Thus conscience doth make cowards of us all,And thus the native hue of resolutionIs sicklied o'er with the palecastofthought,And enterprises of great pith and moment Withthisregardtheir currents turn awry And lose the name of action"

import string

# print(string.ascii_lowercase)
# print(string.digits)
# print(string.hexdigits)
# print(string.punctuation)

# create a translation table
trans_table = str.maketrans('','', string.punctuation)
hamlet_simplified = hamlet_speech.translate(trans_table)
print(hamlet_simplified.replace("\n", " "))





