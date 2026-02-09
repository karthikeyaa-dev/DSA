def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    mapping_s_t = {}
    mapping_t_s = {}
    for c1, c2 in zip(s, t):
        if mapping_s_t.get(c1, c2) != c2 or mapping_t_s.get(c2, c1) != c1:
            return False
        mapping_s_t[c1] = c2
        mapping_t_s[c2] = c1
    return True

print(is_isomorphic("add", "egg"))  # True
