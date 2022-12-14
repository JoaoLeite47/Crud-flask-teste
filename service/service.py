from dao.dao import TesteDao


class ServiceTest:
    def selectClientes():
        conex = TesteDao.conectar()
        results = TesteDao.selectClientes(conex[0])
        result_total = []
        for cliente in results:
            cliente = {'rg': cliente[0], 'dt_nascimento': cliente[1], 'cnh': cliente[2],
                       'nome': cliente[3], 'endereco': cliente[4], 'cpf': cliente[5]}
            result_total.append(cliente)
        return result_total

    def selectCliente(cpf):
        conex = TesteDao.conectar()
        results = TesteDao.selectCliente(conex[0], cpf)
        result_total = []
        for cliente in results:
            cliente = {'rg': cliente[0], 'dt_nascimento': cliente[1], 'cnh': cliente[2],
                       'nome': cliente[3], 'endereco': cliente[4], 'cpf': cliente[5]}
            result_total.append(cliente)
        return result_total

    def criarCliente(userDetails):
        conex = TesteDao.conectar()
        results = TesteDao.criarCliente(conex[0], conex[1], userDetails)
        return results

    def updateCliente(cpf, userDetails):
        conex = TesteDao.conectar()
        results = TesteDao.updateCliente(conex[0], conex[1], cpf, userDetails)
        return results

    def deleteCliente(cpf):
        conex = TesteDao.conectar()
        results = TesteDao.deleteCliente(conex[0], conex[1], cpf)
        return results

    def selectCategorias():
        conex = TesteDao.conectar()
        results = TesteDao.selectCategorias(conex[0])
        result_total = []
        for categorias in results:
            categorias = {
                'cod_categ': categorias[0], 'descricao': categorias[1], 'valor_diaria': categorias[2]}
            result_total.append(categorias)
        return result_total

    def selectCategoria(cod_categ):
        conex = TesteDao.conectar()
        results = TesteDao.selectCategoria(conex[0], cod_categ)
        result_total = []
        for categoria in results:
            categoria = {
                'cod_categ': categoria[0], 'descricao': categoria[1], 'valor_diaria': categoria[2]}
            result_total.append(categoria)
        return result_total

    def criarCategoria(userDetails):
        conex = TesteDao.conectar()
        results = TesteDao.criarCategoria(conex[0], conex[1], userDetails)
        return results

    def updateCategoria(userDetails, cod_categ):
        conex = TesteDao.conectar()
        results = TesteDao.updateCategoria(
            conex[0], conex[1], userDetails, cod_categ)
        return results

    def deleteCategoria(cod_categ):
        conex = TesteDao.conectar()
        results = TesteDao.deleteCategoria(conex[0], conex[1], cod_categ)
        return results

    def selectAlocacoes():
        conex = TesteDao.conectar()
        results = TesteDao.selectAlocacoes(conex[0])
        result_total = []
        for alocacao in results:
            alocacao = {'cpf_fk': alocacao[0], 'chassi_fk': alocacao[1], 'dt_saida': alocacao[2],
                        'dt_entrega': alocacao[3], 'id_aloc': alocacao[4]}
            result_total.append(alocacao)
        return result_total

    def selectAlocacao(id_aloc):
        conex = TesteDao.conectar()
        results = TesteDao.selectAlocacao(conex[0], id_aloc)
        result_total = []
        for alocacao in results:
            alocacao = {'cpf_fk': alocacao[0], 'chassi_fk': alocacao[1], 'dt_saida': alocacao[2],
                        'dt_entrega': alocacao[3], 'id_aloc': alocacao[4]}
            result_total.append(alocacao)
        return result_total

    def criarAlocacao(userDetails):
        conex = TesteDao.conectar()
        results = TesteDao.criarAlocacao(conex[0], conex[1], userDetails)
        return results

    def updateAlocacao(userDetails, id_aloc):
        conex = TesteDao.conectar()
        results = TesteDao.updateAlocacao(
            conex[0], conex[1], userDetails, id_aloc)
        return results

    def deleteAlocacao(id_aloc):
        conex = TesteDao.conectar()
        results = TesteDao.deleteAlocacao(conex[0], conex[1], id_aloc)
        return results

    def selectCarros():
        conex = TesteDao.conectar()
        results = TesteDao.selectCarros(conex[0])
        result_total = []
        for carros in results:
            carros = {'chassi': carros[0], 'cor': carros[1], 'modelo': carros[2],
                      'marca': carros[3], 'placa': carros[4], 'ano': carros[5], 'categoria_fk': carros[6]}
            result_total.append(carros)
        return result_total

    def selectCarro(chassi):
        conex = TesteDao.conectar()
        results = TesteDao.selectCarro(conex[0], chassi)
        result_total = []
        for carro in results:
            carro = {'chassi': carro[0], 'cor': carro[1], 'modelo': carro[2],
                     'marca': carro[3], 'placa': carro[4], 'ano': carro[5], 'categoria_fk': carro[6]}
            result_total.append(carro)
        return result_total

    def criarCarro(userDetails):
        conex = TesteDao.conectar()
        results = TesteDao.criarCarro(conex[0], conex[1], userDetails)
        return results

    def updateCarro(userDetails, chassi):
        conex = TesteDao.conectar()
        results = TesteDao.updateCarro(conex[0], conex[1], userDetails, chassi)
        return results

    def deleteCarro(chassi):
        conex = TesteDao.conectar()
        results = TesteDao.deleteCarro(conex[0], conex[1], chassi)
        return results
