journal = {'ibis': 'Bin near the beach.', 'magpie': 'Swooping in local park.', 'noisy miner': 'Outside kitchen window.', 'seagull': 'Stealing my chips.', 'cockatoo': 'Neighbours lemon tree.', 'lorikeet': 'Palm tree.', 'peregrine falcon': 'On the livestream.', 'emu': 'Mutawintji National Park.', 'wedge-tailed eagle': 'Driving to Freycinet.', 'penguin': 'Middle Island.', 'kookaburra': 'Old gumtree.', 'nativehen': 'Being a turbo chook.'}

bird = input("Enter a bird: ")
bird_lower = bird.lower()

if bird_lower in journal:
  print(journal[bird_lower])

else:
  print("Never seen that bird!")
