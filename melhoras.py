class Nenem:
  def __init__(self, saude):
    self.saude = saude


if __name__ == "__main__":

  def desejar_melhoras(nenem):
      if nenem.saude == 1:
          return "Fica bem logo, meu nenem. Tô aqui pro que precisar, apenas a uma ligação de distância"
      else:
          return "Espero que você esteja melhor. Me liga que já to indo te ver"
  
  saude_nenem = int(input("Como está se sentido hoje? \n Digite: \n 1 - para doentinha \n 2 - para \"tô melhor\"\n"))
  
  meu_nenem = Nenem(saude_nenem)
  
  print(desejar_melhoras(meu_nenem))
