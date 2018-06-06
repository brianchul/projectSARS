def modifyKeyword(keyword,lists,modify):
    for content in lists:
        if keyword in content:
            pos = lists.index(content)
            lists[pos] = content.replace(keyword, modify)
    return lists