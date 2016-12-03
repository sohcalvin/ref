# pip install py2neo

from py2neo import Graph, Path
graph = Graph()
graph.gg
tx = graph.cypher.begin()

for name in ["Alice", "Bob", "Carol"]:
    tx.append("CREATE (person:Person {name:{name}}) RETURN person", name=name)
alice, bob, carol = [result.one for result in tx.commit()]

friends = Path(alice, "KNOWS", bob, "KNOWS", carol)
graph.create(friends)