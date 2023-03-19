import sqlite3
conn = sqlite3.connect('player.db')
c = conn.cursor()
# Creates a table for Players
c.execute("""CREATE TABLE players (
  refnum integer,
  team text,
  name text,
  str integer,
  str_mod integer,
  dex integer,
  dex_mod integer,
  wis integer,
  wis_mod integer,
  cha integer,
  cha_mod integer,
  mag integer,
  mag_mod integer,
  dmag integer,
  dmag_mod integer,
  gk integer,
  gk_mod integer
  )""");

c.execute("""CREATE TABLE captains (
  team text,
  name text
  )""")


c.execute("INSERT INTO players VALUES (1,'Kobolds', 'Jitcy',	14,	2,	14,	2,	16,	3,	15,	2,	15,	2,	15,	2,	13,	1)")

c.execute("INSERT INTO players VALUES (2,'Kobolds','Sage Bogey of the Realm',	11,	0,	10,	0,	12,	1,	13,	1,	14,	2,	14,	2, 0, 0)")

c.execute("INSERT INTO players VALUES (3,'Kobolds','Illusionist Peppy',	10,	0,	13,	1,	12,	1,	13,	1,	10,	0,	16,	3, 0, 0)")

c.execute("INSERT INTO players VALUES (4,'Kobolds','Pyromancer Duzzle',	8,	-1,	8,	-1,	16,	3,	10,	0,	15,	2,	12,	1, 0, 0)")

c.execute("INSERT INTO players VALUES (5,'Kobolds','Shaman Fugh',	16,	3,	14,	2,	12,	1,	15,	2,	14,	2,	16,	3, 0, 0)")

c.execute("INSERT INTO players VALUES (1,'Souls','Bloody Mary',	10,	0,	11,	0,	16,	3,	9,	-1,	14,	2,	11,	0,	17,	3)")

c.execute("INSERT INTO players VALUES (2,'Souls','Masque of the Red Death',	14,	2,	12,	1,	13,	1,	15,	2,	13,	1,	17,	3, 0, 0)")

c.execute("INSERT INTO players VALUES (3,'Souls','The Ghost of Gremplin',	10,	0,	14,	2,	10,	0,	15,	2,	10,	0,	16,	3, 0, 0)")

c.execute("INSERT INTO players VALUES (4,'Souls','Toru',	9,	-1,	11,	0,	10,	0,	13,	1,	8,	-1,	13,	1, 0, 0)")

c.execute("INSERT INTO players VALUES (5,'Souls','Elf',	8,	-1,	8,	-1,	14,	2,	16,	3,	14,	2,	15,	2, 0, 0)")

c.execute("INSERT INTO players VALUES (1,'Wizards','Enchanter Corky',	12,	1,	8,	-1,	9,	-1,	13,	1,	13,	1,	9,	-1,	15,	2)")

c.execute("INSERT INTO players VALUES (2,'Wizards','Adept Cromwell',	13,	1,	11,	0,	11,	0,	13,	1,	15,	2,	16,	3, 0, 0)")

c.execute("INSERT INTO players VALUES (3,'Wizards','Arcanist Magnus',	9,	-1,	16,	3,	10,	0,	8,	-1,	8,	-1,	13,	1, 0, 0)")

c.execute("INSERT INTO players VALUES (4,'Wizards','Arcanist Eden',	14,	2,	9,	-1,	11,	0,	10,	0,	10,	0,	13,	1, 0, 0)")

c.execute("INSERT INTO players VALUES (5,'Wizards','Dotta',	14,	2,	9,	-1,	16,	3,	16,	3,	12,	1,	13,	1, 0, 0)")

c.execute("INSERT INTO players VALUES (1,'Warriors','Bearsnake',	12,	1,	8,	-1,	12,	1,	18,	4,	11,	0,	8,	-1,	18,	4)")

c.execute("INSERT INTO players VALUES (2,'Warriors','Beowulf',	13,	1,	11,	0,	15,	2,	6,	-2,	13,	1,	13,	1,	0, 0)")

c.execute("INSERT INTO players VALUES (3,'Warriors','Heracles',	15,	2,	16,	3,	14,	2,	13,	1,	13,	1,	10,	0,	0, 0)")

c.execute("INSERT INTO players VALUES (4,'Warriors','Atalanta',	16,	3,	14,	2,	9,	-1,	11,	0,	7,	-2,	13,	1,	0, 0)")

c.execute("INSERT INTO players VALUES (5,'Warriors','Gligamesh',	10,	0,	15,	2,	12,	1,	10,	0,	17,	3,	14,	2,	0, 0)")

c.execute("INSERT INTO players VALUES (1,'Beasts','Nightmare Imp',  15, 2,  13, 1,  9, -1,  14, 2,  14, 2,  16, 3,  14, 2)")

c.execute("INSERT INTO players VALUES (2,'Beasts','Magus Wazir',  10, 0,  11, 0,  11, 0,  14, 2,  10, 0,  14, 2,  0, 0)")

c.execute("INSERT INTO players VALUES (3,'Beasts','Chaos Chimera',  13, 1, 15, 2,  16, 3,  12, 1,  16, 3,  16, 3,  0, 0)")

c.execute("INSERT INTO players VALUES (4,'Beasts','Bugbear Chieftain',  12, 1,  10, 0,  13, 1,  10, 0,  11, 0,  10, 0,  0, 0)")

c.execute("INSERT INTO players VALUES (5,'Beasts','Gigas Chad',  8, -1,  11, 0,  14, 2,  8, -1,  12, 1,  9, -1,  0, 0)")



c.execute("INSERT INTO captains VALUES ('Beasts','Magus Wazir')")

c.execute("INSERT INTO captains VALUES ('Warriors','Bearsnake')")

c.execute("INSERT INTO captains VALUES ('Wizards','Dotta')")

c.execute("INSERT INTO captains VALUES ('Souls','Elf')")

c.execute("INSERT INTO captains VALUES ('Kobolds','Jitcy')")




conn.commit()
conn.close()
