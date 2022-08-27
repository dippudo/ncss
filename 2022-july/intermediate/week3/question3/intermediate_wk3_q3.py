proposal = []
camCount = 0


while camCount < 3:
    stock = input("Shop stock: ")
    stockLower = str(stock.lower())
  
    if "cam" in stockLower:
        proposal.append(stock)
        camCount = camCount + 1
  

proposal.sort()
proposal.reverse()
proposalJoin = ", ".join(proposal)

print(f"Proposals: {proposalJoin}")
