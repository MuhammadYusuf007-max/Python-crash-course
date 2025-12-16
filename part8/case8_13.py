def build_profile(first, last, **kwargs):
    kwargs['first_name'] = first
    kwargs['last_name'] = last
    return kwargs

# user_profile = build_profile("Yusuf", "Mukhammadov", location = 'Bukhara', age=21, married=False)

# print(user_profile)