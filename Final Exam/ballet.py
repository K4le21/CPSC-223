def in_troupe(dancerName, troupeName = 'ABT'):
    abt_dancers = ['Sylvie', 'Natalie', 'Johnathan', 'Isabella', 'Sara', 'Jerry']
    ncb_dancers = ['Ingram','Patrick', 'Takako', 'Misty', 'Amanda']

    dancerName = dancerName.title()
    troupeName = troupeName.upper()

    if troupeName == 'NCB':
        if dancerName in ncb_dancers:
            return True

    if troupeName == 'ABT':
        if dancerName in abt_dancers:
            return True

    return False
