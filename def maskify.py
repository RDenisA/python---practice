def maskify(cc):
    ccMasked = ''
    for i in cc[:-4]:
        ccMasked += '#'
    ccMasked += cc[-4:]
    return ccMasked


print(maskify('SF$SDfgsd2eA'))
