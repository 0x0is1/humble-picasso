def ci_renew(keyword, raw_keywords):
    keywords = raw_keywords.split('-')
    keyidx = keywords.index(keyword)
    if keyidx >= len(keywords)-1:
        keyword = keywords[0]
        keyidx = 0
    else: 
        keyword = keywords[keyidx + 1]
        keyidx+=1
    return keyword, keyidx