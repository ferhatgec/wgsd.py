import wgsd

x = wgsd.wgsd()
x.parse_file('example.wgsd')

print(x.find_key('profile1', 'use_music'),
      x.find_key('profile1', 'character_name'),
      x.find_key('profile2', 'empty'))
x.change_key('profile2', 'empty', False)

print(x.find_key('profile2', 'empty'))

print(f'regenerated:\n{x.generate()}')