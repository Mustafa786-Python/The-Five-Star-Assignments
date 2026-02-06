"Task to do"
"""
1- Add a new artwork to the MoMA’s contribution, titled Composition with Red, Blue,
and Yellow.
2. Identify shared artworks among all three museums that could be placed in a Shared
Masterpieces display. Display the list of artworks common to all three collections.
3. Add new artworks to both the Louvre and the Rijksmuseum collections:
o Louvre: {Raft of the Medusa, Liberty Leading the People}
o Rijksmuseum: {The Jewish Bride, The Milkmaid}
4. Create a master list of unique artworks across all three museums to determine the total
number of different pieces available in the exhibition.
5. The Rijksmuseum finds out that they are no longer allowed to display The
Milkmaid. Remove this artwork from the Rijksmuseum’s collection without affecting
the other museums’ collections.
6. Identify unique pieces in MoMA’s collection that are not contributed by the Louvre or
the Rijksmuseum. This will help the organizers create a section for Exclusive Pieces
from MoMA.
"""


# Global Art Exhibition
moma_artworks = {"Starry Night", "The Persistence of Memory",
                 "The Scream", "Girl with a Pearl Earring"}

# Louvre Museum contributes the following pieces:
louvre_artworks = {"Mona Lisa", "The Scream",
                   "Liberty Leading the People", "Girl with a Pearl Earring"}

# Rijksmuseum contributes the following pieces:
rijksmuseum_artworks = {
    "The Night Watch", "Girl with a Pearl Earring", "The Milkmaid", "Starry Night"}


"Task1"

moma_artworks.add("Composition with Red, Blue, and Yellow",)
print("Updated moma artworks is:")
for i in rijksmuseum_artworks:
    print(f"\u25CF {i}")


"Task2"
print("--" * 50)
print()
print("Share artworks among three:")
shared = moma_artworks & louvre_artworks & rijksmuseum_artworks
print(shared)
print()

"Task3"
print("--" * 50)
print()

louvre_artworks.update(["Raft of the Medusa", "Liberty Leading the People"])
print(f"Updated louvre_artworks is")
for i in louvre_artworks:
    print(f"\u25CF {i}")
print()
# Adding new Art works to rijksmuseum_artworks
rijksmuseum_artworks.update(["The Jewish Bride", "The Milkmaid"])
print(f"Updated rijksmuseum_artworks is: ")
for i in rijksmuseum_artworks:
    print(f"\u25CF {i}")


"Task4"
print("--" * 50)
print()
print("Unique artworks of the museums:")

unique_arts = moma_artworks.union(louvre_artworks, rijksmuseum_artworks)
print(f"The unique artworks are: {unique_arts}")
print()
# Unique in moma_artworks
unique1 = moma_artworks - louvre_artworks - rijksmuseum_artworks
print("Unique artworks of moma_artworks are")
for i in unique1:
    print(f"\u25CF {i}")

print()

# Unique in louvre_artworks
unique2 = louvre_artworks - moma_artworks - rijksmuseum_artworks
print("Unique artworks of louvre_artworks are:")
for i in unique2:
    print(f"\u25CF {i}")

print()


# Unique in rijksmuseum_artworks
unique3 = rijksmuseum_artworks - moma_artworks - louvre_artworks
print("Unique artworks of rijksmuseum_artworks are:")
for i in unique2:
    print(f"\u25CF {i}")

print()

"Task 5"
print("--" * 50)
print()
rijksmuseum_artworks.discard("The Milkmaid")
print("The updated list of rijksmuseum_artworks after removing The Milkmaid:")
for i in rijksmuseum_artworks:
    print(f"\u25CF {i}")
print()

"Task 6"
print("Unique artworks of moma_artworks are")
for i in unique1:
    print(f"\u25CF {i}")