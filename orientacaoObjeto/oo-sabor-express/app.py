from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_praca.receber_avaliacao('Breno', 10)
restaurante_praca.receber_avaliacao('Ana', 8)
restaurante_praca.receber_avaliacao('Mila', 2)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()