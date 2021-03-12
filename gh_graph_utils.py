def augment_owns(graph, user):
    graph.add_node(user.login, node_type = 'user')
    repos = user.get_repos()
    for repo in repos:
        graph.add_node(repo.name, node_type = 'repo')
        graph.add_edge(user.login, repo.name, edge_type = 'owns')
    return repos

def augment_stargazers(graph, repo):
    gazers = repo.get_stargazers()
    for stargazer in gazers:
        graph.add_node(stargazer.login, node_type = 'user')
        graph.add_edge(stargazer.login, repo.name, edge_type = 'gazes')
    return repos