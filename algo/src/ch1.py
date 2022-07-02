'''
    Implementation of algorithms found in chapter 1 of Algorithm Design by Jon 
    Kleinberg and Eva Tardos.
'''


def gale_shapley(m_prefs, f_prefs):
    """
    gale_shapley returns a stable matching scheme given the preference lists of each male and female.

    :param m_prefs: 2-dimensional array containing the preference lists of males. m_prefs[i] is the preference list of male i. 
    :param f_prefs: 2-dimensional array containing the preference lists of females. f_prefs[i] is the preference list of female i.
    :return: 1-dimensional array matches, containing matchings. Female i is married to matches[i] under this scheme.
    """

    n = len(m_prefs)
    free_m = list(range(n))
    f_is_free = [True] * n
    matches = [0] * n

    # rank[i][j] is the ranking of male j by female i
    rank = [[0] * n for _ in range(n)]
    for w in range(n):
        for j in range(n):
            rank[w][f_prefs[j]] = j

    # next[i] is male i's most preferred female to which he has not engaged
    next = [0] * n

    while free_m:
        m = free_m.pop()
        f = m_prefs[next[m]]
        next[m] += 1
        if f_is_free[f]:
            f_is_free[f] = False
            matches[f] = m
        elif rank[matches[f]] > rank[m]:
            free_m.push(matches[f])
            matches[f] = m
    return matches
