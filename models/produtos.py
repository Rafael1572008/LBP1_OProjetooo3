class Produto:
    def __init__(self, id, nome, preco, img):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.img = img

    def __repr__(self):
        return f"Produtos(id={self.id}, nome={self.nome}, preco={self.preco}, img={self.img})"      

produtos = [Produto(0, "AMD Radeon RX 7900 XT", 5500, "https://tpucdn.com/gpu-specs/images/c/3912-front.small.jpg"),
            Produto(1, "NVIDIA GeForce RTX 4090", 15000, "https://tpucdn.com/gpu-specs/images/c/3889-front.small.jpg")]