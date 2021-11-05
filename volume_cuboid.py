def cuboid_volume(l):
    if type(l) not in [int,float]:
        raise TypeError('The length of cuboid can only be a valid integer or a float')
    return (l*l*l)

