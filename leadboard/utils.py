def getUniqueScores(queryset):
    s = set()
    result = []
    for a in queryset:
        if a.name_id not in s:
            result.append(a)
            s.add(a.name_id)
    return result